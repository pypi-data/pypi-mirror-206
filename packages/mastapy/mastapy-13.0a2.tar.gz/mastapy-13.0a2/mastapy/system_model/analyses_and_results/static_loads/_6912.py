"""_6912.py

RootAssemblyLoadCase
"""
from typing import List

from mastapy._internal import constructor, conversion
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.system_model.part_model import _2454
from mastapy.nodal_analysis.varying_input_components import _94, _93, _98
from mastapy.math_utility.control import _1565
from mastapy.system_model.analyses_and_results.static_loads import _6769, _6829, _6783
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROOT_ASSEMBLY_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'RootAssemblyLoadCase')


__docformat__ = 'restructuredtext en'
__all__ = ('RootAssemblyLoadCase',)


class RootAssemblyLoadCase(_6783.AssemblyLoadCase):
    """RootAssemblyLoadCase

    This is a mastapy class.
    """

    TYPE = _ROOT_ASSEMBLY_LOAD_CASE

    class _Cast_RootAssemblyLoadCase:
        """Special nested class for casting RootAssemblyLoadCase to subclasses."""

        def __init__(self, parent: 'RootAssemblyLoadCase'):
            self._parent = parent

        @property
        def assembly_load_case(self):
            return self._parent._cast(_6783.AssemblyLoadCase)

        @property
        def abstract_assembly_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6771
            
            return self._parent._cast(_6771.AbstractAssemblyLoadCase)

        @property
        def part_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6892
            
            return self._parent._cast(_6892.PartLoadCase)

        @property
        def part_analysis(self):
            from mastapy.system_model.analyses_and_results import _2636
            
            return self._parent._cast(_2636.PartAnalysis)

        @property
        def design_entity_single_context_analysis(self):
            from mastapy.system_model.analyses_and_results import _2632
            
            return self._parent._cast(_2632.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(self):
            from mastapy.system_model.analyses_and_results import _2630
            
            return self._parent._cast(_2630.DesignEntityAnalysis)

        @property
        def root_assembly_load_case(self) -> 'RootAssemblyLoadCase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'RootAssemblyLoadCase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def brake_force_gain(self) -> 'float':
        """float: 'BrakeForceGain' is the original name of this property."""

        temp = self.wrapped.BrakeForceGain

        if temp is None:
            return 0.0

        return temp

    @brake_force_gain.setter
    def brake_force_gain(self, value: 'float'):
        self.wrapped.BrakeForceGain = float(value) if value else 0.0

    @property
    def max_brake_force(self) -> 'float':
        """float: 'MaxBrakeForce' is the original name of this property."""

        temp = self.wrapped.MaxBrakeForce

        if temp is None:
            return 0.0

        return temp

    @max_brake_force.setter
    def max_brake_force(self, value: 'float'):
        self.wrapped.MaxBrakeForce = float(value) if value else 0.0

    @property
    def oil_initial_temperature(self) -> 'float':
        """float: 'OilInitialTemperature' is the original name of this property."""

        temp = self.wrapped.OilInitialTemperature

        if temp is None:
            return 0.0

        return temp

    @oil_initial_temperature.setter
    def oil_initial_temperature(self, value: 'float'):
        self.wrapped.OilInitialTemperature = float(value) if value else 0.0

    @property
    def rayleigh_damping_alpha(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'RayleighDampingAlpha' is the original name of this property."""

        temp = self.wrapped.RayleighDampingAlpha

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @rayleigh_damping_alpha.setter
    def rayleigh_damping_alpha(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.RayleighDampingAlpha = value

    @property
    def assembly_design(self) -> '_2454.RootAssembly':
        """RootAssembly: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def brake_force_input_values(self) -> '_94.ForceInputComponent':
        """ForceInputComponent: 'BrakeForceInputValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BrakeForceInputValues

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def drive_cycle_pid_control_settings(self) -> '_1565.PIDControlSettings':
        """PIDControlSettings: 'DriveCyclePIDControlSettings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DriveCyclePIDControlSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def load_case(self) -> '_6769.StaticLoadCase':
        """StaticLoadCase: 'LoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def road_incline_input_values(self) -> '_93.AngleInputComponent':
        """AngleInputComponent: 'RoadInclineInputValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RoadInclineInputValues

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def target_vehicle_speed(self) -> '_98.VelocityInputComponent':
        """VelocityInputComponent: 'TargetVehicleSpeed' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TargetVehicleSpeed

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def supercharger_rotor_sets(self) -> 'List[_6829.CylindricalGearSetLoadCase]':
        """List[CylindricalGearSetLoadCase]: 'SuperchargerRotorSets' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SuperchargerRotorSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'RootAssemblyLoadCase._Cast_RootAssemblyLoadCase':
        return self._Cast_RootAssemblyLoadCase(self)
