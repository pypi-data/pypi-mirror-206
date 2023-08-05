"""_1967.py

LoadedAngularContactBallBearingElement
"""
from mastapy.bearings.bearing_results.rolling import _1985
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_ANGULAR_CONTACT_BALL_BEARING_ELEMENT = python_net_import('SMT.MastaAPI.Bearings.BearingResults.Rolling', 'LoadedAngularContactBallBearingElement')


__docformat__ = 'restructuredtext en'
__all__ = ('LoadedAngularContactBallBearingElement',)


class LoadedAngularContactBallBearingElement(_1985.LoadedBallBearingElement):
    """LoadedAngularContactBallBearingElement

    This is a mastapy class.
    """

    TYPE = _LOADED_ANGULAR_CONTACT_BALL_BEARING_ELEMENT

    class _Cast_LoadedAngularContactBallBearingElement:
        """Special nested class for casting LoadedAngularContactBallBearingElement to subclasses."""

        def __init__(self, parent: 'LoadedAngularContactBallBearingElement'):
            self._parent = parent

        @property
        def loaded_ball_bearing_element(self):
            return self._parent._cast(_1985.LoadedBallBearingElement)

        @property
        def loaded_element(self):
            from mastapy.bearings.bearing_results.rolling import _1999
            
            return self._parent._cast(_1999.LoadedElement)

        @property
        def loaded_angular_contact_thrust_ball_bearing_element(self):
            from mastapy.bearings.bearing_results.rolling import _1970
            
            return self._parent._cast(_1970.LoadedAngularContactThrustBallBearingElement)

        @property
        def loaded_angular_contact_ball_bearing_element(self) -> 'LoadedAngularContactBallBearingElement':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'LoadedAngularContactBallBearingElement.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'LoadedAngularContactBallBearingElement._Cast_LoadedAngularContactBallBearingElement':
        return self._Cast_LoadedAngularContactBallBearingElement(self)
