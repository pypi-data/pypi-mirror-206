"""_2894.py

HypoidGearMeshCompoundSystemDeflection
"""
from typing import List

from mastapy.system_model.connections_and_sockets.gears import _2296
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections import _2742
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2835
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HYPOID_GEAR_MESH_COMPOUND_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound', 'HypoidGearMeshCompoundSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('HypoidGearMeshCompoundSystemDeflection',)


class HypoidGearMeshCompoundSystemDeflection(_2835.AGMAGleasonConicalGearMeshCompoundSystemDeflection):
    """HypoidGearMeshCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _HYPOID_GEAR_MESH_COMPOUND_SYSTEM_DEFLECTION

    class _Cast_HypoidGearMeshCompoundSystemDeflection:
        """Special nested class for casting HypoidGearMeshCompoundSystemDeflection to subclasses."""

        def __init__(self, parent: 'HypoidGearMeshCompoundSystemDeflection'):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_mesh_compound_system_deflection(self):
            return self._parent._cast(_2835.AGMAGleasonConicalGearMeshCompoundSystemDeflection)

        @property
        def conical_gear_mesh_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2863
            
            return self._parent._cast(_2863.ConicalGearMeshCompoundSystemDeflection)

        @property
        def gear_mesh_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2890
            
            return self._parent._cast(_2890.GearMeshCompoundSystemDeflection)

        @property
        def inter_mountable_component_connection_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2896
            
            return self._parent._cast(_2896.InterMountableComponentConnectionCompoundSystemDeflection)

        @property
        def connection_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2865
            
            return self._parent._cast(_2865.ConnectionCompoundSystemDeflection)

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
        def hypoid_gear_mesh_compound_system_deflection(self) -> 'HypoidGearMeshCompoundSystemDeflection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'HypoidGearMeshCompoundSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2296.HypoidGearMesh':
        """HypoidGearMesh: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_design(self) -> '_2296.HypoidGearMesh':
        """HypoidGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_analysis_cases_ready(self) -> 'List[_2742.HypoidGearMeshSystemDeflection]':
        """List[HypoidGearMeshSystemDeflection]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def connection_analysis_cases(self) -> 'List[_2742.HypoidGearMeshSystemDeflection]':
        """List[HypoidGearMeshSystemDeflection]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'HypoidGearMeshCompoundSystemDeflection._Cast_HypoidGearMeshCompoundSystemDeflection':
        return self._Cast_HypoidGearMeshCompoundSystemDeflection(self)
