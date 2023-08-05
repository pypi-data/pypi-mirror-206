"""_1147.py

ConicalGearCutter
"""
from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy.gears.gear_designs.conical import (
    _1155, _1156, _1165, _1164
)
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_CUTTER = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Conical', 'ConicalGearCutter')


__docformat__ = 'restructuredtext en'
__all__ = ('ConicalGearCutter',)


class ConicalGearCutter(_0.APIBase):
    """ConicalGearCutter

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_CUTTER

    class _Cast_ConicalGearCutter:
        """Special nested class for casting ConicalGearCutter to subclasses."""

        def __init__(self, parent: 'ConicalGearCutter'):
            self._parent = parent

        @property
        def pinion_finish_cutter(self):
            from mastapy.gears.manufacturing.bevel.cutters import _808
            
            return self._parent._cast(_808.PinionFinishCutter)

        @property
        def pinion_rough_cutter(self):
            from mastapy.gears.manufacturing.bevel.cutters import _809
            
            return self._parent._cast(_809.PinionRoughCutter)

        @property
        def wheel_finish_cutter(self):
            from mastapy.gears.manufacturing.bevel.cutters import _810
            
            return self._parent._cast(_810.WheelFinishCutter)

        @property
        def wheel_rough_cutter(self):
            from mastapy.gears.manufacturing.bevel.cutters import _811
            
            return self._parent._cast(_811.WheelRoughCutter)

        @property
        def dummy_conical_gear_cutter(self):
            from mastapy.gears.gear_designs.conical import _1157
            
            return self._parent._cast(_1157.DummyConicalGearCutter)

        @property
        def conical_gear_cutter(self) -> 'ConicalGearCutter':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConicalGearCutter.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def calculated_point_width(self) -> 'float':
        """float: 'CalculatedPointWidth' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CalculatedPointWidth

        if temp is None:
            return 0.0

        return temp

    @property
    def cutter_blade_type(self) -> '_1155.CutterBladeType':
        """CutterBladeType: 'CutterBladeType' is the original name of this property."""

        temp = self.wrapped.CutterBladeType

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, _1155.CutterBladeType)
        return constructor.new_from_mastapy_type(_1155.CutterBladeType)(value) if value is not None else None

    @cutter_blade_type.setter
    def cutter_blade_type(self, value: '_1155.CutterBladeType'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value, _1155.CutterBladeType.type_())
        self.wrapped.CutterBladeType = value

    @property
    def cutter_gauge_length(self) -> '_1156.CutterGaugeLengths':
        """CutterGaugeLengths: 'CutterGaugeLength' is the original name of this property."""

        temp = self.wrapped.CutterGaugeLength

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, _1156.CutterGaugeLengths)
        return constructor.new_from_mastapy_type(_1156.CutterGaugeLengths)(value) if value is not None else None

    @cutter_gauge_length.setter
    def cutter_gauge_length(self, value: '_1156.CutterGaugeLengths'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value, _1156.CutterGaugeLengths.type_())
        self.wrapped.CutterGaugeLength = value

    @property
    def inner_blade_angle_convex(self) -> 'float':
        """float: 'InnerBladeAngleConvex' is the original name of this property."""

        temp = self.wrapped.InnerBladeAngleConvex

        if temp is None:
            return 0.0

        return temp

    @inner_blade_angle_convex.setter
    def inner_blade_angle_convex(self, value: 'float'):
        self.wrapped.InnerBladeAngleConvex = float(value) if value else 0.0

    @property
    def inner_blade_point_radius_convex(self) -> 'float':
        """float: 'InnerBladePointRadiusConvex' is the original name of this property."""

        temp = self.wrapped.InnerBladePointRadiusConvex

        if temp is None:
            return 0.0

        return temp

    @inner_blade_point_radius_convex.setter
    def inner_blade_point_radius_convex(self, value: 'float'):
        self.wrapped.InnerBladePointRadiusConvex = float(value) if value else 0.0

    @property
    def inner_edge_radius_convex(self) -> 'float':
        """float: 'InnerEdgeRadiusConvex' is the original name of this property."""

        temp = self.wrapped.InnerEdgeRadiusConvex

        if temp is None:
            return 0.0

        return temp

    @inner_edge_radius_convex.setter
    def inner_edge_radius_convex(self, value: 'float'):
        self.wrapped.InnerEdgeRadiusConvex = float(value) if value else 0.0

    @property
    def inner_parabolic_apex_location_convex(self) -> 'float':
        """float: 'InnerParabolicApexLocationConvex' is the original name of this property."""

        temp = self.wrapped.InnerParabolicApexLocationConvex

        if temp is None:
            return 0.0

        return temp

    @inner_parabolic_apex_location_convex.setter
    def inner_parabolic_apex_location_convex(self, value: 'float'):
        self.wrapped.InnerParabolicApexLocationConvex = float(value) if value else 0.0

    @property
    def inner_parabolic_coefficient_convex(self) -> 'float':
        """float: 'InnerParabolicCoefficientConvex' is the original name of this property."""

        temp = self.wrapped.InnerParabolicCoefficientConvex

        if temp is None:
            return 0.0

        return temp

    @inner_parabolic_coefficient_convex.setter
    def inner_parabolic_coefficient_convex(self, value: 'float'):
        self.wrapped.InnerParabolicCoefficientConvex = float(value) if value else 0.0

    @property
    def inner_spherical_radius_convex(self) -> 'float':
        """float: 'InnerSphericalRadiusConvex' is the original name of this property."""

        temp = self.wrapped.InnerSphericalRadiusConvex

        if temp is None:
            return 0.0

        return temp

    @inner_spherical_radius_convex.setter
    def inner_spherical_radius_convex(self, value: 'float'):
        self.wrapped.InnerSphericalRadiusConvex = float(value) if value else 0.0

    @property
    def inner_toprem_angle_convex(self) -> 'float':
        """float: 'InnerTopremAngleConvex' is the original name of this property."""

        temp = self.wrapped.InnerTopremAngleConvex

        if temp is None:
            return 0.0

        return temp

    @inner_toprem_angle_convex.setter
    def inner_toprem_angle_convex(self, value: 'float'):
        self.wrapped.InnerTopremAngleConvex = float(value) if value else 0.0

    @property
    def inner_toprem_length_convex(self) -> 'float':
        """float: 'InnerTopremLengthConvex' is the original name of this property."""

        temp = self.wrapped.InnerTopremLengthConvex

        if temp is None:
            return 0.0

        return temp

    @inner_toprem_length_convex.setter
    def inner_toprem_length_convex(self, value: 'float'):
        self.wrapped.InnerTopremLengthConvex = float(value) if value else 0.0

    @property
    def inner_toprem_letter_convex(self) -> '_1165.TopremLetter':
        """TopremLetter: 'InnerTopremLetterConvex' is the original name of this property."""

        temp = self.wrapped.InnerTopremLetterConvex

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, _1165.TopremLetter)
        return constructor.new_from_mastapy_type(_1165.TopremLetter)(value) if value is not None else None

    @inner_toprem_letter_convex.setter
    def inner_toprem_letter_convex(self, value: '_1165.TopremLetter'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value, _1165.TopremLetter.type_())
        self.wrapped.InnerTopremLetterConvex = value

    @property
    def input_toprem_as(self) -> '_1164.TopremEntryType':
        """TopremEntryType: 'InputTopremAs' is the original name of this property."""

        temp = self.wrapped.InputTopremAs

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, _1164.TopremEntryType)
        return constructor.new_from_mastapy_type(_1164.TopremEntryType)(value) if value is not None else None

    @input_toprem_as.setter
    def input_toprem_as(self, value: '_1164.TopremEntryType'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value, _1164.TopremEntryType.type_())
        self.wrapped.InputTopremAs = value

    @property
    def outer_blade_angle_concave(self) -> 'float':
        """float: 'OuterBladeAngleConcave' is the original name of this property."""

        temp = self.wrapped.OuterBladeAngleConcave

        if temp is None:
            return 0.0

        return temp

    @outer_blade_angle_concave.setter
    def outer_blade_angle_concave(self, value: 'float'):
        self.wrapped.OuterBladeAngleConcave = float(value) if value else 0.0

    @property
    def outer_blade_point_radius_concave(self) -> 'float':
        """float: 'OuterBladePointRadiusConcave' is the original name of this property."""

        temp = self.wrapped.OuterBladePointRadiusConcave

        if temp is None:
            return 0.0

        return temp

    @outer_blade_point_radius_concave.setter
    def outer_blade_point_radius_concave(self, value: 'float'):
        self.wrapped.OuterBladePointRadiusConcave = float(value) if value else 0.0

    @property
    def outer_edge_radius_concave(self) -> 'float':
        """float: 'OuterEdgeRadiusConcave' is the original name of this property."""

        temp = self.wrapped.OuterEdgeRadiusConcave

        if temp is None:
            return 0.0

        return temp

    @outer_edge_radius_concave.setter
    def outer_edge_radius_concave(self, value: 'float'):
        self.wrapped.OuterEdgeRadiusConcave = float(value) if value else 0.0

    @property
    def outer_parabolic_apex_location_concave(self) -> 'float':
        """float: 'OuterParabolicApexLocationConcave' is the original name of this property."""

        temp = self.wrapped.OuterParabolicApexLocationConcave

        if temp is None:
            return 0.0

        return temp

    @outer_parabolic_apex_location_concave.setter
    def outer_parabolic_apex_location_concave(self, value: 'float'):
        self.wrapped.OuterParabolicApexLocationConcave = float(value) if value else 0.0

    @property
    def outer_parabolic_coefficient_concave(self) -> 'float':
        """float: 'OuterParabolicCoefficientConcave' is the original name of this property."""

        temp = self.wrapped.OuterParabolicCoefficientConcave

        if temp is None:
            return 0.0

        return temp

    @outer_parabolic_coefficient_concave.setter
    def outer_parabolic_coefficient_concave(self, value: 'float'):
        self.wrapped.OuterParabolicCoefficientConcave = float(value) if value else 0.0

    @property
    def outer_spherical_radius_concave(self) -> 'float':
        """float: 'OuterSphericalRadiusConcave' is the original name of this property."""

        temp = self.wrapped.OuterSphericalRadiusConcave

        if temp is None:
            return 0.0

        return temp

    @outer_spherical_radius_concave.setter
    def outer_spherical_radius_concave(self, value: 'float'):
        self.wrapped.OuterSphericalRadiusConcave = float(value) if value else 0.0

    @property
    def outer_toprem_angle_concave(self) -> 'float':
        """float: 'OuterTopremAngleConcave' is the original name of this property."""

        temp = self.wrapped.OuterTopremAngleConcave

        if temp is None:
            return 0.0

        return temp

    @outer_toprem_angle_concave.setter
    def outer_toprem_angle_concave(self, value: 'float'):
        self.wrapped.OuterTopremAngleConcave = float(value) if value else 0.0

    @property
    def outer_toprem_length_concave(self) -> 'float':
        """float: 'OuterTopremLengthConcave' is the original name of this property."""

        temp = self.wrapped.OuterTopremLengthConcave

        if temp is None:
            return 0.0

        return temp

    @outer_toprem_length_concave.setter
    def outer_toprem_length_concave(self, value: 'float'):
        self.wrapped.OuterTopremLengthConcave = float(value) if value else 0.0

    @property
    def outer_toprem_letter_concave(self) -> '_1165.TopremLetter':
        """TopremLetter: 'OuterTopremLetterConcave' is the original name of this property."""

        temp = self.wrapped.OuterTopremLetterConcave

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, _1165.TopremLetter)
        return constructor.new_from_mastapy_type(_1165.TopremLetter)(value) if value is not None else None

    @outer_toprem_letter_concave.setter
    def outer_toprem_letter_concave(self, value: '_1165.TopremLetter'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value, _1165.TopremLetter.type_())
        self.wrapped.OuterTopremLetterConcave = value

    @property
    def protuberance_at_concave_blade(self) -> 'float':
        """float: 'ProtuberanceAtConcaveBlade' is the original name of this property."""

        temp = self.wrapped.ProtuberanceAtConcaveBlade

        if temp is None:
            return 0.0

        return temp

    @protuberance_at_concave_blade.setter
    def protuberance_at_concave_blade(self, value: 'float'):
        self.wrapped.ProtuberanceAtConcaveBlade = float(value) if value else 0.0

    @property
    def protuberance_at_convex_blade(self) -> 'float':
        """float: 'ProtuberanceAtConvexBlade' is the original name of this property."""

        temp = self.wrapped.ProtuberanceAtConvexBlade

        if temp is None:
            return 0.0

        return temp

    @protuberance_at_convex_blade.setter
    def protuberance_at_convex_blade(self, value: 'float'):
        self.wrapped.ProtuberanceAtConvexBlade = float(value) if value else 0.0

    @property
    def radius(self) -> 'float':
        """float: 'Radius' is the original name of this property."""

        temp = self.wrapped.Radius

        if temp is None:
            return 0.0

        return temp

    @radius.setter
    def radius(self, value: 'float'):
        self.wrapped.Radius = float(value) if value else 0.0

    @property
    def cast_to(self) -> 'ConicalGearCutter._Cast_ConicalGearCutter':
        return self._Cast_ConicalGearCutter(self)
