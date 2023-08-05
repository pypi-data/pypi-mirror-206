"""_968.py

KlingelnbergCycloPalloidSpiralBevelGearDesign
"""
from mastapy._internal import constructor
from mastapy.gears.gear_designs.klingelnberg_conical import _976
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_DESIGN = python_net_import('SMT.MastaAPI.Gears.GearDesigns.KlingelnbergSpiralBevel', 'KlingelnbergCycloPalloidSpiralBevelGearDesign')


__docformat__ = 'restructuredtext en'
__all__ = ('KlingelnbergCycloPalloidSpiralBevelGearDesign',)


class KlingelnbergCycloPalloidSpiralBevelGearDesign(_976.KlingelnbergConicalGearDesign):
    """KlingelnbergCycloPalloidSpiralBevelGearDesign

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_DESIGN

    class _Cast_KlingelnbergCycloPalloidSpiralBevelGearDesign:
        """Special nested class for casting KlingelnbergCycloPalloidSpiralBevelGearDesign to subclasses."""

        def __init__(self, parent: 'KlingelnbergCycloPalloidSpiralBevelGearDesign'):
            self._parent = parent

        @property
        def klingelnberg_conical_gear_design(self):
            return self._parent._cast(_976.KlingelnbergConicalGearDesign)

        @property
        def conical_gear_design(self):
            from mastapy.gears.gear_designs.conical import _1148
            
            return self._parent._cast(_1148.ConicalGearDesign)

        @property
        def gear_design(self):
            from mastapy.gears.gear_designs import _942
            
            return self._parent._cast(_942.GearDesign)

        @property
        def gear_design_component(self):
            from mastapy.gears.gear_designs import _943
            
            return self._parent._cast(_943.GearDesignComponent)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_design(self) -> 'KlingelnbergCycloPalloidSpiralBevelGearDesign':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'KlingelnbergCycloPalloidSpiralBevelGearDesign.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def face_width(self) -> 'float':
        """float: 'FaceWidth' is the original name of this property."""

        temp = self.wrapped.FaceWidth

        if temp is None:
            return 0.0

        return temp

    @face_width.setter
    def face_width(self, value: 'float'):
        self.wrapped.FaceWidth = float(value) if value else 0.0

    @property
    def generating_cone_angle(self) -> 'float':
        """float: 'GeneratingConeAngle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GeneratingConeAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def inner_root_diameter(self) -> 'float':
        """float: 'InnerRootDiameter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerRootDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def inner_tip_diameter(self) -> 'float':
        """float: 'InnerTipDiameter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerTipDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def inner_tip_diameter_with_tooth_chamfer(self) -> 'float':
        """float: 'InnerTipDiameterWithToothChamfer' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerTipDiameterWithToothChamfer

        if temp is None:
            return 0.0

        return temp

    @property
    def mean_pitch_diameter(self) -> 'float':
        """float: 'MeanPitchDiameter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeanPitchDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def mean_spiral_angle(self) -> 'float':
        """float: 'MeanSpiralAngle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeanSpiralAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def outer_root_diameter(self) -> 'float':
        """float: 'OuterRootDiameter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterRootDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def outer_tip_diameter(self) -> 'float':
        """float: 'OuterTipDiameter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterTipDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def pitch_depth(self) -> 'float':
        """float: 'PitchDepth' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PitchDepth

        if temp is None:
            return 0.0

        return temp

    @property
    def pitch_diameter(self) -> 'float':
        """float: 'PitchDiameter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PitchDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self) -> 'KlingelnbergCycloPalloidSpiralBevelGearDesign._Cast_KlingelnbergCycloPalloidSpiralBevelGearDesign':
        return self._Cast_KlingelnbergCycloPalloidSpiralBevelGearDesign(self)
