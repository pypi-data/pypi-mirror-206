"""_293.py

LoadAndSpeedCombinedPowerLoss
"""
from mastapy.materials.efficiency import _298
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOAD_AND_SPEED_COMBINED_POWER_LOSS = python_net_import('SMT.MastaAPI.Materials.Efficiency', 'LoadAndSpeedCombinedPowerLoss')


__docformat__ = 'restructuredtext en'
__all__ = ('LoadAndSpeedCombinedPowerLoss',)


class LoadAndSpeedCombinedPowerLoss(_298.PowerLoss):
    """LoadAndSpeedCombinedPowerLoss

    This is a mastapy class.
    """

    TYPE = _LOAD_AND_SPEED_COMBINED_POWER_LOSS

    class _Cast_LoadAndSpeedCombinedPowerLoss:
        """Special nested class for casting LoadAndSpeedCombinedPowerLoss to subclasses."""

        def __init__(self, parent: 'LoadAndSpeedCombinedPowerLoss'):
            self._parent = parent

        @property
        def power_loss(self):
            return self._parent._cast(_298.PowerLoss)

        @property
        def load_and_speed_combined_power_loss(self) -> 'LoadAndSpeedCombinedPowerLoss':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'LoadAndSpeedCombinedPowerLoss.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'LoadAndSpeedCombinedPowerLoss._Cast_LoadAndSpeedCombinedPowerLoss':
        return self._Cast_LoadAndSpeedCombinedPowerLoss(self)
