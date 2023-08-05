"""_4626.py

MassDiscModalAnalysis
"""
from typing import List

from mastapy.system_model.part_model import _2442
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6885
from mastapy.system_model.analyses_and_results.system_deflections import _2758
from mastapy.system_model.analyses_and_results.modal_analyses import _4679
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MASS_DISC_MODAL_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses', 'MassDiscModalAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('MassDiscModalAnalysis',)


class MassDiscModalAnalysis(_4679.VirtualComponentModalAnalysis):
    """MassDiscModalAnalysis

    This is a mastapy class.
    """

    TYPE = _MASS_DISC_MODAL_ANALYSIS

    class _Cast_MassDiscModalAnalysis:
        """Special nested class for casting MassDiscModalAnalysis to subclasses."""

        def __init__(self, parent: 'MassDiscModalAnalysis'):
            self._parent = parent

        @property
        def virtual_component_modal_analysis(self):
            return self._parent._cast(_4679.VirtualComponentModalAnalysis)

        @property
        def mountable_component_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4631
            
            return self._parent._cast(_4631.MountableComponentModalAnalysis)

        @property
        def component_modal_analysis(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4572
            
            return self._parent._cast(_4572.ComponentModalAnalysis)

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
        def mass_disc_modal_analysis(self) -> 'MassDiscModalAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'MassDiscModalAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2442.MassDisc':
        """MassDisc: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_load_case(self) -> '_6885.MassDiscLoadCase':
        """MassDiscLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results(self) -> '_2758.MassDiscSystemDeflection':
        """MassDiscSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def planetaries(self) -> 'List[MassDiscModalAnalysis]':
        """List[MassDiscModalAnalysis]: 'Planetaries' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'MassDiscModalAnalysis._Cast_MassDiscModalAnalysis':
        return self._Cast_MassDiscModalAnalysis(self)
