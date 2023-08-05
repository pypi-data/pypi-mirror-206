"""_2930.py

SpecialisedAssemblyCompoundSystemDeflection
"""
from typing import List

from mastapy.system_model.analyses_and_results.system_deflections import _2785
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2830
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPECIALISED_ASSEMBLY_COMPOUND_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound', 'SpecialisedAssemblyCompoundSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('SpecialisedAssemblyCompoundSystemDeflection',)


class SpecialisedAssemblyCompoundSystemDeflection(_2830.AbstractAssemblyCompoundSystemDeflection):
    """SpecialisedAssemblyCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _SPECIALISED_ASSEMBLY_COMPOUND_SYSTEM_DEFLECTION

    class _Cast_SpecialisedAssemblyCompoundSystemDeflection:
        """Special nested class for casting SpecialisedAssemblyCompoundSystemDeflection to subclasses."""

        def __init__(self, parent: 'SpecialisedAssemblyCompoundSystemDeflection'):
            self._parent = parent

        @property
        def abstract_assembly_compound_system_deflection(self):
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
        def belt_drive_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2840
            
            return self._parent._cast(_2840.BeltDriveCompoundSystemDeflection)

        @property
        def bevel_differential_gear_set_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2843
            
            return self._parent._cast(_2843.BevelDifferentialGearSetCompoundSystemDeflection)

        @property
        def bevel_gear_set_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2848
            
            return self._parent._cast(_2848.BevelGearSetCompoundSystemDeflection)

        @property
        def bolted_joint_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2850
            
            return self._parent._cast(_2850.BoltedJointCompoundSystemDeflection)

        @property
        def clutch_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2851
            
            return self._parent._cast(_2851.ClutchCompoundSystemDeflection)

        @property
        def concept_coupling_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2856
            
            return self._parent._cast(_2856.ConceptCouplingCompoundSystemDeflection)

        @property
        def concept_gear_set_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2861
            
            return self._parent._cast(_2861.ConceptGearSetCompoundSystemDeflection)

        @property
        def conical_gear_set_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2864
            
            return self._parent._cast(_2864.ConicalGearSetCompoundSystemDeflection)

        @property
        def coupling_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2867
            
            return self._parent._cast(_2867.CouplingCompoundSystemDeflection)

        @property
        def cvt_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2871
            
            return self._parent._cast(_2871.CVTCompoundSystemDeflection)

        @property
        def cycloidal_assembly_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2873
            
            return self._parent._cast(_2873.CycloidalAssemblyCompoundSystemDeflection)

        @property
        def cylindrical_gear_set_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2879
            
            return self._parent._cast(_2879.CylindricalGearSetCompoundSystemDeflection)

        @property
        def face_gear_set_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2886
            
            return self._parent._cast(_2886.FaceGearSetCompoundSystemDeflection)

        @property
        def flexible_pin_assembly_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2888
            
            return self._parent._cast(_2888.FlexiblePinAssemblyCompoundSystemDeflection)

        @property
        def gear_set_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2891
            
            return self._parent._cast(_2891.GearSetCompoundSystemDeflection)

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
        def part_to_part_shear_coupling_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2911
            
            return self._parent._cast(_2911.PartToPartShearCouplingCompoundSystemDeflection)

        @property
        def planetary_gear_set_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2915
            
            return self._parent._cast(_2915.PlanetaryGearSetCompoundSystemDeflection)

        @property
        def rolling_ring_assembly_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2922
            
            return self._parent._cast(_2922.RollingRingAssemblyCompoundSystemDeflection)

        @property
        def spiral_bevel_gear_set_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2933
            
            return self._parent._cast(_2933.SpiralBevelGearSetCompoundSystemDeflection)

        @property
        def spring_damper_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2934
            
            return self._parent._cast(_2934.SpringDamperCompoundSystemDeflection)

        @property
        def straight_bevel_diff_gear_set_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2939
            
            return self._parent._cast(_2939.StraightBevelDiffGearSetCompoundSystemDeflection)

        @property
        def straight_bevel_gear_set_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2942
            
            return self._parent._cast(_2942.StraightBevelGearSetCompoundSystemDeflection)

        @property
        def synchroniser_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2945
            
            return self._parent._cast(_2945.SynchroniserCompoundSystemDeflection)

        @property
        def torque_converter_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2949
            
            return self._parent._cast(_2949.TorqueConverterCompoundSystemDeflection)

        @property
        def worm_gear_set_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2957
            
            return self._parent._cast(_2957.WormGearSetCompoundSystemDeflection)

        @property
        def zerol_bevel_gear_set_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2960
            
            return self._parent._cast(_2960.ZerolBevelGearSetCompoundSystemDeflection)

        @property
        def specialised_assembly_compound_system_deflection(self) -> 'SpecialisedAssemblyCompoundSystemDeflection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'SpecialisedAssemblyCompoundSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(self) -> 'List[_2785.SpecialisedAssemblySystemDeflection]':
        """List[SpecialisedAssemblySystemDeflection]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_2785.SpecialisedAssemblySystemDeflection]':
        """List[SpecialisedAssemblySystemDeflection]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'SpecialisedAssemblyCompoundSystemDeflection._Cast_SpecialisedAssemblyCompoundSystemDeflection':
        return self._Cast_SpecialisedAssemblyCompoundSystemDeflection(self)
