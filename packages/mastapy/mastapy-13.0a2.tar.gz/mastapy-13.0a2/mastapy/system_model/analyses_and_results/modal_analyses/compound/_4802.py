"""_4802.py

SpiralBevelGearSetCompoundModalAnalysis
"""
from typing import List

from mastapy.system_model.part_model.gears import _2523
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses import _4658
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4800, _4801, _4719
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPIRAL_BEVEL_GEAR_SET_COMPOUND_MODAL_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound', 'SpiralBevelGearSetCompoundModalAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('SpiralBevelGearSetCompoundModalAnalysis',)


class SpiralBevelGearSetCompoundModalAnalysis(_4719.BevelGearSetCompoundModalAnalysis):
    """SpiralBevelGearSetCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _SPIRAL_BEVEL_GEAR_SET_COMPOUND_MODAL_ANALYSIS

    class _Cast_SpiralBevelGearSetCompoundModalAnalysis:
        """Special nested class for casting SpiralBevelGearSetCompoundModalAnalysis to subclasses."""

        def __init__(self, parent: 'SpiralBevelGearSetCompoundModalAnalysis'):
            self._parent = parent

        @property
        def bevel_gear_set_compound_modal_analysis(self):
            return self._parent._cast(_4719.BevelGearSetCompoundModalAnalysis)

        @property
        def agma_gleason_conical_gear_set_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4707
            
            return self._parent._cast(_4707.AGMAGleasonConicalGearSetCompoundModalAnalysis)

        @property
        def conical_gear_set_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4735
            
            return self._parent._cast(_4735.ConicalGearSetCompoundModalAnalysis)

        @property
        def gear_set_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4761
            
            return self._parent._cast(_4761.GearSetCompoundModalAnalysis)

        @property
        def specialised_assembly_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4799
            
            return self._parent._cast(_4799.SpecialisedAssemblyCompoundModalAnalysis)

        @property
        def abstract_assembly_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4701
            
            return self._parent._cast(_4701.AbstractAssemblyCompoundModalAnalysis)

        @property
        def part_compound_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4780
            
            return self._parent._cast(_4780.PartCompoundModalAnalysis)

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
        def spiral_bevel_gear_set_compound_modal_analysis(self) -> 'SpiralBevelGearSetCompoundModalAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'SpiralBevelGearSetCompoundModalAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2523.SpiralBevelGearSet':
        """SpiralBevelGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_design(self) -> '_2523.SpiralBevelGearSet':
        """SpiralBevelGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_4658.SpiralBevelGearSetModalAnalysis]':
        """List[SpiralBevelGearSetModalAnalysis]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def spiral_bevel_gears_compound_modal_analysis(self) -> 'List[_4800.SpiralBevelGearCompoundModalAnalysis]':
        """List[SpiralBevelGearCompoundModalAnalysis]: 'SpiralBevelGearsCompoundModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SpiralBevelGearsCompoundModalAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def spiral_bevel_meshes_compound_modal_analysis(self) -> 'List[_4801.SpiralBevelGearMeshCompoundModalAnalysis]':
        """List[SpiralBevelGearMeshCompoundModalAnalysis]: 'SpiralBevelMeshesCompoundModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SpiralBevelMeshesCompoundModalAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_4658.SpiralBevelGearSetModalAnalysis]':
        """List[SpiralBevelGearSetModalAnalysis]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'SpiralBevelGearSetCompoundModalAnalysis._Cast_SpiralBevelGearSetCompoundModalAnalysis':
        return self._Cast_SpiralBevelGearSetCompoundModalAnalysis(self)
