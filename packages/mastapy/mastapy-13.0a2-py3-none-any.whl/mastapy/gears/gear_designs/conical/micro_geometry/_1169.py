"""_1169.py

ConicalGearProfileModification
"""
from mastapy.gears.micro_geometry import _577
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_PROFILE_MODIFICATION = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Conical.MicroGeometry', 'ConicalGearProfileModification')


__docformat__ = 'restructuredtext en'
__all__ = ('ConicalGearProfileModification',)


class ConicalGearProfileModification(_577.ProfileModification):
    """ConicalGearProfileModification

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_PROFILE_MODIFICATION

    class _Cast_ConicalGearProfileModification:
        """Special nested class for casting ConicalGearProfileModification to subclasses."""

        def __init__(self, parent: 'ConicalGearProfileModification'):
            self._parent = parent

        @property
        def profile_modification(self):
            return self._parent._cast(_577.ProfileModification)

        @property
        def modification(self):
            from mastapy.gears.micro_geometry import _574
            
            return self._parent._cast(_574.Modification)

        @property
        def conical_gear_profile_modification(self) -> 'ConicalGearProfileModification':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConicalGearProfileModification.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'ConicalGearProfileModification._Cast_ConicalGearProfileModification':
        return self._Cast_ConicalGearProfileModification(self)
