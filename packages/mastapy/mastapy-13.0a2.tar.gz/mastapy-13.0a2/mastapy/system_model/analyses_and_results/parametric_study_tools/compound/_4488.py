"""_4488.py

KlingelnbergCycloPalloidHypoidGearMeshCompoundParametricStudyTool
"""
from typing import List

from mastapy.system_model.connections_and_sockets.gears import _2300
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4347
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4485
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_MESH_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound', 'KlingelnbergCycloPalloidHypoidGearMeshCompoundParametricStudyTool')


__docformat__ = 'restructuredtext en'
__all__ = ('KlingelnbergCycloPalloidHypoidGearMeshCompoundParametricStudyTool',)


class KlingelnbergCycloPalloidHypoidGearMeshCompoundParametricStudyTool(_4485.KlingelnbergCycloPalloidConicalGearMeshCompoundParametricStudyTool):
    """KlingelnbergCycloPalloidHypoidGearMeshCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_MESH_COMPOUND_PARAMETRIC_STUDY_TOOL

    class _Cast_KlingelnbergCycloPalloidHypoidGearMeshCompoundParametricStudyTool:
        """Special nested class for casting KlingelnbergCycloPalloidHypoidGearMeshCompoundParametricStudyTool to subclasses."""

        def __init__(self, parent: 'KlingelnbergCycloPalloidHypoidGearMeshCompoundParametricStudyTool'):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_parametric_study_tool(self):
            return self._parent._cast(_4485.KlingelnbergCycloPalloidConicalGearMeshCompoundParametricStudyTool)

        @property
        def conical_gear_mesh_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4451
            
            return self._parent._cast(_4451.ConicalGearMeshCompoundParametricStudyTool)

        @property
        def gear_mesh_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4477
            
            return self._parent._cast(_4477.GearMeshCompoundParametricStudyTool)

        @property
        def inter_mountable_component_connection_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4483
            
            return self._parent._cast(_4483.InterMountableComponentConnectionCompoundParametricStudyTool)

        @property
        def connection_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4453
            
            return self._parent._cast(_4453.ConnectionCompoundParametricStudyTool)

        @property
        def connection_compound_analysis(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7501
            
            return self._parent._cast(_7501.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7505
            
            return self._parent._cast(_7505.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(self):
            from mastapy.system_model.analyses_and_results import _2630
            
            return self._parent._cast(_2630.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_parametric_study_tool(self) -> 'KlingelnbergCycloPalloidHypoidGearMeshCompoundParametricStudyTool':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'KlingelnbergCycloPalloidHypoidGearMeshCompoundParametricStudyTool.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2300.KlingelnbergCycloPalloidHypoidGearMesh':
        """KlingelnbergCycloPalloidHypoidGearMesh: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_design(self) -> '_2300.KlingelnbergCycloPalloidHypoidGearMesh':
        """KlingelnbergCycloPalloidHypoidGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_analysis_cases_ready(self) -> 'List[_4347.KlingelnbergCycloPalloidHypoidGearMeshParametricStudyTool]':
        """List[KlingelnbergCycloPalloidHypoidGearMeshParametricStudyTool]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def connection_analysis_cases(self) -> 'List[_4347.KlingelnbergCycloPalloidHypoidGearMeshParametricStudyTool]':
        """List[KlingelnbergCycloPalloidHypoidGearMeshParametricStudyTool]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'KlingelnbergCycloPalloidHypoidGearMeshCompoundParametricStudyTool._Cast_KlingelnbergCycloPalloidHypoidGearMeshCompoundParametricStudyTool':
        return self._Cast_KlingelnbergCycloPalloidHypoidGearMeshCompoundParametricStudyTool(self)
