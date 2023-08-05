"""_4344.py

KlingelnbergCycloPalloidConicalGearMeshParametricStudyTool
"""
from mastapy.system_model.connections_and_sockets.gears import _2299
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4303
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_MESH_PARAMETRIC_STUDY_TOOL = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools', 'KlingelnbergCycloPalloidConicalGearMeshParametricStudyTool')


__docformat__ = 'restructuredtext en'
__all__ = ('KlingelnbergCycloPalloidConicalGearMeshParametricStudyTool',)


class KlingelnbergCycloPalloidConicalGearMeshParametricStudyTool(_4303.ConicalGearMeshParametricStudyTool):
    """KlingelnbergCycloPalloidConicalGearMeshParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_MESH_PARAMETRIC_STUDY_TOOL

    class _Cast_KlingelnbergCycloPalloidConicalGearMeshParametricStudyTool:
        """Special nested class for casting KlingelnbergCycloPalloidConicalGearMeshParametricStudyTool to subclasses."""

        def __init__(self, parent: 'KlingelnbergCycloPalloidConicalGearMeshParametricStudyTool'):
            self._parent = parent

        @property
        def conical_gear_mesh_parametric_study_tool(self):
            return self._parent._cast(_4303.ConicalGearMeshParametricStudyTool)

        @property
        def gear_mesh_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4336
            
            return self._parent._cast(_4336.GearMeshParametricStudyTool)

        @property
        def inter_mountable_component_connection_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4343
            
            return self._parent._cast(_4343.InterMountableComponentConnectionParametricStudyTool)

        @property
        def connection_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4306
            
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
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4347
            
            return self._parent._cast(_4347.KlingelnbergCycloPalloidHypoidGearMeshParametricStudyTool)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4350
            
            return self._parent._cast(_4350.KlingelnbergCycloPalloidSpiralBevelGearMeshParametricStudyTool)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_parametric_study_tool(self) -> 'KlingelnbergCycloPalloidConicalGearMeshParametricStudyTool':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'KlingelnbergCycloPalloidConicalGearMeshParametricStudyTool.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_2299.KlingelnbergCycloPalloidConicalGearMesh':
        """KlingelnbergCycloPalloidConicalGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'KlingelnbergCycloPalloidConicalGearMeshParametricStudyTool._Cast_KlingelnbergCycloPalloidConicalGearMeshParametricStudyTool':
        return self._Cast_KlingelnbergCycloPalloidConicalGearMeshParametricStudyTool(self)
