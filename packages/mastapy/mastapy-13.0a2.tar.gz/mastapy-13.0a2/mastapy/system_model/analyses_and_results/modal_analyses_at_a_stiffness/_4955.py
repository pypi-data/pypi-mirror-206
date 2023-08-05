"""_4955.py

WormGearModalAnalysisAtAStiffness
"""
from mastapy.system_model.part_model.gears import _2530
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6946
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4890
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_WORM_GEAR_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness', 'WormGearModalAnalysisAtAStiffness')


__docformat__ = 'restructuredtext en'
__all__ = ('WormGearModalAnalysisAtAStiffness',)


class WormGearModalAnalysisAtAStiffness(_4890.GearModalAnalysisAtAStiffness):
    """WormGearModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _WORM_GEAR_MODAL_ANALYSIS_AT_A_STIFFNESS

    class _Cast_WormGearModalAnalysisAtAStiffness:
        """Special nested class for casting WormGearModalAnalysisAtAStiffness to subclasses."""

        def __init__(self, parent: 'WormGearModalAnalysisAtAStiffness'):
            self._parent = parent

        @property
        def gear_modal_analysis_at_a_stiffness(self):
            return self._parent._cast(_4890.GearModalAnalysisAtAStiffness)

        @property
        def mountable_component_modal_analysis_at_a_stiffness(self):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4908
            
            return self._parent._cast(_4908.MountableComponentModalAnalysisAtAStiffness)

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
        def worm_gear_modal_analysis_at_a_stiffness(self) -> 'WormGearModalAnalysisAtAStiffness':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'WormGearModalAnalysisAtAStiffness.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2530.WormGear':
        """WormGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_load_case(self) -> '_6946.WormGearLoadCase':
        """WormGearLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'WormGearModalAnalysisAtAStiffness._Cast_WormGearModalAnalysisAtAStiffness':
        return self._Cast_WormGearModalAnalysisAtAStiffness(self)
