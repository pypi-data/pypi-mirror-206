"""_2870.py

CVTBeltConnectionCompoundSystemDeflection
"""
from typing import List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections import _2711
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2839
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_BELT_CONNECTION_COMPOUND_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound', 'CVTBeltConnectionCompoundSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('CVTBeltConnectionCompoundSystemDeflection',)


class CVTBeltConnectionCompoundSystemDeflection(_2839.BeltConnectionCompoundSystemDeflection):
    """CVTBeltConnectionCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _CVT_BELT_CONNECTION_COMPOUND_SYSTEM_DEFLECTION

    class _Cast_CVTBeltConnectionCompoundSystemDeflection:
        """Special nested class for casting CVTBeltConnectionCompoundSystemDeflection to subclasses."""

        def __init__(self, parent: 'CVTBeltConnectionCompoundSystemDeflection'):
            self._parent = parent

        @property
        def belt_connection_compound_system_deflection(self):
            return self._parent._cast(_2839.BeltConnectionCompoundSystemDeflection)

        @property
        def inter_mountable_component_connection_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2896
            
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
        def cvt_belt_connection_compound_system_deflection(self) -> 'CVTBeltConnectionCompoundSystemDeflection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CVTBeltConnectionCompoundSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def belt_safety_factor_for_clamping_force(self) -> 'float':
        """float: 'BeltSafetyFactorForClampingForce' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BeltSafetyFactorForClampingForce

        if temp is None:
            return 0.0

        return temp

    @property
    def connection_analysis_cases_ready(self) -> 'List[_2711.CVTBeltConnectionSystemDeflection]':
        """List[CVTBeltConnectionSystemDeflection]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def connection_analysis_cases(self) -> 'List[_2711.CVTBeltConnectionSystemDeflection]':
        """List[CVTBeltConnectionSystemDeflection]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'CVTBeltConnectionCompoundSystemDeflection._Cast_CVTBeltConnectionCompoundSystemDeflection':
        return self._Cast_CVTBeltConnectionCompoundSystemDeflection(self)
