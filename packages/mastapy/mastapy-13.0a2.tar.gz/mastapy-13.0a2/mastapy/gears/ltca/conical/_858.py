"""_858.py

ConicalGearBendingStiffness
"""
from mastapy.gears.ltca import _828
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_BENDING_STIFFNESS = python_net_import('SMT.MastaAPI.Gears.LTCA.Conical', 'ConicalGearBendingStiffness')


__docformat__ = 'restructuredtext en'
__all__ = ('ConicalGearBendingStiffness',)


class ConicalGearBendingStiffness(_828.GearBendingStiffness):
    """ConicalGearBendingStiffness

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_BENDING_STIFFNESS

    class _Cast_ConicalGearBendingStiffness:
        """Special nested class for casting ConicalGearBendingStiffness to subclasses."""

        def __init__(self, parent: 'ConicalGearBendingStiffness'):
            self._parent = parent

        @property
        def gear_bending_stiffness(self):
            return self._parent._cast(_828.GearBendingStiffness)

        @property
        def gear_stiffness(self):
            from mastapy.gears.ltca import _842
            
            return self._parent._cast(_842.GearStiffness)

        @property
        def fe_stiffness(self):
            from mastapy.nodal_analysis import _66
            
            return self._parent._cast(_66.FEStiffness)

        @property
        def conical_gear_bending_stiffness(self) -> 'ConicalGearBendingStiffness':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConicalGearBendingStiffness.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'ConicalGearBendingStiffness._Cast_ConicalGearBendingStiffness':
        return self._Cast_ConicalGearBendingStiffness(self)
