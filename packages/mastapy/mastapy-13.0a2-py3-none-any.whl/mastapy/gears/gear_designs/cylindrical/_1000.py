"""_1000.py

CrossedAxisCylindricalGearPairPointContact
"""
from mastapy.gears.gear_designs.cylindrical import _998
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CROSSED_AXIS_CYLINDRICAL_GEAR_PAIR_POINT_CONTACT = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Cylindrical', 'CrossedAxisCylindricalGearPairPointContact')


__docformat__ = 'restructuredtext en'
__all__ = ('CrossedAxisCylindricalGearPairPointContact',)


class CrossedAxisCylindricalGearPairPointContact(_998.CrossedAxisCylindricalGearPair):
    """CrossedAxisCylindricalGearPairPointContact

    This is a mastapy class.
    """

    TYPE = _CROSSED_AXIS_CYLINDRICAL_GEAR_PAIR_POINT_CONTACT

    class _Cast_CrossedAxisCylindricalGearPairPointContact:
        """Special nested class for casting CrossedAxisCylindricalGearPairPointContact to subclasses."""

        def __init__(self, parent: 'CrossedAxisCylindricalGearPairPointContact'):
            self._parent = parent

        @property
        def crossed_axis_cylindrical_gear_pair(self):
            return self._parent._cast(_998.CrossedAxisCylindricalGearPair)

        @property
        def crossed_axis_cylindrical_gear_pair_point_contact(self) -> 'CrossedAxisCylindricalGearPairPointContact':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CrossedAxisCylindricalGearPairPointContact.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'CrossedAxisCylindricalGearPairPointContact._Cast_CrossedAxisCylindricalGearPairPointContact':
        return self._Cast_CrossedAxisCylindricalGearPairPointContact(self)
