"""_7381.py

BevelDifferentialGearSetCompoundAdvancedSystemDeflection
"""
from typing import List

from mastapy.system_model.part_model.gears import _2495
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7248
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7379, _7380, _7386
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_GEAR_SET_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound', 'BevelDifferentialGearSetCompoundAdvancedSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('BevelDifferentialGearSetCompoundAdvancedSystemDeflection',)


class BevelDifferentialGearSetCompoundAdvancedSystemDeflection(_7386.BevelGearSetCompoundAdvancedSystemDeflection):
    """BevelDifferentialGearSetCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_GEAR_SET_COMPOUND_ADVANCED_SYSTEM_DEFLECTION

    class _Cast_BevelDifferentialGearSetCompoundAdvancedSystemDeflection:
        """Special nested class for casting BevelDifferentialGearSetCompoundAdvancedSystemDeflection to subclasses."""

        def __init__(self, parent: 'BevelDifferentialGearSetCompoundAdvancedSystemDeflection'):
            self._parent = parent

        @property
        def bevel_gear_set_compound_advanced_system_deflection(self):
            return self._parent._cast(_7386.BevelGearSetCompoundAdvancedSystemDeflection)

        @property
        def agma_gleason_conical_gear_set_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7374
            
            return self._parent._cast(_7374.AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection)

        @property
        def conical_gear_set_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7402
            
            return self._parent._cast(_7402.ConicalGearSetCompoundAdvancedSystemDeflection)

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
        def bevel_differential_gear_set_compound_advanced_system_deflection(self) -> 'BevelDifferentialGearSetCompoundAdvancedSystemDeflection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'BevelDifferentialGearSetCompoundAdvancedSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2495.BevelDifferentialGearSet':
        """BevelDifferentialGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_design(self) -> '_2495.BevelDifferentialGearSet':
        """BevelDifferentialGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_7248.BevelDifferentialGearSetAdvancedSystemDeflection]':
        """List[BevelDifferentialGearSetAdvancedSystemDeflection]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def bevel_differential_gears_compound_advanced_system_deflection(self) -> 'List[_7379.BevelDifferentialGearCompoundAdvancedSystemDeflection]':
        """List[BevelDifferentialGearCompoundAdvancedSystemDeflection]: 'BevelDifferentialGearsCompoundAdvancedSystemDeflection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BevelDifferentialGearsCompoundAdvancedSystemDeflection

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def bevel_differential_meshes_compound_advanced_system_deflection(self) -> 'List[_7380.BevelDifferentialGearMeshCompoundAdvancedSystemDeflection]':
        """List[BevelDifferentialGearMeshCompoundAdvancedSystemDeflection]: 'BevelDifferentialMeshesCompoundAdvancedSystemDeflection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BevelDifferentialMeshesCompoundAdvancedSystemDeflection

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_7248.BevelDifferentialGearSetAdvancedSystemDeflection]':
        """List[BevelDifferentialGearSetAdvancedSystemDeflection]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'BevelDifferentialGearSetCompoundAdvancedSystemDeflection._Cast_BevelDifferentialGearSetCompoundAdvancedSystemDeflection':
        return self._Cast_BevelDifferentialGearSetCompoundAdvancedSystemDeflection(self)
