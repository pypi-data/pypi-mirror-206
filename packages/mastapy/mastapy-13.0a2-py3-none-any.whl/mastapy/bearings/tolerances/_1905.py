"""_1905.py

SupportDetail
"""
from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy.bearings.tolerances import _1906, _1901, _1893
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SUPPORT_DETAIL = python_net_import('SMT.MastaAPI.Bearings.Tolerances', 'SupportDetail')


__docformat__ = 'restructuredtext en'
__all__ = ('SupportDetail',)


class SupportDetail(_1893.InterferenceDetail):
    """SupportDetail

    This is a mastapy class.
    """

    TYPE = _SUPPORT_DETAIL

    class _Cast_SupportDetail:
        """Special nested class for casting SupportDetail to subclasses."""

        def __init__(self, parent: 'SupportDetail'):
            self._parent = parent

        @property
        def interference_detail(self):
            return self._parent._cast(_1893.InterferenceDetail)

        @property
        def bearing_connection_component(self):
            from mastapy.bearings.tolerances import _1886
            
            return self._parent._cast(_1886.BearingConnectionComponent)

        @property
        def support_detail(self) -> 'SupportDetail':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'SupportDetail.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def angle_of_radial_error(self) -> 'float':
        """float: 'AngleOfRadialError' is the original name of this property."""

        temp = self.wrapped.AngleOfRadialError

        if temp is None:
            return 0.0

        return temp

    @angle_of_radial_error.setter
    def angle_of_radial_error(self, value: 'float'):
        self.wrapped.AngleOfRadialError = float(value) if value else 0.0

    @property
    def material_source(self) -> '_1906.SupportMaterialSource':
        """SupportMaterialSource: 'MaterialSource' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaterialSource

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, _1906.SupportMaterialSource)
        return constructor.new_from_mastapy_type(_1906.SupportMaterialSource)(value) if value is not None else None

    @property
    def radial_error_magnitude(self) -> 'float':
        """float: 'RadialErrorMagnitude' is the original name of this property."""

        temp = self.wrapped.RadialErrorMagnitude

        if temp is None:
            return 0.0

        return temp

    @radial_error_magnitude.setter
    def radial_error_magnitude(self, value: 'float'):
        self.wrapped.RadialErrorMagnitude = float(value) if value else 0.0

    @property
    def radial_specification_method(self) -> '_1901.RadialSpecificationMethod':
        """RadialSpecificationMethod: 'RadialSpecificationMethod' is the original name of this property."""

        temp = self.wrapped.RadialSpecificationMethod

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, _1901.RadialSpecificationMethod)
        return constructor.new_from_mastapy_type(_1901.RadialSpecificationMethod)(value) if value is not None else None

    @radial_specification_method.setter
    def radial_specification_method(self, value: '_1901.RadialSpecificationMethod'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value, _1901.RadialSpecificationMethod.type_())
        self.wrapped.RadialSpecificationMethod = value

    @property
    def theta_x(self) -> 'float':
        """float: 'ThetaX' is the original name of this property."""

        temp = self.wrapped.ThetaX

        if temp is None:
            return 0.0

        return temp

    @theta_x.setter
    def theta_x(self, value: 'float'):
        self.wrapped.ThetaX = float(value) if value else 0.0

    @property
    def theta_y(self) -> 'float':
        """float: 'ThetaY' is the original name of this property."""

        temp = self.wrapped.ThetaY

        if temp is None:
            return 0.0

        return temp

    @theta_y.setter
    def theta_y(self, value: 'float'):
        self.wrapped.ThetaY = float(value) if value else 0.0

    @property
    def x(self) -> 'float':
        """float: 'X' is the original name of this property."""

        temp = self.wrapped.X

        if temp is None:
            return 0.0

        return temp

    @x.setter
    def x(self, value: 'float'):
        self.wrapped.X = float(value) if value else 0.0

    @property
    def y(self) -> 'float':
        """float: 'Y' is the original name of this property."""

        temp = self.wrapped.Y

        if temp is None:
            return 0.0

        return temp

    @y.setter
    def y(self, value: 'float'):
        self.wrapped.Y = float(value) if value else 0.0

    @property
    def z(self) -> 'float':
        """float: 'Z' is the original name of this property."""

        temp = self.wrapped.Z

        if temp is None:
            return 0.0

        return temp

    @z.setter
    def z(self, value: 'float'):
        self.wrapped.Z = float(value) if value else 0.0

    @property
    def cast_to(self) -> 'SupportDetail._Cast_SupportDetail':
        return self._Cast_SupportDetail(self)
