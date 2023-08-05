"""_356.py

GearMeshRating
"""
from mastapy._internal import constructor
from mastapy.gears.load_case import _870
from mastapy.gears.rating import _349
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_MESH_RATING = python_net_import('SMT.MastaAPI.Gears.Rating', 'GearMeshRating')


__docformat__ = 'restructuredtext en'
__all__ = ('GearMeshRating',)


class GearMeshRating(_349.AbstractGearMeshRating):
    """GearMeshRating

    This is a mastapy class.
    """

    TYPE = _GEAR_MESH_RATING

    class _Cast_GearMeshRating:
        """Special nested class for casting GearMeshRating to subclasses."""

        def __init__(self, parent: 'GearMeshRating'):
            self._parent = parent

        @property
        def abstract_gear_mesh_rating(self):
            return self._parent._cast(_349.AbstractGearMeshRating)

        @property
        def abstract_gear_mesh_analysis(self):
            from mastapy.gears.analysis import _1210
            
            return self._parent._cast(_1210.AbstractGearMeshAnalysis)

        @property
        def zerol_bevel_gear_mesh_rating(self):
            from mastapy.gears.rating.zerol_bevel import _365
            
            return self._parent._cast(_365.ZerolBevelGearMeshRating)

        @property
        def worm_gear_mesh_rating(self):
            from mastapy.gears.rating.worm import _369
            
            return self._parent._cast(_369.WormGearMeshRating)

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
        def face_gear_mesh_rating(self):
            from mastapy.gears.rating.face import _443
            
            return self._parent._cast(_443.FaceGearMeshRating)

        @property
        def cylindrical_gear_mesh_rating(self):
            from mastapy.gears.rating.cylindrical import _454
            
            return self._parent._cast(_454.CylindricalGearMeshRating)

        @property
        def conical_gear_mesh_rating(self):
            from mastapy.gears.rating.conical import _534
            
            return self._parent._cast(_534.ConicalGearMeshRating)

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
        def gear_mesh_rating(self) -> 'GearMeshRating':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GearMeshRating.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def driving_gear(self) -> 'str':
        """str: 'DrivingGear' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DrivingGear

        if temp is None:
            return ''

        return temp

    @property
    def energy_loss(self) -> 'float':
        """float: 'EnergyLoss' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.EnergyLoss

        if temp is None:
            return 0.0

        return temp

    @property
    def is_loaded(self) -> 'bool':
        """bool: 'IsLoaded' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.IsLoaded

        if temp is None:
            return False

        return temp

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
    def pinion_name(self) -> 'str':
        """str: 'PinionName' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PinionName

        if temp is None:
            return ''

        return temp

    @property
    def pinion_torque(self) -> 'float':
        """float: 'PinionTorque' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PinionTorque

        if temp is None:
            return 0.0

        return temp

    @property
    def signed_pinion_torque(self) -> 'float':
        """float: 'SignedPinionTorque' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SignedPinionTorque

        if temp is None:
            return 0.0

        return temp

    @property
    def signed_wheel_torque(self) -> 'float':
        """float: 'SignedWheelTorque' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SignedWheelTorque

        if temp is None:
            return 0.0

        return temp

    @property
    def total_energy(self) -> 'float':
        """float: 'TotalEnergy' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TotalEnergy

        if temp is None:
            return 0.0

        return temp

    @property
    def wheel_name(self) -> 'str':
        """str: 'WheelName' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WheelName

        if temp is None:
            return ''

        return temp

    @property
    def wheel_torque(self) -> 'float':
        """float: 'WheelTorque' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WheelTorque

        if temp is None:
            return 0.0

        return temp

    @property
    def mesh_load_case(self) -> '_870.MeshLoadCase':
        """MeshLoadCase: 'MeshLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeshLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'GearMeshRating._Cast_GearMeshRating':
        return self._Cast_GearMeshRating(self)
