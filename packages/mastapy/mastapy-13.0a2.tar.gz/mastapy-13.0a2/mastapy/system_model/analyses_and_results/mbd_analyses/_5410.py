"""_5410.py

GearMultibodyDynamicsAnalysis
"""
from typing import List

from mastapy._math.vector_3d import Vector3D
from mastapy._internal import constructor, conversion
from mastapy.system_model.part_model.gears import _2509
from mastapy.system_model.analyses_and_results.mbd_analyses.reporting import _5496
from mastapy.system_model.analyses_and_results.mbd_analyses import _5435
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses', 'GearMultibodyDynamicsAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('GearMultibodyDynamicsAnalysis',)


class GearMultibodyDynamicsAnalysis(_5435.MountableComponentMultibodyDynamicsAnalysis):
    """GearMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _GEAR_MULTIBODY_DYNAMICS_ANALYSIS

    class _Cast_GearMultibodyDynamicsAnalysis:
        """Special nested class for casting GearMultibodyDynamicsAnalysis to subclasses."""

        def __init__(self, parent: 'GearMultibodyDynamicsAnalysis'):
            self._parent = parent

        @property
        def mountable_component_multibody_dynamics_analysis(self):
            return self._parent._cast(_5435.MountableComponentMultibodyDynamicsAnalysis)

        @property
        def component_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5375
            
            return self._parent._cast(_5375.ComponentMultibodyDynamicsAnalysis)

        @property
        def part_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5437
            
            return self._parent._cast(_5437.PartMultibodyDynamicsAnalysis)

        @property
        def part_time_series_load_analysis_case(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7511
            
            return self._parent._cast(_7511.PartTimeSeriesLoadAnalysisCase)

        @property
        def part_analysis_case(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7507
            
            return self._parent._cast(_7507.PartAnalysisCase)

        @property
        def part_analysis(self):
            from mastapy.system_model.analyses_and_results import _2636
            
            return self._parent._cast(_2636.PartAnalysis)

        @property
        def design_entity_single_context_analysis(self):
            from mastapy.system_model.analyses_and_results import _2632
            
            return self._parent._cast(_2632.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(self):
            from mastapy.system_model.analyses_and_results import _2630
            
            return self._parent._cast(_2630.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5352
            
            return self._parent._cast(_5352.AGMAGleasonConicalGearMultibodyDynamicsAnalysis)

        @property
        def bevel_differential_gear_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5361
            
            return self._parent._cast(_5361.BevelDifferentialGearMultibodyDynamicsAnalysis)

        @property
        def bevel_differential_planet_gear_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5363
            
            return self._parent._cast(_5363.BevelDifferentialPlanetGearMultibodyDynamicsAnalysis)

        @property
        def bevel_differential_sun_gear_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5364
            
            return self._parent._cast(_5364.BevelDifferentialSunGearMultibodyDynamicsAnalysis)

        @property
        def bevel_gear_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5366
            
            return self._parent._cast(_5366.BevelGearMultibodyDynamicsAnalysis)

        @property
        def concept_gear_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5380
            
            return self._parent._cast(_5380.ConceptGearMultibodyDynamicsAnalysis)

        @property
        def conical_gear_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5383
            
            return self._parent._cast(_5383.ConicalGearMultibodyDynamicsAnalysis)

        @property
        def cylindrical_gear_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5398
            
            return self._parent._cast(_5398.CylindricalGearMultibodyDynamicsAnalysis)

        @property
        def cylindrical_planet_gear_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5400
            
            return self._parent._cast(_5400.CylindricalPlanetGearMultibodyDynamicsAnalysis)

        @property
        def face_gear_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5404
            
            return self._parent._cast(_5404.FaceGearMultibodyDynamicsAnalysis)

        @property
        def hypoid_gear_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5414
            
            return self._parent._cast(_5414.HypoidGearMultibodyDynamicsAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5422
            
            return self._parent._cast(_5422.KlingelnbergCycloPalloidConicalGearMultibodyDynamicsAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5425
            
            return self._parent._cast(_5425.KlingelnbergCycloPalloidHypoidGearMultibodyDynamicsAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5428
            
            return self._parent._cast(_5428.KlingelnbergCycloPalloidSpiralBevelGearMultibodyDynamicsAnalysis)

        @property
        def spiral_bevel_gear_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5461
            
            return self._parent._cast(_5461.SpiralBevelGearMultibodyDynamicsAnalysis)

        @property
        def straight_bevel_diff_gear_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5467
            
            return self._parent._cast(_5467.StraightBevelDiffGearMultibodyDynamicsAnalysis)

        @property
        def straight_bevel_gear_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5470
            
            return self._parent._cast(_5470.StraightBevelGearMultibodyDynamicsAnalysis)

        @property
        def straight_bevel_planet_gear_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5472
            
            return self._parent._cast(_5472.StraightBevelPlanetGearMultibodyDynamicsAnalysis)

        @property
        def straight_bevel_sun_gear_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5473
            
            return self._parent._cast(_5473.StraightBevelSunGearMultibodyDynamicsAnalysis)

        @property
        def worm_gear_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5488
            
            return self._parent._cast(_5488.WormGearMultibodyDynamicsAnalysis)

        @property
        def zerol_bevel_gear_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5491
            
            return self._parent._cast(_5491.ZerolBevelGearMultibodyDynamicsAnalysis)

        @property
        def gear_multibody_dynamics_analysis(self) -> 'GearMultibodyDynamicsAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GearMultibodyDynamicsAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def gear_mesh_forces_on_shaft(self) -> 'Vector3D':
        """Vector3D: 'GearMeshForcesOnShaft' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearMeshForcesOnShaft

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)
        return value

    @property
    def gear_mesh_moments_on_shaft(self) -> 'Vector3D':
        """Vector3D: 'GearMeshMomentsOnShaft' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearMeshMomentsOnShaft

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)
        return value

    @property
    def gear_mesh_torque(self) -> 'List[float]':
        """List[float]: 'GearMeshTorque' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearMeshTorque

        if temp is None:
            return None

        value = conversion.to_list_any(temp)
        return value

    @property
    def component_design(self) -> '_2509.Gear':
        """Gear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def peak_gear_torque(self) -> 'List[_5496.DynamicTorqueResultAtTime]':
        """List[DynamicTorqueResultAtTime]: 'PeakGearTorque' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PeakGearTorque

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'GearMultibodyDynamicsAnalysis._Cast_GearMultibodyDynamicsAnalysis':
        return self._Cast_GearMultibodyDynamicsAnalysis(self)
