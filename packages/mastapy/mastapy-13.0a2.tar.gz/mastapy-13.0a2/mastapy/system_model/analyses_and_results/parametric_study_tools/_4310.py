"""_4310.py

CouplingParametricStudyTool
"""
from mastapy.system_model.part_model.couplings import _2562
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4387
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_PARAMETRIC_STUDY_TOOL = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools', 'CouplingParametricStudyTool')


__docformat__ = 'restructuredtext en'
__all__ = ('CouplingParametricStudyTool',)


class CouplingParametricStudyTool(_4387.SpecialisedAssemblyParametricStudyTool):
    """CouplingParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _COUPLING_PARAMETRIC_STUDY_TOOL

    class _Cast_CouplingParametricStudyTool:
        """Special nested class for casting CouplingParametricStudyTool to subclasses."""

        def __init__(self, parent: 'CouplingParametricStudyTool'):
            self._parent = parent

        @property
        def specialised_assembly_parametric_study_tool(self):
            return self._parent._cast(_4387.SpecialisedAssemblyParametricStudyTool)

        @property
        def abstract_assembly_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4271
            
            return self._parent._cast(_4271.AbstractAssemblyParametricStudyTool)

        @property
        def part_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4368
            
            return self._parent._cast(_4368.PartParametricStudyTool)

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
        def clutch_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4294
            
            return self._parent._cast(_4294.ClutchParametricStudyTool)

        @property
        def concept_coupling_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4299
            
            return self._parent._cast(_4299.ConceptCouplingParametricStudyTool)

        @property
        def part_to_part_shear_coupling_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4371
            
            return self._parent._cast(_4371.PartToPartShearCouplingParametricStudyTool)

        @property
        def spring_damper_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4393
            
            return self._parent._cast(_4393.SpringDamperParametricStudyTool)

        @property
        def torque_converter_parametric_study_tool(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4407
            
            return self._parent._cast(_4407.TorqueConverterParametricStudyTool)

        @property
        def coupling_parametric_study_tool(self) -> 'CouplingParametricStudyTool':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CouplingParametricStudyTool.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2562.Coupling':
        """Coupling: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'CouplingParametricStudyTool._Cast_CouplingParametricStudyTool':
        return self._Cast_CouplingParametricStudyTool(self)
