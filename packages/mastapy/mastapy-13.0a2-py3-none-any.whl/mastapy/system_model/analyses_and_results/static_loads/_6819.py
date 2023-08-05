"""_6819.py

CVTLoadCase
"""
from typing import List

from mastapy._internal import constructor, conversion
from mastapy.system_model.part_model.couplings import _2565
from mastapy.system_model.analyses_and_results.static_loads import _6820, _6786
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'CVTLoadCase')


__docformat__ = 'restructuredtext en'
__all__ = ('CVTLoadCase',)


class CVTLoadCase(_6786.BeltDriveLoadCase):
    """CVTLoadCase

    This is a mastapy class.
    """

    TYPE = _CVT_LOAD_CASE

    class _Cast_CVTLoadCase:
        """Special nested class for casting CVTLoadCase to subclasses."""

        def __init__(self, parent: 'CVTLoadCase'):
            self._parent = parent

        @property
        def belt_drive_load_case(self):
            return self._parent._cast(_6786.BeltDriveLoadCase)

        @property
        def specialised_assembly_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6916
            
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
        def cvt_load_case(self) -> 'CVTLoadCase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CVTLoadCase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def speed_ratio(self) -> 'float':
        """float: 'SpeedRatio' is the original name of this property."""

        temp = self.wrapped.SpeedRatio

        if temp is None:
            return 0.0

        return temp

    @speed_ratio.setter
    def speed_ratio(self, value: 'float'):
        self.wrapped.SpeedRatio = float(value) if value else 0.0

    @property
    def assembly_design(self) -> '_2565.CVT':
        """CVT: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def pulleys(self) -> 'List[_6820.CVTPulleyLoadCase]':
        """List[CVTPulleyLoadCase]: 'Pulleys' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Pulleys

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'CVTLoadCase._Cast_CVTLoadCase':
        return self._Cast_CVTLoadCase(self)
