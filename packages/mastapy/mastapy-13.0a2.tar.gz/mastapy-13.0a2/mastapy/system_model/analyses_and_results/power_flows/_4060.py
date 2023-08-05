"""_4060.py

CylindricalPlanetGearPowerFlow
"""
from mastapy.system_model.part_model.gears import _2506
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4058
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_PLANET_GEAR_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows', 'CylindricalPlanetGearPowerFlow')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalPlanetGearPowerFlow',)


class CylindricalPlanetGearPowerFlow(_4058.CylindricalGearPowerFlow):
    """CylindricalPlanetGearPowerFlow

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_PLANET_GEAR_POWER_FLOW

    class _Cast_CylindricalPlanetGearPowerFlow:
        """Special nested class for casting CylindricalPlanetGearPowerFlow to subclasses."""

        def __init__(self, parent: 'CylindricalPlanetGearPowerFlow'):
            self._parent = parent

        @property
        def cylindrical_gear_power_flow(self):
            return self._parent._cast(_4058.CylindricalGearPowerFlow)

        @property
        def gear_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4069
            
            return self._parent._cast(_4069.GearPowerFlow)

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
        def cylindrical_planet_gear_power_flow(self) -> 'CylindricalPlanetGearPowerFlow':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CylindricalPlanetGearPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2506.CylindricalPlanetGear':
        """CylindricalPlanetGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'CylindricalPlanetGearPowerFlow._Cast_CylindricalPlanetGearPowerFlow':
        return self._Cast_CylindricalPlanetGearPowerFlow(self)
