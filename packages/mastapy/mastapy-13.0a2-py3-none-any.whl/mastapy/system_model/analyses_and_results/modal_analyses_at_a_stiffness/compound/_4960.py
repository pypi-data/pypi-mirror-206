"""_4960.py

AbstractAssemblyCompoundModalAnalysisAtAStiffness
"""
from typing import List

from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4830
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5039
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_ASSEMBLY_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness.Compound', 'AbstractAssemblyCompoundModalAnalysisAtAStiffness')


__docformat__ = 'restructuredtext en'
__all__ = ('AbstractAssemblyCompoundModalAnalysisAtAStiffness',)


class AbstractAssemblyCompoundModalAnalysisAtAStiffness(_5039.PartCompoundModalAnalysisAtAStiffness):
    """AbstractAssemblyCompoundModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_ASSEMBLY_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS

    class _Cast_AbstractAssemblyCompoundModalAnalysisAtAStiffness:
        """Special nested class for casting AbstractAssemblyCompoundModalAnalysisAtAStiffness to subclasses."""

        def __init__(self, parent: 'AbstractAssemblyCompoundModalAnalysisAtAStiffness'):
            self._parent = parent

        @property
        def part_compound_modal_analysis_at_a_stiffness(self):
            return self._parent._cast(_5039.PartCompoundModalAnalysisAtAStiffness)

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
        def agma_gleason_conical_gear_set_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _4966
            
            return self._parent._cast(_4966.AGMAGleasonConicalGearSetCompoundModalAnalysisAtAStiffness)

        @property
        def assembly_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _4967
            
            return self._parent._cast(_4967.AssemblyCompoundModalAnalysisAtAStiffness)

        @property
        def belt_drive_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _4970
            
            return self._parent._cast(_4970.BeltDriveCompoundModalAnalysisAtAStiffness)

        @property
        def bevel_differential_gear_set_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _4973
            
            return self._parent._cast(_4973.BevelDifferentialGearSetCompoundModalAnalysisAtAStiffness)

        @property
        def bevel_gear_set_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _4978
            
            return self._parent._cast(_4978.BevelGearSetCompoundModalAnalysisAtAStiffness)

        @property
        def bolted_joint_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _4980
            
            return self._parent._cast(_4980.BoltedJointCompoundModalAnalysisAtAStiffness)

        @property
        def clutch_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _4981
            
            return self._parent._cast(_4981.ClutchCompoundModalAnalysisAtAStiffness)

        @property
        def concept_coupling_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _4986
            
            return self._parent._cast(_4986.ConceptCouplingCompoundModalAnalysisAtAStiffness)

        @property
        def concept_gear_set_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _4991
            
            return self._parent._cast(_4991.ConceptGearSetCompoundModalAnalysisAtAStiffness)

        @property
        def conical_gear_set_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _4994
            
            return self._parent._cast(_4994.ConicalGearSetCompoundModalAnalysisAtAStiffness)

        @property
        def coupling_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _4997
            
            return self._parent._cast(_4997.CouplingCompoundModalAnalysisAtAStiffness)

        @property
        def cvt_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5001
            
            return self._parent._cast(_5001.CVTCompoundModalAnalysisAtAStiffness)

        @property
        def cycloidal_assembly_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5003
            
            return self._parent._cast(_5003.CycloidalAssemblyCompoundModalAnalysisAtAStiffness)

        @property
        def cylindrical_gear_set_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5009
            
            return self._parent._cast(_5009.CylindricalGearSetCompoundModalAnalysisAtAStiffness)

        @property
        def face_gear_set_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5015
            
            return self._parent._cast(_5015.FaceGearSetCompoundModalAnalysisAtAStiffness)

        @property
        def flexible_pin_assembly_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5017
            
            return self._parent._cast(_5017.FlexiblePinAssemblyCompoundModalAnalysisAtAStiffness)

        @property
        def gear_set_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5020
            
            return self._parent._cast(_5020.GearSetCompoundModalAnalysisAtAStiffness)

        @property
        def hypoid_gear_set_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5024
            
            return self._parent._cast(_5024.HypoidGearSetCompoundModalAnalysisAtAStiffness)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5028
            
            return self._parent._cast(_5028.KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtAStiffness)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5031
            
            return self._parent._cast(_5031.KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysisAtAStiffness)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5034
            
            return self._parent._cast(_5034.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysisAtAStiffness)

        @property
        def part_to_part_shear_coupling_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5040
            
            return self._parent._cast(_5040.PartToPartShearCouplingCompoundModalAnalysisAtAStiffness)

        @property
        def planetary_gear_set_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5044
            
            return self._parent._cast(_5044.PlanetaryGearSetCompoundModalAnalysisAtAStiffness)

        @property
        def rolling_ring_assembly_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5051
            
            return self._parent._cast(_5051.RollingRingAssemblyCompoundModalAnalysisAtAStiffness)

        @property
        def root_assembly_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5054
            
            return self._parent._cast(_5054.RootAssemblyCompoundModalAnalysisAtAStiffness)

        @property
        def specialised_assembly_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5058
            
            return self._parent._cast(_5058.SpecialisedAssemblyCompoundModalAnalysisAtAStiffness)

        @property
        def spiral_bevel_gear_set_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5061
            
            return self._parent._cast(_5061.SpiralBevelGearSetCompoundModalAnalysisAtAStiffness)

        @property
        def spring_damper_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5062
            
            return self._parent._cast(_5062.SpringDamperCompoundModalAnalysisAtAStiffness)

        @property
        def straight_bevel_diff_gear_set_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5067
            
            return self._parent._cast(_5067.StraightBevelDiffGearSetCompoundModalAnalysisAtAStiffness)

        @property
        def straight_bevel_gear_set_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5070
            
            return self._parent._cast(_5070.StraightBevelGearSetCompoundModalAnalysisAtAStiffness)

        @property
        def synchroniser_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5073
            
            return self._parent._cast(_5073.SynchroniserCompoundModalAnalysisAtAStiffness)

        @property
        def torque_converter_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5077
            
            return self._parent._cast(_5077.TorqueConverterCompoundModalAnalysisAtAStiffness)

        @property
        def worm_gear_set_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5085
            
            return self._parent._cast(_5085.WormGearSetCompoundModalAnalysisAtAStiffness)

        @property
        def zerol_bevel_gear_set_compound_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5088
            
            return self._parent._cast(_5088.ZerolBevelGearSetCompoundModalAnalysisAtAStiffness)

        @property
        def abstract_assembly_compound_modal_analysis_at_a_stiffness(self) -> 'AbstractAssemblyCompoundModalAnalysisAtAStiffness':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AbstractAssemblyCompoundModalAnalysisAtAStiffness.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(self) -> 'List[_4830.AbstractAssemblyModalAnalysisAtAStiffness]':
        """List[AbstractAssemblyModalAnalysisAtAStiffness]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_4830.AbstractAssemblyModalAnalysisAtAStiffness]':
        """List[AbstractAssemblyModalAnalysisAtAStiffness]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'AbstractAssemblyCompoundModalAnalysisAtAStiffness._Cast_AbstractAssemblyCompoundModalAnalysisAtAStiffness':
        return self._Cast_AbstractAssemblyCompoundModalAnalysisAtAStiffness(self)
