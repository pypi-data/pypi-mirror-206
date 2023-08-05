"""_708.py

CylindricalGearRealCutterDesign
"""
from PIL.Image import Image

from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor, conversion
from mastapy.gears.manufacturing.cylindrical.cutters import _699, _701
from mastapy.gears.manufacturing.cylindrical.cutters.tangibles import _718
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_REAL_CUTTER_DESIGN = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Cylindrical.Cutters', 'CylindricalGearRealCutterDesign')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearRealCutterDesign',)


class CylindricalGearRealCutterDesign(_701.CylindricalGearAbstractCutterDesign):
    """CylindricalGearRealCutterDesign

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_REAL_CUTTER_DESIGN

    class _Cast_CylindricalGearRealCutterDesign:
        """Special nested class for casting CylindricalGearRealCutterDesign to subclasses."""

        def __init__(self, parent: 'CylindricalGearRealCutterDesign'):
            self._parent = parent

        @property
        def cylindrical_gear_abstract_cutter_design(self):
            return self._parent._cast(_701.CylindricalGearAbstractCutterDesign)

        @property
        def named_database_item(self):
            from mastapy.utility.databases import _1816
            
            return self._parent._cast(_1816.NamedDatabaseItem)

        @property
        def cylindrical_gear_form_grinding_wheel(self):
            from mastapy.gears.manufacturing.cylindrical.cutters import _702
            
            return self._parent._cast(_702.CylindricalGearFormGrindingWheel)

        @property
        def cylindrical_gear_grinding_worm(self):
            from mastapy.gears.manufacturing.cylindrical.cutters import _703
            
            return self._parent._cast(_703.CylindricalGearGrindingWorm)

        @property
        def cylindrical_gear_hob_design(self):
            from mastapy.gears.manufacturing.cylindrical.cutters import _704
            
            return self._parent._cast(_704.CylindricalGearHobDesign)

        @property
        def cylindrical_gear_plunge_shaver(self):
            from mastapy.gears.manufacturing.cylindrical.cutters import _705
            
            return self._parent._cast(_705.CylindricalGearPlungeShaver)

        @property
        def cylindrical_gear_rack_design(self):
            from mastapy.gears.manufacturing.cylindrical.cutters import _707
            
            return self._parent._cast(_707.CylindricalGearRackDesign)

        @property
        def cylindrical_gear_shaper(self):
            from mastapy.gears.manufacturing.cylindrical.cutters import _709
            
            return self._parent._cast(_709.CylindricalGearShaper)

        @property
        def cylindrical_gear_shaver(self):
            from mastapy.gears.manufacturing.cylindrical.cutters import _710
            
            return self._parent._cast(_710.CylindricalGearShaver)

        @property
        def involute_cutter_design(self):
            from mastapy.gears.manufacturing.cylindrical.cutters import _713
            
            return self._parent._cast(_713.InvoluteCutterDesign)

        @property
        def cylindrical_gear_real_cutter_design(self) -> 'CylindricalGearRealCutterDesign':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CylindricalGearRealCutterDesign.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cutter_and_gear_normal_base_pitch_comparison_tolerance(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'CutterAndGearNormalBasePitchComparisonTolerance' is the original name of this property."""

        temp = self.wrapped.CutterAndGearNormalBasePitchComparisonTolerance

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @cutter_and_gear_normal_base_pitch_comparison_tolerance.setter
    def cutter_and_gear_normal_base_pitch_comparison_tolerance(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.CutterAndGearNormalBasePitchComparisonTolerance = value

    @property
    def has_tolerances(self) -> 'bool':
        """bool: 'HasTolerances' is the original name of this property."""

        temp = self.wrapped.HasTolerances

        if temp is None:
            return False

        return temp

    @has_tolerances.setter
    def has_tolerances(self, value: 'bool'):
        self.wrapped.HasTolerances = bool(value) if value else False

    @property
    def nominal_cutter_drawing(self) -> 'Image':
        """Image: 'NominalCutterDrawing' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NominalCutterDrawing

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)
        return value

    @property
    def normal_base_pitch(self) -> 'float':
        """float: 'NormalBasePitch' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NormalBasePitch

        if temp is None:
            return 0.0

        return temp

    @property
    def normal_pitch(self) -> 'float':
        """float: 'NormalPitch' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NormalPitch

        if temp is None:
            return 0.0

        return temp

    @property
    def normal_pressure_angle_constant_base_pitch(self) -> 'float':
        """float: 'NormalPressureAngleConstantBasePitch' is the original name of this property."""

        temp = self.wrapped.NormalPressureAngleConstantBasePitch

        if temp is None:
            return 0.0

        return temp

    @normal_pressure_angle_constant_base_pitch.setter
    def normal_pressure_angle_constant_base_pitch(self, value: 'float'):
        self.wrapped.NormalPressureAngleConstantBasePitch = float(value) if value else 0.0

    @property
    def number_of_points_for_reporting_fillet_shape(self) -> 'overridable.Overridable_int':
        """overridable.Overridable_int: 'NumberOfPointsForReportingFilletShape' is the original name of this property."""

        temp = self.wrapped.NumberOfPointsForReportingFilletShape

        if temp is None:
            return 0

        return constructor.new_from_mastapy_type(overridable.Overridable_int)(temp) if temp is not None else 0

    @number_of_points_for_reporting_fillet_shape.setter
    def number_of_points_for_reporting_fillet_shape(self, value: 'overridable.Overridable_int.implicit_type()'):
        wrapper_type = overridable.Overridable_int.wrapper_type()
        enclosed_type = overridable.Overridable_int.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0, is_overridden)
        self.wrapped.NumberOfPointsForReportingFilletShape = value

    @property
    def number_of_points_for_reporting_main_blade_shape(self) -> 'overridable.Overridable_int':
        """overridable.Overridable_int: 'NumberOfPointsForReportingMainBladeShape' is the original name of this property."""

        temp = self.wrapped.NumberOfPointsForReportingMainBladeShape

        if temp is None:
            return 0

        return constructor.new_from_mastapy_type(overridable.Overridable_int)(temp) if temp is not None else 0

    @number_of_points_for_reporting_main_blade_shape.setter
    def number_of_points_for_reporting_main_blade_shape(self, value: 'overridable.Overridable_int.implicit_type()'):
        wrapper_type = overridable.Overridable_int.wrapper_type()
        enclosed_type = overridable.Overridable_int.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0, is_overridden)
        self.wrapped.NumberOfPointsForReportingMainBladeShape = value

    @property
    def specify_custom_blade_shape(self) -> 'bool':
        """bool: 'SpecifyCustomBladeShape' is the original name of this property."""

        temp = self.wrapped.SpecifyCustomBladeShape

        if temp is None:
            return False

        return temp

    @specify_custom_blade_shape.setter
    def specify_custom_blade_shape(self, value: 'bool'):
        self.wrapped.SpecifyCustomBladeShape = bool(value) if value else False

    @property
    def customised_cutting_edge_profile(self) -> '_699.CustomisableEdgeProfile':
        """CustomisableEdgeProfile: 'CustomisedCuttingEdgeProfile' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CustomisedCuttingEdgeProfile

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def nominal_cutter_shape(self) -> '_718.CutterShapeDefinition':
        """CutterShapeDefinition: 'NominalCutterShape' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NominalCutterShape

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'CylindricalGearRealCutterDesign._Cast_CylindricalGearRealCutterDesign':
        return self._Cast_CylindricalGearRealCutterDesign(self)
