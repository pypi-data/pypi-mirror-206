"""_2035.py

LoadedThreePointContactBallBearingElement
"""
from mastapy.bearings.bearing_results.rolling import _2004
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_THREE_POINT_CONTACT_BALL_BEARING_ELEMENT = python_net_import('SMT.MastaAPI.Bearings.BearingResults.Rolling', 'LoadedThreePointContactBallBearingElement')


__docformat__ = 'restructuredtext en'
__all__ = ('LoadedThreePointContactBallBearingElement',)


class LoadedThreePointContactBallBearingElement(_2004.LoadedMultiPointContactBallBearingElement):
    """LoadedThreePointContactBallBearingElement

    This is a mastapy class.
    """

    TYPE = _LOADED_THREE_POINT_CONTACT_BALL_BEARING_ELEMENT

    class _Cast_LoadedThreePointContactBallBearingElement:
        """Special nested class for casting LoadedThreePointContactBallBearingElement to subclasses."""

        def __init__(self, parent: 'LoadedThreePointContactBallBearingElement'):
            self._parent = parent

        @property
        def loaded_multi_point_contact_ball_bearing_element(self):
            return self._parent._cast(_2004.LoadedMultiPointContactBallBearingElement)

        @property
        def loaded_ball_bearing_element(self):
            from mastapy.bearings.bearing_results.rolling import _1985
            
            return self._parent._cast(_1985.LoadedBallBearingElement)

        @property
        def loaded_element(self):
            from mastapy.bearings.bearing_results.rolling import _1999
            
            return self._parent._cast(_1999.LoadedElement)

        @property
        def loaded_three_point_contact_ball_bearing_element(self) -> 'LoadedThreePointContactBallBearingElement':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'LoadedThreePointContactBallBearingElement.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'LoadedThreePointContactBallBearingElement._Cast_LoadedThreePointContactBallBearingElement':
        return self._Cast_LoadedThreePointContactBallBearingElement(self)
