"""_2156.py

TaperRollerBearing
"""
from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy.bearings import _1861
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.bearings.bearing_designs.rolling import _2146
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TAPER_ROLLER_BEARING = python_net_import('SMT.MastaAPI.Bearings.BearingDesigns.Rolling', 'TaperRollerBearing')


__docformat__ = 'restructuredtext en'
__all__ = ('TaperRollerBearing',)


class TaperRollerBearing(_2146.NonBarrelRollerBearing):
    """TaperRollerBearing

    This is a mastapy class.
    """

    TYPE = _TAPER_ROLLER_BEARING

    class _Cast_TaperRollerBearing:
        """Special nested class for casting TaperRollerBearing to subclasses."""

        def __init__(self, parent: 'TaperRollerBearing'):
            self._parent = parent

        @property
        def non_barrel_roller_bearing(self):
            return self._parent._cast(_2146.NonBarrelRollerBearing)

        @property
        def roller_bearing(self):
            from mastapy.bearings.bearing_designs.rolling import _2147
            
            return self._parent._cast(_2147.RollerBearing)

        @property
        def rolling_bearing(self):
            from mastapy.bearings.bearing_designs.rolling import _2150
            
            return self._parent._cast(_2150.RollingBearing)

        @property
        def detailed_bearing(self):
            from mastapy.bearings.bearing_designs import _2116
            
            return self._parent._cast(_2116.DetailedBearing)

        @property
        def non_linear_bearing(self):
            from mastapy.bearings.bearing_designs import _2119
            
            return self._parent._cast(_2119.NonLinearBearing)

        @property
        def bearing_design(self):
            from mastapy.bearings.bearing_designs import _2115
            
            return self._parent._cast(_2115.BearingDesign)

        @property
        def taper_roller_bearing(self) -> 'TaperRollerBearing':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'TaperRollerBearing.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembled_width(self) -> 'float':
        """float: 'AssembledWidth' is the original name of this property."""

        temp = self.wrapped.AssembledWidth

        if temp is None:
            return 0.0

        return temp

    @assembled_width.setter
    def assembled_width(self, value: 'float'):
        self.wrapped.AssembledWidth = float(value) if value else 0.0

    @property
    def bearing_measurement_type(self) -> '_1861.BearingMeasurementType':
        """BearingMeasurementType: 'BearingMeasurementType' is the original name of this property."""

        temp = self.wrapped.BearingMeasurementType

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, _1861.BearingMeasurementType)
        return constructor.new_from_mastapy_type(_1861.BearingMeasurementType)(value) if value is not None else None

    @bearing_measurement_type.setter
    def bearing_measurement_type(self, value: '_1861.BearingMeasurementType'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value, _1861.BearingMeasurementType.type_())
        self.wrapped.BearingMeasurementType = value

    @property
    def cone_angle(self) -> 'float':
        """float: 'ConeAngle' is the original name of this property."""

        temp = self.wrapped.ConeAngle

        if temp is None:
            return 0.0

        return temp

    @cone_angle.setter
    def cone_angle(self, value: 'float'):
        self.wrapped.ConeAngle = float(value) if value else 0.0

    @property
    def cup_angle(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'CupAngle' is the original name of this property."""

        temp = self.wrapped.CupAngle

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @cup_angle.setter
    def cup_angle(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.CupAngle = value

    @property
    def effective_centre_from_front_face(self) -> 'float':
        """float: 'EffectiveCentreFromFrontFace' is the original name of this property."""

        temp = self.wrapped.EffectiveCentreFromFrontFace

        if temp is None:
            return 0.0

        return temp

    @effective_centre_from_front_face.setter
    def effective_centre_from_front_face(self, value: 'float'):
        self.wrapped.EffectiveCentreFromFrontFace = float(value) if value else 0.0

    @property
    def effective_centre_to_front_face_set_by_changing_outer_ring_offset(self) -> 'float':
        """float: 'EffectiveCentreToFrontFaceSetByChangingOuterRingOffset' is the original name of this property."""

        temp = self.wrapped.EffectiveCentreToFrontFaceSetByChangingOuterRingOffset

        if temp is None:
            return 0.0

        return temp

    @effective_centre_to_front_face_set_by_changing_outer_ring_offset.setter
    def effective_centre_to_front_face_set_by_changing_outer_ring_offset(self, value: 'float'):
        self.wrapped.EffectiveCentreToFrontFaceSetByChangingOuterRingOffset = float(value) if value else 0.0

    @property
    def element_taper_angle(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'ElementTaperAngle' is the original name of this property."""

        temp = self.wrapped.ElementTaperAngle

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @element_taper_angle.setter
    def element_taper_angle(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.ElementTaperAngle = value

    @property
    def inner_ring_back_face_corner_radius(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'InnerRingBackFaceCornerRadius' is the original name of this property."""

        temp = self.wrapped.InnerRingBackFaceCornerRadius

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @inner_ring_back_face_corner_radius.setter
    def inner_ring_back_face_corner_radius(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.InnerRingBackFaceCornerRadius = value

    @property
    def inner_ring_front_face_corner_radius(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'InnerRingFrontFaceCornerRadius' is the original name of this property."""

        temp = self.wrapped.InnerRingFrontFaceCornerRadius

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @inner_ring_front_face_corner_radius.setter
    def inner_ring_front_face_corner_radius(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.InnerRingFrontFaceCornerRadius = value

    @property
    def left_element_corner_radius(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'LeftElementCornerRadius' is the original name of this property."""

        temp = self.wrapped.LeftElementCornerRadius

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @left_element_corner_radius.setter
    def left_element_corner_radius(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.LeftElementCornerRadius = value

    @property
    def mean_inner_race_diameter(self) -> 'float':
        """float: 'MeanInnerRaceDiameter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeanInnerRaceDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def mean_outer_race_diameter(self) -> 'float':
        """float: 'MeanOuterRaceDiameter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeanOuterRaceDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def outer_ring_back_face_corner_radius(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'OuterRingBackFaceCornerRadius' is the original name of this property."""

        temp = self.wrapped.OuterRingBackFaceCornerRadius

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @outer_ring_back_face_corner_radius.setter
    def outer_ring_back_face_corner_radius(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.OuterRingBackFaceCornerRadius = value

    @property
    def outer_ring_front_face_corner_radius(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'OuterRingFrontFaceCornerRadius' is the original name of this property."""

        temp = self.wrapped.OuterRingFrontFaceCornerRadius

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @outer_ring_front_face_corner_radius.setter
    def outer_ring_front_face_corner_radius(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.OuterRingFrontFaceCornerRadius = value

    @property
    def right_element_corner_radius(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'RightElementCornerRadius' is the original name of this property."""

        temp = self.wrapped.RightElementCornerRadius

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @right_element_corner_radius.setter
    def right_element_corner_radius(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.RightElementCornerRadius = value

    @property
    def width(self) -> 'float':
        """float: 'Width' is the original name of this property."""

        temp = self.wrapped.Width

        if temp is None:
            return 0.0

        return temp

    @width.setter
    def width(self, value: 'float'):
        self.wrapped.Width = float(value) if value else 0.0

    @property
    def width_setting_inner_and_outer_ring_width(self) -> 'float':
        """float: 'WidthSettingInnerAndOuterRingWidth' is the original name of this property."""

        temp = self.wrapped.WidthSettingInnerAndOuterRingWidth

        if temp is None:
            return 0.0

        return temp

    @width_setting_inner_and_outer_ring_width.setter
    def width_setting_inner_and_outer_ring_width(self, value: 'float'):
        self.wrapped.WidthSettingInnerAndOuterRingWidth = float(value) if value else 0.0

    @property
    def cast_to(self) -> 'TaperRollerBearing._Cast_TaperRollerBearing':
        return self._Cast_TaperRollerBearing(self)
