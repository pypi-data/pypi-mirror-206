"""_4311.py

CVTBeltConnectionParametricStudyTool
"""
from mastapy.system_model.connections_and_sockets import _2254
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4280
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_BELT_CONNECTION_PARAMETRIC_STUDY_TOOL = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools', 'CVTBeltConnectionParametricStudyTool')


__docformat__ = 'restructuredtext en'
__all__ = ('CVTBeltConnectionParametricStudyTool',)


class CVTBeltConnectionParametricStudyTool(_4280.BeltConnectionParametricStudyTool):
    """CVTBeltConnectionParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _CVT_BELT_CONNECTION_PARAMETRIC_STUDY_TOOL

    class _Cast_CVTBeltConnectionParametricStudyTool:
        """Special nested class for casting CVTBeltConnectionParametricStudyTool to subclasses."""

        def __init__(self, parent: 'CVTBeltConnectionParametricStudyTool'):
            self._parent = parent

        @property
        def belt_connection_parametric_study_tool(self):
            return self._parent._cast(_4280.BeltConnectionParametricStudyTool)

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
        def cvt_belt_connection_parametric_study_tool(self) -> 'CVTBeltConnectionParametricStudyTool':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CVTBeltConnectionParametricStudyTool.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_2254.CVTBeltConnection':
        """CVTBeltConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'CVTBeltConnectionParametricStudyTool._Cast_CVTBeltConnectionParametricStudyTool':
        return self._Cast_CVTBeltConnectionParametricStudyTool(self)
