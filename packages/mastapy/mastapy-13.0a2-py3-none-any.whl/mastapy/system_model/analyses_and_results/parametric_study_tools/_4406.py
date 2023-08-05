"""_4406.py

TorqueConverterConnectionParametricStudyTool
"""
from typing import List

from mastapy.system_model.connections_and_sockets.couplings import _2333
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6936
from mastapy.system_model.analyses_and_results.system_deflections import _2807
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4308
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_CONNECTION_PARAMETRIC_STUDY_TOOL = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools', 'TorqueConverterConnectionParametricStudyTool')


__docformat__ = 'restructuredtext en'
__all__ = ('TorqueConverterConnectionParametricStudyTool',)


class TorqueConverterConnectionParametricStudyTool(_4308.CouplingConnectionParametricStudyTool):
    """TorqueConverterConnectionParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _TORQUE_CONVERTER_CONNECTION_PARAMETRIC_STUDY_TOOL

    class _Cast_TorqueConverterConnectionParametricStudyTool:
        """Special nested class for casting TorqueConverterConnectionParametricStudyTool to subclasses."""

        def __init__(self, parent: 'TorqueConverterConnectionParametricStudyTool'):
            self._parent = parent

        @property
        def coupling_connection_parametric_study_tool(self):
            return self._parent._cast(_4308.CouplingConnectionParametricStudyTool)

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
        def torque_converter_connection_parametric_study_tool(self) -> 'TorqueConverterConnectionParametricStudyTool':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'TorqueConverterConnectionParametricStudyTool.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_2333.TorqueConverterConnection':
        """TorqueConverterConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_load_case(self) -> '_6936.TorqueConverterConnectionLoadCase':
        """TorqueConverterConnectionLoadCase: 'ConnectionLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_system_deflection_results(self) -> 'List[_2807.TorqueConverterConnectionSystemDeflection]':
        """List[TorqueConverterConnectionSystemDeflection]: 'ConnectionSystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionSystemDeflectionResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'TorqueConverterConnectionParametricStudyTool._Cast_TorqueConverterConnectionParametricStudyTool':
        return self._Cast_TorqueConverterConnectionParametricStudyTool(self)
