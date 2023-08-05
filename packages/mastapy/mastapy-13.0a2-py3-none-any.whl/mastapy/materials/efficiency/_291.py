"""_291.py

IndependentPowerLoss
"""
from mastapy._internal import constructor
from mastapy.materials.efficiency import _298
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INDEPENDENT_POWER_LOSS = python_net_import('SMT.MastaAPI.Materials.Efficiency', 'IndependentPowerLoss')


__docformat__ = 'restructuredtext en'
__all__ = ('IndependentPowerLoss',)


class IndependentPowerLoss(_298.PowerLoss):
    """IndependentPowerLoss

    This is a mastapy class.
    """

    TYPE = _INDEPENDENT_POWER_LOSS

    class _Cast_IndependentPowerLoss:
        """Special nested class for casting IndependentPowerLoss to subclasses."""

        def __init__(self, parent: 'IndependentPowerLoss'):
            self._parent = parent

        @property
        def power_loss(self):
            return self._parent._cast(_298.PowerLoss)

        @property
        def independent_power_loss(self) -> 'IndependentPowerLoss':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'IndependentPowerLoss.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def load_dependent_power_loss(self) -> 'float':
        """float: 'LoadDependentPowerLoss' is the original name of this property."""

        temp = self.wrapped.LoadDependentPowerLoss

        if temp is None:
            return 0.0

        return temp

    @load_dependent_power_loss.setter
    def load_dependent_power_loss(self, value: 'float'):
        self.wrapped.LoadDependentPowerLoss = float(value) if value else 0.0

    @property
    def speed_dependent_power_loss(self) -> 'float':
        """float: 'SpeedDependentPowerLoss' is the original name of this property."""

        temp = self.wrapped.SpeedDependentPowerLoss

        if temp is None:
            return 0.0

        return temp

    @speed_dependent_power_loss.setter
    def speed_dependent_power_loss(self, value: 'float'):
        self.wrapped.SpeedDependentPowerLoss = float(value) if value else 0.0

    @property
    def cast_to(self) -> 'IndependentPowerLoss._Cast_IndependentPowerLoss':
        return self._Cast_IndependentPowerLoss(self)
