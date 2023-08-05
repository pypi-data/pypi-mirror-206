"""_6932.py

SynchroniserLoadCase
"""
from mastapy.system_model.part_model.couplings import _2581
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6916
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'SynchroniserLoadCase')


__docformat__ = 'restructuredtext en'
__all__ = ('SynchroniserLoadCase',)


class SynchroniserLoadCase(_6916.SpecialisedAssemblyLoadCase):
    """SynchroniserLoadCase

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_LOAD_CASE

    class _Cast_SynchroniserLoadCase:
        """Special nested class for casting SynchroniserLoadCase to subclasses."""

        def __init__(self, parent: 'SynchroniserLoadCase'):
            self._parent = parent

        @property
        def specialised_assembly_load_case(self):
            return self._parent._cast(_6916.SpecialisedAssemblyLoadCase)

        @property
        def abstract_assembly_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6771
            
            return self._parent._cast(_6771.AbstractAssemblyLoadCase)

        @property
        def part_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6892
            
            return self._parent._cast(_6892.PartLoadCase)

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
        def synchroniser_load_case(self) -> 'SynchroniserLoadCase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'SynchroniserLoadCase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2581.Synchroniser':
        """Synchroniser: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'SynchroniserLoadCase._Cast_SynchroniserLoadCase':
        return self._Cast_SynchroniserLoadCase(self)
