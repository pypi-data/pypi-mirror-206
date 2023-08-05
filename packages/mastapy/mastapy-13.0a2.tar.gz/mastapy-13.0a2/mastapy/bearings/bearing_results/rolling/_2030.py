"""_2030.py

LoadedSphericalThrustRollerBearingElement
"""
from mastapy.bearings.bearing_results.rolling import _2024
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_SPHERICAL_THRUST_ROLLER_BEARING_ELEMENT = python_net_import('SMT.MastaAPI.Bearings.BearingResults.Rolling', 'LoadedSphericalThrustRollerBearingElement')


__docformat__ = 'restructuredtext en'
__all__ = ('LoadedSphericalThrustRollerBearingElement',)


class LoadedSphericalThrustRollerBearingElement(_2024.LoadedSphericalRollerBearingElement):
    """LoadedSphericalThrustRollerBearingElement

    This is a mastapy class.
    """

    TYPE = _LOADED_SPHERICAL_THRUST_ROLLER_BEARING_ELEMENT

    class _Cast_LoadedSphericalThrustRollerBearingElement:
        """Special nested class for casting LoadedSphericalThrustRollerBearingElement to subclasses."""

        def __init__(self, parent: 'LoadedSphericalThrustRollerBearingElement'):
            self._parent = parent

        @property
        def loaded_spherical_roller_bearing_element(self):
            return self._parent._cast(_2024.LoadedSphericalRollerBearingElement)

        @property
        def loaded_roller_bearing_element(self):
            from mastapy.bearings.bearing_results.rolling import _2013
            
            return self._parent._cast(_2013.LoadedRollerBearingElement)

        @property
        def loaded_element(self):
            from mastapy.bearings.bearing_results.rolling import _1999
            
            return self._parent._cast(_1999.LoadedElement)

        @property
        def loaded_spherical_thrust_roller_bearing_element(self) -> 'LoadedSphericalThrustRollerBearingElement':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'LoadedSphericalThrustRollerBearingElement.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'LoadedSphericalThrustRollerBearingElement._Cast_LoadedSphericalThrustRollerBearingElement':
        return self._Cast_LoadedSphericalThrustRollerBearingElement(self)
