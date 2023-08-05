"""_2885.py

FaceGearMeshCompoundSystemDeflection
"""
from typing import List

from mastapy.system_model.connections_and_sockets.gears import _2292
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections import _2733
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2890
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_MESH_COMPOUND_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound', 'FaceGearMeshCompoundSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('FaceGearMeshCompoundSystemDeflection',)


class FaceGearMeshCompoundSystemDeflection(_2890.GearMeshCompoundSystemDeflection):
    """FaceGearMeshCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _FACE_GEAR_MESH_COMPOUND_SYSTEM_DEFLECTION

    class _Cast_FaceGearMeshCompoundSystemDeflection:
        """Special nested class for casting FaceGearMeshCompoundSystemDeflection to subclasses."""

        def __init__(self, parent: 'FaceGearMeshCompoundSystemDeflection'):
            self._parent = parent

        @property
        def gear_mesh_compound_system_deflection(self):
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
        def face_gear_mesh_compound_system_deflection(self) -> 'FaceGearMeshCompoundSystemDeflection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'FaceGearMeshCompoundSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2292.FaceGearMesh':
        """FaceGearMesh: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_design(self) -> '_2292.FaceGearMesh':
        """FaceGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_analysis_cases_ready(self) -> 'List[_2733.FaceGearMeshSystemDeflection]':
        """List[FaceGearMeshSystemDeflection]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def connection_analysis_cases(self) -> 'List[_2733.FaceGearMeshSystemDeflection]':
        """List[FaceGearMeshSystemDeflection]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'FaceGearMeshCompoundSystemDeflection._Cast_FaceGearMeshCompoundSystemDeflection':
        return self._Cast_FaceGearMeshCompoundSystemDeflection(self)
