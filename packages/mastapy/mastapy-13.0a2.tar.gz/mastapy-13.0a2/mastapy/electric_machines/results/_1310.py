"""_1310.py

DynamicForceResults
"""
from typing import List

from mastapy.math_utility import _1501
from mastapy._internal import constructor, conversion
from mastapy.electric_machines.harmonic_load_data import _1366
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DYNAMIC_FORCE_RESULTS = python_net_import('SMT.MastaAPI.ElectricMachines.Results', 'DynamicForceResults')


__docformat__ = 'restructuredtext en'
__all__ = ('DynamicForceResults',)


class DynamicForceResults(_1366.ElectricMachineHarmonicLoadDataBase):
    """DynamicForceResults

    This is a mastapy class.
    """

    TYPE = _DYNAMIC_FORCE_RESULTS

    class _Cast_DynamicForceResults:
        """Special nested class for casting DynamicForceResults to subclasses."""

        def __init__(self, parent: 'DynamicForceResults'):
            self._parent = parent

        @property
        def electric_machine_harmonic_load_data_base(self):
            return self._parent._cast(_1366.ElectricMachineHarmonicLoadDataBase)

        @property
        def speed_dependent_harmonic_load_data(self):
            from mastapy.electric_machines.harmonic_load_data import _1371
            
            return self._parent._cast(_1371.SpeedDependentHarmonicLoadData)

        @property
        def harmonic_load_data_base(self):
            from mastapy.electric_machines.harmonic_load_data import _1368
            
            return self._parent._cast(_1368.HarmonicLoadDataBase)

        @property
        def dynamic_force_results(self) -> 'DynamicForceResults':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'DynamicForceResults.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def excitations(self) -> 'List[_1501.FourierSeries]':
        """List[FourierSeries]: 'Excitations' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Excitations

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'DynamicForceResults._Cast_DynamicForceResults':
        return self._Cast_DynamicForceResults(self)
