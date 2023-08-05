"""_152.py

GeometryModellerAngleDimension
"""
from mastapy._internal import constructor
from mastapy.nodal_analysis.geometry_modeller_link import _151
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEOMETRY_MODELLER_ANGLE_DIMENSION = python_net_import('SMT.MastaAPI.NodalAnalysis.GeometryModellerLink', 'GeometryModellerAngleDimension')


__docformat__ = 'restructuredtext en'
__all__ = ('GeometryModellerAngleDimension',)


class GeometryModellerAngleDimension(_151.BaseGeometryModellerDimension):
    """GeometryModellerAngleDimension

    This is a mastapy class.
    """

    TYPE = _GEOMETRY_MODELLER_ANGLE_DIMENSION

    class _Cast_GeometryModellerAngleDimension:
        """Special nested class for casting GeometryModellerAngleDimension to subclasses."""

        def __init__(self, parent: 'GeometryModellerAngleDimension'):
            self._parent = parent

        @property
        def base_geometry_modeller_dimension(self):
            return self._parent._cast(_151.BaseGeometryModellerDimension)

        @property
        def geometry_modeller_angle_dimension(self) -> 'GeometryModellerAngleDimension':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GeometryModellerAngleDimension.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def angle(self) -> 'float':
        """float: 'Angle' is the original name of this property."""

        temp = self.wrapped.Angle

        if temp is None:
            return 0.0

        return temp

    @angle.setter
    def angle(self, value: 'float'):
        self.wrapped.Angle = float(value) if value else 0.0

    @property
    def cast_to(self) -> 'GeometryModellerAngleDimension._Cast_GeometryModellerAngleDimension':
        return self._Cast_GeometryModellerAngleDimension(self)
