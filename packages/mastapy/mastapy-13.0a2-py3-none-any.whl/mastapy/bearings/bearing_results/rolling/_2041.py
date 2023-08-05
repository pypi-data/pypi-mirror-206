"""_2041.py

LoadedToroidalRollerBearingElement
"""
from mastapy._internal import constructor
from mastapy.bearings.bearing_results.rolling import _2013
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_TOROIDAL_ROLLER_BEARING_ELEMENT = python_net_import('SMT.MastaAPI.Bearings.BearingResults.Rolling', 'LoadedToroidalRollerBearingElement')


__docformat__ = 'restructuredtext en'
__all__ = ('LoadedToroidalRollerBearingElement',)


class LoadedToroidalRollerBearingElement(_2013.LoadedRollerBearingElement):
    """LoadedToroidalRollerBearingElement

    This is a mastapy class.
    """

    TYPE = _LOADED_TOROIDAL_ROLLER_BEARING_ELEMENT

    class _Cast_LoadedToroidalRollerBearingElement:
        """Special nested class for casting LoadedToroidalRollerBearingElement to subclasses."""

        def __init__(self, parent: 'LoadedToroidalRollerBearingElement'):
            self._parent = parent

        @property
        def loaded_roller_bearing_element(self):
            return self._parent._cast(_2013.LoadedRollerBearingElement)

        @property
        def loaded_element(self):
            from mastapy.bearings.bearing_results.rolling import _1999
            
            return self._parent._cast(_1999.LoadedElement)

        @property
        def loaded_toroidal_roller_bearing_element(self) -> 'LoadedToroidalRollerBearingElement':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'LoadedToroidalRollerBearingElement.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def contact_angle(self) -> 'float':
        """float: 'ContactAngle' is the original name of this property."""

        temp = self.wrapped.ContactAngle

        if temp is None:
            return 0.0

        return temp

    @contact_angle.setter
    def contact_angle(self, value: 'float'):
        self.wrapped.ContactAngle = float(value) if value else 0.0

    @property
    def cast_to(self) -> 'LoadedToroidalRollerBearingElement._Cast_LoadedToroidalRollerBearingElement':
        return self._Cast_LoadedToroidalRollerBearingElement(self)
