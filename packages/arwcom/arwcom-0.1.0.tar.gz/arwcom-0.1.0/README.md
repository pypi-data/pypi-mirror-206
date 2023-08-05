# arwcom

Lightweight Python 3 API to access Windows COM Objects

## Developer Configuration

[Configure VS Code for Microsoft C++](https://code.visualstudio.com/docs/cpp/config-msvc)

## References

Python Bindings Libraries

- [pywin32](https://github.com/mhammond/pywin32)
  - Access to many of the Windows APIs from Python
- [win32com](https://github.com/mhammond/pywin32/tree/master/com/win32com)
  - Python COM Extensions, example: `xl = win32com.client.Dispatch("Excel.Application")`

- [comtypes](https://github.com/enthought/comtypes)
  - Lightweight Python COM package, based on the ctypes_FFI library, in less than 10000 lines of code (not counting the tests).

- [win32-setctime](https://github.com/Delgan/win32-setctime)
  - Pure python package using `from ctypes import windll, wintypes, byref, FormatError, WinError`

- [SoundCard](https://github.com/bastibe/SoundCard/pull/89)
  - Patch for combase.dll `_ole32 = _ffi.dlopen('ole32')` and `_combase.CoUninitialize()`
- [Python ctypes.OleDLL() Examples](https://www.programcreek.com/python/example/124455/ctypes.OleDLL)
  - General examples of using `ctypes.OleDLL`
- [NSF2X](https://github.com/adb014/nsf2x/blob/master/mapiex.py#L351)
  - Example of finding a DLL in C2R version of COM object and get a COM object
- [MSL-LoadLib](https://github.com/MSLNZ/msl-loadlib/blob/main/msl/loadlib/load_library.py#L162)
  - Supported: `LIBTYPES = ['cdll', 'windll', 'oledll', 'net', 'clr', 'java', 'com', 'activex']`
- [pywinauto test_backend.py](https://github.com/pywinauto/pywinauto/blob/0da29f04583a9996bcfec10cefda4ddb86b880cc/pywinauto/unittests/test_backend.py#L70)
  - Unit tests for Windows COM threading mode initialization by mocking pythoncom.CoInitializeEx
- [Spark](https://github.com/xya/Spark/blob/master/src/spark/gui/filetypes/win32.py)
  - `CoInitializeEx = windll.ole32.CoInitializeEx`
- [pystrict3](https://github.com/JohannesBuchner/pystrict3/blob/master/tests/data/recipe-308035.py)
  - Manual `pythoncom.CoInitializeEx(pythoncom.COINIT_APARTMENTTHREADED)` and `pythoncom.CoUninitialize()`

- [pywin32-stubs](https://github.com/kaluluosi/pywin32-stubs/tree/master/win32-stubs)
  - pywin32-stubs is generated from pywin32.chm
- [pymfc](https://github.com/atsuoishimoto/pymfc)
- [r2com](https://github.com/newlog/r2com)
  - Reversing a binary calling the CoCreateInstance function from the OLE32.DLL library
  - <https://reverseengineering.stackexchange.com/questions/2822/com-interface-methods/2823#2823>
- [ComIDA](https://github.com/airbus-cert/comida/blob/master/comida.py#L371)
  - `ea_cocreateinstance = find_import("ole32", "CoCreateInstance") or find_import("api-ms-win-core-com-l1-1-0", "CoCreateInstance")`

Other language bindings to COM

- [Go OLE](https://github.com/go-ole/go-ole)

C/C++ Examples

- [Fastboi](https://github.com/DXPower/Fastboi)
  - A lightweight and simple C++20 game engine written over SDL2. It implements a basic component model and event system.
- [Win32batch-GokhleSir](https://github.com/lihas/Win32CodingAssignments)
  - COM, Class factory, Containment, Aggregation, Automation, etc.
- [CommeCOM](https://github.com/alexonea/CommeCOM)
  - Header-only library providing basic means for working with "comme" (like) COM objects - querying interfaces and acccessing functionality from dynamically loaded plug-ins (DLLs or shared objects)
- [EasyOLE: C/C++ OLE Automation Client Library](https://github.com/abhisek/EasyOLE)
  - Ease the development of OLE Automation Clients in C/C++ handling the internal not-so-friendly aspects of COM interfaces
- [OLEVIEW Sample: ActiveX Object Viewer](https://github.com/microsoft/VCSamples/tree/master/VC2010Samples/MFC/ole/oleview)
  - Illustrates how to implement ActiveX Object viewers through custom ActiveX interfaces
- [MapWinGis](https://github.com/orapow/MapWinGis/blob/master/src/Utilities/ComHelper.cpp)

Writing COM Applications

- [OLE Component Object Model](https://docs.microsoft.com/en-us/windows/win32/multimedia/c---and-ole-programming-concepts)
  - General overview of COM
- [Get Started with Win32 and C++](https://docs.microsoft.com/en-us/windows/win32/learnwin32/learn-to-program-for-windows)
  - Write a desktop program in C++ using Win32 and COM APIs
- [COM Clients and Servers](https://docs.microsoft.com/en-us/windows/win32/com/com-clients-and-servers)
  - Getting a Pointer to an Object, COM Glossary, etc.
- [Active Template Library (ATL) Concepts](https://docs.microsoft.com/en-us/cpp/atl/active-template-library-atl-concepts?view=msvc-160)
  - Active Template Library (ATL) is a set of template-based C++ classes that let you create small, fast Component Object Model (COM) objects
  - CComPtr Class from atlbase.h

COM API Reference

- [Windows System Services APIs](https://docs.microsoft.com/en-us/windows/win32/apiindex/windows-api-list#system-services)
  - COM, COM+
- [Component Object Model (COM)](https://docs.microsoft.com/en-us/windows/win32/api/_com/)
  - Overview of the Component Object Model (COM) technology, header files, methods e.g. IUnknown interface (unknwn.h)

Books

- Essential COM by Don Box
- Atl Internals by Brent Rector
- Inside COM by Dale Rogerson
- Inside COM+ by Guy Eddon and Henry Eddon <https://thrysoee.dk/InsideCOM+/ch03b.htm>
