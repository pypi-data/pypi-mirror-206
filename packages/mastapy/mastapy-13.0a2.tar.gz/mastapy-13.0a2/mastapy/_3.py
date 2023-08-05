"""_3.py

PythonUtility
"""
from mastapy._internal import constructor
from mastapy._internal.class_property import classproperty
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PYTHON_UTILITY = python_net_import('SMT.MastaAPI', 'PythonUtility')


__docformat__ = 'restructuredtext en'
__all__ = ('PythonUtility',)


class PythonUtility:
    """PythonUtility

    This is a mastapy class.
    """

    TYPE = _PYTHON_UTILITY

    class _Cast_PythonUtility:
        """Special nested class for casting PythonUtility to subclasses."""

        def __init__(self, parent: 'PythonUtility'):
            self._parent = parent

        @property
        def python_utility(self) -> 'PythonUtility':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'PythonUtility.TYPE'):
        self.wrapped = instance_to_wrap
        if not hasattr(self.wrapped, 'reference_count'):
            self.wrapped.reference_count = 0
        self.wrapped.reference_count += 1

    @classproperty
    def python_install_directory(cls) -> 'str':
        """str: 'PythonInstallDirectory' is the original name of this property."""

        temp = PythonUtility.TYPE.PythonInstallDirectory

        if temp is None:
            return ''

        return temp

    @python_install_directory.setter
    def python_install_directory(cls, value: 'str'):
        PythonUtility.TYPE.PythonInstallDirectory = str(value) if value else ''

    @property
    def cast_to(self) -> 'PythonUtility._Cast_PythonUtility':
        return self._Cast_PythonUtility(self)
