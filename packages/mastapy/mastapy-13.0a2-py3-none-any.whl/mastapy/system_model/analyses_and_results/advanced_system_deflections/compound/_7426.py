"""_7426.py

GearCompoundAdvancedSystemDeflection
"""
from typing import List

from mastapy.gears.rating import _354
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7295
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7445
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound', 'GearCompoundAdvancedSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('GearCompoundAdvancedSystemDeflection',)


class GearCompoundAdvancedSystemDeflection(_7445.MountableComponentCompoundAdvancedSystemDeflection):
    """GearCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _GEAR_COMPOUND_ADVANCED_SYSTEM_DEFLECTION

    class _Cast_GearCompoundAdvancedSystemDeflection:
        """Special nested class for casting GearCompoundAdvancedSystemDeflection to subclasses."""

        def __init__(self, parent: 'GearCompoundAdvancedSystemDeflection'):
            self._parent = parent

        @property
        def mountable_component_compound_advanced_system_deflection(self):
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
        def agma_gleason_conical_gear_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7372
            
            return self._parent._cast(_7372.AGMAGleasonConicalGearCompoundAdvancedSystemDeflection)

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
        def bevel_gear_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7384
            
            return self._parent._cast(_7384.BevelGearCompoundAdvancedSystemDeflection)

        @property
        def concept_gear_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7397
            
            return self._parent._cast(_7397.ConceptGearCompoundAdvancedSystemDeflection)

        @property
        def conical_gear_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7400
            
            return self._parent._cast(_7400.ConicalGearCompoundAdvancedSystemDeflection)

        @property
        def cylindrical_gear_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7415
            
            return self._parent._cast(_7415.CylindricalGearCompoundAdvancedSystemDeflection)

        @property
        def cylindrical_planet_gear_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7418
            
            return self._parent._cast(_7418.CylindricalPlanetGearCompoundAdvancedSystemDeflection)

        @property
        def face_gear_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7421
            
            return self._parent._cast(_7421.FaceGearCompoundAdvancedSystemDeflection)

        @property
        def hypoid_gear_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7430
            
            return self._parent._cast(_7430.HypoidGearCompoundAdvancedSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7434
            
            return self._parent._cast(_7434.KlingelnbergCycloPalloidConicalGearCompoundAdvancedSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7437
            
            return self._parent._cast(_7437.KlingelnbergCycloPalloidHypoidGearCompoundAdvancedSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7440
            
            return self._parent._cast(_7440.KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedSystemDeflection)

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
        def worm_gear_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7491
            
            return self._parent._cast(_7491.WormGearCompoundAdvancedSystemDeflection)

        @property
        def zerol_bevel_gear_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7494
            
            return self._parent._cast(_7494.ZerolBevelGearCompoundAdvancedSystemDeflection)

        @property
        def gear_compound_advanced_system_deflection(self) -> 'GearCompoundAdvancedSystemDeflection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GearCompoundAdvancedSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def gear_duty_cycle_rating(self) -> '_354.GearDutyCycleRating':
        """GearDutyCycleRating: 'GearDutyCycleRating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearDutyCycleRating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_analysis_cases(self) -> 'List[_7295.GearAdvancedSystemDeflection]':
        """List[GearAdvancedSystemDeflection]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases_ready(self) -> 'List[_7295.GearAdvancedSystemDeflection]':
        """List[GearAdvancedSystemDeflection]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'GearCompoundAdvancedSystemDeflection._Cast_GearCompoundAdvancedSystemDeflection':
        return self._Cast_GearCompoundAdvancedSystemDeflection(self)
