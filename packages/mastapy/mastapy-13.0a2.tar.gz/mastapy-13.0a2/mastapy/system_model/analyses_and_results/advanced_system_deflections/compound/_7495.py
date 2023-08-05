"""_7495.py

ZerolBevelGearMeshCompoundAdvancedSystemDeflection
"""
from typing import List

from mastapy.system_model.connections_and_sockets.gears import _2312
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7366
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7385
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ZEROL_BEVEL_GEAR_MESH_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound', 'ZerolBevelGearMeshCompoundAdvancedSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('ZerolBevelGearMeshCompoundAdvancedSystemDeflection',)


class ZerolBevelGearMeshCompoundAdvancedSystemDeflection(_7385.BevelGearMeshCompoundAdvancedSystemDeflection):
    """ZerolBevelGearMeshCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _ZEROL_BEVEL_GEAR_MESH_COMPOUND_ADVANCED_SYSTEM_DEFLECTION

    class _Cast_ZerolBevelGearMeshCompoundAdvancedSystemDeflection:
        """Special nested class for casting ZerolBevelGearMeshCompoundAdvancedSystemDeflection to subclasses."""

        def __init__(self, parent: 'ZerolBevelGearMeshCompoundAdvancedSystemDeflection'):
            self._parent = parent

        @property
        def bevel_gear_mesh_compound_advanced_system_deflection(self):
            return self._parent._cast(_7385.BevelGearMeshCompoundAdvancedSystemDeflection)

        @property
        def agma_gleason_conical_gear_mesh_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7373
            
            return self._parent._cast(_7373.AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection)

        @property
        def conical_gear_mesh_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7401
            
            return self._parent._cast(_7401.ConicalGearMeshCompoundAdvancedSystemDeflection)

        @property
        def gear_mesh_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7427
            
            return self._parent._cast(_7427.GearMeshCompoundAdvancedSystemDeflection)

        @property
        def inter_mountable_component_connection_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7433
            
            return self._parent._cast(_7433.InterMountableComponentConnectionCompoundAdvancedSystemDeflection)

        @property
        def connection_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7403
            
            return self._parent._cast(_7403.ConnectionCompoundAdvancedSystemDeflection)

        @property
        def connection_compound_analysis(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7501
            
            return self._parent._cast(_7501.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7505
            
            return self._parent._cast(_7505.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(self):
            from mastapy.system_model.analyses_and_results import _2630
            
            return self._parent._cast(_2630.DesignEntityAnalysis)

        @property
        def zerol_bevel_gear_mesh_compound_advanced_system_deflection(self) -> 'ZerolBevelGearMeshCompoundAdvancedSystemDeflection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ZerolBevelGearMeshCompoundAdvancedSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2312.ZerolBevelGearMesh':
        """ZerolBevelGearMesh: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_design(self) -> '_2312.ZerolBevelGearMesh':
        """ZerolBevelGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_analysis_cases_ready(self) -> 'List[_7366.ZerolBevelGearMeshAdvancedSystemDeflection]':
        """List[ZerolBevelGearMeshAdvancedSystemDeflection]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def connection_analysis_cases(self) -> 'List[_7366.ZerolBevelGearMeshAdvancedSystemDeflection]':
        """List[ZerolBevelGearMeshAdvancedSystemDeflection]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'ZerolBevelGearMeshCompoundAdvancedSystemDeflection._Cast_ZerolBevelGearMeshCompoundAdvancedSystemDeflection':
        return self._Cast_ZerolBevelGearMeshCompoundAdvancedSystemDeflection(self)
