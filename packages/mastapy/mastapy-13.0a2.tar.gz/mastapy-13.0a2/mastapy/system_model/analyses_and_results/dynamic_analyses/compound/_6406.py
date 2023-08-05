"""_6406.py

ConicalGearMeshCompoundDynamicAnalysis
"""
from typing import List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6276
from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6432
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_MESH_COMPOUND_DYNAMIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound', 'ConicalGearMeshCompoundDynamicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('ConicalGearMeshCompoundDynamicAnalysis',)


class ConicalGearMeshCompoundDynamicAnalysis(_6432.GearMeshCompoundDynamicAnalysis):
    """ConicalGearMeshCompoundDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_MESH_COMPOUND_DYNAMIC_ANALYSIS

    class _Cast_ConicalGearMeshCompoundDynamicAnalysis:
        """Special nested class for casting ConicalGearMeshCompoundDynamicAnalysis to subclasses."""

        def __init__(self, parent: 'ConicalGearMeshCompoundDynamicAnalysis'):
            self._parent = parent

        @property
        def gear_mesh_compound_dynamic_analysis(self):
            return self._parent._cast(_6432.GearMeshCompoundDynamicAnalysis)

        @property
        def inter_mountable_component_connection_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6438
            
            return self._parent._cast(_6438.InterMountableComponentConnectionCompoundDynamicAnalysis)

        @property
        def connection_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6408
            
            return self._parent._cast(_6408.ConnectionCompoundDynamicAnalysis)

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
        def agma_gleason_conical_gear_mesh_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6378
            
            return self._parent._cast(_6378.AGMAGleasonConicalGearMeshCompoundDynamicAnalysis)

        @property
        def bevel_differential_gear_mesh_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6385
            
            return self._parent._cast(_6385.BevelDifferentialGearMeshCompoundDynamicAnalysis)

        @property
        def bevel_gear_mesh_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6390
            
            return self._parent._cast(_6390.BevelGearMeshCompoundDynamicAnalysis)

        @property
        def hypoid_gear_mesh_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6436
            
            return self._parent._cast(_6436.HypoidGearMeshCompoundDynamicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6440
            
            return self._parent._cast(_6440.KlingelnbergCycloPalloidConicalGearMeshCompoundDynamicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6443
            
            return self._parent._cast(_6443.KlingelnbergCycloPalloidHypoidGearMeshCompoundDynamicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6446
            
            return self._parent._cast(_6446.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundDynamicAnalysis)

        @property
        def spiral_bevel_gear_mesh_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6473
            
            return self._parent._cast(_6473.SpiralBevelGearMeshCompoundDynamicAnalysis)

        @property
        def straight_bevel_diff_gear_mesh_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6479
            
            return self._parent._cast(_6479.StraightBevelDiffGearMeshCompoundDynamicAnalysis)

        @property
        def straight_bevel_gear_mesh_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6482
            
            return self._parent._cast(_6482.StraightBevelGearMeshCompoundDynamicAnalysis)

        @property
        def zerol_bevel_gear_mesh_compound_dynamic_analysis(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6500
            
            return self._parent._cast(_6500.ZerolBevelGearMeshCompoundDynamicAnalysis)

        @property
        def conical_gear_mesh_compound_dynamic_analysis(self) -> 'ConicalGearMeshCompoundDynamicAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConicalGearMeshCompoundDynamicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def planetaries(self) -> 'List[ConicalGearMeshCompoundDynamicAnalysis]':
        """List[ConicalGearMeshCompoundDynamicAnalysis]: 'Planetaries' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def connection_analysis_cases(self) -> 'List[_6276.ConicalGearMeshDynamicAnalysis]':
        """List[ConicalGearMeshDynamicAnalysis]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def connection_analysis_cases_ready(self) -> 'List[_6276.ConicalGearMeshDynamicAnalysis]':
        """List[ConicalGearMeshDynamicAnalysis]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'ConicalGearMeshCompoundDynamicAnalysis._Cast_ConicalGearMeshCompoundDynamicAnalysis':
        return self._Cast_ConicalGearMeshCompoundDynamicAnalysis(self)
