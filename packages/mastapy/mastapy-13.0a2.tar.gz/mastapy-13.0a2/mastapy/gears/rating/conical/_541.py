"""_541.py

ConicalMeshSingleFlankRating
"""
from mastapy.gears.rating import _362
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_MESH_SINGLE_FLANK_RATING = python_net_import('SMT.MastaAPI.Gears.Rating.Conical', 'ConicalMeshSingleFlankRating')


__docformat__ = 'restructuredtext en'
__all__ = ('ConicalMeshSingleFlankRating',)


class ConicalMeshSingleFlankRating(_362.MeshSingleFlankRating):
    """ConicalMeshSingleFlankRating

    This is a mastapy class.
    """

    TYPE = _CONICAL_MESH_SINGLE_FLANK_RATING

    class _Cast_ConicalMeshSingleFlankRating:
        """Special nested class for casting ConicalMeshSingleFlankRating to subclasses."""

        def __init__(self, parent: 'ConicalMeshSingleFlankRating'):
            self._parent = parent

        @property
        def mesh_single_flank_rating(self):
            return self._parent._cast(_362.MeshSingleFlankRating)

        @property
        def iso10300_mesh_single_flank_rating(self):
            from mastapy.gears.rating.iso_10300 import _418
            
            return self._parent._cast(_418.ISO10300MeshSingleFlankRating)

        @property
        def iso_10300_mesh_single_flank_rating_bevel_method_b2(self):
            from mastapy.gears.rating.iso_10300 import _419
            
            return self._parent._cast(_419.Iso10300MeshSingleFlankRatingBevelMethodB2)

        @property
        def iso_10300_mesh_single_flank_rating_hypoid_method_b2(self):
            from mastapy.gears.rating.iso_10300 import _420
            
            return self._parent._cast(_420.Iso10300MeshSingleFlankRatingHypoidMethodB2)

        @property
        def iso10300_mesh_single_flank_rating_method_b1(self):
            from mastapy.gears.rating.iso_10300 import _421
            
            return self._parent._cast(_421.ISO10300MeshSingleFlankRatingMethodB1)

        @property
        def iso10300_mesh_single_flank_rating_method_b2(self):
            from mastapy.gears.rating.iso_10300 import _422
            
            return self._parent._cast(_422.ISO10300MeshSingleFlankRatingMethodB2)

        @property
        def gleason_hypoid_mesh_single_flank_rating(self):
            from mastapy.gears.rating.hypoid.standards import _439
            
            return self._parent._cast(_439.GleasonHypoidMeshSingleFlankRating)

        @property
        def agma_spiral_bevel_mesh_single_flank_rating(self):
            from mastapy.gears.rating.bevel.standards import _553
            
            return self._parent._cast(_553.AGMASpiralBevelMeshSingleFlankRating)

        @property
        def gleason_spiral_bevel_mesh_single_flank_rating(self):
            from mastapy.gears.rating.bevel.standards import _555
            
            return self._parent._cast(_555.GleasonSpiralBevelMeshSingleFlankRating)

        @property
        def spiral_bevel_mesh_single_flank_rating(self):
            from mastapy.gears.rating.bevel.standards import _557
            
            return self._parent._cast(_557.SpiralBevelMeshSingleFlankRating)

        @property
        def conical_mesh_single_flank_rating(self) -> 'ConicalMeshSingleFlankRating':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConicalMeshSingleFlankRating.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'ConicalMeshSingleFlankRating._Cast_ConicalMeshSingleFlankRating':
        return self._Cast_ConicalMeshSingleFlankRating(self)
