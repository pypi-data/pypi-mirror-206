"""_4135.py

VirtualComponentPowerFlow
"""
from mastapy._internal import constructor
from mastapy.system_model.part_model import _2459
from mastapy.system_model.analyses_and_results.power_flows import _4087
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_VIRTUAL_COMPONENT_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows', 'VirtualComponentPowerFlow')


__docformat__ = 'restructuredtext en'
__all__ = ('VirtualComponentPowerFlow',)


class VirtualComponentPowerFlow(_4087.MountableComponentPowerFlow):
    """VirtualComponentPowerFlow

    This is a mastapy class.
    """

    TYPE = _VIRTUAL_COMPONENT_POWER_FLOW

    class _Cast_VirtualComponentPowerFlow:
        """Special nested class for casting VirtualComponentPowerFlow to subclasses."""

        def __init__(self, parent: 'VirtualComponentPowerFlow'):
            self._parent = parent

        @property
        def mountable_component_power_flow(self):
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
        def mass_disc_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4085
            
            return self._parent._cast(_4085.MassDiscPowerFlow)

        @property
        def measurement_component_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4086
            
            return self._parent._cast(_4086.MeasurementComponentPowerFlow)

        @property
        def point_load_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4096
            
            return self._parent._cast(_4096.PointLoadPowerFlow)

        @property
        def power_load_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4099
            
            return self._parent._cast(_4099.PowerLoadPowerFlow)

        @property
        def unbalanced_mass_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4134
            
            return self._parent._cast(_4134.UnbalancedMassPowerFlow)

        @property
        def virtual_component_power_flow(self) -> 'VirtualComponentPowerFlow':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'VirtualComponentPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def power(self) -> 'float':
        """float: 'Power' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Power

        if temp is None:
            return 0.0

        return temp

    @property
    def torque(self) -> 'float':
        """float: 'Torque' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Torque

        if temp is None:
            return 0.0

        return temp

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
    def cast_to(self) -> 'VirtualComponentPowerFlow._Cast_VirtualComponentPowerFlow':
        return self._Cast_VirtualComponentPowerFlow(self)
