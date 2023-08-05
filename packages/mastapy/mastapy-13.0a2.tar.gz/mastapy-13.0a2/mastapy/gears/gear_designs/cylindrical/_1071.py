"""_1071.py

StandardRackFlank
"""
from mastapy.gears.gear_designs.cylindrical import _1004
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STANDARD_RACK_FLANK = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Cylindrical', 'StandardRackFlank')


__docformat__ = 'restructuredtext en'
__all__ = ('StandardRackFlank',)


class StandardRackFlank(_1004.CylindricalGearBasicRackFlank):
    """StandardRackFlank

    This is a mastapy class.
    """

    TYPE = _STANDARD_RACK_FLANK

    class _Cast_StandardRackFlank:
        """Special nested class for casting StandardRackFlank to subclasses."""

        def __init__(self, parent: 'StandardRackFlank'):
            self._parent = parent

        @property
        def cylindrical_gear_basic_rack_flank(self):
            return self._parent._cast(_1004.CylindricalGearBasicRackFlank)

        @property
        def cylindrical_gear_abstract_rack_flank(self):
            from mastapy.gears.gear_designs.cylindrical import _1002
            
            return self._parent._cast(_1002.CylindricalGearAbstractRackFlank)

        @property
        def standard_rack_flank(self) -> 'StandardRackFlank':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'StandardRackFlank.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'StandardRackFlank._Cast_StandardRackFlank':
        return self._Cast_StandardRackFlank(self)
