"""_507.py

ISO63361996MeshSingleFlankRating
"""
from mastapy._internal import constructor
from mastapy.gears.rating.cylindrical.iso6336 import _515
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ISO63361996_MESH_SINGLE_FLANK_RATING = python_net_import('SMT.MastaAPI.Gears.Rating.Cylindrical.ISO6336', 'ISO63361996MeshSingleFlankRating')


__docformat__ = 'restructuredtext en'
__all__ = ('ISO63361996MeshSingleFlankRating',)


class ISO63361996MeshSingleFlankRating(_515.ISO6336AbstractMetalMeshSingleFlankRating):
    """ISO63361996MeshSingleFlankRating

    This is a mastapy class.
    """

    TYPE = _ISO63361996_MESH_SINGLE_FLANK_RATING

    class _Cast_ISO63361996MeshSingleFlankRating:
        """Special nested class for casting ISO63361996MeshSingleFlankRating to subclasses."""

        def __init__(self, parent: 'ISO63361996MeshSingleFlankRating'):
            self._parent = parent

        @property
        def iso6336_abstract_metal_mesh_single_flank_rating(self):
            return self._parent._cast(_515.ISO6336AbstractMetalMeshSingleFlankRating)

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
        def din3990_mesh_single_flank_rating(self):
            from mastapy.gears.rating.cylindrical.din3990 import _528
            
            return self._parent._cast(_528.DIN3990MeshSingleFlankRating)

        @property
        def iso63361996_mesh_single_flank_rating(self) -> 'ISO63361996MeshSingleFlankRating':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ISO63361996MeshSingleFlankRating.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def helix_angle_factor_contact(self) -> 'float':
        """float: 'HelixAngleFactorContact' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HelixAngleFactorContact

        if temp is None:
            return 0.0

        return temp

    @property
    def rating_standard_name(self) -> 'str':
        """str: 'RatingStandardName' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RatingStandardName

        if temp is None:
            return ''

        return temp

    @property
    def transverse_load_factor_bending(self) -> 'float':
        """float: 'TransverseLoadFactorBending' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TransverseLoadFactorBending

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self) -> 'ISO63361996MeshSingleFlankRating._Cast_ISO63361996MeshSingleFlankRating':
        return self._Cast_ISO63361996MeshSingleFlankRating(self)
