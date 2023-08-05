"""_1004.py

CylindricalGearBasicRackFlank
"""
from mastapy.gears.gear_designs.cylindrical import _1002
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_BASIC_RACK_FLANK = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Cylindrical', 'CylindricalGearBasicRackFlank')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearBasicRackFlank',)


class CylindricalGearBasicRackFlank(_1002.CylindricalGearAbstractRackFlank):
    """CylindricalGearBasicRackFlank

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_BASIC_RACK_FLANK

    class _Cast_CylindricalGearBasicRackFlank:
        """Special nested class for casting CylindricalGearBasicRackFlank to subclasses."""

        def __init__(self, parent: 'CylindricalGearBasicRackFlank'):
            self._parent = parent

        @property
        def cylindrical_gear_abstract_rack_flank(self):
            return self._parent._cast(_1002.CylindricalGearAbstractRackFlank)

        @property
        def standard_rack_flank(self):
            from mastapy.gears.gear_designs.cylindrical import _1071
            
            return self._parent._cast(_1071.StandardRackFlank)

        @property
        def cylindrical_gear_basic_rack_flank(self) -> 'CylindricalGearBasicRackFlank':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CylindricalGearBasicRackFlank.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'CylindricalGearBasicRackFlank._Cast_CylindricalGearBasicRackFlank':
        return self._Cast_CylindricalGearBasicRackFlank(self)
