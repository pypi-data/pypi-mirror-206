"""_6943.py

UnbalancedMassHarmonicLoadData
"""
from typing import List

from mastapy._internal.implicit import enum_with_selected_value
from mastapy.math_utility import _1492, _1501
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import enum_with_selected_value_runtime, conversion, constructor
from mastapy.electric_machines.harmonic_load_data import _1371
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_UNBALANCED_MASS_HARMONIC_LOAD_DATA = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'UnbalancedMassHarmonicLoadData')


__docformat__ = 'restructuredtext en'
__all__ = ('UnbalancedMassHarmonicLoadData',)


class UnbalancedMassHarmonicLoadData(_1371.SpeedDependentHarmonicLoadData):
    """UnbalancedMassHarmonicLoadData

    This is a mastapy class.
    """

    TYPE = _UNBALANCED_MASS_HARMONIC_LOAD_DATA

    class _Cast_UnbalancedMassHarmonicLoadData:
        """Special nested class for casting UnbalancedMassHarmonicLoadData to subclasses."""

        def __init__(self, parent: 'UnbalancedMassHarmonicLoadData'):
            self._parent = parent

        @property
        def speed_dependent_harmonic_load_data(self):
            return self._parent._cast(_1371.SpeedDependentHarmonicLoadData)

        @property
        def harmonic_load_data_base(self):
            from mastapy.electric_machines.harmonic_load_data import _1368
            
            return self._parent._cast(_1368.HarmonicLoadDataBase)

        @property
        def unbalanced_mass_harmonic_load_data(self) -> 'UnbalancedMassHarmonicLoadData':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'UnbalancedMassHarmonicLoadData.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def degree_of_freedom(self) -> 'enum_with_selected_value.EnumWithSelectedValue_DegreesOfFreedom':
        """enum_with_selected_value.EnumWithSelectedValue_DegreesOfFreedom: 'DegreeOfFreedom' is the original name of this property."""

        temp = self.wrapped.DegreeOfFreedom

        if temp is None:
            return None

        value = enum_with_selected_value.EnumWithSelectedValue_DegreesOfFreedom.wrapped_type()
        return enum_with_selected_value_runtime.create(temp, value) if temp is not None else None

    @degree_of_freedom.setter
    def degree_of_freedom(self, value: 'enum_with_selected_value.EnumWithSelectedValue_DegreesOfFreedom.implicit_type()'):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = enum_with_selected_value.EnumWithSelectedValue_DegreesOfFreedom.implicit_type()
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.DegreeOfFreedom = value

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
    def cast_to(self) -> 'UnbalancedMassHarmonicLoadData._Cast_UnbalancedMassHarmonicLoadData':
        return self._Cast_UnbalancedMassHarmonicLoadData(self)
