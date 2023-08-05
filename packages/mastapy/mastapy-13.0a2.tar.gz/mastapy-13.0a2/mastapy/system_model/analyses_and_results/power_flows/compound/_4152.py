"""_4152.py

BeltDriveCompoundPowerFlow
"""
from typing import List

from mastapy.system_model.part_model.couplings import _2555
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows import _4019
from mastapy.system_model.analyses_and_results.power_flows.compound import _4240
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BELT_DRIVE_COMPOUND_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound', 'BeltDriveCompoundPowerFlow')


__docformat__ = 'restructuredtext en'
__all__ = ('BeltDriveCompoundPowerFlow',)


class BeltDriveCompoundPowerFlow(_4240.SpecialisedAssemblyCompoundPowerFlow):
    """BeltDriveCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _BELT_DRIVE_COMPOUND_POWER_FLOW

    class _Cast_BeltDriveCompoundPowerFlow:
        """Special nested class for casting BeltDriveCompoundPowerFlow to subclasses."""

        def __init__(self, parent: 'BeltDriveCompoundPowerFlow'):
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
        def cvt_compound_power_flow(self):
            from mastapy.system_model.analyses_and_results.power_flows.compound import _4183
            
            return self._parent._cast(_4183.CVTCompoundPowerFlow)

        @property
        def belt_drive_compound_power_flow(self) -> 'BeltDriveCompoundPowerFlow':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'BeltDriveCompoundPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2555.BeltDrive':
        """BeltDrive: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_design(self) -> '_2555.BeltDrive':
        """BeltDrive: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_4019.BeltDrivePowerFlow]':
        """List[BeltDrivePowerFlow]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_4019.BeltDrivePowerFlow]':
        """List[BeltDrivePowerFlow]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'BeltDriveCompoundPowerFlow._Cast_BeltDriveCompoundPowerFlow':
        return self._Cast_BeltDriveCompoundPowerFlow(self)
