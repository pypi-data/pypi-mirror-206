"""_7493.py

WormGearSetCompoundAdvancedSystemDeflection
"""
from typing import List

from mastapy.system_model.part_model.gears import _2531
from mastapy._internal import constructor, conversion
from mastapy.gears.rating.worm import _371
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7364
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7491, _7492, _7428
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_WORM_GEAR_SET_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound', 'WormGearSetCompoundAdvancedSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('WormGearSetCompoundAdvancedSystemDeflection',)


class WormGearSetCompoundAdvancedSystemDeflection(_7428.GearSetCompoundAdvancedSystemDeflection):
    """WormGearSetCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _WORM_GEAR_SET_COMPOUND_ADVANCED_SYSTEM_DEFLECTION

    class _Cast_WormGearSetCompoundAdvancedSystemDeflection:
        """Special nested class for casting WormGearSetCompoundAdvancedSystemDeflection to subclasses."""

        def __init__(self, parent: 'WormGearSetCompoundAdvancedSystemDeflection'):
            self._parent = parent

        @property
        def gear_set_compound_advanced_system_deflection(self):
            return self._parent._cast(_7428.GearSetCompoundAdvancedSystemDeflection)

        @property
        def specialised_assembly_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7466
            
            return self._parent._cast(_7466.SpecialisedAssemblyCompoundAdvancedSystemDeflection)

        @property
        def abstract_assembly_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7368
            
            return self._parent._cast(_7368.AbstractAssemblyCompoundAdvancedSystemDeflection)

        @property
        def part_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7447
            
            return self._parent._cast(_7447.PartCompoundAdvancedSystemDeflection)

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
        def worm_gear_set_compound_advanced_system_deflection(self) -> 'WormGearSetCompoundAdvancedSystemDeflection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'WormGearSetCompoundAdvancedSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2531.WormGearSet':
        """WormGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_design(self) -> '_2531.WormGearSet':
        """WormGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_duty_cycle_rating(self) -> '_371.WormGearSetDutyCycleRating':
        """WormGearSetDutyCycleRating: 'GearDutyCycleRating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearDutyCycleRating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def worm_gear_duty_cycle_rating(self) -> '_371.WormGearSetDutyCycleRating':
        """WormGearSetDutyCycleRating: 'WormGearDutyCycleRating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WormGearDutyCycleRating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_7364.WormGearSetAdvancedSystemDeflection]':
        """List[WormGearSetAdvancedSystemDeflection]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def worm_gears_compound_advanced_system_deflection(self) -> 'List[_7491.WormGearCompoundAdvancedSystemDeflection]':
        """List[WormGearCompoundAdvancedSystemDeflection]: 'WormGearsCompoundAdvancedSystemDeflection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WormGearsCompoundAdvancedSystemDeflection

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def worm_meshes_compound_advanced_system_deflection(self) -> 'List[_7492.WormGearMeshCompoundAdvancedSystemDeflection]':
        """List[WormGearMeshCompoundAdvancedSystemDeflection]: 'WormMeshesCompoundAdvancedSystemDeflection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WormMeshesCompoundAdvancedSystemDeflection

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_7364.WormGearSetAdvancedSystemDeflection]':
        """List[WormGearSetAdvancedSystemDeflection]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'WormGearSetCompoundAdvancedSystemDeflection._Cast_WormGearSetCompoundAdvancedSystemDeflection':
        return self._Cast_WormGearSetCompoundAdvancedSystemDeflection(self)
