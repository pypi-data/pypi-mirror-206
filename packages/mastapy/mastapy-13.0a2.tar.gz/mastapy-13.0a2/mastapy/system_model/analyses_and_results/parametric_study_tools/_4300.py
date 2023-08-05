"""_4300.py

ConceptGearMeshParametricStudyTool
"""
from typing import List

from mastapy.system_model.connections_and_sockets.gears import _2286
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6806
from mastapy.system_model.analyses_and_results.system_deflections import _2699
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4336
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_GEAR_MESH_PARAMETRIC_STUDY_TOOL = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools', 'ConceptGearMeshParametricStudyTool')


__docformat__ = 'restructuredtext en'
__all__ = ('ConceptGearMeshParametricStudyTool',)


class ConceptGearMeshParametricStudyTool(_4336.GearMeshParametricStudyTool):
    """ConceptGearMeshParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _CONCEPT_GEAR_MESH_PARAMETRIC_STUDY_TOOL

    class _Cast_ConceptGearMeshParametricStudyTool:
        """Special nested class for casting ConceptGearMeshParametricStudyTool to subclasses."""

        def __init__(self, parent: 'ConceptGearMeshParametricStudyTool'):
            self._parent = parent

        @property
        def gear_mesh_parametric_study_tool(self):
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
        def concept_gear_mesh_parametric_study_tool(self) -> 'ConceptGearMeshParametricStudyTool':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConceptGearMeshParametricStudyTool.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_2286.ConceptGearMesh':
        """ConceptGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_load_case(self) -> '_6806.ConceptGearMeshLoadCase':
        """ConceptGearMeshLoadCase: 'ConnectionLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_system_deflection_results(self) -> 'List[_2699.ConceptGearMeshSystemDeflection]':
        """List[ConceptGearMeshSystemDeflection]: 'ConnectionSystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionSystemDeflectionResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'ConceptGearMeshParametricStudyTool._Cast_ConceptGearMeshParametricStudyTool':
        return self._Cast_ConceptGearMeshParametricStudyTool(self)
