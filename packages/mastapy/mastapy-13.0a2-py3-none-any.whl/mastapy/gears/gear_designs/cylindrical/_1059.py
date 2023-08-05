"""_1059.py

NamedPlanetSideBandAmplitudeFactor
"""
from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_NAMED_PLANET_SIDE_BAND_AMPLITUDE_FACTOR = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Cylindrical', 'NamedPlanetSideBandAmplitudeFactor')


__docformat__ = 'restructuredtext en'
__all__ = ('NamedPlanetSideBandAmplitudeFactor',)


class NamedPlanetSideBandAmplitudeFactor(_0.APIBase):
    """NamedPlanetSideBandAmplitudeFactor

    This is a mastapy class.
    """

    TYPE = _NAMED_PLANET_SIDE_BAND_AMPLITUDE_FACTOR

    class _Cast_NamedPlanetSideBandAmplitudeFactor:
        """Special nested class for casting NamedPlanetSideBandAmplitudeFactor to subclasses."""

        def __init__(self, parent: 'NamedPlanetSideBandAmplitudeFactor'):
            self._parent = parent

        @property
        def named_planet_side_band_amplitude_factor(self) -> 'NamedPlanetSideBandAmplitudeFactor':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'NamedPlanetSideBandAmplitudeFactor.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def planetary_sidebands_amplitude_factor(self) -> 'float':
        """float: 'PlanetarySidebandsAmplitudeFactor' is the original name of this property."""

        temp = self.wrapped.PlanetarySidebandsAmplitudeFactor

        if temp is None:
            return 0.0

        return temp

    @planetary_sidebands_amplitude_factor.setter
    def planetary_sidebands_amplitude_factor(self, value: 'float'):
        self.wrapped.PlanetarySidebandsAmplitudeFactor = float(value) if value else 0.0

    @property
    def cast_to(self) -> 'NamedPlanetSideBandAmplitudeFactor._Cast_NamedPlanetSideBandAmplitudeFactor':
        return self._Cast_NamedPlanetSideBandAmplitudeFactor(self)
