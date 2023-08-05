"""_7384.py

BevelGearCompoundAdvancedSystemDeflection
"""
from typing import List

from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7251
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7372
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound', 'BevelGearCompoundAdvancedSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('BevelGearCompoundAdvancedSystemDeflection',)


class BevelGearCompoundAdvancedSystemDeflection(_7372.AGMAGleasonConicalGearCompoundAdvancedSystemDeflection):
    """BevelGearCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_COMPOUND_ADVANCED_SYSTEM_DEFLECTION

    class _Cast_BevelGearCompoundAdvancedSystemDeflection:
        """Special nested class for casting BevelGearCompoundAdvancedSystemDeflection to subclasses."""

        def __init__(self, parent: 'BevelGearCompoundAdvancedSystemDeflection'):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_compound_advanced_system_deflection(self):
            return self._parent._cast(_7372.AGMAGleasonConicalGearCompoundAdvancedSystemDeflection)

        @property
        def conical_gear_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7400
            
            return self._parent._cast(_7400.ConicalGearCompoundAdvancedSystemDeflection)

        @property
        def gear_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7426
            
            return self._parent._cast(_7426.GearCompoundAdvancedSystemDeflection)

        @property
        def mountable_component_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7445
            
            return self._parent._cast(_7445.MountableComponentCompoundAdvancedSystemDeflection)

        @property
        def component_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7393
            
            return self._parent._cast(_7393.ComponentCompoundAdvancedSystemDeflection)

        @property
        def part_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7447
            
            return self._parent._cast(_7447.PartCompoundAdvancedSystemDeflection)

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
        def bevel_differential_gear_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7379
            
            return self._parent._cast(_7379.BevelDifferentialGearCompoundAdvancedSystemDeflection)

        @property
        def bevel_differential_planet_gear_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7382
            
            return self._parent._cast(_7382.BevelDifferentialPlanetGearCompoundAdvancedSystemDeflection)

        @property
        def bevel_differential_sun_gear_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7383
            
            return self._parent._cast(_7383.BevelDifferentialSunGearCompoundAdvancedSystemDeflection)

        @property
        def spiral_bevel_gear_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7467
            
            return self._parent._cast(_7467.SpiralBevelGearCompoundAdvancedSystemDeflection)

        @property
        def straight_bevel_diff_gear_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7473
            
            return self._parent._cast(_7473.StraightBevelDiffGearCompoundAdvancedSystemDeflection)

        @property
        def straight_bevel_gear_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7476
            
            return self._parent._cast(_7476.StraightBevelGearCompoundAdvancedSystemDeflection)

        @property
        def straight_bevel_planet_gear_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7479
            
            return self._parent._cast(_7479.StraightBevelPlanetGearCompoundAdvancedSystemDeflection)

        @property
        def straight_bevel_sun_gear_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7480
            
            return self._parent._cast(_7480.StraightBevelSunGearCompoundAdvancedSystemDeflection)

        @property
        def zerol_bevel_gear_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7494
            
            return self._parent._cast(_7494.ZerolBevelGearCompoundAdvancedSystemDeflection)

        @property
        def bevel_gear_compound_advanced_system_deflection(self) -> 'BevelGearCompoundAdvancedSystemDeflection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'BevelGearCompoundAdvancedSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self) -> 'List[_7251.BevelGearAdvancedSystemDeflection]':
        """List[BevelGearAdvancedSystemDeflection]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases_ready(self) -> 'List[_7251.BevelGearAdvancedSystemDeflection]':
        """List[BevelGearAdvancedSystemDeflection]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'BevelGearCompoundAdvancedSystemDeflection._Cast_BevelGearCompoundAdvancedSystemDeflection':
        return self._Cast_BevelGearCompoundAdvancedSystemDeflection(self)
