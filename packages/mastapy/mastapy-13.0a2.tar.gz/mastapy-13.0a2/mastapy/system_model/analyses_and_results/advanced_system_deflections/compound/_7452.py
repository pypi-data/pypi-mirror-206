"""_7452.py

PlanetaryGearSetCompoundAdvancedSystemDeflection
"""
from typing import List

from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7322
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7417
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANETARY_GEAR_SET_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound', 'PlanetaryGearSetCompoundAdvancedSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('PlanetaryGearSetCompoundAdvancedSystemDeflection',)


class PlanetaryGearSetCompoundAdvancedSystemDeflection(_7417.CylindricalGearSetCompoundAdvancedSystemDeflection):
    """PlanetaryGearSetCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _PLANETARY_GEAR_SET_COMPOUND_ADVANCED_SYSTEM_DEFLECTION

    class _Cast_PlanetaryGearSetCompoundAdvancedSystemDeflection:
        """Special nested class for casting PlanetaryGearSetCompoundAdvancedSystemDeflection to subclasses."""

        def __init__(self, parent: 'PlanetaryGearSetCompoundAdvancedSystemDeflection'):
            self._parent = parent

        @property
        def cylindrical_gear_set_compound_advanced_system_deflection(self):
            return self._parent._cast(_7417.CylindricalGearSetCompoundAdvancedSystemDeflection)

        @property
        def gear_set_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7428
            
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
        def planetary_gear_set_compound_advanced_system_deflection(self) -> 'PlanetaryGearSetCompoundAdvancedSystemDeflection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'PlanetaryGearSetCompoundAdvancedSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_7322.PlanetaryGearSetAdvancedSystemDeflection]':
        """List[PlanetaryGearSetAdvancedSystemDeflection]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_7322.PlanetaryGearSetAdvancedSystemDeflection]':
        """List[PlanetaryGearSetAdvancedSystemDeflection]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'PlanetaryGearSetCompoundAdvancedSystemDeflection._Cast_PlanetaryGearSetCompoundAdvancedSystemDeflection':
        return self._Cast_PlanetaryGearSetCompoundAdvancedSystemDeflection(self)
