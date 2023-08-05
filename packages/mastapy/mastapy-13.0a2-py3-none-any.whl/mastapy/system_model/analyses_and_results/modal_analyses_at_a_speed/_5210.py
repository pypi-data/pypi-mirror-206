"""_5210.py

UnbalancedMassModalAnalysisAtASpeed
"""
from mastapy.system_model.part_model import _2457
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6944
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5211
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_UNBALANCED_MASS_MODAL_ANALYSIS_AT_A_SPEED = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed', 'UnbalancedMassModalAnalysisAtASpeed')


__docformat__ = 'restructuredtext en'
__all__ = ('UnbalancedMassModalAnalysisAtASpeed',)


class UnbalancedMassModalAnalysisAtASpeed(_5211.VirtualComponentModalAnalysisAtASpeed):
    """UnbalancedMassModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _UNBALANCED_MASS_MODAL_ANALYSIS_AT_A_SPEED

    class _Cast_UnbalancedMassModalAnalysisAtASpeed:
        """Special nested class for casting UnbalancedMassModalAnalysisAtASpeed to subclasses."""

        def __init__(self, parent: 'UnbalancedMassModalAnalysisAtASpeed'):
            self._parent = parent

        @property
        def virtual_component_modal_analysis_at_a_speed(self):
            return self._parent._cast(_5211.VirtualComponentModalAnalysisAtASpeed)

        @property
        def mountable_component_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5166
            
            return self._parent._cast(_5166.MountableComponentModalAnalysisAtASpeed)

        @property
        def component_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5114
            
            return self._parent._cast(_5114.ComponentModalAnalysisAtASpeed)

        @property
        def part_modal_analysis_at_a_speed(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5168
            
            return self._parent._cast(_5168.PartModalAnalysisAtASpeed)

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
        def unbalanced_mass_modal_analysis_at_a_speed(self) -> 'UnbalancedMassModalAnalysisAtASpeed':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'UnbalancedMassModalAnalysisAtASpeed.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2457.UnbalancedMass':
        """UnbalancedMass: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_load_case(self) -> '_6944.UnbalancedMassLoadCase':
        """UnbalancedMassLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'UnbalancedMassModalAnalysisAtASpeed._Cast_UnbalancedMassModalAnalysisAtASpeed':
        return self._Cast_UnbalancedMassModalAnalysisAtASpeed(self)
