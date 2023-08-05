"""_1894.py

InterferenceTolerance
"""
from mastapy.bearings.tolerances import _1889, _1886
from mastapy._internal import enum_with_selected_value_runtime, constructor, conversion
from mastapy.bearings import _1873
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INTERFERENCE_TOLERANCE = python_net_import('SMT.MastaAPI.Bearings.Tolerances', 'InterferenceTolerance')


__docformat__ = 'restructuredtext en'
__all__ = ('InterferenceTolerance',)


class InterferenceTolerance(_1886.BearingConnectionComponent):
    """InterferenceTolerance

    This is a mastapy class.
    """

    TYPE = _INTERFERENCE_TOLERANCE

    class _Cast_InterferenceTolerance:
        """Special nested class for casting InterferenceTolerance to subclasses."""

        def __init__(self, parent: 'InterferenceTolerance'):
            self._parent = parent

        @property
        def bearing_connection_component(self):
            return self._parent._cast(_1886.BearingConnectionComponent)

        @property
        def inner_ring_tolerance(self):
            from mastapy.bearings.tolerances import _1891
            
            return self._parent._cast(_1891.InnerRingTolerance)

        @property
        def inner_support_tolerance(self):
            from mastapy.bearings.tolerances import _1892
            
            return self._parent._cast(_1892.InnerSupportTolerance)

        @property
        def outer_ring_tolerance(self):
            from mastapy.bearings.tolerances import _1897
            
            return self._parent._cast(_1897.OuterRingTolerance)

        @property
        def outer_support_tolerance(self):
            from mastapy.bearings.tolerances import _1898
            
            return self._parent._cast(_1898.OuterSupportTolerance)

        @property
        def ring_tolerance(self):
            from mastapy.bearings.tolerances import _1902
            
            return self._parent._cast(_1902.RingTolerance)

        @property
        def support_tolerance(self):
            from mastapy.bearings.tolerances import _1907
            
            return self._parent._cast(_1907.SupportTolerance)

        @property
        def interference_tolerance(self) -> 'InterferenceTolerance':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'InterferenceTolerance.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def definition_option(self) -> '_1889.BearingToleranceDefinitionOptions':
        """BearingToleranceDefinitionOptions: 'DefinitionOption' is the original name of this property."""

        temp = self.wrapped.DefinitionOption

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, _1889.BearingToleranceDefinitionOptions)
        return constructor.new_from_mastapy_type(_1889.BearingToleranceDefinitionOptions)(value) if value is not None else None

    @definition_option.setter
    def definition_option(self, value: '_1889.BearingToleranceDefinitionOptions'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value, _1889.BearingToleranceDefinitionOptions.type_())
        self.wrapped.DefinitionOption = value

    @property
    def mounting_point_surface_finish(self) -> '_1873.MountingPointSurfaceFinishes':
        """MountingPointSurfaceFinishes: 'MountingPointSurfaceFinish' is the original name of this property."""

        temp = self.wrapped.MountingPointSurfaceFinish

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, _1873.MountingPointSurfaceFinishes)
        return constructor.new_from_mastapy_type(_1873.MountingPointSurfaceFinishes)(value) if value is not None else None

    @mounting_point_surface_finish.setter
    def mounting_point_surface_finish(self, value: '_1873.MountingPointSurfaceFinishes'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value, _1873.MountingPointSurfaceFinishes.type_())
        self.wrapped.MountingPointSurfaceFinish = value

    @property
    def non_contacting_diameter(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'NonContactingDiameter' is the original name of this property."""

        temp = self.wrapped.NonContactingDiameter

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @non_contacting_diameter.setter
    def non_contacting_diameter(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.NonContactingDiameter = value

    @property
    def surface_fitting_reduction(self) -> 'float':
        """float: 'SurfaceFittingReduction' is the original name of this property."""

        temp = self.wrapped.SurfaceFittingReduction

        if temp is None:
            return 0.0

        return temp

    @surface_fitting_reduction.setter
    def surface_fitting_reduction(self, value: 'float'):
        self.wrapped.SurfaceFittingReduction = float(value) if value else 0.0

    @property
    def tolerance_lower_limit(self) -> 'float':
        """float: 'ToleranceLowerLimit' is the original name of this property."""

        temp = self.wrapped.ToleranceLowerLimit

        if temp is None:
            return 0.0

        return temp

    @tolerance_lower_limit.setter
    def tolerance_lower_limit(self, value: 'float'):
        self.wrapped.ToleranceLowerLimit = float(value) if value else 0.0

    @property
    def tolerance_upper_limit(self) -> 'float':
        """float: 'ToleranceUpperLimit' is the original name of this property."""

        temp = self.wrapped.ToleranceUpperLimit

        if temp is None:
            return 0.0

        return temp

    @tolerance_upper_limit.setter
    def tolerance_upper_limit(self, value: 'float'):
        self.wrapped.ToleranceUpperLimit = float(value) if value else 0.0

    @property
    def cast_to(self) -> 'InterferenceTolerance._Cast_InterferenceTolerance':
        return self._Cast_InterferenceTolerance(self)
