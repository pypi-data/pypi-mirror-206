"""_1996.py

LoadedDeepGrooveBallBearingElement
"""
from mastapy.bearings.bearing_results.rolling import _1985
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_DEEP_GROOVE_BALL_BEARING_ELEMENT = python_net_import('SMT.MastaAPI.Bearings.BearingResults.Rolling', 'LoadedDeepGrooveBallBearingElement')


__docformat__ = 'restructuredtext en'
__all__ = ('LoadedDeepGrooveBallBearingElement',)


class LoadedDeepGrooveBallBearingElement(_1985.LoadedBallBearingElement):
    """LoadedDeepGrooveBallBearingElement

    This is a mastapy class.
    """

    TYPE = _LOADED_DEEP_GROOVE_BALL_BEARING_ELEMENT

    class _Cast_LoadedDeepGrooveBallBearingElement:
        """Special nested class for casting LoadedDeepGrooveBallBearingElement to subclasses."""

        def __init__(self, parent: 'LoadedDeepGrooveBallBearingElement'):
            self._parent = parent

        @property
        def loaded_ball_bearing_element(self):
            return self._parent._cast(_1985.LoadedBallBearingElement)

        @property
        def loaded_element(self):
            from mastapy.bearings.bearing_results.rolling import _1999
            
            return self._parent._cast(_1999.LoadedElement)

        @property
        def loaded_deep_groove_ball_bearing_element(self) -> 'LoadedDeepGrooveBallBearingElement':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'LoadedDeepGrooveBallBearingElement.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'LoadedDeepGrooveBallBearingElement._Cast_LoadedDeepGrooveBallBearingElement':
        return self._Cast_LoadedDeepGrooveBallBearingElement(self)
