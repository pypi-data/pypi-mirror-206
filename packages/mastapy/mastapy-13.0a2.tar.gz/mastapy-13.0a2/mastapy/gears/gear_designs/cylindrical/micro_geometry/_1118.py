"""_1118.py

ParabolicCylindricalGearTriangularEndModification
"""
from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1123
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PARABOLIC_CYLINDRICAL_GEAR_TRIANGULAR_END_MODIFICATION = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Cylindrical.MicroGeometry', 'ParabolicCylindricalGearTriangularEndModification')


__docformat__ = 'restructuredtext en'
__all__ = ('ParabolicCylindricalGearTriangularEndModification',)


class ParabolicCylindricalGearTriangularEndModification(_1123.SingleCylindricalGearTriangularEndModification):
    """ParabolicCylindricalGearTriangularEndModification

    This is a mastapy class.
    """

    TYPE = _PARABOLIC_CYLINDRICAL_GEAR_TRIANGULAR_END_MODIFICATION

    class _Cast_ParabolicCylindricalGearTriangularEndModification:
        """Special nested class for casting ParabolicCylindricalGearTriangularEndModification to subclasses."""

        def __init__(self, parent: 'ParabolicCylindricalGearTriangularEndModification'):
            self._parent = parent

        @property
        def single_cylindrical_gear_triangular_end_modification(self):
            return self._parent._cast(_1123.SingleCylindricalGearTriangularEndModification)

        @property
        def parabolic_cylindrical_gear_triangular_end_modification(self) -> 'ParabolicCylindricalGearTriangularEndModification':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ParabolicCylindricalGearTriangularEndModification.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'ParabolicCylindricalGearTriangularEndModification._Cast_ParabolicCylindricalGearTriangularEndModification':
        return self._Cast_ParabolicCylindricalGearTriangularEndModification(self)
