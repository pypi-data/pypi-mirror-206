"""_2890.py

GearMeshCompoundSystemDeflection
"""
from typing import List

from mastapy.system_model.analyses_and_results.system_deflections import _2738
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2896
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_MESH_COMPOUND_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound', 'GearMeshCompoundSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('GearMeshCompoundSystemDeflection',)


class GearMeshCompoundSystemDeflection(_2896.InterMountableComponentConnectionCompoundSystemDeflection):
    """GearMeshCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _GEAR_MESH_COMPOUND_SYSTEM_DEFLECTION

    class _Cast_GearMeshCompoundSystemDeflection:
        """Special nested class for casting GearMeshCompoundSystemDeflection to subclasses."""

        def __init__(self, parent: 'GearMeshCompoundSystemDeflection'):
            self._parent = parent

        @property
        def inter_mountable_component_connection_compound_system_deflection(self):
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
        def agma_gleason_conical_gear_mesh_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2835
            
            return self._parent._cast(_2835.AGMAGleasonConicalGearMeshCompoundSystemDeflection)

        @property
        def bevel_differential_gear_mesh_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2842
            
            return self._parent._cast(_2842.BevelDifferentialGearMeshCompoundSystemDeflection)

        @property
        def bevel_gear_mesh_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2847
            
            return self._parent._cast(_2847.BevelGearMeshCompoundSystemDeflection)

        @property
        def concept_gear_mesh_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2860
            
            return self._parent._cast(_2860.ConceptGearMeshCompoundSystemDeflection)

        @property
        def conical_gear_mesh_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2863
            
            return self._parent._cast(_2863.ConicalGearMeshCompoundSystemDeflection)

        @property
        def cylindrical_gear_mesh_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2878
            
            return self._parent._cast(_2878.CylindricalGearMeshCompoundSystemDeflection)

        @property
        def face_gear_mesh_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2885
            
            return self._parent._cast(_2885.FaceGearMeshCompoundSystemDeflection)

        @property
        def hypoid_gear_mesh_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2894
            
            return self._parent._cast(_2894.HypoidGearMeshCompoundSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2898
            
            return self._parent._cast(_2898.KlingelnbergCycloPalloidConicalGearMeshCompoundSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2901
            
            return self._parent._cast(_2901.KlingelnbergCycloPalloidHypoidGearMeshCompoundSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2904
            
            return self._parent._cast(_2904.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundSystemDeflection)

        @property
        def spiral_bevel_gear_mesh_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2932
            
            return self._parent._cast(_2932.SpiralBevelGearMeshCompoundSystemDeflection)

        @property
        def straight_bevel_diff_gear_mesh_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2938
            
            return self._parent._cast(_2938.StraightBevelDiffGearMeshCompoundSystemDeflection)

        @property
        def straight_bevel_gear_mesh_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2941
            
            return self._parent._cast(_2941.StraightBevelGearMeshCompoundSystemDeflection)

        @property
        def worm_gear_mesh_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2956
            
            return self._parent._cast(_2956.WormGearMeshCompoundSystemDeflection)

        @property
        def zerol_bevel_gear_mesh_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2959
            
            return self._parent._cast(_2959.ZerolBevelGearMeshCompoundSystemDeflection)

        @property
        def gear_mesh_compound_system_deflection(self) -> 'GearMeshCompoundSystemDeflection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GearMeshCompoundSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(self) -> 'List[_2738.GearMeshSystemDeflection]':
        """List[GearMeshSystemDeflection]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def connection_analysis_cases_ready(self) -> 'List[_2738.GearMeshSystemDeflection]':
        """List[GearMeshSystemDeflection]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'GearMeshCompoundSystemDeflection._Cast_GearMeshCompoundSystemDeflection':
        return self._Cast_GearMeshCompoundSystemDeflection(self)
