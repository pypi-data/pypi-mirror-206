"""_511.py

ISO63362019MeshSingleFlankRating
"""
from mastapy._internal import constructor
from mastapy.gears.rating.cylindrical.iso6336 import _509
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ISO63362019_MESH_SINGLE_FLANK_RATING = python_net_import('SMT.MastaAPI.Gears.Rating.Cylindrical.ISO6336', 'ISO63362019MeshSingleFlankRating')


__docformat__ = 'restructuredtext en'
__all__ = ('ISO63362019MeshSingleFlankRating',)


class ISO63362019MeshSingleFlankRating(_509.ISO63362006MeshSingleFlankRating):
    """ISO63362019MeshSingleFlankRating

    This is a mastapy class.
    """

    TYPE = _ISO63362019_MESH_SINGLE_FLANK_RATING

    class _Cast_ISO63362019MeshSingleFlankRating:
        """Special nested class for casting ISO63362019MeshSingleFlankRating to subclasses."""

        def __init__(self, parent: 'ISO63362019MeshSingleFlankRating'):
            self._parent = parent

        @property
        def iso63362006_mesh_single_flank_rating(self):
            return self._parent._cast(_509.ISO63362006MeshSingleFlankRating)

        @property
        def iso6336_abstract_metal_mesh_single_flank_rating(self):
            from mastapy.gears.rating.cylindrical.iso6336 import _515
            
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
        def iso63362019_mesh_single_flank_rating(self) -> 'ISO63362019MeshSingleFlankRating':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ISO63362019MeshSingleFlankRating.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def micro_geometry_factor(self) -> 'float':
        """float: 'MicroGeometryFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MicroGeometryFactor

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
    def cast_to(self) -> 'ISO63362019MeshSingleFlankRating._Cast_ISO63362019MeshSingleFlankRating':
        return self._Cast_ISO63362019MeshSingleFlankRating(self)
