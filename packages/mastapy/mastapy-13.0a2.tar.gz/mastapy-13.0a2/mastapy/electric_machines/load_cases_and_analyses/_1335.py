"""_1335.py

DynamicForceAnalysis
"""
from typing import List

from mastapy._internal import constructor, conversion
from mastapy.electric_machines.load_cases_and_analyses import _1336, _1343, _1339
from mastapy.electric_machines.results import _1310
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DYNAMIC_FORCE_ANALYSIS = python_net_import('SMT.MastaAPI.ElectricMachines.LoadCasesAndAnalyses', 'DynamicForceAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('DynamicForceAnalysis',)


class DynamicForceAnalysis(_1339.ElectricMachineAnalysis):
    """DynamicForceAnalysis

    This is a mastapy class.
    """

    TYPE = _DYNAMIC_FORCE_ANALYSIS

    class _Cast_DynamicForceAnalysis:
        """Special nested class for casting DynamicForceAnalysis to subclasses."""

        def __init__(self, parent: 'DynamicForceAnalysis'):
            self._parent = parent

        @property
        def electric_machine_analysis(self):
            return self._parent._cast(_1339.ElectricMachineAnalysis)

        @property
        def dynamic_force_analysis(self) -> 'DynamicForceAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'DynamicForceAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def number_of_steps_per_operating_point(self) -> 'int':
        """int: 'NumberOfStepsPerOperatingPoint' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NumberOfStepsPerOperatingPoint

        if temp is None:
            return 0

        return temp

    @property
    def load_case(self) -> '_1336.DynamicForceLoadCase':
        """DynamicForceLoadCase: 'LoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def results(self) -> '_1310.DynamicForceResults':
        """DynamicForceResults: 'Results' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Results

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def single_operating_point_analyses(self) -> 'List[_1343.ElectricMachineFEAnalysis]':
        """List[ElectricMachineFEAnalysis]: 'SingleOperatingPointAnalyses' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SingleOperatingPointAnalyses

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'DynamicForceAnalysis._Cast_DynamicForceAnalysis':
        return self._Cast_DynamicForceAnalysis(self)
