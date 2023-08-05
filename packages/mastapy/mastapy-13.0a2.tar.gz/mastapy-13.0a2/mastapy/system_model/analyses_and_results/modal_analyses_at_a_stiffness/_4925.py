"""_4925.py

RootAssemblyModalAnalysisAtAStiffness
"""
from mastapy.system_model.part_model import _2454
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _2616, _4837
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROOT_ASSEMBLY_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness', 'RootAssemblyModalAnalysisAtAStiffness')


__docformat__ = 'restructuredtext en'
__all__ = ('RootAssemblyModalAnalysisAtAStiffness',)


class RootAssemblyModalAnalysisAtAStiffness(_4837.AssemblyModalAnalysisAtAStiffness):
    """RootAssemblyModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _ROOT_ASSEMBLY_MODAL_ANALYSIS_AT_A_STIFFNESS

    class _Cast_RootAssemblyModalAnalysisAtAStiffness:
        """Special nested class for casting RootAssemblyModalAnalysisAtAStiffness to subclasses."""

        def __init__(self, parent: 'RootAssemblyModalAnalysisAtAStiffness'):
            self._parent = parent

        @property
        def assembly_modal_analysis_at_a_stiffness(self):
            return self._parent._cast(_4837.AssemblyModalAnalysisAtAStiffness)

        @property
        def abstract_assembly_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4830
            
            return self._parent._cast(_4830.AbstractAssemblyModalAnalysisAtAStiffness)

        @property
        def part_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4910
            
            return self._parent._cast(_4910.PartModalAnalysisAtAStiffness)

        @property
        def part_static_load_analysis_case(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7510
            
            return self._parent._cast(_7510.PartStaticLoadAnalysisCase)

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
        def root_assembly_modal_analysis_at_a_stiffness(self) -> 'RootAssemblyModalAnalysisAtAStiffness':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'RootAssemblyModalAnalysisAtAStiffness.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2454.RootAssembly':
        """RootAssembly: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def modal_analysis_at_a_stiffness_inputs(self) -> '_2616.ModalAnalysisAtAStiffness':
        """ModalAnalysisAtAStiffness: 'ModalAnalysisAtAStiffnessInputs' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ModalAnalysisAtAStiffnessInputs

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'RootAssemblyModalAnalysisAtAStiffness._Cast_RootAssemblyModalAnalysisAtAStiffness':
        return self._Cast_RootAssemblyModalAnalysisAtAStiffness(self)
