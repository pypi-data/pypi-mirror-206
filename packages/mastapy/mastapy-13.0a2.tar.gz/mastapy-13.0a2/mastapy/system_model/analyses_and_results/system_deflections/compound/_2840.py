"""_2840.py

BeltDriveCompoundSystemDeflection
"""
from typing import List

from mastapy.system_model.part_model.couplings import _2555
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections import _2679
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2930
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BELT_DRIVE_COMPOUND_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound', 'BeltDriveCompoundSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('BeltDriveCompoundSystemDeflection',)


class BeltDriveCompoundSystemDeflection(_2930.SpecialisedAssemblyCompoundSystemDeflection):
    """BeltDriveCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _BELT_DRIVE_COMPOUND_SYSTEM_DEFLECTION

    class _Cast_BeltDriveCompoundSystemDeflection:
        """Special nested class for casting BeltDriveCompoundSystemDeflection to subclasses."""

        def __init__(self, parent: 'BeltDriveCompoundSystemDeflection'):
            self._parent = parent

        @property
        def specialised_assembly_compound_system_deflection(self):
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
        def cvt_compound_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import _2871
            
            return self._parent._cast(_2871.CVTCompoundSystemDeflection)

        @property
        def belt_drive_compound_system_deflection(self) -> 'BeltDriveCompoundSystemDeflection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'BeltDriveCompoundSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2555.BeltDrive':
        """BeltDrive: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_design(self) -> '_2555.BeltDrive':
        """BeltDrive: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_2679.BeltDriveSystemDeflection]':
        """List[BeltDriveSystemDeflection]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_2679.BeltDriveSystemDeflection]':
        """List[BeltDriveSystemDeflection]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'BeltDriveCompoundSystemDeflection._Cast_BeltDriveCompoundSystemDeflection':
        return self._Cast_BeltDriveCompoundSystemDeflection(self)
