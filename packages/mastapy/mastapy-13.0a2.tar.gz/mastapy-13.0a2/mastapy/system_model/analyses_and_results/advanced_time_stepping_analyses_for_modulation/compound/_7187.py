"""_7187.py

PlanetaryGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
"""
from typing import List

from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7058
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7152
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANETARY_GEAR_SET_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation.Compound', 'PlanetaryGearSetCompoundAdvancedTimeSteppingAnalysisForModulation')


__docformat__ = 'restructuredtext en'
__all__ = ('PlanetaryGearSetCompoundAdvancedTimeSteppingAnalysisForModulation',)


class PlanetaryGearSetCompoundAdvancedTimeSteppingAnalysisForModulation(_7152.CylindricalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation):
    """PlanetaryGearSetCompoundAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _PLANETARY_GEAR_SET_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION

    class _Cast_PlanetaryGearSetCompoundAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting PlanetaryGearSetCompoundAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(self, parent: 'PlanetaryGearSetCompoundAdvancedTimeSteppingAnalysisForModulation'):
            self._parent = parent

        @property
        def cylindrical_gear_set_compound_advanced_time_stepping_analysis_for_modulation(self):
            return self._parent._cast(_7152.CylindricalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def gear_set_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7163
            
            return self._parent._cast(_7163.GearSetCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def specialised_assembly_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7201
            
            return self._parent._cast(_7201.SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def abstract_assembly_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7103
            
            return self._parent._cast(_7103.AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def part_compound_advanced_time_stepping_analysis_for_modulation(self):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7182
            
            return self._parent._cast(_7182.PartCompoundAdvancedTimeSteppingAnalysisForModulation)

        @property
        def part_compound_analysis(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7508
            
            return self._parent._cast(_7508.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7505
            
            return self._parent._cast(_7505.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(self):
            from mastapy.system_model.analyses_and_results import _2630
            
            return self._parent._cast(_2630.DesignEntityAnalysis)

        @property
        def planetary_gear_set_compound_advanced_time_stepping_analysis_for_modulation(self) -> 'PlanetaryGearSetCompoundAdvancedTimeSteppingAnalysisForModulation':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'PlanetaryGearSetCompoundAdvancedTimeSteppingAnalysisForModulation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_7058.PlanetaryGearSetAdvancedTimeSteppingAnalysisForModulation]':
        """List[PlanetaryGearSetAdvancedTimeSteppingAnalysisForModulation]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_7058.PlanetaryGearSetAdvancedTimeSteppingAnalysisForModulation]':
        """List[PlanetaryGearSetAdvancedTimeSteppingAnalysisForModulation]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'PlanetaryGearSetCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_PlanetaryGearSetCompoundAdvancedTimeSteppingAnalysisForModulation':
        return self._Cast_PlanetaryGearSetCompoundAdvancedTimeSteppingAnalysisForModulation(self)
