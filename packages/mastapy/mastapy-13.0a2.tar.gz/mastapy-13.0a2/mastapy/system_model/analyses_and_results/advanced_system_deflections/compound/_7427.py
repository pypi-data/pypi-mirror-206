"""_7427.py

GearMeshCompoundAdvancedSystemDeflection
"""
from typing import List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7296
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7433
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_MESH_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound', 'GearMeshCompoundAdvancedSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('GearMeshCompoundAdvancedSystemDeflection',)


class GearMeshCompoundAdvancedSystemDeflection(_7433.InterMountableComponentConnectionCompoundAdvancedSystemDeflection):
    """GearMeshCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _GEAR_MESH_COMPOUND_ADVANCED_SYSTEM_DEFLECTION

    class _Cast_GearMeshCompoundAdvancedSystemDeflection:
        """Special nested class for casting GearMeshCompoundAdvancedSystemDeflection to subclasses."""

        def __init__(self, parent: 'GearMeshCompoundAdvancedSystemDeflection'):
            self._parent = parent

        @property
        def inter_mountable_component_connection_compound_advanced_system_deflection(self):
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
        def agma_gleason_conical_gear_mesh_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7373
            
            return self._parent._cast(_7373.AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection)

        @property
        def bevel_differential_gear_mesh_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7380
            
            return self._parent._cast(_7380.BevelDifferentialGearMeshCompoundAdvancedSystemDeflection)

        @property
        def bevel_gear_mesh_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7385
            
            return self._parent._cast(_7385.BevelGearMeshCompoundAdvancedSystemDeflection)

        @property
        def concept_gear_mesh_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7398
            
            return self._parent._cast(_7398.ConceptGearMeshCompoundAdvancedSystemDeflection)

        @property
        def conical_gear_mesh_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7401
            
            return self._parent._cast(_7401.ConicalGearMeshCompoundAdvancedSystemDeflection)

        @property
        def cylindrical_gear_mesh_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7416
            
            return self._parent._cast(_7416.CylindricalGearMeshCompoundAdvancedSystemDeflection)

        @property
        def face_gear_mesh_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7422
            
            return self._parent._cast(_7422.FaceGearMeshCompoundAdvancedSystemDeflection)

        @property
        def hypoid_gear_mesh_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7431
            
            return self._parent._cast(_7431.HypoidGearMeshCompoundAdvancedSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7435
            
            return self._parent._cast(_7435.KlingelnbergCycloPalloidConicalGearMeshCompoundAdvancedSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7438
            
            return self._parent._cast(_7438.KlingelnbergCycloPalloidHypoidGearMeshCompoundAdvancedSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7441
            
            return self._parent._cast(_7441.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundAdvancedSystemDeflection)

        @property
        def spiral_bevel_gear_mesh_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7468
            
            return self._parent._cast(_7468.SpiralBevelGearMeshCompoundAdvancedSystemDeflection)

        @property
        def straight_bevel_diff_gear_mesh_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7474
            
            return self._parent._cast(_7474.StraightBevelDiffGearMeshCompoundAdvancedSystemDeflection)

        @property
        def straight_bevel_gear_mesh_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7477
            
            return self._parent._cast(_7477.StraightBevelGearMeshCompoundAdvancedSystemDeflection)

        @property
        def worm_gear_mesh_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7492
            
            return self._parent._cast(_7492.WormGearMeshCompoundAdvancedSystemDeflection)

        @property
        def zerol_bevel_gear_mesh_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7495
            
            return self._parent._cast(_7495.ZerolBevelGearMeshCompoundAdvancedSystemDeflection)

        @property
        def gear_mesh_compound_advanced_system_deflection(self) -> 'GearMeshCompoundAdvancedSystemDeflection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GearMeshCompoundAdvancedSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def minimum_separation_left_flank(self) -> 'float':
        """float: 'MinimumSeparationLeftFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MinimumSeparationLeftFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def minimum_separation_right_flank(self) -> 'float':
        """float: 'MinimumSeparationRightFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MinimumSeparationRightFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def connection_analysis_cases(self) -> 'List[_7296.GearMeshAdvancedSystemDeflection]':
        """List[GearMeshAdvancedSystemDeflection]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def connection_analysis_cases_ready(self) -> 'List[_7296.GearMeshAdvancedSystemDeflection]':
        """List[GearMeshAdvancedSystemDeflection]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'GearMeshCompoundAdvancedSystemDeflection._Cast_GearMeshCompoundAdvancedSystemDeflection':
        return self._Cast_GearMeshCompoundAdvancedSystemDeflection(self)
