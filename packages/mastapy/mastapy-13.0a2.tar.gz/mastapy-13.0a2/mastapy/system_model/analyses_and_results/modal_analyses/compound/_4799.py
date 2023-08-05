"""_4799.py

SpecialisedAssemblyCompoundModalAnalysis
"""
from typing import List

from mastapy.system_model.analyses_and_results.modal_analyses import _4655
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4701
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPECIALISED_ASSEMBLY_COMPOUND_MODAL_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound', 'SpecialisedAssemblyCompoundModalAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('SpecialisedAssemblyCompoundModalAnalysis',)


class SpecialisedAssemblyCompoundModalAnalysis(_4701.AbstractAssemblyCompoundModalAnalysis):
    """SpecialisedAssemblyCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _SPECIALISED_ASSEMBLY_COMPOUND_MODAL_ANALYSIS

    class _Cast_SpecialisedAssemblyCompoundModalAnalysis:
        """Special nested class for casting SpecialisedAssemblyCompoundModalAnalysis to subclasses."""

        def __init__(self, parent: 'SpecialisedAssemblyCompoundModalAnalysis'):
            self._parent = parent

        @property
        def abstract_assembly_compound_modal_analysis(self):
            return self._parent._cast(_4701.AbstractAssemblyCompoundModalAnalysis)

        @property
        def part_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4780
            
            return self._parent._cast(_4780.PartCompoundModalAnalysis)

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
        def agma_gleason_conical_gear_set_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4707
            
            return self._parent._cast(_4707.AGMAGleasonConicalGearSetCompoundModalAnalysis)

        @property
        def belt_drive_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4711
            
            return self._parent._cast(_4711.BeltDriveCompoundModalAnalysis)

        @property
        def bevel_differential_gear_set_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4714
            
            return self._parent._cast(_4714.BevelDifferentialGearSetCompoundModalAnalysis)

        @property
        def bevel_gear_set_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4719
            
            return self._parent._cast(_4719.BevelGearSetCompoundModalAnalysis)

        @property
        def bolted_joint_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4721
            
            return self._parent._cast(_4721.BoltedJointCompoundModalAnalysis)

        @property
        def clutch_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4722
            
            return self._parent._cast(_4722.ClutchCompoundModalAnalysis)

        @property
        def concept_coupling_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4727
            
            return self._parent._cast(_4727.ConceptCouplingCompoundModalAnalysis)

        @property
        def concept_gear_set_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4732
            
            return self._parent._cast(_4732.ConceptGearSetCompoundModalAnalysis)

        @property
        def conical_gear_set_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4735
            
            return self._parent._cast(_4735.ConicalGearSetCompoundModalAnalysis)

        @property
        def coupling_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4738
            
            return self._parent._cast(_4738.CouplingCompoundModalAnalysis)

        @property
        def cvt_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4742
            
            return self._parent._cast(_4742.CVTCompoundModalAnalysis)

        @property
        def cycloidal_assembly_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4744
            
            return self._parent._cast(_4744.CycloidalAssemblyCompoundModalAnalysis)

        @property
        def cylindrical_gear_set_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4750
            
            return self._parent._cast(_4750.CylindricalGearSetCompoundModalAnalysis)

        @property
        def face_gear_set_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4756
            
            return self._parent._cast(_4756.FaceGearSetCompoundModalAnalysis)

        @property
        def flexible_pin_assembly_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4758
            
            return self._parent._cast(_4758.FlexiblePinAssemblyCompoundModalAnalysis)

        @property
        def gear_set_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4761
            
            return self._parent._cast(_4761.GearSetCompoundModalAnalysis)

        @property
        def hypoid_gear_set_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4765
            
            return self._parent._cast(_4765.HypoidGearSetCompoundModalAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4769
            
            return self._parent._cast(_4769.KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4772
            
            return self._parent._cast(_4772.KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4775
            
            return self._parent._cast(_4775.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysis)

        @property
        def part_to_part_shear_coupling_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4781
            
            return self._parent._cast(_4781.PartToPartShearCouplingCompoundModalAnalysis)

        @property
        def planetary_gear_set_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4785
            
            return self._parent._cast(_4785.PlanetaryGearSetCompoundModalAnalysis)

        @property
        def rolling_ring_assembly_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4792
            
            return self._parent._cast(_4792.RollingRingAssemblyCompoundModalAnalysis)

        @property
        def spiral_bevel_gear_set_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4802
            
            return self._parent._cast(_4802.SpiralBevelGearSetCompoundModalAnalysis)

        @property
        def spring_damper_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4803
            
            return self._parent._cast(_4803.SpringDamperCompoundModalAnalysis)

        @property
        def straight_bevel_diff_gear_set_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4808
            
            return self._parent._cast(_4808.StraightBevelDiffGearSetCompoundModalAnalysis)

        @property
        def straight_bevel_gear_set_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4811
            
            return self._parent._cast(_4811.StraightBevelGearSetCompoundModalAnalysis)

        @property
        def synchroniser_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4814
            
            return self._parent._cast(_4814.SynchroniserCompoundModalAnalysis)

        @property
        def torque_converter_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4818
            
            return self._parent._cast(_4818.TorqueConverterCompoundModalAnalysis)

        @property
        def worm_gear_set_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4826
            
            return self._parent._cast(_4826.WormGearSetCompoundModalAnalysis)

        @property
        def zerol_bevel_gear_set_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4829
            
            return self._parent._cast(_4829.ZerolBevelGearSetCompoundModalAnalysis)

        @property
        def specialised_assembly_compound_modal_analysis(self) -> 'SpecialisedAssemblyCompoundModalAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'SpecialisedAssemblyCompoundModalAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(self) -> 'List[_4655.SpecialisedAssemblyModalAnalysis]':
        """List[SpecialisedAssemblyModalAnalysis]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_4655.SpecialisedAssemblyModalAnalysis]':
        """List[SpecialisedAssemblyModalAnalysis]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'SpecialisedAssemblyCompoundModalAnalysis._Cast_SpecialisedAssemblyCompoundModalAnalysis':
        return self._Cast_SpecialisedAssemblyCompoundModalAnalysis(self)
