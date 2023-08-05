"""_960.py

StraightBevelDiffGearDesign
"""
from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy.gears.gear_designs.bevel import _1179, _1174
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_DIFF_GEAR_DESIGN = python_net_import('SMT.MastaAPI.Gears.GearDesigns.StraightBevelDiff', 'StraightBevelDiffGearDesign')


__docformat__ = 'restructuredtext en'
__all__ = ('StraightBevelDiffGearDesign',)


class StraightBevelDiffGearDesign(_1174.BevelGearDesign):
    """StraightBevelDiffGearDesign

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_DIFF_GEAR_DESIGN

    class _Cast_StraightBevelDiffGearDesign:
        """Special nested class for casting StraightBevelDiffGearDesign to subclasses."""

        def __init__(self, parent: 'StraightBevelDiffGearDesign'):
            self._parent = parent

        @property
        def bevel_gear_design(self):
            return self._parent._cast(_1174.BevelGearDesign)

        @property
        def agma_gleason_conical_gear_design(self):
            from mastapy.gears.gear_designs.agma_gleason_conical import _1187
            
            return self._parent._cast(_1187.AGMAGleasonConicalGearDesign)

        @property
        def conical_gear_design(self):
            from mastapy.gears.gear_designs.conical import _1148
            
            return self._parent._cast(_1148.ConicalGearDesign)

        @property
        def gear_design(self):
            from mastapy.gears.gear_designs import _942
            
            return self._parent._cast(_942.GearDesign)

        @property
        def gear_design_component(self):
            from mastapy.gears.gear_designs import _943
            
            return self._parent._cast(_943.GearDesignComponent)

        @property
        def straight_bevel_diff_gear_design(self) -> 'StraightBevelDiffGearDesign':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'StraightBevelDiffGearDesign.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def allowable_peak_bending_stress(self) -> 'float':
        """float: 'AllowablePeakBendingStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AllowablePeakBendingStress

        if temp is None:
            return 0.0

        return temp

    @property
    def allowable_performance_bending_stress(self) -> 'float':
        """float: 'AllowablePerformanceBendingStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AllowablePerformanceBendingStress

        if temp is None:
            return 0.0

        return temp

    @property
    def edge_radius(self) -> 'float':
        """float: 'EdgeRadius' is the original name of this property."""

        temp = self.wrapped.EdgeRadius

        if temp is None:
            return 0.0

        return temp

    @edge_radius.setter
    def edge_radius(self, value: 'float'):
        self.wrapped.EdgeRadius = float(value) if value else 0.0

    @property
    def edge_radius_from(self) -> '_1179.EdgeRadiusType':
        """EdgeRadiusType: 'EdgeRadiusFrom' is the original name of this property."""

        temp = self.wrapped.EdgeRadiusFrom

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, _1179.EdgeRadiusType)
        return constructor.new_from_mastapy_type(_1179.EdgeRadiusType)(value) if value is not None else None

    @edge_radius_from.setter
    def edge_radius_from(self, value: '_1179.EdgeRadiusType'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value, _1179.EdgeRadiusType.type_())
        self.wrapped.EdgeRadiusFrom = value

    @property
    def limited_point_width_large_end(self) -> 'float':
        """float: 'LimitedPointWidthLargeEnd' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LimitedPointWidthLargeEnd

        if temp is None:
            return 0.0

        return temp

    @property
    def limited_point_width_small_end(self) -> 'float':
        """float: 'LimitedPointWidthSmallEnd' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LimitedPointWidthSmallEnd

        if temp is None:
            return 0.0

        return temp

    @property
    def max_radius_cutter_blades(self) -> 'float':
        """float: 'MaxRadiusCutterBlades' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaxRadiusCutterBlades

        if temp is None:
            return 0.0

        return temp

    @property
    def max_radius_interference(self) -> 'float':
        """float: 'MaxRadiusInterference' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaxRadiusInterference

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_edge_radius(self) -> 'float':
        """float: 'MaximumEdgeRadius' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumEdgeRadius

        if temp is None:
            return 0.0

        return temp

    @property
    def outer_chordal_addendum(self) -> 'float':
        """float: 'OuterChordalAddendum' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterChordalAddendum

        if temp is None:
            return 0.0

        return temp

    @property
    def outer_chordal_thickness(self) -> 'float':
        """float: 'OuterChordalThickness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterChordalThickness

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self) -> 'StraightBevelDiffGearDesign._Cast_StraightBevelDiffGearDesign':
        return self._Cast_StraightBevelDiffGearDesign(self)
