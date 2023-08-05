"""_944.py

GearMeshDesign
"""
from mastapy._internal import constructor
from mastapy.gears.gear_designs import _942, _943
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_MESH_DESIGN = python_net_import('SMT.MastaAPI.Gears.GearDesigns', 'GearMeshDesign')


__docformat__ = 'restructuredtext en'
__all__ = ('GearMeshDesign',)


class GearMeshDesign(_943.GearDesignComponent):
    """GearMeshDesign

    This is a mastapy class.
    """

    TYPE = _GEAR_MESH_DESIGN

    class _Cast_GearMeshDesign:
        """Special nested class for casting GearMeshDesign to subclasses."""

        def __init__(self, parent: 'GearMeshDesign'):
            self._parent = parent

        @property
        def gear_design_component(self):
            return self._parent._cast(_943.GearDesignComponent)

        @property
        def zerol_bevel_gear_mesh_design(self):
            from mastapy.gears.gear_designs.zerol_bevel import _948
            
            return self._parent._cast(_948.ZerolBevelGearMeshDesign)

        @property
        def worm_gear_mesh_design(self):
            from mastapy.gears.gear_designs.worm import _953
            
            return self._parent._cast(_953.WormGearMeshDesign)

        @property
        def straight_bevel_gear_mesh_design(self):
            from mastapy.gears.gear_designs.straight_bevel import _957
            
            return self._parent._cast(_957.StraightBevelGearMeshDesign)

        @property
        def straight_bevel_diff_gear_mesh_design(self):
            from mastapy.gears.gear_designs.straight_bevel_diff import _961
            
            return self._parent._cast(_961.StraightBevelDiffGearMeshDesign)

        @property
        def spiral_bevel_gear_mesh_design(self):
            from mastapy.gears.gear_designs.spiral_bevel import _965
            
            return self._parent._cast(_965.SpiralBevelGearMeshDesign)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_design(self):
            from mastapy.gears.gear_designs.klingelnberg_spiral_bevel import _969
            
            return self._parent._cast(_969.KlingelnbergCycloPalloidSpiralBevelGearMeshDesign)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_design(self):
            from mastapy.gears.gear_designs.klingelnberg_hypoid import _973
            
            return self._parent._cast(_973.KlingelnbergCycloPalloidHypoidGearMeshDesign)

        @property
        def klingelnberg_conical_gear_mesh_design(self):
            from mastapy.gears.gear_designs.klingelnberg_conical import _977
            
            return self._parent._cast(_977.KlingelnbergConicalGearMeshDesign)

        @property
        def hypoid_gear_mesh_design(self):
            from mastapy.gears.gear_designs.hypoid import _981
            
            return self._parent._cast(_981.HypoidGearMeshDesign)

        @property
        def face_gear_mesh_design(self):
            from mastapy.gears.gear_designs.face import _986
            
            return self._parent._cast(_986.FaceGearMeshDesign)

        @property
        def cylindrical_gear_mesh_design(self):
            from mastapy.gears.gear_designs.cylindrical import _1013
            
            return self._parent._cast(_1013.CylindricalGearMeshDesign)

        @property
        def conical_gear_mesh_design(self):
            from mastapy.gears.gear_designs.conical import _1149
            
            return self._parent._cast(_1149.ConicalGearMeshDesign)

        @property
        def concept_gear_mesh_design(self):
            from mastapy.gears.gear_designs.concept import _1171
            
            return self._parent._cast(_1171.ConceptGearMeshDesign)

        @property
        def bevel_gear_mesh_design(self):
            from mastapy.gears.gear_designs.bevel import _1175
            
            return self._parent._cast(_1175.BevelGearMeshDesign)

        @property
        def agma_gleason_conical_gear_mesh_design(self):
            from mastapy.gears.gear_designs.agma_gleason_conical import _1188
            
            return self._parent._cast(_1188.AGMAGleasonConicalGearMeshDesign)

        @property
        def gear_mesh_design(self) -> 'GearMeshDesign':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GearMeshDesign.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def axial_contact_ratio_rating_for_nvh(self) -> 'float':
        """float: 'AxialContactRatioRatingForNVH' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AxialContactRatioRatingForNVH

        if temp is None:
            return 0.0

        return temp

    @property
    def has_hunting_ratio(self) -> 'bool':
        """bool: 'HasHuntingRatio' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HasHuntingRatio

        if temp is None:
            return False

        return temp

    @property
    def highest_common_factor_of_teeth_numbers(self) -> 'int':
        """int: 'HighestCommonFactorOfTeethNumbers' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HighestCommonFactorOfTeethNumbers

        if temp is None:
            return 0

        return temp

    @property
    def hunting_tooth_factor(self) -> 'float':
        """float: 'HuntingToothFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HuntingToothFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def name(self) -> 'str':
        """str: 'Name' is the original name of this property."""

        temp = self.wrapped.Name

        if temp is None:
            return ''

        return temp

    @name.setter
    def name(self, value: 'str'):
        self.wrapped.Name = str(value) if value else ''

    @property
    def speed_ratio_a_to_b(self) -> 'float':
        """float: 'SpeedRatioAToB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SpeedRatioAToB

        if temp is None:
            return 0.0

        return temp

    @property
    def torque_ratio_a_to_b(self) -> 'float':
        """float: 'TorqueRatioAToB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TorqueRatioAToB

        if temp is None:
            return 0.0

        return temp

    @property
    def transverse_contact_ratio_rating_for_nvh(self) -> 'float':
        """float: 'TransverseContactRatioRatingForNVH' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TransverseContactRatioRatingForNVH

        if temp is None:
            return 0.0

        return temp

    @property
    def transverse_and_axial_contact_ratio_rating_for_nvh(self) -> 'float':
        """float: 'TransverseAndAxialContactRatioRatingForNVH' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TransverseAndAxialContactRatioRatingForNVH

        if temp is None:
            return 0.0

        return temp

    @property
    def gear_a(self) -> '_942.GearDesign':
        """GearDesign: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b(self) -> '_942.GearDesign':
        """GearDesign: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'GearMeshDesign._Cast_GearMeshDesign':
        return self._Cast_GearMeshDesign(self)
