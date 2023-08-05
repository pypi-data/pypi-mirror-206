"""_1970.py

LoadedAngularContactThrustBallBearingElement
"""
from mastapy.bearings.bearing_results.rolling import _1967
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_ANGULAR_CONTACT_THRUST_BALL_BEARING_ELEMENT = python_net_import('SMT.MastaAPI.Bearings.BearingResults.Rolling', 'LoadedAngularContactThrustBallBearingElement')


__docformat__ = 'restructuredtext en'
__all__ = ('LoadedAngularContactThrustBallBearingElement',)


class LoadedAngularContactThrustBallBearingElement(_1967.LoadedAngularContactBallBearingElement):
    """LoadedAngularContactThrustBallBearingElement

    This is a mastapy class.
    """

    TYPE = _LOADED_ANGULAR_CONTACT_THRUST_BALL_BEARING_ELEMENT

    class _Cast_LoadedAngularContactThrustBallBearingElement:
        """Special nested class for casting LoadedAngularContactThrustBallBearingElement to subclasses."""

        def __init__(self, parent: 'LoadedAngularContactThrustBallBearingElement'):
            self._parent = parent

        @property
        def loaded_angular_contact_ball_bearing_element(self):
            return self._parent._cast(_1967.LoadedAngularContactBallBearingElement)

        @property
        def loaded_ball_bearing_element(self):
            from mastapy.bearings.bearing_results.rolling import _1985
            
            return self._parent._cast(_1985.LoadedBallBearingElement)

        @property
        def loaded_element(self):
            from mastapy.bearings.bearing_results.rolling import _1999
            
            return self._parent._cast(_1999.LoadedElement)

        @property
        def loaded_angular_contact_thrust_ball_bearing_element(self) -> 'LoadedAngularContactThrustBallBearingElement':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'LoadedAngularContactThrustBallBearingElement.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'LoadedAngularContactThrustBallBearingElement._Cast_LoadedAngularContactThrustBallBearingElement':
        return self._Cast_LoadedAngularContactThrustBallBearingElement(self)
