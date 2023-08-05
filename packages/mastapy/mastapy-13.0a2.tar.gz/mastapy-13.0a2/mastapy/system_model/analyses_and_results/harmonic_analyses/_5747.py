"""_5747.py

KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysis
"""
from typing import List

from mastapy.system_model.part_model.gears import _2518
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6881
from mastapy.system_model.analyses_and_results.system_deflections import _2751
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5745, _5746, _5744
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET_HARMONIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses', 'KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysis',)


class KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysis(_5744.KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysis):
    """KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET_HARMONIC_ANALYSIS

    class _Cast_KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysis:
        """Special nested class for casting KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysis to subclasses."""

        def __init__(self, parent: 'KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysis'):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_harmonic_analysis(self):
            return self._parent._cast(_5744.KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysis)

        @property
        def conical_gear_set_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5684
            
            return self._parent._cast(_5684.ConicalGearSetHarmonicAnalysis)

        @property
        def gear_set_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5727
            
            return self._parent._cast(_5727.GearSetHarmonicAnalysis)

        @property
        def specialised_assembly_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5777
            
            return self._parent._cast(_5777.SpecialisedAssemblyHarmonicAnalysis)

        @property
        def abstract_assembly_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5648
            
            return self._parent._cast(_5648.AbstractAssemblyHarmonicAnalysis)

        @property
        def part_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5755
            
            return self._parent._cast(_5755.PartHarmonicAnalysis)

        @property
        def part_static_load_analysis_case(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7510
            
            return self._parent._cast(_7510.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7507
            
            return self._parent._cast(_7507.PartAnalysisCase)

        @property
        def part_analysis(self):
            from mastapy.system_model.analyses_and_results import _2636
            
            return self._parent._cast(_2636.PartAnalysis)

        @property
        def design_entity_single_context_analysis(self):
            from mastapy.system_model.analyses_and_results import _2632
            
            return self._parent._cast(_2632.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(self):
            from mastapy.system_model.analyses_and_results import _2630
            
            return self._parent._cast(_2630.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_harmonic_analysis(self) -> 'KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

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
    def assembly_load_case(self) -> '_6881.KlingelnbergCycloPalloidHypoidGearSetLoadCase':
        """KlingelnbergCycloPalloidHypoidGearSetLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results(self) -> '_2751.KlingelnbergCycloPalloidHypoidGearSetSystemDeflection':
        """KlingelnbergCycloPalloidHypoidGearSetSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gears_harmonic_analysis(self) -> 'List[_5745.KlingelnbergCycloPalloidHypoidGearHarmonicAnalysis]':
        """List[KlingelnbergCycloPalloidHypoidGearHarmonicAnalysis]: 'GearsHarmonicAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearsHarmonicAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def klingelnberg_cyclo_palloid_hypoid_gears_harmonic_analysis(self) -> 'List[_5745.KlingelnbergCycloPalloidHypoidGearHarmonicAnalysis]':
        """List[KlingelnbergCycloPalloidHypoidGearHarmonicAnalysis]: 'KlingelnbergCycloPalloidHypoidGearsHarmonicAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.KlingelnbergCycloPalloidHypoidGearsHarmonicAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def meshes_harmonic_analysis(self) -> 'List[_5746.KlingelnbergCycloPalloidHypoidGearMeshHarmonicAnalysis]':
        """List[KlingelnbergCycloPalloidHypoidGearMeshHarmonicAnalysis]: 'MeshesHarmonicAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeshesHarmonicAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def klingelnberg_cyclo_palloid_hypoid_meshes_harmonic_analysis(self) -> 'List[_5746.KlingelnbergCycloPalloidHypoidGearMeshHarmonicAnalysis]':
        """List[KlingelnbergCycloPalloidHypoidGearMeshHarmonicAnalysis]: 'KlingelnbergCycloPalloidHypoidMeshesHarmonicAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.KlingelnbergCycloPalloidHypoidMeshesHarmonicAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysis':
        return self._Cast_KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysis(self)
