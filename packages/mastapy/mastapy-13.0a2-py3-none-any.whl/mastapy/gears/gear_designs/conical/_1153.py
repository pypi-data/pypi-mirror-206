"""_1153.py

ConicalMeshedGearDesign
"""
from mastapy._internal import constructor
from mastapy.gears.gear_designs import _943
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_MESHED_GEAR_DESIGN = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Conical', 'ConicalMeshedGearDesign')


__docformat__ = 'restructuredtext en'
__all__ = ('ConicalMeshedGearDesign',)


class ConicalMeshedGearDesign(_943.GearDesignComponent):
    """ConicalMeshedGearDesign

    This is a mastapy class.
    """

    TYPE = _CONICAL_MESHED_GEAR_DESIGN

    class _Cast_ConicalMeshedGearDesign:
        """Special nested class for casting ConicalMeshedGearDesign to subclasses."""

        def __init__(self, parent: 'ConicalMeshedGearDesign'):
            self._parent = parent

        @property
        def gear_design_component(self):
            return self._parent._cast(_943.GearDesignComponent)

        @property
        def zerol_bevel_meshed_gear_design(self):
            from mastapy.gears.gear_designs.zerol_bevel import _950
            
            return self._parent._cast(_950.ZerolBevelMeshedGearDesign)

        @property
        def straight_bevel_meshed_gear_design(self):
            from mastapy.gears.gear_designs.straight_bevel import _959
            
            return self._parent._cast(_959.StraightBevelMeshedGearDesign)

        @property
        def straight_bevel_diff_meshed_gear_design(self):
            from mastapy.gears.gear_designs.straight_bevel_diff import _963
            
            return self._parent._cast(_963.StraightBevelDiffMeshedGearDesign)

        @property
        def spiral_bevel_meshed_gear_design(self):
            from mastapy.gears.gear_designs.spiral_bevel import _967
            
            return self._parent._cast(_967.SpiralBevelMeshedGearDesign)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_meshed_gear_design(self):
            from mastapy.gears.gear_designs.klingelnberg_spiral_bevel import _971
            
            return self._parent._cast(_971.KlingelnbergCycloPalloidSpiralBevelMeshedGearDesign)

        @property
        def klingelnberg_cyclo_palloid_hypoid_meshed_gear_design(self):
            from mastapy.gears.gear_designs.klingelnberg_hypoid import _975
            
            return self._parent._cast(_975.KlingelnbergCycloPalloidHypoidMeshedGearDesign)

        @property
        def klingelnberg_conical_meshed_gear_design(self):
            from mastapy.gears.gear_designs.klingelnberg_conical import _979
            
            return self._parent._cast(_979.KlingelnbergConicalMeshedGearDesign)

        @property
        def hypoid_meshed_gear_design(self):
            from mastapy.gears.gear_designs.hypoid import _983
            
            return self._parent._cast(_983.HypoidMeshedGearDesign)

        @property
        def bevel_meshed_gear_design(self):
            from mastapy.gears.gear_designs.bevel import _1177
            
            return self._parent._cast(_1177.BevelMeshedGearDesign)

        @property
        def agma_gleason_conical_meshed_gear_design(self):
            from mastapy.gears.gear_designs.agma_gleason_conical import _1190
            
            return self._parent._cast(_1190.AGMAGleasonConicalMeshedGearDesign)

        @property
        def conical_meshed_gear_design(self) -> 'ConicalMeshedGearDesign':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConicalMeshedGearDesign.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def axial_force_type(self) -> 'str':
        """str: 'AxialForceType' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AxialForceType

        if temp is None:
            return ''

        return temp

    @property
    def axial_force_type_convex(self) -> 'str':
        """str: 'AxialForceTypeConvex' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AxialForceTypeConvex

        if temp is None:
            return ''

        return temp

    @property
    def gleason_axial_factor_concave(self) -> 'float':
        """float: 'GleasonAxialFactorConcave' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GleasonAxialFactorConcave

        if temp is None:
            return 0.0

        return temp

    @property
    def gleason_axial_factor_convex(self) -> 'float':
        """float: 'GleasonAxialFactorConvex' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GleasonAxialFactorConvex

        if temp is None:
            return 0.0

        return temp

    @property
    def gleason_separating_factor_concave(self) -> 'float':
        """float: 'GleasonSeparatingFactorConcave' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GleasonSeparatingFactorConcave

        if temp is None:
            return 0.0

        return temp

    @property
    def gleason_separating_factor_convex(self) -> 'float':
        """float: 'GleasonSeparatingFactorConvex' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GleasonSeparatingFactorConvex

        if temp is None:
            return 0.0

        return temp

    @property
    def module(self) -> 'float':
        """float: 'Module' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Module

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
    def pitch_angle(self) -> 'float':
        """float: 'PitchAngle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PitchAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def radial_force_type_concave(self) -> 'str':
        """str: 'RadialForceTypeConcave' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RadialForceTypeConcave

        if temp is None:
            return ''

        return temp

    @property
    def radial_force_type_convex(self) -> 'str':
        """str: 'RadialForceTypeConvex' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RadialForceTypeConvex

        if temp is None:
            return ''

        return temp

    @property
    def cast_to(self) -> 'ConicalMeshedGearDesign._Cast_ConicalMeshedGearDesign':
        return self._Cast_ConicalMeshedGearDesign(self)
