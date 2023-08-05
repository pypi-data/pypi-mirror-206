"""_151.py

BaseGeometryModellerDimension
"""
from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BASE_GEOMETRY_MODELLER_DIMENSION = python_net_import('SMT.MastaAPI.NodalAnalysis.GeometryModellerLink', 'BaseGeometryModellerDimension')


__docformat__ = 'restructuredtext en'
__all__ = ('BaseGeometryModellerDimension',)


class BaseGeometryModellerDimension(_0.APIBase):
    """BaseGeometryModellerDimension

    This is a mastapy class.
    """

    TYPE = _BASE_GEOMETRY_MODELLER_DIMENSION

    class _Cast_BaseGeometryModellerDimension:
        """Special nested class for casting BaseGeometryModellerDimension to subclasses."""

        def __init__(self, parent: 'BaseGeometryModellerDimension'):
            self._parent = parent

        @property
        def geometry_modeller_angle_dimension(self):
            from mastapy.nodal_analysis.geometry_modeller_link import _152
            
            return self._parent._cast(_152.GeometryModellerAngleDimension)

        @property
        def geometry_modeller_count_dimension(self):
            from mastapy.nodal_analysis.geometry_modeller_link import _153
            
            return self._parent._cast(_153.GeometryModellerCountDimension)

        @property
        def geometry_modeller_length_dimension(self):
            from mastapy.nodal_analysis.geometry_modeller_link import _158
            
            return self._parent._cast(_158.GeometryModellerLengthDimension)

        @property
        def geometry_modeller_unitless_dimension(self):
            from mastapy.nodal_analysis.geometry_modeller_link import _160
            
            return self._parent._cast(_160.GeometryModellerUnitlessDimension)

        @property
        def base_geometry_modeller_dimension(self) -> 'BaseGeometryModellerDimension':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'BaseGeometryModellerDimension.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def name(self) -> 'str':
        """str: 'Name' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Name

        if temp is None:
            return ''

        return temp

    @property
    def cast_to(self) -> 'BaseGeometryModellerDimension._Cast_BaseGeometryModellerDimension':
        return self._Cast_BaseGeometryModellerDimension(self)
