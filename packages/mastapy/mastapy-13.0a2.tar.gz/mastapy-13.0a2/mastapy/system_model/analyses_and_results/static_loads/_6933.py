"""_6933.py

SynchroniserPartLoadCase
"""
from mastapy.system_model.part_model.couplings import _2584
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6816
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_PART_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'SynchroniserPartLoadCase')


__docformat__ = 'restructuredtext en'
__all__ = ('SynchroniserPartLoadCase',)


class SynchroniserPartLoadCase(_6816.CouplingHalfLoadCase):
    """SynchroniserPartLoadCase

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_PART_LOAD_CASE

    class _Cast_SynchroniserPartLoadCase:
        """Special nested class for casting SynchroniserPartLoadCase to subclasses."""

        def __init__(self, parent: 'SynchroniserPartLoadCase'):
            self._parent = parent

        @property
        def coupling_half_load_case(self):
            return self._parent._cast(_6816.CouplingHalfLoadCase)

        @property
        def mountable_component_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6888
            
            return self._parent._cast(_6888.MountableComponentLoadCase)

        @property
        def component_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6801
            
            return self._parent._cast(_6801.ComponentLoadCase)

        @property
        def part_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6892
            
            return self._parent._cast(_6892.PartLoadCase)

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
        def synchroniser_half_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6931
            
            return self._parent._cast(_6931.SynchroniserHalfLoadCase)

        @property
        def synchroniser_sleeve_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6934
            
            return self._parent._cast(_6934.SynchroniserSleeveLoadCase)

        @property
        def synchroniser_part_load_case(self) -> 'SynchroniserPartLoadCase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'SynchroniserPartLoadCase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2584.SynchroniserPart':
        """SynchroniserPart: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'SynchroniserPartLoadCase._Cast_SynchroniserPartLoadCase':
        return self._Cast_SynchroniserPartLoadCase(self)
