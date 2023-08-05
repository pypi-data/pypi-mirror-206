"""_4179.py

CouplingCompoundPowerFlow
"""
from typing import List

from mastapy.system_model.analyses_and_results.power_flows import _4048
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4240
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_COMPOUND_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound', 'CouplingCompoundPowerFlow')


__docformat__ = 'restructuredtext en'
__all__ = ('CouplingCompoundPowerFlow',)


class CouplingCompoundPowerFlow(_4240.SpecialisedAssemblyCompoundPowerFlow):
    """CouplingCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _COUPLING_COMPOUND_POWER_FLOW

    class _Cast_CouplingCompoundPowerFlow:
        """Special nested class for casting CouplingCompoundPowerFlow to subclasses."""

        def __init__(self, parent: 'CouplingCompoundPowerFlow'):
            self._parent = parent

        @property
        def specialised_assembly_compound_power_flow(self):
            return self._parent._cast(_4240.SpecialisedAssemblyCompoundPowerFlow)

        @property
        def abstract_assembly_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4142
            
            return self._parent._cast(_4142.AbstractAssemblyCompoundPowerFlow)

        @property
        def part_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4221
            
            return self._parent._cast(_4221.PartCompoundPowerFlow)

        @property
        def part_compound_analysis(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7508
            
            return self._parent._cast(_7508.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7505
            
            return self._parent._cast(_7505.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(self):
            from mastapy.system_model.analyses_and_results import _2630
            
            return self._parent._cast(_2630.DesignEntityAnalysis)

        @property
        def clutch_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4163
            
            return self._parent._cast(_4163.ClutchCompoundPowerFlow)

        @property
        def concept_coupling_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4168
            
            return self._parent._cast(_4168.ConceptCouplingCompoundPowerFlow)

        @property
        def part_to_part_shear_coupling_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4222
            
            return self._parent._cast(_4222.PartToPartShearCouplingCompoundPowerFlow)

        @property
        def spring_damper_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4244
            
            return self._parent._cast(_4244.SpringDamperCompoundPowerFlow)

        @property
        def torque_converter_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4259
            
            return self._parent._cast(_4259.TorqueConverterCompoundPowerFlow)

        @property
        def coupling_compound_power_flow(self) -> 'CouplingCompoundPowerFlow':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CouplingCompoundPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(self) -> 'List[_4048.CouplingPowerFlow]':
        """List[CouplingPowerFlow]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_4048.CouplingPowerFlow]':
        """List[CouplingPowerFlow]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'CouplingCompoundPowerFlow._Cast_CouplingCompoundPowerFlow':
        return self._Cast_CouplingCompoundPowerFlow(self)
