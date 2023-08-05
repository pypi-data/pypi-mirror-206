"""_2907.py

MeasurementComponentCompoundSystemDeflection
"""
from typing import List

from mastapy.system_model.part_model import _2443
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections import _2759
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2954
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MEASUREMENT_COMPONENT_COMPOUND_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound', 'MeasurementComponentCompoundSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('MeasurementComponentCompoundSystemDeflection',)


class MeasurementComponentCompoundSystemDeflection(_2954.VirtualComponentCompoundSystemDeflection):
    """MeasurementComponentCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _MEASUREMENT_COMPONENT_COMPOUND_SYSTEM_DEFLECTION

    class _Cast_MeasurementComponentCompoundSystemDeflection:
        """Special nested class for casting MeasurementComponentCompoundSystemDeflection to subclasses."""

        def __init__(self, parent: 'MeasurementComponentCompoundSystemDeflection'):
            self._parent = parent

        @property
        def virtual_component_compound_system_deflection(self):
            return self._parent._cast(_2954.VirtualComponentCompoundSystemDeflection)

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
        def measurement_component_compound_system_deflection(self) -> 'MeasurementComponentCompoundSystemDeflection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'MeasurementComponentCompoundSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2443.MeasurementComponent':
        """MeasurementComponent: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_2759.MeasurementComponentSystemDeflection]':
        """List[MeasurementComponentSystemDeflection]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases(self) -> 'List[_2759.MeasurementComponentSystemDeflection]':
        """List[MeasurementComponentSystemDeflection]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'MeasurementComponentCompoundSystemDeflection._Cast_MeasurementComponentCompoundSystemDeflection':
        return self._Cast_MeasurementComponentCompoundSystemDeflection(self)
