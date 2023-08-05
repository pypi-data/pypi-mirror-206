"""_7476.py

StraightBevelGearCompoundAdvancedSystemDeflection
"""
from typing import List

from mastapy.system_model.part_model.gears import _2526
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7346
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7384
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_GEAR_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound', 'StraightBevelGearCompoundAdvancedSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('StraightBevelGearCompoundAdvancedSystemDeflection',)


class StraightBevelGearCompoundAdvancedSystemDeflection(_7384.BevelGearCompoundAdvancedSystemDeflection):
    """StraightBevelGearCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_GEAR_COMPOUND_ADVANCED_SYSTEM_DEFLECTION

    class _Cast_StraightBevelGearCompoundAdvancedSystemDeflection:
        """Special nested class for casting StraightBevelGearCompoundAdvancedSystemDeflection to subclasses."""

        def __init__(self, parent: 'StraightBevelGearCompoundAdvancedSystemDeflection'):
            self._parent = parent

        @property
        def bevel_gear_compound_advanced_system_deflection(self):
            return self._parent._cast(_7384.BevelGearCompoundAdvancedSystemDeflection)

        @property
        def agma_gleason_conical_gear_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7372
            
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
        def straight_bevel_gear_compound_advanced_system_deflection(self) -> 'StraightBevelGearCompoundAdvancedSystemDeflection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'StraightBevelGearCompoundAdvancedSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2526.StraightBevelGear':
        """StraightBevelGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_7346.StraightBevelGearAdvancedSystemDeflection]':
        """List[StraightBevelGearAdvancedSystemDeflection]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases(self) -> 'List[_7346.StraightBevelGearAdvancedSystemDeflection]':
        """List[StraightBevelGearAdvancedSystemDeflection]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'StraightBevelGearCompoundAdvancedSystemDeflection._Cast_StraightBevelGearCompoundAdvancedSystemDeflection':
        return self._Cast_StraightBevelGearCompoundAdvancedSystemDeflection(self)
