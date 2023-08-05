"""_5408.py

GearMeshMultibodyDynamicsAnalysis
"""
from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy.nodal_analysis import _69
from mastapy.system_model.connections_and_sockets.gears import _2294
from mastapy.system_model.analyses_and_results.mbd_analyses import _5420
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_MESH_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses', 'GearMeshMultibodyDynamicsAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('GearMeshMultibodyDynamicsAnalysis',)


class GearMeshMultibodyDynamicsAnalysis(_5420.InterMountableComponentConnectionMultibodyDynamicsAnalysis):
    """GearMeshMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _GEAR_MESH_MULTIBODY_DYNAMICS_ANALYSIS

    class _Cast_GearMeshMultibodyDynamicsAnalysis:
        """Special nested class for casting GearMeshMultibodyDynamicsAnalysis to subclasses."""

        def __init__(self, parent: 'GearMeshMultibodyDynamicsAnalysis'):
            self._parent = parent

        @property
        def inter_mountable_component_connection_multibody_dynamics_analysis(self):
            return self._parent._cast(_5420.InterMountableComponentConnectionMultibodyDynamicsAnalysis)

        @property
        def connection_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5385
            
            return self._parent._cast(_5385.ConnectionMultibodyDynamicsAnalysis)

        @property
        def connection_time_series_load_analysis_case(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7504
            
            return self._parent._cast(_7504.ConnectionTimeSeriesLoadAnalysisCase)

        @property
        def connection_analysis_case(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7500
            
            return self._parent._cast(_7500.ConnectionAnalysisCase)

        @property
        def connection_analysis(self):
            from mastapy.system_model.analyses_and_results import _2628
            
            return self._parent._cast(_2628.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(self):
            from mastapy.system_model.analyses_and_results import _2632
            
            return self._parent._cast(_2632.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(self):
            from mastapy.system_model.analyses_and_results import _2630
            
            return self._parent._cast(_2630.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5351
            
            return self._parent._cast(_5351.AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis)

        @property
        def bevel_differential_gear_mesh_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5360
            
            return self._parent._cast(_5360.BevelDifferentialGearMeshMultibodyDynamicsAnalysis)

        @property
        def bevel_gear_mesh_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5365
            
            return self._parent._cast(_5365.BevelGearMeshMultibodyDynamicsAnalysis)

        @property
        def concept_gear_mesh_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5379
            
            return self._parent._cast(_5379.ConceptGearMeshMultibodyDynamicsAnalysis)

        @property
        def conical_gear_mesh_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5382
            
            return self._parent._cast(_5382.ConicalGearMeshMultibodyDynamicsAnalysis)

        @property
        def cylindrical_gear_mesh_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5397
            
            return self._parent._cast(_5397.CylindricalGearMeshMultibodyDynamicsAnalysis)

        @property
        def face_gear_mesh_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5403
            
            return self._parent._cast(_5403.FaceGearMeshMultibodyDynamicsAnalysis)

        @property
        def hypoid_gear_mesh_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5413
            
            return self._parent._cast(_5413.HypoidGearMeshMultibodyDynamicsAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5421
            
            return self._parent._cast(_5421.KlingelnbergCycloPalloidConicalGearMeshMultibodyDynamicsAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5424
            
            return self._parent._cast(_5424.KlingelnbergCycloPalloidHypoidGearMeshMultibodyDynamicsAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5427
            
            return self._parent._cast(_5427.KlingelnbergCycloPalloidSpiralBevelGearMeshMultibodyDynamicsAnalysis)

        @property
        def spiral_bevel_gear_mesh_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5460
            
            return self._parent._cast(_5460.SpiralBevelGearMeshMultibodyDynamicsAnalysis)

        @property
        def straight_bevel_diff_gear_mesh_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5466
            
            return self._parent._cast(_5466.StraightBevelDiffGearMeshMultibodyDynamicsAnalysis)

        @property
        def straight_bevel_gear_mesh_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5469
            
            return self._parent._cast(_5469.StraightBevelGearMeshMultibodyDynamicsAnalysis)

        @property
        def worm_gear_mesh_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5487
            
            return self._parent._cast(_5487.WormGearMeshMultibodyDynamicsAnalysis)

        @property
        def zerol_bevel_gear_mesh_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5490
            
            return self._parent._cast(_5490.ZerolBevelGearMeshMultibodyDynamicsAnalysis)

        @property
        def gear_mesh_multibody_dynamics_analysis(self) -> 'GearMeshMultibodyDynamicsAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GearMeshMultibodyDynamicsAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def average_sliding_velocity_left_flank(self) -> 'float':
        """float: 'AverageSlidingVelocityLeftFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AverageSlidingVelocityLeftFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def average_sliding_velocity_right_flank(self) -> 'float':
        """float: 'AverageSlidingVelocityRightFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AverageSlidingVelocityRightFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def coefficient_of_friction_left_flank(self) -> 'float':
        """float: 'CoefficientOfFrictionLeftFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CoefficientOfFrictionLeftFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def coefficient_of_friction_right_flank(self) -> 'float':
        """float: 'CoefficientOfFrictionRightFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CoefficientOfFrictionRightFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def contact_status(self) -> '_69.GearMeshContactStatus':
        """GearMeshContactStatus: 'ContactStatus' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ContactStatus

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, _69.GearMeshContactStatus)
        return constructor.new_from_mastapy_type(_69.GearMeshContactStatus)(value) if value is not None else None

    @property
    def equivalent_misalignment_left_flank(self) -> 'float':
        """float: 'EquivalentMisalignmentLeftFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.EquivalentMisalignmentLeftFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def equivalent_misalignment_right_flank(self) -> 'float':
        """float: 'EquivalentMisalignmentRightFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.EquivalentMisalignmentRightFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def force_normal_to_left_flank(self) -> 'float':
        """float: 'ForceNormalToLeftFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ForceNormalToLeftFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def force_normal_to_right_flank(self) -> 'float':
        """float: 'ForceNormalToRightFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ForceNormalToRightFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def impact_power_left_flank(self) -> 'float':
        """float: 'ImpactPowerLeftFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ImpactPowerLeftFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def impact_power_right_flank(self) -> 'float':
        """float: 'ImpactPowerRightFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ImpactPowerRightFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def impact_power_total(self) -> 'float':
        """float: 'ImpactPowerTotal' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ImpactPowerTotal

        if temp is None:
            return 0.0

        return temp

    @property
    def mesh_power_loss(self) -> 'float':
        """float: 'MeshPowerLoss' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeshPowerLoss

        if temp is None:
            return 0.0

        return temp

    @property
    def misalignment_due_to_tilt_left_flank(self) -> 'float':
        """float: 'MisalignmentDueToTiltLeftFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MisalignmentDueToTiltLeftFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def misalignment_due_to_tilt_right_flank(self) -> 'float':
        """float: 'MisalignmentDueToTiltRightFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MisalignmentDueToTiltRightFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def normal_stiffness(self) -> 'float':
        """float: 'NormalStiffness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NormalStiffness

        if temp is None:
            return 0.0

        return temp

    @property
    def normal_stiffness_left_flank(self) -> 'float':
        """float: 'NormalStiffnessLeftFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NormalStiffnessLeftFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def normal_stiffness_right_flank(self) -> 'float':
        """float: 'NormalStiffnessRightFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NormalStiffnessRightFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def pitch_line_velocity_left_flank(self) -> 'float':
        """float: 'PitchLineVelocityLeftFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PitchLineVelocityLeftFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def pitch_line_velocity_right_flank(self) -> 'float':
        """float: 'PitchLineVelocityRightFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PitchLineVelocityRightFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def separation(self) -> 'float':
        """float: 'Separation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Separation

        if temp is None:
            return 0.0

        return temp

    @property
    def separation_normal_to_left_flank(self) -> 'float':
        """float: 'SeparationNormalToLeftFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SeparationNormalToLeftFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def separation_normal_to_right_flank(self) -> 'float':
        """float: 'SeparationNormalToRightFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SeparationNormalToRightFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def separation_transverse_to_left_flank(self) -> 'float':
        """float: 'SeparationTransverseToLeftFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SeparationTransverseToLeftFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def separation_transverse_to_right_flank(self) -> 'float':
        """float: 'SeparationTransverseToRightFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SeparationTransverseToRightFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def strain_energy_left_flank(self) -> 'float':
        """float: 'StrainEnergyLeftFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StrainEnergyLeftFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def strain_energy_right_flank(self) -> 'float':
        """float: 'StrainEnergyRightFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StrainEnergyRightFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def strain_energy_total(self) -> 'float':
        """float: 'StrainEnergyTotal' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StrainEnergyTotal

        if temp is None:
            return 0.0

        return temp

    @property
    def tilt_stiffness(self) -> 'float':
        """float: 'TiltStiffness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TiltStiffness

        if temp is None:
            return 0.0

        return temp

    @property
    def tooth_passing_frequency(self) -> 'float':
        """float: 'ToothPassingFrequency' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ToothPassingFrequency

        if temp is None:
            return 0.0

        return temp

    @property
    def tooth_passing_speed_gear_a(self) -> 'float':
        """float: 'ToothPassingSpeedGearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ToothPassingSpeedGearA

        if temp is None:
            return 0.0

        return temp

    @property
    def tooth_passing_speed_gear_b(self) -> 'float':
        """float: 'ToothPassingSpeedGearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ToothPassingSpeedGearB

        if temp is None:
            return 0.0

        return temp

    @property
    def transverse_stiffness_left_flank(self) -> 'float':
        """float: 'TransverseStiffnessLeftFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TransverseStiffnessLeftFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def transverse_stiffness_right_flank(self) -> 'float':
        """float: 'TransverseStiffnessRightFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TransverseStiffnessRightFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def connection_design(self) -> '_2294.GearMesh':
        """GearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'GearMeshMultibodyDynamicsAnalysis._Cast_GearMeshMultibodyDynamicsAnalysis':
        return self._Cast_GearMeshMultibodyDynamicsAnalysis(self)
