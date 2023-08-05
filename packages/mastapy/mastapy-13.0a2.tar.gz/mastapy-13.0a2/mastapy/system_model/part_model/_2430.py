"""_2430.py

EnginePartLoad
"""
from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ENGINE_PART_LOAD = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'EnginePartLoad')


__docformat__ = 'restructuredtext en'
__all__ = ('EnginePartLoad',)


class EnginePartLoad(_0.APIBase):
    """EnginePartLoad

    This is a mastapy class.
    """

    TYPE = _ENGINE_PART_LOAD

    class _Cast_EnginePartLoad:
        """Special nested class for casting EnginePartLoad to subclasses."""

        def __init__(self, parent: 'EnginePartLoad'):
            self._parent = parent

        @property
        def engine_part_load(self) -> 'EnginePartLoad':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'EnginePartLoad.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def consumption(self) -> 'float':
        """float: 'Consumption' is the original name of this property."""

        temp = self.wrapped.Consumption

        if temp is None:
            return 0.0

        return temp

    @consumption.setter
    def consumption(self, value: 'float'):
        self.wrapped.Consumption = float(value) if value else 0.0

    @property
    def throttle(self) -> 'float':
        """float: 'Throttle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Throttle

        if temp is None:
            return 0.0

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
    def cast_to(self) -> 'EnginePartLoad._Cast_EnginePartLoad':
        return self._Cast_EnginePartLoad(self)
