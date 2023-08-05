"""_2737.py

FlexiblePinAssemblySystemDeflection
"""
from typing import List

from mastapy._internal import constructor, conversion
from mastapy.system_model.part_model import _2434
from mastapy.system_model.analyses_and_results.static_loads import _6852
from mastapy.system_model.analyses_and_results.system_deflections import (
    _2783, _2721, _2677, _2780,
    _2757, _2762, _2724, _2785
)
from mastapy.system_model.analyses_and_results.power_flows import _4067
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FLEXIBLE_PIN_ASSEMBLY_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections', 'FlexiblePinAssemblySystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('FlexiblePinAssemblySystemDeflection',)


class FlexiblePinAssemblySystemDeflection(_2785.SpecialisedAssemblySystemDeflection):
    """FlexiblePinAssemblySystemDeflection

    This is a mastapy class.
    """

    TYPE = _FLEXIBLE_PIN_ASSEMBLY_SYSTEM_DEFLECTION

    class _Cast_FlexiblePinAssemblySystemDeflection:
        """Special nested class for casting FlexiblePinAssemblySystemDeflection to subclasses."""

        def __init__(self, parent: 'FlexiblePinAssemblySystemDeflection'):
            self._parent = parent

        @property
        def specialised_assembly_system_deflection(self):
            return self._parent._cast(_2785.SpecialisedAssemblySystemDeflection)

        @property
        def abstract_assembly_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2664
            
            return self._parent._cast(_2664.AbstractAssemblySystemDeflection)

        @property
        def part_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2764
            
            return self._parent._cast(_2764.PartSystemDeflection)

        @property
        def part_fe_analysis(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7509
            
            return self._parent._cast(_7509.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7510
            
            return self._parent._cast(_7510.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7507
            
            return self._parent._cast(_7507.PartAnalysisCase)

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
        def flexible_pin_assembly_system_deflection(self) -> 'FlexiblePinAssemblySystemDeflection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'FlexiblePinAssemblySystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def pin_tangential_oscillation_amplitude(self) -> 'float':
        """float: 'PinTangentialOscillationAmplitude' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PinTangentialOscillationAmplitude

        if temp is None:
            return 0.0

        return temp

    @property
    def pin_tangential_oscillation_frequency(self) -> 'float':
        """float: 'PinTangentialOscillationFrequency' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PinTangentialOscillationFrequency

        if temp is None:
            return 0.0

        return temp

    @property
    def assembly_design(self) -> '_2434.FlexiblePinAssembly':
        """FlexiblePinAssembly: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_load_case(self) -> '_6852.FlexiblePinAssemblyLoadCase':
        """FlexiblePinAssemblyLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def flexible_pin_shaft_details(self) -> '_2783.ShaftSystemDeflection':
        """ShaftSystemDeflection: 'FlexiblePinShaftDetails' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FlexiblePinShaftDetails

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def pin_analysis(self) -> '_2783.ShaftSystemDeflection':
        """ShaftSystemDeflection: 'PinAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PinAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results(self) -> '_4067.FlexiblePinAssemblyPowerFlow':
        """FlexiblePinAssemblyPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def separate_gear_set_details(self) -> '_2721.CylindricalGearSetSystemDeflection':
        """CylindricalGearSetSystemDeflection: 'SeparateGearSetDetails' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SeparateGearSetDetails

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def spindle_analyses(self) -> '_2783.ShaftSystemDeflection':
        """ShaftSystemDeflection: 'SpindleAnalyses' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SpindleAnalyses

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bearing_static_analyses(self) -> 'List[_2677.BearingSystemDeflection]':
        """List[BearingSystemDeflection]: 'BearingStaticAnalyses' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BearingStaticAnalyses

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def flexible_pin_fit_details(self) -> 'List[_2780.ShaftHubConnectionSystemDeflection]':
        """List[ShaftHubConnectionSystemDeflection]: 'FlexiblePinFitDetails' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FlexiblePinFitDetails

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def load_sharing_factor_reporters(self) -> 'List[_2757.LoadSharingFactorReporter]':
        """List[LoadSharingFactorReporter]: 'LoadSharingFactorReporters' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LoadSharingFactorReporters

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def observed_pin_stiffness_reporters(self) -> 'List[_2762.ObservedPinStiffnessReporter]':
        """List[ObservedPinStiffnessReporter]: 'ObservedPinStiffnessReporters' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ObservedPinStiffnessReporters

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def pin_spindle_fit_analyses(self) -> 'List[_2780.ShaftHubConnectionSystemDeflection]':
        """List[ShaftHubConnectionSystemDeflection]: 'PinSpindleFitAnalyses' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PinSpindleFitAnalyses

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def planet_gear_system_deflections(self) -> 'List[_2724.CylindricalGearSystemDeflection]':
        """List[CylindricalGearSystemDeflection]: 'PlanetGearSystemDeflections' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PlanetGearSystemDeflections

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'FlexiblePinAssemblySystemDeflection._Cast_FlexiblePinAssemblySystemDeflection':
        return self._Cast_FlexiblePinAssemblySystemDeflection(self)
