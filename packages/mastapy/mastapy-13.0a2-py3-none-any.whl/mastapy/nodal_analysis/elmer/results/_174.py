"""_174.py

Data3D
"""
from typing import List

from mastapy._internal import constructor, conversion
from mastapy.nodal_analysis.elmer.results import _172
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DATA_3D = python_net_import('SMT.MastaAPI.NodalAnalysis.Elmer.Results', 'Data3D')


__docformat__ = 'restructuredtext en'
__all__ = ('Data3D',)


class Data3D(_172.Data):
    """Data3D

    This is a mastapy class.
    """

    TYPE = _DATA_3D

    class _Cast_Data3D:
        """Special nested class for casting Data3D to subclasses."""

        def __init__(self, parent: 'Data3D'):
            self._parent = parent

        @property
        def data(self):
            return self._parent._cast(_172.Data)

        @property
        def data_3d(self) -> 'Data3D':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'Data3D.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def x_data(self) -> 'List[float]':
        """List[float]: 'XData' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.XData

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, float)
        return value

    @property
    def y_data(self) -> 'List[float]':
        """List[float]: 'YData' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.YData

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, float)
        return value

    @property
    def z_data(self) -> 'List[float]':
        """List[float]: 'ZData' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ZData

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, float)
        return value

    @property
    def cast_to(self) -> 'Data3D._Cast_Data3D':
        return self._Cast_Data3D(self)
