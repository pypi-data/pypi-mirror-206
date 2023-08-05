"""_4048.py

CouplingPowerFlow
"""
from mastapy.system_model.part_model.couplings import _2562
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4110
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows', 'CouplingPowerFlow')


__docformat__ = 'restructuredtext en'
__all__ = ('CouplingPowerFlow',)


class CouplingPowerFlow(_4110.SpecialisedAssemblyPowerFlow):
    """CouplingPowerFlow

    This is a mastapy class.
    """

    TYPE = _COUPLING_POWER_FLOW

    class _Cast_CouplingPowerFlow:
        """Special nested class for casting CouplingPowerFlow to subclasses."""

        def __init__(self, parent: 'CouplingPowerFlow'):
            self._parent = parent

        @property
        def specialised_assembly_power_flow(self):
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
        def clutch_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4032
            
            return self._parent._cast(_4032.ClutchPowerFlow)

        @property
        def concept_coupling_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4037
            
            return self._parent._cast(_4037.ConceptCouplingPowerFlow)

        @property
        def part_to_part_shear_coupling_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4092
            
            return self._parent._cast(_4092.PartToPartShearCouplingPowerFlow)

        @property
        def spring_damper_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4116
            
            return self._parent._cast(_4116.SpringDamperPowerFlow)

        @property
        def torque_converter_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4131
            
            return self._parent._cast(_4131.TorqueConverterPowerFlow)

        @property
        def coupling_power_flow(self) -> 'CouplingPowerFlow':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CouplingPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2562.Coupling':
        """Coupling: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'CouplingPowerFlow._Cast_CouplingPowerFlow':
        return self._Cast_CouplingPowerFlow(self)
