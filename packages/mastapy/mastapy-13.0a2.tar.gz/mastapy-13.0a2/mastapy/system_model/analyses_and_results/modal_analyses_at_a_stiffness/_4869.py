"""_4869.py

CouplingModalAnalysisAtAStiffness
"""
from mastapy.system_model.part_model.couplings import _2562
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4929
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness', 'CouplingModalAnalysisAtAStiffness')


__docformat__ = 'restructuredtext en'
__all__ = ('CouplingModalAnalysisAtAStiffness',)


class CouplingModalAnalysisAtAStiffness(_4929.SpecialisedAssemblyModalAnalysisAtAStiffness):
    """CouplingModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _COUPLING_MODAL_ANALYSIS_AT_A_STIFFNESS

    class _Cast_CouplingModalAnalysisAtAStiffness:
        """Special nested class for casting CouplingModalAnalysisAtAStiffness to subclasses."""

        def __init__(self, parent: 'CouplingModalAnalysisAtAStiffness'):
            self._parent = parent

        @property
        def specialised_assembly_modal_analysis_at_a_stiffness(self):
            return self._parent._cast(_4929.SpecialisedAssemblyModalAnalysisAtAStiffness)

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
        def clutch_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4853
            
            return self._parent._cast(_4853.ClutchModalAnalysisAtAStiffness)

        @property
        def concept_coupling_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4858
            
            return self._parent._cast(_4858.ConceptCouplingModalAnalysisAtAStiffness)

        @property
        def part_to_part_shear_coupling_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4913
            
            return self._parent._cast(_4913.PartToPartShearCouplingModalAnalysisAtAStiffness)

        @property
        def spring_damper_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4935
            
            return self._parent._cast(_4935.SpringDamperModalAnalysisAtAStiffness)

        @property
        def torque_converter_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4949
            
            return self._parent._cast(_4949.TorqueConverterModalAnalysisAtAStiffness)

        @property
        def coupling_modal_analysis_at_a_stiffness(self) -> 'CouplingModalAnalysisAtAStiffness':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CouplingModalAnalysisAtAStiffness.TYPE'):
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
    def cast_to(self) -> 'CouplingModalAnalysisAtAStiffness._Cast_CouplingModalAnalysisAtAStiffness':
        return self._Cast_CouplingModalAnalysisAtAStiffness(self)
