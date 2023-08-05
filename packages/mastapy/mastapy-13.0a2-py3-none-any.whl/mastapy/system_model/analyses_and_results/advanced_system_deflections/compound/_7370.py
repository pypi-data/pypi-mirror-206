"""_7370.py

AbstractShaftOrHousingCompoundAdvancedSystemDeflection
"""
from typing import List

from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7234
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7393
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_OR_HOUSING_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound', 'AbstractShaftOrHousingCompoundAdvancedSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('AbstractShaftOrHousingCompoundAdvancedSystemDeflection',)


class AbstractShaftOrHousingCompoundAdvancedSystemDeflection(_7393.ComponentCompoundAdvancedSystemDeflection):
    """AbstractShaftOrHousingCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_OR_HOUSING_COMPOUND_ADVANCED_SYSTEM_DEFLECTION

    class _Cast_AbstractShaftOrHousingCompoundAdvancedSystemDeflection:
        """Special nested class for casting AbstractShaftOrHousingCompoundAdvancedSystemDeflection to subclasses."""

        def __init__(self, parent: 'AbstractShaftOrHousingCompoundAdvancedSystemDeflection'):
            self._parent = parent

        @property
        def component_compound_advanced_system_deflection(self):
            return self._parent._cast(_7393.ComponentCompoundAdvancedSystemDeflection)

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
        def abstract_shaft_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7369
            
            return self._parent._cast(_7369.AbstractShaftCompoundAdvancedSystemDeflection)

        @property
        def cycloidal_disc_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7413
            
            return self._parent._cast(_7413.CycloidalDiscCompoundAdvancedSystemDeflection)

        @property
        def fe_part_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7424
            
            return self._parent._cast(_7424.FEPartCompoundAdvancedSystemDeflection)

        @property
        def shaft_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7463
            
            return self._parent._cast(_7463.ShaftCompoundAdvancedSystemDeflection)

        @property
        def abstract_shaft_or_housing_compound_advanced_system_deflection(self) -> 'AbstractShaftOrHousingCompoundAdvancedSystemDeflection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AbstractShaftOrHousingCompoundAdvancedSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self) -> 'List[_7234.AbstractShaftOrHousingAdvancedSystemDeflection]':
        """List[AbstractShaftOrHousingAdvancedSystemDeflection]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases_ready(self) -> 'List[_7234.AbstractShaftOrHousingAdvancedSystemDeflection]':
        """List[AbstractShaftOrHousingAdvancedSystemDeflection]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'AbstractShaftOrHousingCompoundAdvancedSystemDeflection._Cast_AbstractShaftOrHousingCompoundAdvancedSystemDeflection':
        return self._Cast_AbstractShaftOrHousingCompoundAdvancedSystemDeflection(self)
