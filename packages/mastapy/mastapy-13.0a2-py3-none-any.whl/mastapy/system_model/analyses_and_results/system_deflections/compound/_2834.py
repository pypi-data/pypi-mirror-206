"""_2834.py

AGMAGleasonConicalGearCompoundSystemDeflection
"""
from typing import List

from mastapy.system_model.analyses_and_results.system_deflections import _2670
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2862
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_COMPOUND_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound', 'AGMAGleasonConicalGearCompoundSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('AGMAGleasonConicalGearCompoundSystemDeflection',)


class AGMAGleasonConicalGearCompoundSystemDeflection(_2862.ConicalGearCompoundSystemDeflection):
    """AGMAGleasonConicalGearCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_COMPOUND_SYSTEM_DEFLECTION

    class _Cast_AGMAGleasonConicalGearCompoundSystemDeflection:
        """Special nested class for casting AGMAGleasonConicalGearCompoundSystemDeflection to subclasses."""

        def __init__(self, parent: 'AGMAGleasonConicalGearCompoundSystemDeflection'):
            self._parent = parent

        @property
        def conical_gear_compound_system_deflection(self):
            return self._parent._cast(_2862.ConicalGearCompoundSystemDeflection)

        @property
        def gear_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2889
            
            return self._parent._cast(_2889.GearCompoundSystemDeflection)

        @property
        def mountable_component_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2908
            
            return self._parent._cast(_2908.MountableComponentCompoundSystemDeflection)

        @property
        def component_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2855
            
            return self._parent._cast(_2855.ComponentCompoundSystemDeflection)

        @property
        def part_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2910
            
            return self._parent._cast(_2910.PartCompoundSystemDeflection)

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
        def bevel_differential_gear_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2841
            
            return self._parent._cast(_2841.BevelDifferentialGearCompoundSystemDeflection)

        @property
        def bevel_differential_planet_gear_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2844
            
            return self._parent._cast(_2844.BevelDifferentialPlanetGearCompoundSystemDeflection)

        @property
        def bevel_differential_sun_gear_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2845
            
            return self._parent._cast(_2845.BevelDifferentialSunGearCompoundSystemDeflection)

        @property
        def bevel_gear_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2846
            
            return self._parent._cast(_2846.BevelGearCompoundSystemDeflection)

        @property
        def hypoid_gear_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2893
            
            return self._parent._cast(_2893.HypoidGearCompoundSystemDeflection)

        @property
        def spiral_bevel_gear_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2931
            
            return self._parent._cast(_2931.SpiralBevelGearCompoundSystemDeflection)

        @property
        def straight_bevel_diff_gear_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2937
            
            return self._parent._cast(_2937.StraightBevelDiffGearCompoundSystemDeflection)

        @property
        def straight_bevel_gear_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2940
            
            return self._parent._cast(_2940.StraightBevelGearCompoundSystemDeflection)

        @property
        def straight_bevel_planet_gear_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2943
            
            return self._parent._cast(_2943.StraightBevelPlanetGearCompoundSystemDeflection)

        @property
        def straight_bevel_sun_gear_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2944
            
            return self._parent._cast(_2944.StraightBevelSunGearCompoundSystemDeflection)

        @property
        def zerol_bevel_gear_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2958
            
            return self._parent._cast(_2958.ZerolBevelGearCompoundSystemDeflection)

        @property
        def agma_gleason_conical_gear_compound_system_deflection(self) -> 'AGMAGleasonConicalGearCompoundSystemDeflection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AGMAGleasonConicalGearCompoundSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self) -> 'List[_2670.AGMAGleasonConicalGearSystemDeflection]':
        """List[AGMAGleasonConicalGearSystemDeflection]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases_ready(self) -> 'List[_2670.AGMAGleasonConicalGearSystemDeflection]':
        """List[AGMAGleasonConicalGearSystemDeflection]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'AGMAGleasonConicalGearCompoundSystemDeflection._Cast_AGMAGleasonConicalGearCompoundSystemDeflection':
        return self._Cast_AGMAGleasonConicalGearCompoundSystemDeflection(self)
