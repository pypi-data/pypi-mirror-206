"""_6886.py

MeasurementComponentLoadCase
"""
from mastapy.system_model.part_model import _2443
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6945
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MEASUREMENT_COMPONENT_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'MeasurementComponentLoadCase')


__docformat__ = 'restructuredtext en'
__all__ = ('MeasurementComponentLoadCase',)


class MeasurementComponentLoadCase(_6945.VirtualComponentLoadCase):
    """MeasurementComponentLoadCase

    This is a mastapy class.
    """

    TYPE = _MEASUREMENT_COMPONENT_LOAD_CASE

    class _Cast_MeasurementComponentLoadCase:
        """Special nested class for casting MeasurementComponentLoadCase to subclasses."""

        def __init__(self, parent: 'MeasurementComponentLoadCase'):
            self._parent = parent

        @property
        def virtual_component_load_case(self):
            return self._parent._cast(_6945.VirtualComponentLoadCase)

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
        def measurement_component_load_case(self) -> 'MeasurementComponentLoadCase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'MeasurementComponentLoadCase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2443.MeasurementComponent':
        """MeasurementComponent: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'MeasurementComponentLoadCase._Cast_MeasurementComponentLoadCase':
        return self._Cast_MeasurementComponentLoadCase(self)
