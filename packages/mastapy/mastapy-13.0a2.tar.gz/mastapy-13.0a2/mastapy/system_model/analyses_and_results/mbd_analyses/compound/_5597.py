"""_5597.py

SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis
"""
from typing import List

from mastapy.system_model.analyses_and_results.mbd_analyses import _5459
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5499
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPECIALISED_ASSEMBLY_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound', 'SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis',)


class SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis(_5499.AbstractAssemblyCompoundMultibodyDynamicsAnalysis):
    """SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _SPECIALISED_ASSEMBLY_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS

    class _Cast_SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis:
        """Special nested class for casting SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis to subclasses."""

        def __init__(self, parent: 'SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis'):
            self._parent = parent

        @property
        def abstract_assembly_compound_multibody_dynamics_analysis(self):
            return self._parent._cast(_5499.AbstractAssemblyCompoundMultibodyDynamicsAnalysis)

        @property
        def part_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5578
            
            return self._parent._cast(_5578.PartCompoundMultibodyDynamicsAnalysis)

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
        def agma_gleason_conical_gear_set_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5505
            
            return self._parent._cast(_5505.AGMAGleasonConicalGearSetCompoundMultibodyDynamicsAnalysis)

        @property
        def belt_drive_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5509
            
            return self._parent._cast(_5509.BeltDriveCompoundMultibodyDynamicsAnalysis)

        @property
        def bevel_differential_gear_set_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5512
            
            return self._parent._cast(_5512.BevelDifferentialGearSetCompoundMultibodyDynamicsAnalysis)

        @property
        def bevel_gear_set_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5517
            
            return self._parent._cast(_5517.BevelGearSetCompoundMultibodyDynamicsAnalysis)

        @property
        def bolted_joint_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5519
            
            return self._parent._cast(_5519.BoltedJointCompoundMultibodyDynamicsAnalysis)

        @property
        def clutch_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5520
            
            return self._parent._cast(_5520.ClutchCompoundMultibodyDynamicsAnalysis)

        @property
        def concept_coupling_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5525
            
            return self._parent._cast(_5525.ConceptCouplingCompoundMultibodyDynamicsAnalysis)

        @property
        def concept_gear_set_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5530
            
            return self._parent._cast(_5530.ConceptGearSetCompoundMultibodyDynamicsAnalysis)

        @property
        def conical_gear_set_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5533
            
            return self._parent._cast(_5533.ConicalGearSetCompoundMultibodyDynamicsAnalysis)

        @property
        def coupling_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5536
            
            return self._parent._cast(_5536.CouplingCompoundMultibodyDynamicsAnalysis)

        @property
        def cvt_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5540
            
            return self._parent._cast(_5540.CVTCompoundMultibodyDynamicsAnalysis)

        @property
        def cycloidal_assembly_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5542
            
            return self._parent._cast(_5542.CycloidalAssemblyCompoundMultibodyDynamicsAnalysis)

        @property
        def cylindrical_gear_set_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5548
            
            return self._parent._cast(_5548.CylindricalGearSetCompoundMultibodyDynamicsAnalysis)

        @property
        def face_gear_set_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5554
            
            return self._parent._cast(_5554.FaceGearSetCompoundMultibodyDynamicsAnalysis)

        @property
        def flexible_pin_assembly_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5556
            
            return self._parent._cast(_5556.FlexiblePinAssemblyCompoundMultibodyDynamicsAnalysis)

        @property
        def gear_set_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5559
            
            return self._parent._cast(_5559.GearSetCompoundMultibodyDynamicsAnalysis)

        @property
        def hypoid_gear_set_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5563
            
            return self._parent._cast(_5563.HypoidGearSetCompoundMultibodyDynamicsAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5567
            
            return self._parent._cast(_5567.KlingelnbergCycloPalloidConicalGearSetCompoundMultibodyDynamicsAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5570
            
            return self._parent._cast(_5570.KlingelnbergCycloPalloidHypoidGearSetCompoundMultibodyDynamicsAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5573
            
            return self._parent._cast(_5573.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundMultibodyDynamicsAnalysis)

        @property
        def part_to_part_shear_coupling_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5579
            
            return self._parent._cast(_5579.PartToPartShearCouplingCompoundMultibodyDynamicsAnalysis)

        @property
        def planetary_gear_set_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5583
            
            return self._parent._cast(_5583.PlanetaryGearSetCompoundMultibodyDynamicsAnalysis)

        @property
        def rolling_ring_assembly_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5590
            
            return self._parent._cast(_5590.RollingRingAssemblyCompoundMultibodyDynamicsAnalysis)

        @property
        def spiral_bevel_gear_set_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5600
            
            return self._parent._cast(_5600.SpiralBevelGearSetCompoundMultibodyDynamicsAnalysis)

        @property
        def spring_damper_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5601
            
            return self._parent._cast(_5601.SpringDamperCompoundMultibodyDynamicsAnalysis)

        @property
        def straight_bevel_diff_gear_set_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5606
            
            return self._parent._cast(_5606.StraightBevelDiffGearSetCompoundMultibodyDynamicsAnalysis)

        @property
        def straight_bevel_gear_set_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5609
            
            return self._parent._cast(_5609.StraightBevelGearSetCompoundMultibodyDynamicsAnalysis)

        @property
        def synchroniser_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5612
            
            return self._parent._cast(_5612.SynchroniserCompoundMultibodyDynamicsAnalysis)

        @property
        def torque_converter_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5616
            
            return self._parent._cast(_5616.TorqueConverterCompoundMultibodyDynamicsAnalysis)

        @property
        def worm_gear_set_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5624
            
            return self._parent._cast(_5624.WormGearSetCompoundMultibodyDynamicsAnalysis)

        @property
        def zerol_bevel_gear_set_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5627
            
            return self._parent._cast(_5627.ZerolBevelGearSetCompoundMultibodyDynamicsAnalysis)

        @property
        def specialised_assembly_compound_multibody_dynamics_analysis(self) -> 'SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(self) -> 'List[_5459.SpecialisedAssemblyMultibodyDynamicsAnalysis]':
        """List[SpecialisedAssemblyMultibodyDynamicsAnalysis]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_5459.SpecialisedAssemblyMultibodyDynamicsAnalysis]':
        """List[SpecialisedAssemblyMultibodyDynamicsAnalysis]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis':
        return self._Cast_SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis(self)
