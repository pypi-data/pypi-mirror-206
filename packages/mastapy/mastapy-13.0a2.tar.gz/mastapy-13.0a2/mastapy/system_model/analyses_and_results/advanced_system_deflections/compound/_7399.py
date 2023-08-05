"""_7399.py

ConceptGearSetCompoundAdvancedSystemDeflection
"""
from typing import List

from mastapy.system_model.part_model.gears import _2501
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7266
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7397, _7398, _7428
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_GEAR_SET_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound', 'ConceptGearSetCompoundAdvancedSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('ConceptGearSetCompoundAdvancedSystemDeflection',)


class ConceptGearSetCompoundAdvancedSystemDeflection(_7428.GearSetCompoundAdvancedSystemDeflection):
    """ConceptGearSetCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _CONCEPT_GEAR_SET_COMPOUND_ADVANCED_SYSTEM_DEFLECTION

    class _Cast_ConceptGearSetCompoundAdvancedSystemDeflection:
        """Special nested class for casting ConceptGearSetCompoundAdvancedSystemDeflection to subclasses."""

        def __init__(self, parent: 'ConceptGearSetCompoundAdvancedSystemDeflection'):
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
        def concept_gear_set_compound_advanced_system_deflection(self) -> 'ConceptGearSetCompoundAdvancedSystemDeflection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConceptGearSetCompoundAdvancedSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2501.ConceptGearSet':
        """ConceptGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_design(self) -> '_2501.ConceptGearSet':
        """ConceptGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_7266.ConceptGearSetAdvancedSystemDeflection]':
        """List[ConceptGearSetAdvancedSystemDeflection]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def concept_gears_compound_advanced_system_deflection(self) -> 'List[_7397.ConceptGearCompoundAdvancedSystemDeflection]':
        """List[ConceptGearCompoundAdvancedSystemDeflection]: 'ConceptGearsCompoundAdvancedSystemDeflection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConceptGearsCompoundAdvancedSystemDeflection

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def concept_meshes_compound_advanced_system_deflection(self) -> 'List[_7398.ConceptGearMeshCompoundAdvancedSystemDeflection]':
        """List[ConceptGearMeshCompoundAdvancedSystemDeflection]: 'ConceptMeshesCompoundAdvancedSystemDeflection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConceptMeshesCompoundAdvancedSystemDeflection

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_7266.ConceptGearSetAdvancedSystemDeflection]':
        """List[ConceptGearSetAdvancedSystemDeflection]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'ConceptGearSetCompoundAdvancedSystemDeflection._Cast_ConceptGearSetCompoundAdvancedSystemDeflection':
        return self._Cast_ConceptGearSetCompoundAdvancedSystemDeflection(self)
