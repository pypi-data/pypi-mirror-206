"""_2911.py

PartToPartShearCouplingCompoundSystemDeflection
"""
from typing import List

from mastapy.system_model.part_model.couplings import _2567
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections import _2767
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2867
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_TO_PART_SHEAR_COUPLING_COMPOUND_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound', 'PartToPartShearCouplingCompoundSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('PartToPartShearCouplingCompoundSystemDeflection',)


class PartToPartShearCouplingCompoundSystemDeflection(_2867.CouplingCompoundSystemDeflection):
    """PartToPartShearCouplingCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _PART_TO_PART_SHEAR_COUPLING_COMPOUND_SYSTEM_DEFLECTION

    class _Cast_PartToPartShearCouplingCompoundSystemDeflection:
        """Special nested class for casting PartToPartShearCouplingCompoundSystemDeflection to subclasses."""

        def __init__(self, parent: 'PartToPartShearCouplingCompoundSystemDeflection'):
            self._parent = parent

        @property
        def coupling_compound_system_deflection(self):
            return self._parent._cast(_2867.CouplingCompoundSystemDeflection)

        @property
        def specialised_assembly_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2930
            
            return self._parent._cast(_2930.SpecialisedAssemblyCompoundSystemDeflection)

        @property
        def abstract_assembly_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2830
            
            return self._parent._cast(_2830.AbstractAssemblyCompoundSystemDeflection)

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
        def part_to_part_shear_coupling_compound_system_deflection(self) -> 'PartToPartShearCouplingCompoundSystemDeflection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'PartToPartShearCouplingCompoundSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2567.PartToPartShearCoupling':
        """PartToPartShearCoupling: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_design(self) -> '_2567.PartToPartShearCoupling':
        """PartToPartShearCoupling: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_2767.PartToPartShearCouplingSystemDeflection]':
        """List[PartToPartShearCouplingSystemDeflection]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_2767.PartToPartShearCouplingSystemDeflection]':
        """List[PartToPartShearCouplingSystemDeflection]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'PartToPartShearCouplingCompoundSystemDeflection._Cast_PartToPartShearCouplingCompoundSystemDeflection':
        return self._Cast_PartToPartShearCouplingCompoundSystemDeflection(self)
