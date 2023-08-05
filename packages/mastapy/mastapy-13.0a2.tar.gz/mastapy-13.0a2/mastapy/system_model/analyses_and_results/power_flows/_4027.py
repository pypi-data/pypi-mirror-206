"""_4027.py

BevelGearSetPowerFlow
"""
from mastapy.system_model.part_model.gears import _2499
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4015
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_SET_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows', 'BevelGearSetPowerFlow')


__docformat__ = 'restructuredtext en'
__all__ = ('BevelGearSetPowerFlow',)


class BevelGearSetPowerFlow(_4015.AGMAGleasonConicalGearSetPowerFlow):
    """BevelGearSetPowerFlow

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_SET_POWER_FLOW

    class _Cast_BevelGearSetPowerFlow:
        """Special nested class for casting BevelGearSetPowerFlow to subclasses."""

        def __init__(self, parent: 'BevelGearSetPowerFlow'):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_set_power_flow(self):
            return self._parent._cast(_4015.AGMAGleasonConicalGearSetPowerFlow)

        @property
        def conical_gear_set_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4043
            
            return self._parent._cast(_4043.ConicalGearSetPowerFlow)

        @property
        def gear_set_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4070
            
            return self._parent._cast(_4070.GearSetPowerFlow)

        @property
        def specialised_assembly_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4110
            
            return self._parent._cast(_4110.SpecialisedAssemblyPowerFlow)

        @property
        def abstract_assembly_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4009
            
            return self._parent._cast(_4009.AbstractAssemblyPowerFlow)

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
        def bevel_differential_gear_set_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4022
            
            return self._parent._cast(_4022.BevelDifferentialGearSetPowerFlow)

        @property
        def spiral_bevel_gear_set_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4113
            
            return self._parent._cast(_4113.SpiralBevelGearSetPowerFlow)

        @property
        def straight_bevel_diff_gear_set_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4119
            
            return self._parent._cast(_4119.StraightBevelDiffGearSetPowerFlow)

        @property
        def straight_bevel_gear_set_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4122
            
            return self._parent._cast(_4122.StraightBevelGearSetPowerFlow)

        @property
        def zerol_bevel_gear_set_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4141
            
            return self._parent._cast(_4141.ZerolBevelGearSetPowerFlow)

        @property
        def bevel_gear_set_power_flow(self) -> 'BevelGearSetPowerFlow':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'BevelGearSetPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2499.BevelGearSet':
        """BevelGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'BevelGearSetPowerFlow._Cast_BevelGearSetPowerFlow':
        return self._Cast_BevelGearSetPowerFlow(self)
