"""_2431.py

EngineSpeed
"""
from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ENGINE_SPEED = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'EngineSpeed')


__docformat__ = 'restructuredtext en'
__all__ = ('EngineSpeed',)


class EngineSpeed(_0.APIBase):
    """EngineSpeed

    This is a mastapy class.
    """

    TYPE = _ENGINE_SPEED

    class _Cast_EngineSpeed:
        """Special nested class for casting EngineSpeed to subclasses."""

        def __init__(self, parent: 'EngineSpeed'):
            self._parent = parent

        @property
        def engine_speed(self) -> 'EngineSpeed':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'EngineSpeed.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def can_do_efficiency(self) -> 'bool':
        """bool: 'CanDoEfficiency' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CanDoEfficiency

        if temp is None:
            return False

        return temp

    @property
    def number_of_part_loads(self) -> 'int':
        """int: 'NumberOfPartLoads' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NumberOfPartLoads

        if temp is None:
            return 0

        return temp

    @property
    def number_of_part_torques(self) -> 'int':
        """int: 'NumberOfPartTorques' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NumberOfPartTorques

        if temp is None:
            return 0

        return temp

    @property
    def part_loads_dummy(self) -> 'str':
        """str: 'PartLoadsDummy' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PartLoadsDummy

        if temp is None:
            return ''

        return temp

    @property
    def torque(self) -> 'float':
        """float: 'Torque' is the original name of this property."""

        temp = self.wrapped.Torque

        if temp is None:
            return 0.0

        return temp

    @torque.setter
    def torque(self, value: 'float'):
        self.wrapped.Torque = float(value) if value else 0.0

    @property
    def cast_to(self) -> 'EngineSpeed._Cast_EngineSpeed':
        return self._Cast_EngineSpeed(self)
