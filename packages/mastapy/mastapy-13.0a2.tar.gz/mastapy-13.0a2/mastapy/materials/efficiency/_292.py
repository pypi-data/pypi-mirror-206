"""_292.py

IndependentResistiveTorque
"""
from mastapy._internal import constructor
from mastapy.materials.efficiency import _299
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INDEPENDENT_RESISTIVE_TORQUE = python_net_import('SMT.MastaAPI.Materials.Efficiency', 'IndependentResistiveTorque')


__docformat__ = 'restructuredtext en'
__all__ = ('IndependentResistiveTorque',)


class IndependentResistiveTorque(_299.ResistiveTorque):
    """IndependentResistiveTorque

    This is a mastapy class.
    """

    TYPE = _INDEPENDENT_RESISTIVE_TORQUE

    class _Cast_IndependentResistiveTorque:
        """Special nested class for casting IndependentResistiveTorque to subclasses."""

        def __init__(self, parent: 'IndependentResistiveTorque'):
            self._parent = parent

        @property
        def resistive_torque(self):
            return self._parent._cast(_299.ResistiveTorque)

        @property
        def independent_resistive_torque(self) -> 'IndependentResistiveTorque':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'IndependentResistiveTorque.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def load_dependent_resistive_torque(self) -> 'float':
        """float: 'LoadDependentResistiveTorque' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LoadDependentResistiveTorque

        if temp is None:
            return 0.0

        return temp

    @property
    def speed_dependent_resistive_torque(self) -> 'float':
        """float: 'SpeedDependentResistiveTorque' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SpeedDependentResistiveTorque

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self) -> 'IndependentResistiveTorque._Cast_IndependentResistiveTorque':
        return self._Cast_IndependentResistiveTorque(self)
