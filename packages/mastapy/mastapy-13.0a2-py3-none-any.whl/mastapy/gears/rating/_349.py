"""_349.py

AbstractGearMeshRating
"""
from mastapy._internal import constructor
from mastapy.gears.analysis import _1210
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_GEAR_MESH_RATING = python_net_import('SMT.MastaAPI.Gears.Rating', 'AbstractGearMeshRating')


__docformat__ = 'restructuredtext en'
__all__ = ('AbstractGearMeshRating',)


class AbstractGearMeshRating(_1210.AbstractGearMeshAnalysis):
    """AbstractGearMeshRating

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_GEAR_MESH_RATING

    class _Cast_AbstractGearMeshRating:
        """Special nested class for casting AbstractGearMeshRating to subclasses."""

        def __init__(self, parent: 'AbstractGearMeshRating'):
            self._parent = parent

        @property
        def abstract_gear_mesh_analysis(self):
            return self._parent._cast(_1210.AbstractGearMeshAnalysis)

        @property
        def gear_mesh_rating(self):
            from mastapy.gears.rating import _356
            
            return self._parent._cast(_356.GearMeshRating)

        @property
        def mesh_duty_cycle_rating(self):
            from mastapy.gears.rating import _361
            
            return self._parent._cast(_361.MeshDutyCycleRating)

        @property
        def zerol_bevel_gear_mesh_rating(self):
            from mastapy.gears.rating.zerol_bevel import _365
            
            return self._parent._cast(_365.ZerolBevelGearMeshRating)

        @property
        def worm_gear_mesh_rating(self):
            from mastapy.gears.rating.worm import _369
            
            return self._parent._cast(_369.WormGearMeshRating)

        @property
        def worm_mesh_duty_cycle_rating(self):
            from mastapy.gears.rating.worm import _373
            
            return self._parent._cast(_373.WormMeshDutyCycleRating)

        @property
        def straight_bevel_gear_mesh_rating(self):
            from mastapy.gears.rating.straight_bevel import _391
            
            return self._parent._cast(_391.StraightBevelGearMeshRating)

        @property
        def straight_bevel_diff_gear_mesh_rating(self):
            from mastapy.gears.rating.straight_bevel_diff import _394
            
            return self._parent._cast(_394.StraightBevelDiffGearMeshRating)

        @property
        def spiral_bevel_gear_mesh_rating(self):
            from mastapy.gears.rating.spiral_bevel import _398
            
            return self._parent._cast(_398.SpiralBevelGearMeshRating)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_rating(self):
            from mastapy.gears.rating.klingelnberg_spiral_bevel import _401
            
            return self._parent._cast(_401.KlingelnbergCycloPalloidSpiralBevelGearMeshRating)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_rating(self):
            from mastapy.gears.rating.klingelnberg_hypoid import _404
            
            return self._parent._cast(_404.KlingelnbergCycloPalloidHypoidGearMeshRating)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_rating(self):
            from mastapy.gears.rating.klingelnberg_conical import _407
            
            return self._parent._cast(_407.KlingelnbergCycloPalloidConicalGearMeshRating)

        @property
        def hypoid_gear_mesh_rating(self):
            from mastapy.gears.rating.hypoid import _434
            
            return self._parent._cast(_434.HypoidGearMeshRating)

        @property
        def face_gear_mesh_duty_cycle_rating(self):
            from mastapy.gears.rating.face import _442
            
            return self._parent._cast(_442.FaceGearMeshDutyCycleRating)

        @property
        def face_gear_mesh_rating(self):
            from mastapy.gears.rating.face import _443
            
            return self._parent._cast(_443.FaceGearMeshRating)

        @property
        def cylindrical_gear_mesh_rating(self):
            from mastapy.gears.rating.cylindrical import _454
            
            return self._parent._cast(_454.CylindricalGearMeshRating)

        @property
        def cylindrical_mesh_duty_cycle_rating(self):
            from mastapy.gears.rating.cylindrical import _462
            
            return self._parent._cast(_462.CylindricalMeshDutyCycleRating)

        @property
        def conical_gear_mesh_rating(self):
            from mastapy.gears.rating.conical import _534
            
            return self._parent._cast(_534.ConicalGearMeshRating)

        @property
        def conical_mesh_duty_cycle_rating(self):
            from mastapy.gears.rating.conical import _539
            
            return self._parent._cast(_539.ConicalMeshDutyCycleRating)

        @property
        def concept_gear_mesh_duty_cycle_rating(self):
            from mastapy.gears.rating.concept import _544
            
            return self._parent._cast(_544.ConceptGearMeshDutyCycleRating)

        @property
        def concept_gear_mesh_rating(self):
            from mastapy.gears.rating.concept import _545
            
            return self._parent._cast(_545.ConceptGearMeshRating)

        @property
        def bevel_gear_mesh_rating(self):
            from mastapy.gears.rating.bevel import _549
            
            return self._parent._cast(_549.BevelGearMeshRating)

        @property
        def agma_gleason_conical_gear_mesh_rating(self):
            from mastapy.gears.rating.agma_gleason_conical import _560
            
            return self._parent._cast(_560.AGMAGleasonConicalGearMeshRating)

        @property
        def abstract_gear_mesh_rating(self) -> 'AbstractGearMeshRating':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AbstractGearMeshRating.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def mesh_efficiency(self) -> 'float':
        """float: 'MeshEfficiency' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeshEfficiency

        if temp is None:
            return 0.0

        return temp

    @property
    def normalized_safety_factor_for_fatigue(self) -> 'float':
        """float: 'NormalizedSafetyFactorForFatigue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NormalizedSafetyFactorForFatigue

        if temp is None:
            return 0.0

        return temp

    @property
    def normalized_safety_factor_for_static(self) -> 'float':
        """float: 'NormalizedSafetyFactorForStatic' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NormalizedSafetyFactorForStatic

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self) -> 'AbstractGearMeshRating._Cast_AbstractGearMeshRating':
        return self._Cast_AbstractGearMeshRating(self)
