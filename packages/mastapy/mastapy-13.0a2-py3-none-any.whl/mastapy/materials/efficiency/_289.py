"""_289.py

CombinedResistiveTorque
"""
from mastapy.materials.efficiency import _299
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COMBINED_RESISTIVE_TORQUE = python_net_import('SMT.MastaAPI.Materials.Efficiency', 'CombinedResistiveTorque')


__docformat__ = 'restructuredtext en'
__all__ = ('CombinedResistiveTorque',)


class CombinedResistiveTorque(_299.ResistiveTorque):
    """CombinedResistiveTorque

    This is a mastapy class.
    """

    TYPE = _COMBINED_RESISTIVE_TORQUE

    class _Cast_CombinedResistiveTorque:
        """Special nested class for casting CombinedResistiveTorque to subclasses."""

        def __init__(self, parent: 'CombinedResistiveTorque'):
            self._parent = parent

        @property
        def resistive_torque(self):
            return self._parent._cast(_299.ResistiveTorque)

        @property
        def combined_resistive_torque(self) -> 'CombinedResistiveTorque':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CombinedResistiveTorque.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'CombinedResistiveTorque._Cast_CombinedResistiveTorque':
        return self._Cast_CombinedResistiveTorque(self)
