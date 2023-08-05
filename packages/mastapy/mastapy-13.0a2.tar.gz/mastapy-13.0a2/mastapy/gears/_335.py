"""_335.py

NamedPlanetAngle
"""
from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_NAMED_PLANET_ANGLE = python_net_import('SMT.MastaAPI.Gears', 'NamedPlanetAngle')


__docformat__ = 'restructuredtext en'
__all__ = ('NamedPlanetAngle',)


class NamedPlanetAngle(_0.APIBase):
    """NamedPlanetAngle

    This is a mastapy class.
    """

    TYPE = _NAMED_PLANET_ANGLE

    class _Cast_NamedPlanetAngle:
        """Special nested class for casting NamedPlanetAngle to subclasses."""

        def __init__(self, parent: 'NamedPlanetAngle'):
            self._parent = parent

        @property
        def named_planet_angle(self) -> 'NamedPlanetAngle':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'NamedPlanetAngle.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def planet_angle(self) -> 'float':
        """float: 'PlanetAngle' is the original name of this property."""

        temp = self.wrapped.PlanetAngle

        if temp is None:
            return 0.0

        return temp

    @planet_angle.setter
    def planet_angle(self, value: 'float'):
        self.wrapped.PlanetAngle = float(value) if value else 0.0

    @property
    def cast_to(self) -> 'NamedPlanetAngle._Cast_NamedPlanetAngle':
        return self._Cast_NamedPlanetAngle(self)
