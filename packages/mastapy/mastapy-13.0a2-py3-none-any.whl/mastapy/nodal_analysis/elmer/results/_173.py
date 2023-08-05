"""_173.py

Data1D
"""
from typing import List

from mastapy._internal import constructor, conversion
from mastapy.nodal_analysis.elmer.results import _172
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DATA_1D = python_net_import('SMT.MastaAPI.NodalAnalysis.Elmer.Results', 'Data1D')


__docformat__ = 'restructuredtext en'
__all__ = ('Data1D',)


class Data1D(_172.Data):
    """Data1D

    This is a mastapy class.
    """

    TYPE = _DATA_1D

    class _Cast_Data1D:
        """Special nested class for casting Data1D to subclasses."""

        def __init__(self, parent: 'Data1D'):
            self._parent = parent

        @property
        def data(self):
            return self._parent._cast(_172.Data)

        @property
        def data_1d(self) -> 'Data1D':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'Data1D.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def data(self) -> 'List[float]':
        """List[float]: 'Data' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Data

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, float)
        return value

    @property
    def cast_to(self) -> 'Data1D._Cast_Data1D':
        return self._Cast_Data1D(self)
