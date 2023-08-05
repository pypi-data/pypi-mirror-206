"""_4308.py

CouplingConnectionParametricStudyTool
"""
from mastapy.system_model.connections_and_sockets.couplings import _2327
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4343
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_CONNECTION_PARAMETRIC_STUDY_TOOL = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools', 'CouplingConnectionParametricStudyTool')


__docformat__ = 'restructuredtext en'
__all__ = ('CouplingConnectionParametricStudyTool',)


class CouplingConnectionParametricStudyTool(_4343.InterMountableComponentConnectionParametricStudyTool):
    """CouplingConnectionParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _COUPLING_CONNECTION_PARAMETRIC_STUDY_TOOL

    class _Cast_CouplingConnectionParametricStudyTool:
        """Special nested class for casting CouplingConnectionParametricStudyTool to subclasses."""

        def __init__(self, parent: 'CouplingConnectionParametricStudyTool'):
            self._parent = parent

        @property
        def inter_mountable_component_connection_parametric_study_tool(self):
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
        def clutch_connection_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4292
            
            return self._parent._cast(_4292.ClutchConnectionParametricStudyTool)

        @property
        def concept_coupling_connection_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4297
            
            return self._parent._cast(_4297.ConceptCouplingConnectionParametricStudyTool)

        @property
        def part_to_part_shear_coupling_connection_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4369
            
            return self._parent._cast(_4369.PartToPartShearCouplingConnectionParametricStudyTool)

        @property
        def spring_damper_connection_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4391
            
            return self._parent._cast(_4391.SpringDamperConnectionParametricStudyTool)

        @property
        def torque_converter_connection_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4406
            
            return self._parent._cast(_4406.TorqueConverterConnectionParametricStudyTool)

        @property
        def coupling_connection_parametric_study_tool(self) -> 'CouplingConnectionParametricStudyTool':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CouplingConnectionParametricStudyTool.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_2327.CouplingConnection':
        """CouplingConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'CouplingConnectionParametricStudyTool._Cast_CouplingConnectionParametricStudyTool':
        return self._Cast_CouplingConnectionParametricStudyTool(self)
