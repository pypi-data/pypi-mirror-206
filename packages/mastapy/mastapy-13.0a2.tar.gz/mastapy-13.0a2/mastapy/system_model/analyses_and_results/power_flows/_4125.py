"""_4125.py

SynchroniserHalfPowerFlow
"""
from mastapy.system_model.analyses_and_results.power_flows import _4030, _4126
from mastapy._internal import constructor
from mastapy.system_model.part_model.couplings import _2583
from mastapy.system_model.analyses_and_results.static_loads import _6931
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_HALF_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows', 'SynchroniserHalfPowerFlow')


__docformat__ = 'restructuredtext en'
__all__ = ('SynchroniserHalfPowerFlow',)


class SynchroniserHalfPowerFlow(_4126.SynchroniserPartPowerFlow):
    """SynchroniserHalfPowerFlow

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_HALF_POWER_FLOW

    class _Cast_SynchroniserHalfPowerFlow:
        """Special nested class for casting SynchroniserHalfPowerFlow to subclasses."""

        def __init__(self, parent: 'SynchroniserHalfPowerFlow'):
            self._parent = parent

        @property
        def synchroniser_part_power_flow(self):
            return self._parent._cast(_4126.SynchroniserPartPowerFlow)

        @property
        def coupling_half_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4047
            
            return self._parent._cast(_4047.CouplingHalfPowerFlow)

        @property
        def mountable_component_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4087
            
            return self._parent._cast(_4087.MountableComponentPowerFlow)

        @property
        def component_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4034
            
            return self._parent._cast(_4034.ComponentPowerFlow)

        @property
        def part_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4089
            
            return self._parent._cast(_4089.PartPowerFlow)

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
        def synchroniser_half_power_flow(self) -> 'SynchroniserHalfPowerFlow':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'SynchroniserHalfPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def clutch_connection(self) -> '_4030.ClutchConnectionPowerFlow':
        """ClutchConnectionPowerFlow: 'ClutchConnection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ClutchConnection

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design(self) -> '_2583.SynchroniserHalf':
        """SynchroniserHalf: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_load_case(self) -> '_6931.SynchroniserHalfLoadCase':
        """SynchroniserHalfLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'SynchroniserHalfPowerFlow._Cast_SynchroniserHalfPowerFlow':
        return self._Cast_SynchroniserHalfPowerFlow(self)
