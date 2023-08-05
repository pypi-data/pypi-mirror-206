"""_2868.py

CouplingConnectionCompoundSystemDeflection
"""
from typing import List

from mastapy.system_model.analyses_and_results.system_deflections import _2708
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2896
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_CONNECTION_COMPOUND_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound', 'CouplingConnectionCompoundSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('CouplingConnectionCompoundSystemDeflection',)


class CouplingConnectionCompoundSystemDeflection(_2896.InterMountableComponentConnectionCompoundSystemDeflection):
    """CouplingConnectionCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _COUPLING_CONNECTION_COMPOUND_SYSTEM_DEFLECTION

    class _Cast_CouplingConnectionCompoundSystemDeflection:
        """Special nested class for casting CouplingConnectionCompoundSystemDeflection to subclasses."""

        def __init__(self, parent: 'CouplingConnectionCompoundSystemDeflection'):
            self._parent = parent

        @property
        def inter_mountable_component_connection_compound_system_deflection(self):
            return self._parent._cast(_2896.InterMountableComponentConnectionCompoundSystemDeflection)

        @property
        def connection_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2865
            
            return self._parent._cast(_2865.ConnectionCompoundSystemDeflection)

        @property
        def connection_compound_analysis(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7501
            
            return self._parent._cast(_7501.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7505
            
            return self._parent._cast(_7505.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(self):
            from mastapy.system_model.analyses_and_results import _2630
            
            return self._parent._cast(_2630.DesignEntityAnalysis)

        @property
        def clutch_connection_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2852
            
            return self._parent._cast(_2852.ClutchConnectionCompoundSystemDeflection)

        @property
        def concept_coupling_connection_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2857
            
            return self._parent._cast(_2857.ConceptCouplingConnectionCompoundSystemDeflection)

        @property
        def part_to_part_shear_coupling_connection_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2912
            
            return self._parent._cast(_2912.PartToPartShearCouplingConnectionCompoundSystemDeflection)

        @property
        def spring_damper_connection_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2935
            
            return self._parent._cast(_2935.SpringDamperConnectionCompoundSystemDeflection)

        @property
        def torque_converter_connection_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2950
            
            return self._parent._cast(_2950.TorqueConverterConnectionCompoundSystemDeflection)

        @property
        def coupling_connection_compound_system_deflection(self) -> 'CouplingConnectionCompoundSystemDeflection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CouplingConnectionCompoundSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(self) -> 'List[_2708.CouplingConnectionSystemDeflection]':
        """List[CouplingConnectionSystemDeflection]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def connection_analysis_cases_ready(self) -> 'List[_2708.CouplingConnectionSystemDeflection]':
        """List[CouplingConnectionSystemDeflection]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'CouplingConnectionCompoundSystemDeflection._Cast_CouplingConnectionCompoundSystemDeflection':
        return self._Cast_CouplingConnectionCompoundSystemDeflection(self)
