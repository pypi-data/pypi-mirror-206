"""_155.py

GeometryModellerDimension
"""
from mastapy.nodal_analysis.geometry_modeller_link import _157
from mastapy._internal import enum_with_selected_value_runtime, constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEOMETRY_MODELLER_DIMENSION = python_net_import('SMT.MastaAPI.NodalAnalysis.GeometryModellerLink', 'GeometryModellerDimension')


__docformat__ = 'restructuredtext en'
__all__ = ('GeometryModellerDimension',)


class GeometryModellerDimension(_0.APIBase):
    """GeometryModellerDimension

    This is a mastapy class.
    """

    TYPE = _GEOMETRY_MODELLER_DIMENSION

    class _Cast_GeometryModellerDimension:
        """Special nested class for casting GeometryModellerDimension to subclasses."""

        def __init__(self, parent: 'GeometryModellerDimension'):
            self._parent = parent

        @property
        def geometry_modeller_dimension(self) -> 'GeometryModellerDimension':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GeometryModellerDimension.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def type_(self) -> '_157.GeometryModellerDimensionType':
        """GeometryModellerDimensionType: 'Type' is the original name of this property."""

        temp = self.wrapped.Type

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, _157.GeometryModellerDimensionType)
        return constructor.new_from_mastapy_type(_157.GeometryModellerDimensionType)(value) if value is not None else None

    @type_.setter
    def type_(self, value: '_157.GeometryModellerDimensionType'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value, _157.GeometryModellerDimensionType.type_())
        self.wrapped.Type = value

    @property
    def value(self) -> 'float':
        """float: 'Value' is the original name of this property."""

        temp = self.wrapped.Value

        if temp is None:
            return 0.0

        return temp

    @value.setter
    def value(self, value: 'float'):
        self.wrapped.Value = float(value) if value else 0.0

    @property
    def cast_to(self) -> 'GeometryModellerDimension._Cast_GeometryModellerDimension':
        return self._Cast_GeometryModellerDimension(self)
