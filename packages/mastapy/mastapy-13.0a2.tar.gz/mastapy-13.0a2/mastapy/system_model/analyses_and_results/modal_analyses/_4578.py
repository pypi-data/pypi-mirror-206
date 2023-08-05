"""_4578.py

ConceptGearSetModalAnalysis
"""
from typing import List

from mastapy.system_model.part_model.gears import _2501
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6807
from mastapy.system_model.analyses_and_results.system_deflections import _2700
from mastapy.system_model.analyses_and_results.modal_analyses import _4577, _4576, _4611
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_GEAR_SET_MODAL_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses', 'ConceptGearSetModalAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('ConceptGearSetModalAnalysis',)


class ConceptGearSetModalAnalysis(_4611.GearSetModalAnalysis):
    """ConceptGearSetModalAnalysis

    This is a mastapy class.
    """

    TYPE = _CONCEPT_GEAR_SET_MODAL_ANALYSIS

    class _Cast_ConceptGearSetModalAnalysis:
        """Special nested class for casting ConceptGearSetModalAnalysis to subclasses."""

        def __init__(self, parent: 'ConceptGearSetModalAnalysis'):
            self._parent = parent

        @property
        def gear_set_modal_analysis(self):
            return self._parent._cast(_4611.GearSetModalAnalysis)

        @property
        def specialised_assembly_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4655
            
            return self._parent._cast(_4655.SpecialisedAssemblyModalAnalysis)

        @property
        def abstract_assembly_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4547
            
            return self._parent._cast(_4547.AbstractAssemblyModalAnalysis)

        @property
        def part_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4635
            
            return self._parent._cast(_4635.PartModalAnalysis)

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
        def concept_gear_set_modal_analysis(self) -> 'ConceptGearSetModalAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConceptGearSetModalAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2501.ConceptGearSet':
        """ConceptGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_load_case(self) -> '_6807.ConceptGearSetLoadCase':
        """ConceptGearSetLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results(self) -> '_2700.ConceptGearSetSystemDeflection':
        """ConceptGearSetSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def concept_gears_modal_analysis(self) -> 'List[_4577.ConceptGearModalAnalysis]':
        """List[ConceptGearModalAnalysis]: 'ConceptGearsModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConceptGearsModalAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def concept_meshes_modal_analysis(self) -> 'List[_4576.ConceptGearMeshModalAnalysis]':
        """List[ConceptGearMeshModalAnalysis]: 'ConceptMeshesModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConceptMeshesModalAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'ConceptGearSetModalAnalysis._Cast_ConceptGearSetModalAnalysis':
        return self._Cast_ConceptGearSetModalAnalysis(self)
