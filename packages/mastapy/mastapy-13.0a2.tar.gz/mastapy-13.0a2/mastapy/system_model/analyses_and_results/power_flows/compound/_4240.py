"""_4240.py

SpecialisedAssemblyCompoundPowerFlow
"""
from typing import List

from mastapy.system_model.analyses_and_results.power_flows import _4110
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4142
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPECIALISED_ASSEMBLY_COMPOUND_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound', 'SpecialisedAssemblyCompoundPowerFlow')


__docformat__ = 'restructuredtext en'
__all__ = ('SpecialisedAssemblyCompoundPowerFlow',)


class SpecialisedAssemblyCompoundPowerFlow(_4142.AbstractAssemblyCompoundPowerFlow):
    """SpecialisedAssemblyCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _SPECIALISED_ASSEMBLY_COMPOUND_POWER_FLOW

    class _Cast_SpecialisedAssemblyCompoundPowerFlow:
        """Special nested class for casting SpecialisedAssemblyCompoundPowerFlow to subclasses."""

        def __init__(self, parent: 'SpecialisedAssemblyCompoundPowerFlow'):
            self._parent = parent

        @property
        def abstract_assembly_compound_power_flow(self):
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
        def agma_gleason_conical_gear_set_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4148
            
            return self._parent._cast(_4148.AGMAGleasonConicalGearSetCompoundPowerFlow)

        @property
        def belt_drive_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4152
            
            return self._parent._cast(_4152.BeltDriveCompoundPowerFlow)

        @property
        def bevel_differential_gear_set_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4155
            
            return self._parent._cast(_4155.BevelDifferentialGearSetCompoundPowerFlow)

        @property
        def bevel_gear_set_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4160
            
            return self._parent._cast(_4160.BevelGearSetCompoundPowerFlow)

        @property
        def bolted_joint_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4162
            
            return self._parent._cast(_4162.BoltedJointCompoundPowerFlow)

        @property
        def clutch_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4163
            
            return self._parent._cast(_4163.ClutchCompoundPowerFlow)

        @property
        def concept_coupling_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4168
            
            return self._parent._cast(_4168.ConceptCouplingCompoundPowerFlow)

        @property
        def concept_gear_set_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4173
            
            return self._parent._cast(_4173.ConceptGearSetCompoundPowerFlow)

        @property
        def conical_gear_set_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4176
            
            return self._parent._cast(_4176.ConicalGearSetCompoundPowerFlow)

        @property
        def coupling_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4179
            
            return self._parent._cast(_4179.CouplingCompoundPowerFlow)

        @property
        def cvt_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4183
            
            return self._parent._cast(_4183.CVTCompoundPowerFlow)

        @property
        def cycloidal_assembly_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4185
            
            return self._parent._cast(_4185.CycloidalAssemblyCompoundPowerFlow)

        @property
        def cylindrical_gear_set_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4191
            
            return self._parent._cast(_4191.CylindricalGearSetCompoundPowerFlow)

        @property
        def face_gear_set_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4197
            
            return self._parent._cast(_4197.FaceGearSetCompoundPowerFlow)

        @property
        def flexible_pin_assembly_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4199
            
            return self._parent._cast(_4199.FlexiblePinAssemblyCompoundPowerFlow)

        @property
        def gear_set_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4202
            
            return self._parent._cast(_4202.GearSetCompoundPowerFlow)

        @property
        def hypoid_gear_set_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4206
            
            return self._parent._cast(_4206.HypoidGearSetCompoundPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4210
            
            return self._parent._cast(_4210.KlingelnbergCycloPalloidConicalGearSetCompoundPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4213
            
            return self._parent._cast(_4213.KlingelnbergCycloPalloidHypoidGearSetCompoundPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4216
            
            return self._parent._cast(_4216.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundPowerFlow)

        @property
        def part_to_part_shear_coupling_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4222
            
            return self._parent._cast(_4222.PartToPartShearCouplingCompoundPowerFlow)

        @property
        def planetary_gear_set_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4226
            
            return self._parent._cast(_4226.PlanetaryGearSetCompoundPowerFlow)

        @property
        def rolling_ring_assembly_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4233
            
            return self._parent._cast(_4233.RollingRingAssemblyCompoundPowerFlow)

        @property
        def spiral_bevel_gear_set_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4243
            
            return self._parent._cast(_4243.SpiralBevelGearSetCompoundPowerFlow)

        @property
        def spring_damper_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4244
            
            return self._parent._cast(_4244.SpringDamperCompoundPowerFlow)

        @property
        def straight_bevel_diff_gear_set_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4249
            
            return self._parent._cast(_4249.StraightBevelDiffGearSetCompoundPowerFlow)

        @property
        def straight_bevel_gear_set_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4252
            
            return self._parent._cast(_4252.StraightBevelGearSetCompoundPowerFlow)

        @property
        def synchroniser_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4255
            
            return self._parent._cast(_4255.SynchroniserCompoundPowerFlow)

        @property
        def torque_converter_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4259
            
            return self._parent._cast(_4259.TorqueConverterCompoundPowerFlow)

        @property
        def worm_gear_set_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4267
            
            return self._parent._cast(_4267.WormGearSetCompoundPowerFlow)

        @property
        def zerol_bevel_gear_set_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4270
            
            return self._parent._cast(_4270.ZerolBevelGearSetCompoundPowerFlow)

        @property
        def specialised_assembly_compound_power_flow(self) -> 'SpecialisedAssemblyCompoundPowerFlow':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'SpecialisedAssemblyCompoundPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(self) -> 'List[_4110.SpecialisedAssemblyPowerFlow]':
        """List[SpecialisedAssemblyPowerFlow]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_4110.SpecialisedAssemblyPowerFlow]':
        """List[SpecialisedAssemblyPowerFlow]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'SpecialisedAssemblyCompoundPowerFlow._Cast_SpecialisedAssemblyCompoundPowerFlow':
        return self._Cast_SpecialisedAssemblyCompoundPowerFlow(self)
