# C:\Program Files (x86)\Windows Kits\10\Include\xx.x.xxxxx.x\um\combaseapi.h

import logging
from ctypes import POINTER, byref, c_float, oledll, pointer
from ctypes.wintypes import LPVOID
from typing import Optional

from arwcom.iunknown import IUnknown
from arwcom.wintypesbase import CLSCTX_SERVER

logger = logging.getLogger(__name__)

ole32 = oledll.ole32

# objbase.h - Component object model definitions
# TODO: Move into separate py file
COINIT_APARTMENTTHREADED = 0x2


def co_initialize_ex():
    hr = ole32.CoInitializeEx(None, COINIT_APARTMENTTHREADED)


def co_uninitialize():
    ole32.CoUninitialize()


def co_create_instance(
    clsid, interface=IUnknown, unk_outer=None, clsctx: int = CLSCTX_SERVER
) -> pointer:
    # cls_ctx is class context
    # p = POINTER(interface)()  # https://stackoverflow.com/a/39913462/5782687
    p = LPVOID()  # FIX THIS PROPERLY
    iid = interface._iid
    ole32.CoCreateInstance(byref(clsid), unk_outer, clsctx, byref(iid), byref(p))
    return p
