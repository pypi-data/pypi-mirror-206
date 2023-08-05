"""_4423.py

AGMAGleasonConicalGearMeshCompoundParametricStudyTool
"""
from typing import List

from mastapy.system_model.analyses_and_results.parametric_study_tools import _4275
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4451
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_MESH_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound', 'AGMAGleasonConicalGearMeshCompoundParametricStudyTool')


__docformat__ = 'restructuredtext en'
__all__ = ('AGMAGleasonConicalGearMeshCompoundParametricStudyTool',)


class AGMAGleasonConicalGearMeshCompoundParametricStudyTool(_4451.ConicalGearMeshCompoundParametricStudyTool):
    """AGMAGleasonConicalGearMeshCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_MESH_COMPOUND_PARAMETRIC_STUDY_TOOL

    class _Cast_AGMAGleasonConicalGearMeshCompoundParametricStudyTool:
        """Special nested class for casting AGMAGleasonConicalGearMeshCompoundParametricStudyTool to subclasses."""

        def __init__(self, parent: 'AGMAGleasonConicalGearMeshCompoundParametricStudyTool'):
            self._parent = parent

        @property
        def conical_gear_mesh_compound_parametric_study_tool(self):
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
        def bevel_differential_gear_mesh_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4430
            
            return self._parent._cast(_4430.BevelDifferentialGearMeshCompoundParametricStudyTool)

        @property
        def bevel_gear_mesh_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4435
            
            return self._parent._cast(_4435.BevelGearMeshCompoundParametricStudyTool)

        @property
        def hypoid_gear_mesh_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4481
            
            return self._parent._cast(_4481.HypoidGearMeshCompoundParametricStudyTool)

        @property
        def spiral_bevel_gear_mesh_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4518
            
            return self._parent._cast(_4518.SpiralBevelGearMeshCompoundParametricStudyTool)

        @property
        def straight_bevel_diff_gear_mesh_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4524
            
            return self._parent._cast(_4524.StraightBevelDiffGearMeshCompoundParametricStudyTool)

        @property
        def straight_bevel_gear_mesh_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4527
            
            return self._parent._cast(_4527.StraightBevelGearMeshCompoundParametricStudyTool)

        @property
        def zerol_bevel_gear_mesh_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4545
            
            return self._parent._cast(_4545.ZerolBevelGearMeshCompoundParametricStudyTool)

        @property
        def agma_gleason_conical_gear_mesh_compound_parametric_study_tool(self) -> 'AGMAGleasonConicalGearMeshCompoundParametricStudyTool':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AGMAGleasonConicalGearMeshCompoundParametricStudyTool.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(self) -> 'List[_4275.AGMAGleasonConicalGearMeshParametricStudyTool]':
        """List[AGMAGleasonConicalGearMeshParametricStudyTool]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def connection_analysis_cases_ready(self) -> 'List[_4275.AGMAGleasonConicalGearMeshParametricStudyTool]':
        """List[AGMAGleasonConicalGearMeshParametricStudyTool]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'AGMAGleasonConicalGearMeshCompoundParametricStudyTool._Cast_AGMAGleasonConicalGearMeshCompoundParametricStudyTool':
        return self._Cast_AGMAGleasonConicalGearMeshCompoundParametricStudyTool(self)
