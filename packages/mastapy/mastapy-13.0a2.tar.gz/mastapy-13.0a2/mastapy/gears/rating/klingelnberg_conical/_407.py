"""_407.py

KlingelnbergCycloPalloidConicalGearMeshRating
"""
from mastapy.gears.rating.conical import _534
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_MESH_RATING = python_net_import('SMT.MastaAPI.Gears.Rating.KlingelnbergConical', 'KlingelnbergCycloPalloidConicalGearMeshRating')


__docformat__ = 'restructuredtext en'
__all__ = ('KlingelnbergCycloPalloidConicalGearMeshRating',)


class KlingelnbergCycloPalloidConicalGearMeshRating(_534.ConicalGearMeshRating):
    """KlingelnbergCycloPalloidConicalGearMeshRating

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_MESH_RATING

    class _Cast_KlingelnbergCycloPalloidConicalGearMeshRating:
        """Special nested class for casting KlingelnbergCycloPalloidConicalGearMeshRating to subclasses."""

        def __init__(self, parent: 'KlingelnbergCycloPalloidConicalGearMeshRating'):
            self._parent = parent

        @property
        def conical_gear_mesh_rating(self):
            return self._parent._cast(_534.ConicalGearMeshRating)

        @property
        def gear_mesh_rating(self):
            from mastapy.gears.rating import _356
            
            return self._parent._cast(_356.GearMeshRating)

        @property
        def abstract_gear_mesh_rating(self):
            from mastapy.gears.rating import _349
            
            return self._parent._cast(_349.AbstractGearMeshRating)

        @property
        def abstract_gear_mesh_analysis(self):
            from mastapy.gears.analysis import _1210
            
            return self._parent._cast(_1210.AbstractGearMeshAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_rating(self):
            from mastapy.gears.rating.klingelnberg_spiral_bevel import _401
            
            return self._parent._cast(_401.KlingelnbergCycloPalloidSpiralBevelGearMeshRating)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_rating(self):
            from mastapy.gears.rating.klingelnberg_hypoid import _404
            
            return self._parent._cast(_404.KlingelnbergCycloPalloidHypoidGearMeshRating)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_rating(self) -> 'KlingelnbergCycloPalloidConicalGearMeshRating':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'KlingelnbergCycloPalloidConicalGearMeshRating.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'KlingelnbergCycloPalloidConicalGearMeshRating._Cast_KlingelnbergCycloPalloidConicalGearMeshRating':
        return self._Cast_KlingelnbergCycloPalloidConicalGearMeshRating(self)
