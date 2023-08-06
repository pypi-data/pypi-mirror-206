"""Parameter Types as defined by SCOS-2000

These are used for both unpacking binary data as well as parsing (default)
values from an instance of SCOS-2000 (e.g. ``CPC_VALUE``).

Suppose you have a PCF definition (with PTC and PFC values) and want to use
that to unpack a byte block (``blob``). In that case you would use the provided
``ParameterType`` class like this::

    ptype = ParameterType.resolve(my_pcf_row)
    value = ptype.unpack(blob)

"""
import struct

from . import shared


_parametercache = {}


class NotEnoughDataToUnpack(shared.Error):
    """Raised when attempting to unpack data from a blob
       that's not big enough to contain that data"""
    def __init__(self, expected, available):
        super().__init__(f"Not enough data to unpack {expected} bytes: "
                         f"{available} bytes available")


class ParameterType:
    """Generic parameter type"""

    @classmethod
    def resolve(cls, pcf):
        """Return an instance of the ParameterType for this parameter characteristics

        May raise ``KeyError`` for invalid ptc/pfc combinations.
        """
        if isinstance(pcf, tuple):
            ptc, pfc = pcf
        else:
            ptc = pcf['PCF_PTC'].value
            pfc = pcf['PCF_PFC'].value

        paramtype = _parametercache.get((ptc, pfc), None)

        if paramtype is not None:
            return paramtype

        if ptc == 1 and pfc == 0:
            paramtype = UnsignedIntegerParameter(1)

        elif ptc == 2:
            # enumerations are special and have their own cache
            paramtype = EnumParameter(pfc)

        elif ptc == 3:
            bitwidth = 0

            if 0 <= pfc <= 12:
                bitwidth = 4 + pfc
            elif pfc == 13:
                bitwidth = 24
            elif pfc == 14:
                bitwidth = 32
            elif pfc == 15:
                raise NotImplementedError("unsigned int with 48 bit is not supported")
            elif pfc == 16:
                raise NotImplementedError("unsigned int with 64 bit is not supported")

            if bitwidth > 0:
                paramtype = UnsignedIntegerParameter(bitwidth)

        elif ptc == 4:
            bitwidth = 0

            if 0 <= pfc <= 12:
                bitwidth = 4 + pfc
            elif pfc == 13:
                bitwidth = 24
            elif pfc == 14:
                bitwidth = 32
            elif pfc == 15:
                raise NotImplementedError("signed int with 48 bit is not supported")
            elif pfc == 16:
                raise NotImplementedError("signed int with 64 bit is not supported")

            if bitwidth > 0:
                paramtype = SignedIntegerParameter(bitwidth)

        elif ptc == 5:
            if pfc == 1:
                # IEEE simple prec. float, 32 bit
                paramtype = FloatParameter()
            elif pfc == 2:
                # IEEE double prec. float, 64 bit
                paramtype = DoubleParameter()
            elif pfc == 3:
                # MIL simple prec. float, 32 bit
                raise NotImplementedError()
            elif pfc == 4:
                # MIL double prec. float, 48 bit
                raise NotImplementedError()

        elif ptc == 6:
            if pfc == 0:
                raise NotImplementedError("variable bitlength not supported")

            elif 1 <= pfc <= 32:
                paramtype = UnsignedIntegerParameter(pfc)

        elif ptc == 7:
            if pfc == 0:
                raise NotImplementedError("Variable length octet-string not implemented")

            else:
                paramtype = OctetStringParameter(pfc)

        elif ptc == 8:
            if pfc == 0:
                raise NotImplementedError("Variable length text strings not implemented")

            else:
                paramtype = TextStringParameter(pfc)

        elif ptc == 9:
            if pfc == 1:
                paramtype = AbsoluteCDSTimeFormat(6)
            elif pfc == 2:
                paramtype = AbsoluteCDSTimeFormat(8)
            elif pfc == 3:
                paramtype = AbsoluteCUCTimeFormat(1, 0)
            elif pfc == 4:
                paramtype = AbsoluteCUCTimeFormat(1, 1)
            elif pfc == 5:
                paramtype = AbsoluteCUCTimeFormat(1, 2)
            elif pfc == 6:
                paramtype = AbsoluteCUCTimeFormat(1, 3)
            elif pfc == 7:
                paramtype = AbsoluteCUCTimeFormat(2, 0)
            elif pfc == 8:
                paramtype = AbsoluteCUCTimeFormat(2, 1)
            elif pfc == 9:
                paramtype = AbsoluteCUCTimeFormat(2, 2)
            elif pfc == 10:
                paramtype = AbsoluteCUCTimeFormat(2, 3)
            elif pfc == 11:
                paramtype = AbsoluteCUCTimeFormat(3, 0)
            elif pfc == 12:
                paramtype = AbsoluteCUCTimeFormat(3, 1)
            elif pfc == 13:
                paramtype = AbsoluteCUCTimeFormat(3, 2)
            elif pfc == 14:
                paramtype = AbsoluteCUCTimeFormat(3, 3)
            elif pfc == 15:
                paramtype = AbsoluteCUCTimeFormat(4, 0)
            elif pfc == 16:
                paramtype = AbsoluteCUCTimeFormat(4, 1)
            elif pfc == 17:
                paramtype = AbsoluteCUCTimeFormat(4, 2)
            elif pfc == 18:
                paramtype = AbsoluteCUCTimeFormat(4, 3)
            elif pfc == 30:
                paramtype = AbsoluteUnixTimeFormat()

        if paramtype is not None:
            _parametercache[(ptc, pfc)] = paramtype
            return paramtype

        raise KeyError(f"Invalid PTC/PFC combination {ptc}/{pfc}")

    def __init__(self, bitwidth):
        self.bitwidth = bitwidth

    def parse(self, text, base=10):
        """Parse the given text in the given base (if applicable)"""
        raise NotImplementedError("Must be implemented in subclasses")

    def unpack(self, blob):
        """Unpack the bytes at `blob` and return the respective value"""
        raise NotImplementedError("Must be implemented in subclasses")


class UnsignedIntegerParameter(ParameterType):
    """An unsigned integer parameter type of variable bitwidth"""
    def unpack(self, blob):
        mask = 2**self.bitwidth - 1
        fmt, width = shared.unpack_uint_format(self.bitwidth)
        while len(blob) < width:
            blob = b'\x00' + blob
        return struct.unpack_from('>'+fmt, blob)[0] & mask

    def parse(self, text, base=10):
        value = int(text, base)

        if value < 0:
            raise ValueError("Negative value")

        return value


class EnumParameter(UnsignedIntegerParameter):
    """Enums are unsigned int"""


class SignedIntegerParameter(ParameterType):
    """A signed integer parameter type of variable bitwidth"""
    def unpack(self, blob):
        mask = 2**self.bitwidth - 1
        fmt, width = shared.unpack_int_format(self.bitwidth)
        while len(blob) < width:
            blob = b'\x00' + blob
        return struct.unpack_from('>'+fmt, blob)[0] & mask

    def parse(self, text, base=10):
        return int(text, base)


class FloatParameter(ParameterType):
    """A simple precision floating point type"""
    def __init__(self):
        super().__init__(32)

    def unpack(self, blob):
        if len(blob) < 4:
            raise NotEnoughDataToUnpack(4, len(blob))
        return struct.unpack_from('>f', blob)[0]

    def parse(self, text, base=None):
        return float(text)


class DoubleParameter(ParameterType):
    """A double precision floating point type"""
    def __init__(self):
        super().__init__(64)

    def unpack(self, blob):
        if len(blob) < 8:
            raise NotEnoughDataToUnpack(8, len(blob))
        return struct.unpack_from('>d', blob)[0]

    def parse(self, text, base=None):
        return float(text)


class OctetStringParameter(ParameterType):
    """A fixed length octet string"""
    def unpack(self, blob):
        # TODO - how is PTC = 7, PFC > 0 interpreted?
        raise NotImplementedError()

    def parse(self, text, base=None):
        raise NotImplementedError()


class TextStringParameter(ParameterType):
    """A fixed length text string"""
    def __init__(self, bitwidth):
        super().__init__(bitwidth*8)

    def unpack(self, blob):
        if len(blob)*8 < self.bitwidth:
            raise NotEnoughDataToUnpack(self.bitwidth, len(blob))
        return str(blob[:self.bitwidth], encoding="ascii", errors="ignore")

    def parse(self, text, base=None):
        return text


class AbsoluteCUCTime:
    """A CCSDS Unsegmented Time Code Timestamp"""
    def __init__(self, coarse, fine):
        self.coarsebytes = coarse
        self.finebytes = fine

    def parse(self, blob):
        # TODO
        return self


class AbsoluteCUCTimeFormat(ParameterType):
    """CCSDS Unsegmented Time Code"""
    def __init__(self, coarsetimebytes, finetimebytes):
        super().__init__((coarsetimebytes + finetimebytes)*8)
        self.coarse = coarsetimebytes
        self.fine = finetimebytes

    def unpack(self, blob):
        if len(blob) < self.coarse + self.fine:
            raise NotEnoughDataToUnpack(self.bitwidth, len(blob))
        return AbsoluteCUCTime(self.coarse, self.fine).parse(blob)

    def parse(self, text, base=None):
        raise NotImplementedError("No textual representation possible for CUC time stamps")


class AbsoluteCDSTimeFormat(ParameterType):
    """CDS time stamp without p-field"""
    def __init__(self, octets):
        super().__init__(octets*8)
        self.octets = octets

    def unpack(self, blob):
        if len(blob) < self.octets:
            raise NotEnoughDataToUnpack(self.bitwidth, len(blob))
        raise NotImplementedError()


class AbsoluteUnixTimeFormat(ParameterType):
    """Absolute timestamp in 8 byte unix time format"""
    def __init__(self):
        super().__init__(64)

    def unpack(self, blob):
        if len(blob) < 8:
            raise NotEnoughDataToUnpack(64, len(blob))
        raise NotImplementedError()


assert 6 == ParameterType.resolve((3, 0)).unpack(b'\xa6')
assert 38 == ParameterType.resolve((3, 2)).unpack(b'\xa6')
assert 0x63c == ParameterType.resolve((3, 8)).unpack(b'\xa6\x3c')