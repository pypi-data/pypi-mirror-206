"""_989.py

FaceGearPinionDesign
"""
from mastapy._internal import constructor
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.gears.gear_designs.face import _984
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_PINION_DESIGN = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Face', 'FaceGearPinionDesign')


__docformat__ = 'restructuredtext en'
__all__ = ('FaceGearPinionDesign',)


class FaceGearPinionDesign(_984.FaceGearDesign):
    """FaceGearPinionDesign

    This is a mastapy class.
    """

    TYPE = _FACE_GEAR_PINION_DESIGN

    class _Cast_FaceGearPinionDesign:
        """Special nested class for casting FaceGearPinionDesign to subclasses."""

        def __init__(self, parent: 'FaceGearPinionDesign'):
            self._parent = parent

        @property
        def face_gear_design(self):
            return self._parent._cast(_984.FaceGearDesign)

        @property
        def gear_design(self):
            from mastapy.gears.gear_designs import _942
            
            return self._parent._cast(_942.GearDesign)

        @property
        def gear_design_component(self):
            from mastapy.gears.gear_designs import _943
            
            return self._parent._cast(_943.GearDesignComponent)

        @property
        def face_gear_pinion_design(self) -> 'FaceGearPinionDesign':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'FaceGearPinionDesign.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def base_diameter(self) -> 'float':
        """float: 'BaseDiameter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BaseDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def base_thickness_half_angle(self) -> 'float':
        """float: 'BaseThicknessHalfAngle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BaseThicknessHalfAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def face_width(self) -> 'float':
        """float: 'FaceWidth' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FaceWidth

        if temp is None:
            return 0.0

        return temp

    @property
    def fillet_radius(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'FilletRadius' is the original name of this property."""

        temp = self.wrapped.FilletRadius

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @fillet_radius.setter
    def fillet_radius(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.FilletRadius = value

    @property
    def normal_thickness(self) -> 'float':
        """float: 'NormalThickness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NormalThickness

        if temp is None:
            return 0.0

        return temp

    @property
    def pitch_cone_angle_with_gear(self) -> 'float':
        """float: 'PitchConeAngleWithGear' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PitchConeAngleWithGear

        if temp is None:
            return 0.0

        return temp

    @property
    def profile_shift_coefficient(self) -> 'float':
        """float: 'ProfileShiftCoefficient' is the original name of this property."""

        temp = self.wrapped.ProfileShiftCoefficient

        if temp is None:
            return 0.0

        return temp

    @profile_shift_coefficient.setter
    def profile_shift_coefficient(self, value: 'float'):
        self.wrapped.ProfileShiftCoefficient = float(value) if value else 0.0

    @property
    def root_diameter(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'RootDiameter' is the original name of this property."""

        temp = self.wrapped.RootDiameter

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @root_diameter.setter
    def root_diameter(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.RootDiameter = value

    @property
    def tip_diameter(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'TipDiameter' is the original name of this property."""

        temp = self.wrapped.TipDiameter

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @tip_diameter.setter
    def tip_diameter(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.TipDiameter = value

    @property
    def whole_depth(self) -> 'float':
        """float: 'WholeDepth' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WholeDepth

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self) -> 'FaceGearPinionDesign._Cast_FaceGearPinionDesign':
        return self._Cast_FaceGearPinionDesign(self)
