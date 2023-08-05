"""_4456.py

CouplingConnectionCompoundParametricStudyTool
"""
from typing import List

from mastapy.system_model.analyses_and_results.parametric_study_tools import _4308
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4483
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_CONNECTION_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound', 'CouplingConnectionCompoundParametricStudyTool')


__docformat__ = 'restructuredtext en'
__all__ = ('CouplingConnectionCompoundParametricStudyTool',)


class CouplingConnectionCompoundParametricStudyTool(_4483.InterMountableComponentConnectionCompoundParametricStudyTool):
    """CouplingConnectionCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _COUPLING_CONNECTION_COMPOUND_PARAMETRIC_STUDY_TOOL

    class _Cast_CouplingConnectionCompoundParametricStudyTool:
        """Special nested class for casting CouplingConnectionCompoundParametricStudyTool to subclasses."""

        def __init__(self, parent: 'CouplingConnectionCompoundParametricStudyTool'):
            self._parent = parent

        @property
        def inter_mountable_component_connection_compound_parametric_study_tool(self):
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
        def clutch_connection_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4440
            
            return self._parent._cast(_4440.ClutchConnectionCompoundParametricStudyTool)

        @property
        def concept_coupling_connection_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4445
            
            return self._parent._cast(_4445.ConceptCouplingConnectionCompoundParametricStudyTool)

        @property
        def part_to_part_shear_coupling_connection_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4499
            
            return self._parent._cast(_4499.PartToPartShearCouplingConnectionCompoundParametricStudyTool)

        @property
        def spring_damper_connection_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4521
            
            return self._parent._cast(_4521.SpringDamperConnectionCompoundParametricStudyTool)

        @property
        def torque_converter_connection_compound_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4536
            
            return self._parent._cast(_4536.TorqueConverterConnectionCompoundParametricStudyTool)

        @property
        def coupling_connection_compound_parametric_study_tool(self) -> 'CouplingConnectionCompoundParametricStudyTool':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CouplingConnectionCompoundParametricStudyTool.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(self) -> 'List[_4308.CouplingConnectionParametricStudyTool]':
        """List[CouplingConnectionParametricStudyTool]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def connection_analysis_cases_ready(self) -> 'List[_4308.CouplingConnectionParametricStudyTool]':
        """List[CouplingConnectionParametricStudyTool]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'CouplingConnectionCompoundParametricStudyTool._Cast_CouplingConnectionCompoundParametricStudyTool':
        return self._Cast_CouplingConnectionCompoundParametricStudyTool(self)
