"""_4213.py

KlingelnbergCycloPalloidHypoidGearSetCompoundPowerFlow
"""
from typing import List

from mastapy.system_model.part_model.gears import _2518
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows import _4081
from mastapy.system_model.analyses_and_results.power_flows.compound import _4211, _4212, _4210
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET_COMPOUND_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound', 'KlingelnbergCycloPalloidHypoidGearSetCompoundPowerFlow')


__docformat__ = 'restructuredtext en'
__all__ = ('KlingelnbergCycloPalloidHypoidGearSetCompoundPowerFlow',)


class KlingelnbergCycloPalloidHypoidGearSetCompoundPowerFlow(_4210.KlingelnbergCycloPalloidConicalGearSetCompoundPowerFlow):
    """KlingelnbergCycloPalloidHypoidGearSetCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET_COMPOUND_POWER_FLOW

    class _Cast_KlingelnbergCycloPalloidHypoidGearSetCompoundPowerFlow:
        """Special nested class for casting KlingelnbergCycloPalloidHypoidGearSetCompoundPowerFlow to subclasses."""

        def __init__(self, parent: 'KlingelnbergCycloPalloidHypoidGearSetCompoundPowerFlow'):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_power_flow(self):
            return self._parent._cast(_4210.KlingelnbergCycloPalloidConicalGearSetCompoundPowerFlow)

        @property
        def conical_gear_set_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4176
            
            return self._parent._cast(_4176.ConicalGearSetCompoundPowerFlow)

        @property
        def gear_set_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4202
            
            return self._parent._cast(_4202.GearSetCompoundPowerFlow)

        @property
        def specialised_assembly_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4240
            
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
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_power_flow(self) -> 'KlingelnbergCycloPalloidHypoidGearSetCompoundPowerFlow':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'KlingelnbergCycloPalloidHypoidGearSetCompoundPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2518.KlingelnbergCycloPalloidHypoidGearSet':
        """KlingelnbergCycloPalloidHypoidGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_design(self) -> '_2518.KlingelnbergCycloPalloidHypoidGearSet':
        """KlingelnbergCycloPalloidHypoidGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_4081.KlingelnbergCycloPalloidHypoidGearSetPowerFlow]':
        """List[KlingelnbergCycloPalloidHypoidGearSetPowerFlow]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def klingelnberg_cyclo_palloid_hypoid_gears_compound_power_flow(self) -> 'List[_4211.KlingelnbergCycloPalloidHypoidGearCompoundPowerFlow]':
        """List[KlingelnbergCycloPalloidHypoidGearCompoundPowerFlow]: 'KlingelnbergCycloPalloidHypoidGearsCompoundPowerFlow' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.KlingelnbergCycloPalloidHypoidGearsCompoundPowerFlow

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def klingelnberg_cyclo_palloid_hypoid_meshes_compound_power_flow(self) -> 'List[_4212.KlingelnbergCycloPalloidHypoidGearMeshCompoundPowerFlow]':
        """List[KlingelnbergCycloPalloidHypoidGearMeshCompoundPowerFlow]: 'KlingelnbergCycloPalloidHypoidMeshesCompoundPowerFlow' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.KlingelnbergCycloPalloidHypoidMeshesCompoundPowerFlow

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_4081.KlingelnbergCycloPalloidHypoidGearSetPowerFlow]':
        """List[KlingelnbergCycloPalloidHypoidGearSetPowerFlow]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'KlingelnbergCycloPalloidHypoidGearSetCompoundPowerFlow._Cast_KlingelnbergCycloPalloidHypoidGearSetCompoundPowerFlow':
        return self._Cast_KlingelnbergCycloPalloidHypoidGearSetCompoundPowerFlow(self)
