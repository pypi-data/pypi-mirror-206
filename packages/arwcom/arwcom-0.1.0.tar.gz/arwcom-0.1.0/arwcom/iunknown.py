# C:\Program Files (x86)\Windows Kits\10\Include\xx.x.xxxxx.x\um\Unknwnbase.h
# C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\VC\Tools\MSVC\xx.xx.xxxxx\atlmfc\include\atlcomcli.h

from arwcom.guiddef import GUID


class _COMInterfaceMetaClass(type):
    # handle com shutting down

    def __new__(self, name, bases, dct):
        """[summary]

        :param name: specifies the class name, becomes the __name__ attribute of the class.
        :type name: [type]
        :param bases: specifies a tuple of the base classes from which the class inherits, becomes the __bases__ attribute of the class.
        :type bases: [type]
        :param dct: specifies a namespace dictionary containing definitions for the class body, becomes the __dict__ attribute of the class.
        :type dct: [type]
        """

        cls = type.__new__(self, name, bases, dct)


class IUnknown(object):
    _iid = GUID("{00000000-0000-0000-C000-000000000046}")
