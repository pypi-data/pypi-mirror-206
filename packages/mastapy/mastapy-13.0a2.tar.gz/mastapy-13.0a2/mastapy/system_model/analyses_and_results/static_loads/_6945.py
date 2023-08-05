"""_6945.py

VirtualComponentLoadCase
"""
from mastapy.system_model.part_model import _2459
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6888
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_VIRTUAL_COMPONENT_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'VirtualComponentLoadCase')


__docformat__ = 'restructuredtext en'
__all__ = ('VirtualComponentLoadCase',)


class VirtualComponentLoadCase(_6888.MountableComponentLoadCase):
    """VirtualComponentLoadCase

    This is a mastapy class.
    """

    TYPE = _VIRTUAL_COMPONENT_LOAD_CASE

    class _Cast_VirtualComponentLoadCase:
        """Special nested class for casting VirtualComponentLoadCase to subclasses."""

        def __init__(self, parent: 'VirtualComponentLoadCase'):
            self._parent = parent

        @property
        def mountable_component_load_case(self):
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
        def mass_disc_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6885
            
            return self._parent._cast(_6885.MassDiscLoadCase)

        @property
        def measurement_component_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6886
            
            return self._parent._cast(_6886.MeasurementComponentLoadCase)

        @property
        def point_load_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6902
            
            return self._parent._cast(_6902.PointLoadLoadCase)

        @property
        def power_load_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6903
            
            return self._parent._cast(_6903.PowerLoadLoadCase)

        @property
        def unbalanced_mass_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6944
            
            return self._parent._cast(_6944.UnbalancedMassLoadCase)

        @property
        def virtual_component_load_case(self) -> 'VirtualComponentLoadCase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'VirtualComponentLoadCase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2459.VirtualComponent':
        """VirtualComponent: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'VirtualComponentLoadCase._Cast_VirtualComponentLoadCase':
        return self._Cast_VirtualComponentLoadCase(self)
