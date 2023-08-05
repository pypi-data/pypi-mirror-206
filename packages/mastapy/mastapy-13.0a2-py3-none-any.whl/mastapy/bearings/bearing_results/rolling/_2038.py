"""_2038.py

LoadedThrustBallBearingElement
"""
from mastapy.bearings.bearing_results.rolling import _1985
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_THRUST_BALL_BEARING_ELEMENT = python_net_import('SMT.MastaAPI.Bearings.BearingResults.Rolling', 'LoadedThrustBallBearingElement')


__docformat__ = 'restructuredtext en'
__all__ = ('LoadedThrustBallBearingElement',)


class LoadedThrustBallBearingElement(_1985.LoadedBallBearingElement):
    """LoadedThrustBallBearingElement

    This is a mastapy class.
    """

    TYPE = _LOADED_THRUST_BALL_BEARING_ELEMENT

    class _Cast_LoadedThrustBallBearingElement:
        """Special nested class for casting LoadedThrustBallBearingElement to subclasses."""

        def __init__(self, parent: 'LoadedThrustBallBearingElement'):
            self._parent = parent

        @property
        def loaded_ball_bearing_element(self):
            return self._parent._cast(_1985.LoadedBallBearingElement)

        @property
        def loaded_element(self):
            from mastapy.bearings.bearing_results.rolling import _1999
            
            return self._parent._cast(_1999.LoadedElement)

        @property
        def loaded_thrust_ball_bearing_element(self) -> 'LoadedThrustBallBearingElement':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'LoadedThrustBallBearingElement.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'LoadedThrustBallBearingElement._Cast_LoadedThrustBallBearingElement':
        return self._Cast_LoadedThrustBallBearingElement(self)
