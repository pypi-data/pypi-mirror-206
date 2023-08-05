"""_4831.py

AbstractShaftModalAnalysisAtAStiffness
"""
from mastapy.system_model.part_model import _2415
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4832
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness', 'AbstractShaftModalAnalysisAtAStiffness')


__docformat__ = 'restructuredtext en'
__all__ = ('AbstractShaftModalAnalysisAtAStiffness',)


class AbstractShaftModalAnalysisAtAStiffness(_4832.AbstractShaftOrHousingModalAnalysisAtAStiffness):
    """AbstractShaftModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_MODAL_ANALYSIS_AT_A_STIFFNESS

    class _Cast_AbstractShaftModalAnalysisAtAStiffness:
        """Special nested class for casting AbstractShaftModalAnalysisAtAStiffness to subclasses."""

        def __init__(self, parent: 'AbstractShaftModalAnalysisAtAStiffness'):
            self._parent = parent

        @property
        def abstract_shaft_or_housing_modal_analysis_at_a_stiffness(self):
            return self._parent._cast(_4832.AbstractShaftOrHousingModalAnalysisAtAStiffness)

        @property
        def component_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4855
            
            return self._parent._cast(_4855.ComponentModalAnalysisAtAStiffness)

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
        def cycloidal_disc_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4875
            
            return self._parent._cast(_4875.CycloidalDiscModalAnalysisAtAStiffness)

        @property
        def shaft_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4927
            
            return self._parent._cast(_4927.ShaftModalAnalysisAtAStiffness)

        @property
        def abstract_shaft_modal_analysis_at_a_stiffness(self) -> 'AbstractShaftModalAnalysisAtAStiffness':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AbstractShaftModalAnalysisAtAStiffness.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2415.AbstractShaft':
        """AbstractShaft: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'AbstractShaftModalAnalysisAtAStiffness._Cast_AbstractShaftModalAnalysisAtAStiffness':
        return self._Cast_AbstractShaftModalAnalysisAtAStiffness(self)
