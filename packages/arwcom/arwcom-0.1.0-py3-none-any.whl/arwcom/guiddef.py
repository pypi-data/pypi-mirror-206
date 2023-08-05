# C:\Program Files (x86)\Windows Kits\10\Include\xx.x.xxxxx.x\shared\guiddef.h

from ctypes import Structure, byref, oledll, wintypes
from typing import Optional, Type, TypeVar

ole32 = oledll.ole32

T = TypeVar("T", bound="Parent")  # type: ignore


class GUID(Structure):
    _fields_ = [
        ("Data1", wintypes.DWORD),
        ("Data2", wintypes.WORD),
        ("Data3", wintypes.WORD),
        ("Data4", wintypes.BYTE * 8),
    ]

    def __init__(self, sz: str = None) -> None:
        self.sz = None  # type: Optional[str]
        if sz is not None:
            ole32.CLSIDFromString(sz, byref(self))

    def get_iid_from_clsid(self) -> None:
        lpsz = wintypes.LPOLESTR()
        ole32.StringFromCLSID(byref(self), byref(lpsz))
        self.sz = lpsz.value
        ole32.CoTaskMemFree(lpsz)

    def __str__(self) -> str:
        if not self.sz:
            self.get_iid_from_clsid()
        return f"{self.sz}"

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}("{self}")'

    @classmethod
    def from_prog_id(cls: Type[T], prog_id: str) -> T:
        inst = cls()
        ole32.CLSIDFromProgID(prog_id, byref(inst))
        return inst

    @classmethod
    def from_sz(cls: Type[T], sz: str) -> T:
        inst = cls()
        ole32.CLSIDFromString(sz, byref(inst))
        return inst
