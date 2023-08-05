"""_2948.py

SynchroniserSleeveCompoundSystemDeflection
"""
from typing import List

from mastapy.system_model.part_model.couplings import _2585
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections import _2802
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2947
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_SLEEVE_COMPOUND_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound', 'SynchroniserSleeveCompoundSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('SynchroniserSleeveCompoundSystemDeflection',)


class SynchroniserSleeveCompoundSystemDeflection(_2947.SynchroniserPartCompoundSystemDeflection):
    """SynchroniserSleeveCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_SLEEVE_COMPOUND_SYSTEM_DEFLECTION

    class _Cast_SynchroniserSleeveCompoundSystemDeflection:
        """Special nested class for casting SynchroniserSleeveCompoundSystemDeflection to subclasses."""

        def __init__(self, parent: 'SynchroniserSleeveCompoundSystemDeflection'):
            self._parent = parent

        @property
        def synchroniser_part_compound_system_deflection(self):
            return self._parent._cast(_2947.SynchroniserPartCompoundSystemDeflection)

        @property
        def coupling_half_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2869
            
            return self._parent._cast(_2869.CouplingHalfCompoundSystemDeflection)

        @property
        def mountable_component_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2908
            
            return self._parent._cast(_2908.MountableComponentCompoundSystemDeflection)

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
        def synchroniser_sleeve_compound_system_deflection(self) -> 'SynchroniserSleeveCompoundSystemDeflection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'SynchroniserSleeveCompoundSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2585.SynchroniserSleeve':
        """SynchroniserSleeve: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_2802.SynchroniserSleeveSystemDeflection]':
        """List[SynchroniserSleeveSystemDeflection]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases(self) -> 'List[_2802.SynchroniserSleeveSystemDeflection]':
        """List[SynchroniserSleeveSystemDeflection]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'SynchroniserSleeveCompoundSystemDeflection._Cast_SynchroniserSleeveCompoundSystemDeflection':
        return self._Cast_SynchroniserSleeveCompoundSystemDeflection(self)
