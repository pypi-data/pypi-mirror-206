"""_489.py

PlasticPlasticVDI2736MeshSingleFlankRating
"""
from mastapy.gears.rating.cylindrical.plastic_vdi2736 import _487
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLASTIC_PLASTIC_VDI2736_MESH_SINGLE_FLANK_RATING = python_net_import('SMT.MastaAPI.Gears.Rating.Cylindrical.PlasticVDI2736', 'PlasticPlasticVDI2736MeshSingleFlankRating')


__docformat__ = 'restructuredtext en'
__all__ = ('PlasticPlasticVDI2736MeshSingleFlankRating',)


class PlasticPlasticVDI2736MeshSingleFlankRating(_487.PlasticGearVDI2736AbstractMeshSingleFlankRating):
    """PlasticPlasticVDI2736MeshSingleFlankRating

    This is a mastapy class.
    """

    TYPE = _PLASTIC_PLASTIC_VDI2736_MESH_SINGLE_FLANK_RATING

    class _Cast_PlasticPlasticVDI2736MeshSingleFlankRating:
        """Special nested class for casting PlasticPlasticVDI2736MeshSingleFlankRating to subclasses."""

        def __init__(self, parent: 'PlasticPlasticVDI2736MeshSingleFlankRating'):
            self._parent = parent

        @property
        def plastic_gear_vdi2736_abstract_mesh_single_flank_rating(self):
            return self._parent._cast(_487.PlasticGearVDI2736AbstractMeshSingleFlankRating)

        @property
        def iso6336_abstract_mesh_single_flank_rating(self):
            from mastapy.gears.rating.cylindrical.iso6336 import _513
            
            return self._parent._cast(_513.ISO6336AbstractMeshSingleFlankRating)

        @property
        def cylindrical_mesh_single_flank_rating(self):
            from mastapy.gears.rating.cylindrical import _463
            
            return self._parent._cast(_463.CylindricalMeshSingleFlankRating)

        @property
        def mesh_single_flank_rating(self):
            from mastapy.gears.rating import _362
            
            return self._parent._cast(_362.MeshSingleFlankRating)

        @property
        def plastic_plastic_vdi2736_mesh_single_flank_rating(self) -> 'PlasticPlasticVDI2736MeshSingleFlankRating':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'PlasticPlasticVDI2736MeshSingleFlankRating.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'PlasticPlasticVDI2736MeshSingleFlankRating._Cast_PlasticPlasticVDI2736MeshSingleFlankRating':
        return self._Cast_PlasticPlasticVDI2736MeshSingleFlankRating(self)
