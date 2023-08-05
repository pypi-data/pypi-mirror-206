"""_1111.py

LinearCylindricalGearTriangularEndModification
"""
from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1123
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LINEAR_CYLINDRICAL_GEAR_TRIANGULAR_END_MODIFICATION = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Cylindrical.MicroGeometry', 'LinearCylindricalGearTriangularEndModification')


__docformat__ = 'restructuredtext en'
__all__ = ('LinearCylindricalGearTriangularEndModification',)


class LinearCylindricalGearTriangularEndModification(_1123.SingleCylindricalGearTriangularEndModification):
    """LinearCylindricalGearTriangularEndModification

    This is a mastapy class.
    """

    TYPE = _LINEAR_CYLINDRICAL_GEAR_TRIANGULAR_END_MODIFICATION

    class _Cast_LinearCylindricalGearTriangularEndModification:
        """Special nested class for casting LinearCylindricalGearTriangularEndModification to subclasses."""

        def __init__(self, parent: 'LinearCylindricalGearTriangularEndModification'):
            self._parent = parent

        @property
        def single_cylindrical_gear_triangular_end_modification(self):
            return self._parent._cast(_1123.SingleCylindricalGearTriangularEndModification)

        @property
        def linear_cylindrical_gear_triangular_end_modification(self) -> 'LinearCylindricalGearTriangularEndModification':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'LinearCylindricalGearTriangularEndModification.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'LinearCylindricalGearTriangularEndModification._Cast_LinearCylindricalGearTriangularEndModification':
        return self._Cast_LinearCylindricalGearTriangularEndModification(self)
