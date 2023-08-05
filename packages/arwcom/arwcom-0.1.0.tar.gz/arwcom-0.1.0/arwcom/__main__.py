# C:\Program Files (x86)\Windows Kits\10\bin\10.0.19041.0\x64\oleview.exe (run as admin)

from arwcom.combaseapi import co_create_instance, co_initialize_ex, co_uninitialize
from arwcom.guiddef import GUID

if __name__ == "__main__":
    co_initialize_ex()
    clsid = GUID.from_prog_id("Excel.Application")
    co_create_instance(clsid)

    print(repr(clsid))
    co_uninitialize()
