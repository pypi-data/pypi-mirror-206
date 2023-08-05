"""_4011.py

AbstractShaftPowerFlow
"""
from mastapy.system_model.part_model import _2415
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4010
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows', 'AbstractShaftPowerFlow')


__docformat__ = 'restructuredtext en'
__all__ = ('AbstractShaftPowerFlow',)


class AbstractShaftPowerFlow(_4010.AbstractShaftOrHousingPowerFlow):
    """AbstractShaftPowerFlow

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_POWER_FLOW

    class _Cast_AbstractShaftPowerFlow:
        """Special nested class for casting AbstractShaftPowerFlow to subclasses."""

        def __init__(self, parent: 'AbstractShaftPowerFlow'):
            self._parent = parent

        @property
        def abstract_shaft_or_housing_power_flow(self):
            return self._parent._cast(_4010.AbstractShaftOrHousingPowerFlow)

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
        def cycloidal_disc_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4055
            
            return self._parent._cast(_4055.CycloidalDiscPowerFlow)

        @property
        def shaft_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4108
            
            return self._parent._cast(_4108.ShaftPowerFlow)

        @property
        def abstract_shaft_power_flow(self) -> 'AbstractShaftPowerFlow':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AbstractShaftPowerFlow.TYPE'):
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
    def cast_to(self) -> 'AbstractShaftPowerFlow._Cast_AbstractShaftPowerFlow':
        return self._Cast_AbstractShaftPowerFlow(self)
