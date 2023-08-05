"""_7255.py

BoltedJointAdvancedSystemDeflection
"""
from typing import List

from mastapy.system_model.part_model import _2423
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6795
from mastapy.system_model.analyses_and_results.system_deflections import _2688
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7336
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BOLTED_JOINT_ADVANCED_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections', 'BoltedJointAdvancedSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('BoltedJointAdvancedSystemDeflection',)


class BoltedJointAdvancedSystemDeflection(_7336.SpecialisedAssemblyAdvancedSystemDeflection):
    """BoltedJointAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _BOLTED_JOINT_ADVANCED_SYSTEM_DEFLECTION

    class _Cast_BoltedJointAdvancedSystemDeflection:
        """Special nested class for casting BoltedJointAdvancedSystemDeflection to subclasses."""

        def __init__(self, parent: 'BoltedJointAdvancedSystemDeflection'):
            self._parent = parent

        @property
        def specialised_assembly_advanced_system_deflection(self):
            return self._parent._cast(_7336.SpecialisedAssemblyAdvancedSystemDeflection)

        @property
        def abstract_assembly_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7232
            
            return self._parent._cast(_7232.AbstractAssemblyAdvancedSystemDeflection)

        @property
        def part_advanced_system_deflection(self):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7317
            
            return self._parent._cast(_7317.PartAdvancedSystemDeflection)

        @property
        def part_static_load_analysis_case(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7510
            
            return self._parent._cast(_7510.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7507
            
            return self._parent._cast(_7507.PartAnalysisCase)

        @property
        def part_analysis(self):
            from mastapy.system_model.analyses_and_results import _2636
            
            return self._parent._cast(_2636.PartAnalysis)

        @property
        def design_entity_single_context_analysis(self):
            from mastapy.system_model.analyses_and_results import _2632
            
            return self._parent._cast(_2632.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(self):
            from mastapy.system_model.analyses_and_results import _2630
            
            return self._parent._cast(_2630.DesignEntityAnalysis)

        @property
        def bolted_joint_advanced_system_deflection(self) -> 'BoltedJointAdvancedSystemDeflection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'BoltedJointAdvancedSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2423.BoltedJoint':
        """BoltedJoint: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_load_case(self) -> '_6795.BoltedJointLoadCase':
        """BoltedJointLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_system_deflection_results(self) -> 'List[_2688.BoltedJointSystemDeflection]':
        """List[BoltedJointSystemDeflection]: 'AssemblySystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblySystemDeflectionResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'BoltedJointAdvancedSystemDeflection._Cast_BoltedJointAdvancedSystemDeflection':
        return self._Cast_BoltedJointAdvancedSystemDeflection(self)
