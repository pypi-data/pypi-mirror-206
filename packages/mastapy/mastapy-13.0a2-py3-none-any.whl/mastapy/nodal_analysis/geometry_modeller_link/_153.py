"""_153.py

GeometryModellerCountDimension
"""
from mastapy._internal import constructor
from mastapy.nodal_analysis.geometry_modeller_link import _151
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEOMETRY_MODELLER_COUNT_DIMENSION = python_net_import('SMT.MastaAPI.NodalAnalysis.GeometryModellerLink', 'GeometryModellerCountDimension')


__docformat__ = 'restructuredtext en'
__all__ = ('GeometryModellerCountDimension',)


class GeometryModellerCountDimension(_151.BaseGeometryModellerDimension):
    """GeometryModellerCountDimension

    This is a mastapy class.
    """

    TYPE = _GEOMETRY_MODELLER_COUNT_DIMENSION

    class _Cast_GeometryModellerCountDimension:
        """Special nested class for casting GeometryModellerCountDimension to subclasses."""

        def __init__(self, parent: 'GeometryModellerCountDimension'):
            self._parent = parent

        @property
        def base_geometry_modeller_dimension(self):
            return self._parent._cast(_151.BaseGeometryModellerDimension)

        @property
        def geometry_modeller_count_dimension(self) -> 'GeometryModellerCountDimension':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GeometryModellerCountDimension.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def count(self) -> 'int':
        """int: 'Count' is the original name of this property."""

        temp = self.wrapped.Count

        if temp is None:
            return 0

        return temp

    @count.setter
    def count(self, value: 'int'):
        self.wrapped.Count = int(value) if value else 0

    @property
    def cast_to(self) -> 'GeometryModellerCountDimension._Cast_GeometryModellerCountDimension':
        return self._Cast_GeometryModellerCountDimension(self)
