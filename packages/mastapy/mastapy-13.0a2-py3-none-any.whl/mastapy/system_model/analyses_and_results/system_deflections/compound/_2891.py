"""_2891.py

GearSetCompoundSystemDeflection
"""
from typing import List

from mastapy.system_model.analyses_and_results.system_deflections import _2739
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2930
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_SET_COMPOUND_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound', 'GearSetCompoundSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('GearSetCompoundSystemDeflection',)


class GearSetCompoundSystemDeflection(_2930.SpecialisedAssemblyCompoundSystemDeflection):
    """GearSetCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _GEAR_SET_COMPOUND_SYSTEM_DEFLECTION

    class _Cast_GearSetCompoundSystemDeflection:
        """Special nested class for casting GearSetCompoundSystemDeflection to subclasses."""

        def __init__(self, parent: 'GearSetCompoundSystemDeflection'):
            self._parent = parent

        @property
        def specialised_assembly_compound_system_deflection(self):
            return self._parent._cast(_2930.SpecialisedAssemblyCompoundSystemDeflection)

        @property
        def abstract_assembly_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2830
            
            return self._parent._cast(_2830.AbstractAssemblyCompoundSystemDeflection)

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
        def agma_gleason_conical_gear_set_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2836
            
            return self._parent._cast(_2836.AGMAGleasonConicalGearSetCompoundSystemDeflection)

        @property
        def bevel_differential_gear_set_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2843
            
            return self._parent._cast(_2843.BevelDifferentialGearSetCompoundSystemDeflection)

        @property
        def bevel_gear_set_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2848
            
            return self._parent._cast(_2848.BevelGearSetCompoundSystemDeflection)

        @property
        def concept_gear_set_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2861
            
            return self._parent._cast(_2861.ConceptGearSetCompoundSystemDeflection)

        @property
        def conical_gear_set_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2864
            
            return self._parent._cast(_2864.ConicalGearSetCompoundSystemDeflection)

        @property
        def cylindrical_gear_set_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2879
            
            return self._parent._cast(_2879.CylindricalGearSetCompoundSystemDeflection)

        @property
        def face_gear_set_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2886
            
            return self._parent._cast(_2886.FaceGearSetCompoundSystemDeflection)

        @property
        def hypoid_gear_set_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2895
            
            return self._parent._cast(_2895.HypoidGearSetCompoundSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2899
            
            return self._parent._cast(_2899.KlingelnbergCycloPalloidConicalGearSetCompoundSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2902
            
            return self._parent._cast(_2902.KlingelnbergCycloPalloidHypoidGearSetCompoundSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2905
            
            return self._parent._cast(_2905.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSystemDeflection)

        @property
        def planetary_gear_set_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2915
            
            return self._parent._cast(_2915.PlanetaryGearSetCompoundSystemDeflection)

        @property
        def spiral_bevel_gear_set_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2933
            
            return self._parent._cast(_2933.SpiralBevelGearSetCompoundSystemDeflection)

        @property
        def straight_bevel_diff_gear_set_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2939
            
            return self._parent._cast(_2939.StraightBevelDiffGearSetCompoundSystemDeflection)

        @property
        def straight_bevel_gear_set_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2942
            
            return self._parent._cast(_2942.StraightBevelGearSetCompoundSystemDeflection)

        @property
        def worm_gear_set_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2957
            
            return self._parent._cast(_2957.WormGearSetCompoundSystemDeflection)

        @property
        def zerol_bevel_gear_set_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2960
            
            return self._parent._cast(_2960.ZerolBevelGearSetCompoundSystemDeflection)

        @property
        def gear_set_compound_system_deflection(self) -> 'GearSetCompoundSystemDeflection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GearSetCompoundSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(self) -> 'List[_2739.GearSetSystemDeflection]':
        """List[GearSetSystemDeflection]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_2739.GearSetSystemDeflection]':
        """List[GearSetSystemDeflection]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'GearSetCompoundSystemDeflection._Cast_GearSetCompoundSystemDeflection':
        return self._Cast_GearSetCompoundSystemDeflection(self)
