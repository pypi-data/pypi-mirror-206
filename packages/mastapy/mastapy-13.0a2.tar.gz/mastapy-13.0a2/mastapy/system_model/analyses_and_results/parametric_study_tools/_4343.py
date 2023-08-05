"""_4343.py

InterMountableComponentConnectionParametricStudyTool
"""
from mastapy.system_model.connections_and_sockets import _2262
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4306
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INTER_MOUNTABLE_COMPONENT_CONNECTION_PARAMETRIC_STUDY_TOOL = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools', 'InterMountableComponentConnectionParametricStudyTool')


__docformat__ = 'restructuredtext en'
__all__ = ('InterMountableComponentConnectionParametricStudyTool',)


class InterMountableComponentConnectionParametricStudyTool(_4306.ConnectionParametricStudyTool):
    """InterMountableComponentConnectionParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _INTER_MOUNTABLE_COMPONENT_CONNECTION_PARAMETRIC_STUDY_TOOL

    class _Cast_InterMountableComponentConnectionParametricStudyTool:
        """Special nested class for casting InterMountableComponentConnectionParametricStudyTool to subclasses."""

        def __init__(self, parent: 'InterMountableComponentConnectionParametricStudyTool'):
            self._parent = parent

        @property
        def connection_parametric_study_tool(self):
            return self._parent._cast(_4306.ConnectionParametricStudyTool)

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
        def agma_gleason_conical_gear_mesh_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4275
            
            return self._parent._cast(_4275.AGMAGleasonConicalGearMeshParametricStudyTool)

        @property
        def belt_connection_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4280
            
            return self._parent._cast(_4280.BeltConnectionParametricStudyTool)

        @property
        def bevel_differential_gear_mesh_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4282
            
            return self._parent._cast(_4282.BevelDifferentialGearMeshParametricStudyTool)

        @property
        def bevel_gear_mesh_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4287
            
            return self._parent._cast(_4287.BevelGearMeshParametricStudyTool)

        @property
        def clutch_connection_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4292
            
            return self._parent._cast(_4292.ClutchConnectionParametricStudyTool)

        @property
        def concept_coupling_connection_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4297
            
            return self._parent._cast(_4297.ConceptCouplingConnectionParametricStudyTool)

        @property
        def concept_gear_mesh_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4300
            
            return self._parent._cast(_4300.ConceptGearMeshParametricStudyTool)

        @property
        def conical_gear_mesh_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4303
            
            return self._parent._cast(_4303.ConicalGearMeshParametricStudyTool)

        @property
        def coupling_connection_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4308
            
            return self._parent._cast(_4308.CouplingConnectionParametricStudyTool)

        @property
        def cvt_belt_connection_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4311
            
            return self._parent._cast(_4311.CVTBeltConnectionParametricStudyTool)

        @property
        def cylindrical_gear_mesh_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4318
            
            return self._parent._cast(_4318.CylindricalGearMeshParametricStudyTool)

        @property
        def face_gear_mesh_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4331
            
            return self._parent._cast(_4331.FaceGearMeshParametricStudyTool)

        @property
        def gear_mesh_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4336
            
            return self._parent._cast(_4336.GearMeshParametricStudyTool)

        @property
        def hypoid_gear_mesh_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4340
            
            return self._parent._cast(_4340.HypoidGearMeshParametricStudyTool)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4344
            
            return self._parent._cast(_4344.KlingelnbergCycloPalloidConicalGearMeshParametricStudyTool)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4347
            
            return self._parent._cast(_4347.KlingelnbergCycloPalloidHypoidGearMeshParametricStudyTool)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4350
            
            return self._parent._cast(_4350.KlingelnbergCycloPalloidSpiralBevelGearMeshParametricStudyTool)

        @property
        def part_to_part_shear_coupling_connection_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4369
            
            return self._parent._cast(_4369.PartToPartShearCouplingConnectionParametricStudyTool)

        @property
        def ring_pins_to_disc_connection_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4379
            
            return self._parent._cast(_4379.RingPinsToDiscConnectionParametricStudyTool)

        @property
        def rolling_ring_connection_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4381
            
            return self._parent._cast(_4381.RollingRingConnectionParametricStudyTool)

        @property
        def spiral_bevel_gear_mesh_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4388
            
            return self._parent._cast(_4388.SpiralBevelGearMeshParametricStudyTool)

        @property
        def spring_damper_connection_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4391
            
            return self._parent._cast(_4391.SpringDamperConnectionParametricStudyTool)

        @property
        def straight_bevel_diff_gear_mesh_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4394
            
            return self._parent._cast(_4394.StraightBevelDiffGearMeshParametricStudyTool)

        @property
        def straight_bevel_gear_mesh_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4397
            
            return self._parent._cast(_4397.StraightBevelGearMeshParametricStudyTool)

        @property
        def torque_converter_connection_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4406
            
            return self._parent._cast(_4406.TorqueConverterConnectionParametricStudyTool)

        @property
        def worm_gear_mesh_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4412
            
            return self._parent._cast(_4412.WormGearMeshParametricStudyTool)

        @property
        def zerol_bevel_gear_mesh_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4415
            
            return self._parent._cast(_4415.ZerolBevelGearMeshParametricStudyTool)

        @property
        def inter_mountable_component_connection_parametric_study_tool(self) -> 'InterMountableComponentConnectionParametricStudyTool':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'InterMountableComponentConnectionParametricStudyTool.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_2262.InterMountableComponentConnection':
        """InterMountableComponentConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'InterMountableComponentConnectionParametricStudyTool._Cast_InterMountableComponentConnectionParametricStudyTool':
        return self._Cast_InterMountableComponentConnectionParametricStudyTool(self)
