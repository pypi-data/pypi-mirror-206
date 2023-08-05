"""_6795.py

BoltedJointLoadCase
"""
from mastapy.system_model.part_model import _2423
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6916
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BOLTED_JOINT_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'BoltedJointLoadCase')


__docformat__ = 'restructuredtext en'
__all__ = ('BoltedJointLoadCase',)


class BoltedJointLoadCase(_6916.SpecialisedAssemblyLoadCase):
    """BoltedJointLoadCase

    This is a mastapy class.
    """

    TYPE = _BOLTED_JOINT_LOAD_CASE

    class _Cast_BoltedJointLoadCase:
        """Special nested class for casting BoltedJointLoadCase to subclasses."""

        def __init__(self, parent: 'BoltedJointLoadCase'):
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
        def bolted_joint_load_case(self) -> 'BoltedJointLoadCase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'BoltedJointLoadCase.TYPE'):
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
    def cast_to(self) -> 'BoltedJointLoadCase._Cast_BoltedJointLoadCase':
        return self._Cast_BoltedJointLoadCase(self)
