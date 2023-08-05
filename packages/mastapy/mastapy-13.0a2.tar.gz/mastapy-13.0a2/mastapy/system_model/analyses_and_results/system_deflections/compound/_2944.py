"""_2944.py

StraightBevelSunGearCompoundSystemDeflection
"""
from typing import List

from mastapy.system_model.analyses_and_results.system_deflections import _2799
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2937
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_SUN_GEAR_COMPOUND_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound', 'StraightBevelSunGearCompoundSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('StraightBevelSunGearCompoundSystemDeflection',)


class StraightBevelSunGearCompoundSystemDeflection(_2937.StraightBevelDiffGearCompoundSystemDeflection):
    """StraightBevelSunGearCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_SUN_GEAR_COMPOUND_SYSTEM_DEFLECTION

    class _Cast_StraightBevelSunGearCompoundSystemDeflection:
        """Special nested class for casting StraightBevelSunGearCompoundSystemDeflection to subclasses."""

        def __init__(self, parent: 'StraightBevelSunGearCompoundSystemDeflection'):
            self._parent = parent

        @property
        def straight_bevel_diff_gear_compound_system_deflection(self):
            return self._parent._cast(_2937.StraightBevelDiffGearCompoundSystemDeflection)

        @property
        def bevel_gear_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2846
            
            return self._parent._cast(_2846.BevelGearCompoundSystemDeflection)

        @property
        def agma_gleason_conical_gear_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2834
            
            return self._parent._cast(_2834.AGMAGleasonConicalGearCompoundSystemDeflection)

        @property
        def conical_gear_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2862
            
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
        def straight_bevel_sun_gear_compound_system_deflection(self) -> 'StraightBevelSunGearCompoundSystemDeflection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'StraightBevelSunGearCompoundSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases_ready(self) -> 'List[_2799.StraightBevelSunGearSystemDeflection]':
        """List[StraightBevelSunGearSystemDeflection]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases(self) -> 'List[_2799.StraightBevelSunGearSystemDeflection]':
        """List[StraightBevelSunGearSystemDeflection]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'StraightBevelSunGearCompoundSystemDeflection._Cast_StraightBevelSunGearCompoundSystemDeflection':
        return self._Cast_StraightBevelSunGearCompoundSystemDeflection(self)
