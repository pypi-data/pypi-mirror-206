"""_7490.py

VirtualComponentCompoundAdvancedSystemDeflection
"""
from typing import List

from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7361
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7445
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_VIRTUAL_COMPONENT_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound', 'VirtualComponentCompoundAdvancedSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('VirtualComponentCompoundAdvancedSystemDeflection',)


class VirtualComponentCompoundAdvancedSystemDeflection(_7445.MountableComponentCompoundAdvancedSystemDeflection):
    """VirtualComponentCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _VIRTUAL_COMPONENT_COMPOUND_ADVANCED_SYSTEM_DEFLECTION

    class _Cast_VirtualComponentCompoundAdvancedSystemDeflection:
        """Special nested class for casting VirtualComponentCompoundAdvancedSystemDeflection to subclasses."""

        def __init__(self, parent: 'VirtualComponentCompoundAdvancedSystemDeflection'):
            self._parent = parent

        @property
        def mountable_component_compound_advanced_system_deflection(self):
            return self._parent._cast(_7445.MountableComponentCompoundAdvancedSystemDeflection)

        @property
        def component_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7393
            
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
        def mass_disc_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7443
            
            return self._parent._cast(_7443.MassDiscCompoundAdvancedSystemDeflection)

        @property
        def measurement_component_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7444
            
            return self._parent._cast(_7444.MeasurementComponentCompoundAdvancedSystemDeflection)

        @property
        def point_load_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7454
            
            return self._parent._cast(_7454.PointLoadCompoundAdvancedSystemDeflection)

        @property
        def power_load_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7455
            
            return self._parent._cast(_7455.PowerLoadCompoundAdvancedSystemDeflection)

        @property
        def unbalanced_mass_compound_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7489
            
            return self._parent._cast(_7489.UnbalancedMassCompoundAdvancedSystemDeflection)

        @property
        def virtual_component_compound_advanced_system_deflection(self) -> 'VirtualComponentCompoundAdvancedSystemDeflection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'VirtualComponentCompoundAdvancedSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self) -> 'List[_7361.VirtualComponentAdvancedSystemDeflection]':
        """List[VirtualComponentAdvancedSystemDeflection]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases_ready(self) -> 'List[_7361.VirtualComponentAdvancedSystemDeflection]':
        """List[VirtualComponentAdvancedSystemDeflection]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'VirtualComponentCompoundAdvancedSystemDeflection._Cast_VirtualComponentCompoundAdvancedSystemDeflection':
        return self._Cast_VirtualComponentCompoundAdvancedSystemDeflection(self)
