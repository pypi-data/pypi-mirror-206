"""_1329.py

LinearDQModel
"""
from mastapy._internal import constructor
from mastapy.electric_machines.results import _1312
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LINEAR_DQ_MODEL = python_net_import('SMT.MastaAPI.ElectricMachines.Results', 'LinearDQModel')


__docformat__ = 'restructuredtext en'
__all__ = ('LinearDQModel',)


class LinearDQModel(_1312.ElectricMachineDQModel):
    """LinearDQModel

    This is a mastapy class.
    """

    TYPE = _LINEAR_DQ_MODEL

    class _Cast_LinearDQModel:
        """Special nested class for casting LinearDQModel to subclasses."""

        def __init__(self, parent: 'LinearDQModel'):
            self._parent = parent

        @property
        def electric_machine_dq_model(self):
            return self._parent._cast(_1312.ElectricMachineDQModel)

        @property
        def linear_dq_model(self) -> 'LinearDQModel':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'LinearDQModel.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def apparent_d_axis_inductance(self) -> 'float':
        """float: 'ApparentDAxisInductance' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ApparentDAxisInductance

        if temp is None:
            return 0.0

        return temp

    @property
    def apparent_q_axis_inductance(self) -> 'float':
        """float: 'ApparentQAxisInductance' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ApparentQAxisInductance

        if temp is None:
            return 0.0

        return temp

    @property
    def base_speed_from_mtpa_at_reference_temperature(self) -> 'float':
        """float: 'BaseSpeedFromMTPAAtReferenceTemperature' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BaseSpeedFromMTPAAtReferenceTemperature

        if temp is None:
            return 0.0

        return temp

    @property
    def max_speed_at_reference_temperature(self) -> 'float':
        """float: 'MaxSpeedAtReferenceTemperature' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaxSpeedAtReferenceTemperature

        if temp is None:
            return 0.0

        return temp

    @property
    def name(self) -> 'str':
        """str: 'Name' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Name

        if temp is None:
            return ''

        return temp

    @property
    def cast_to(self) -> 'LinearDQModel._Cast_LinearDQModel':
        return self._Cast_LinearDQModel(self)
