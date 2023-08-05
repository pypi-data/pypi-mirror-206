"""_2831.py

AbstractShaftCompoundSystemDeflection
"""
from typing import List

from mastapy.system_model.analyses_and_results.system_deflections import _2666
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2832
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_COMPOUND_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound', 'AbstractShaftCompoundSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('AbstractShaftCompoundSystemDeflection',)


class AbstractShaftCompoundSystemDeflection(_2832.AbstractShaftOrHousingCompoundSystemDeflection):
    """AbstractShaftCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_COMPOUND_SYSTEM_DEFLECTION

    class _Cast_AbstractShaftCompoundSystemDeflection:
        """Special nested class for casting AbstractShaftCompoundSystemDeflection to subclasses."""

        def __init__(self, parent: 'AbstractShaftCompoundSystemDeflection'):
            self._parent = parent

        @property
        def abstract_shaft_or_housing_compound_system_deflection(self):
            return self._parent._cast(_2832.AbstractShaftOrHousingCompoundSystemDeflection)

        @property
        def component_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2855
            
            return self._parent._cast(_2855.ComponentCompoundSystemDeflection)

        @property
        def part_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2910
            
            return self._parent._cast(_2910.PartCompoundSystemDeflection)

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
        def cycloidal_disc_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2875
            
            return self._parent._cast(_2875.CycloidalDiscCompoundSystemDeflection)

        @property
        def shaft_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2926
            
            return self._parent._cast(_2926.ShaftCompoundSystemDeflection)

        @property
        def abstract_shaft_compound_system_deflection(self) -> 'AbstractShaftCompoundSystemDeflection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AbstractShaftCompoundSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self) -> 'List[_2666.AbstractShaftSystemDeflection]':
        """List[AbstractShaftSystemDeflection]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases_ready(self) -> 'List[_2666.AbstractShaftSystemDeflection]':
        """List[AbstractShaftSystemDeflection]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'AbstractShaftCompoundSystemDeflection._Cast_AbstractShaftCompoundSystemDeflection':
        return self._Cast_AbstractShaftCompoundSystemDeflection(self)
