"""_6723.py

PlanetaryGearSetCompoundCriticalSpeedAnalysis
"""
from typing import List

from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6594
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6688
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANETARY_GEAR_SET_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound', 'PlanetaryGearSetCompoundCriticalSpeedAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('PlanetaryGearSetCompoundCriticalSpeedAnalysis',)


class PlanetaryGearSetCompoundCriticalSpeedAnalysis(_6688.CylindricalGearSetCompoundCriticalSpeedAnalysis):
    """PlanetaryGearSetCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _PLANETARY_GEAR_SET_COMPOUND_CRITICAL_SPEED_ANALYSIS

    class _Cast_PlanetaryGearSetCompoundCriticalSpeedAnalysis:
        """Special nested class for casting PlanetaryGearSetCompoundCriticalSpeedAnalysis to subclasses."""

        def __init__(self, parent: 'PlanetaryGearSetCompoundCriticalSpeedAnalysis'):
            self._parent = parent

        @property
        def cylindrical_gear_set_compound_critical_speed_analysis(self):
            return self._parent._cast(_6688.CylindricalGearSetCompoundCriticalSpeedAnalysis)

        @property
        def gear_set_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6699
            
            return self._parent._cast(_6699.GearSetCompoundCriticalSpeedAnalysis)

        @property
        def specialised_assembly_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6737
            
            return self._parent._cast(_6737.SpecialisedAssemblyCompoundCriticalSpeedAnalysis)

        @property
        def abstract_assembly_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6639
            
            return self._parent._cast(_6639.AbstractAssemblyCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_critical_speed_analysis(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6718
            
            return self._parent._cast(_6718.PartCompoundCriticalSpeedAnalysis)

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
        def planetary_gear_set_compound_critical_speed_analysis(self) -> 'PlanetaryGearSetCompoundCriticalSpeedAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'PlanetaryGearSetCompoundCriticalSpeedAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_6594.PlanetaryGearSetCriticalSpeedAnalysis]':
        """List[PlanetaryGearSetCriticalSpeedAnalysis]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_6594.PlanetaryGearSetCriticalSpeedAnalysis]':
        """List[PlanetaryGearSetCriticalSpeedAnalysis]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'PlanetaryGearSetCompoundCriticalSpeedAnalysis._Cast_PlanetaryGearSetCompoundCriticalSpeedAnalysis':
        return self._Cast_PlanetaryGearSetCompoundCriticalSpeedAnalysis(self)
