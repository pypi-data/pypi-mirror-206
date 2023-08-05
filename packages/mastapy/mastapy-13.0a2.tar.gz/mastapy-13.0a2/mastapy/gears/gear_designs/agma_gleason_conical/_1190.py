"""_1190.py

AGMAGleasonConicalMeshedGearDesign
"""
from mastapy._internal import constructor
from mastapy.gears.gear_designs.conical import _1153
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_MESHED_GEAR_DESIGN = python_net_import('SMT.MastaAPI.Gears.GearDesigns.AGMAGleasonConical', 'AGMAGleasonConicalMeshedGearDesign')


__docformat__ = 'restructuredtext en'
__all__ = ('AGMAGleasonConicalMeshedGearDesign',)


class AGMAGleasonConicalMeshedGearDesign(_1153.ConicalMeshedGearDesign):
    """AGMAGleasonConicalMeshedGearDesign

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_MESHED_GEAR_DESIGN

    class _Cast_AGMAGleasonConicalMeshedGearDesign:
        """Special nested class for casting AGMAGleasonConicalMeshedGearDesign to subclasses."""

        def __init__(self, parent: 'AGMAGleasonConicalMeshedGearDesign'):
            self._parent = parent

        @property
        def conical_meshed_gear_design(self):
            return self._parent._cast(_1153.ConicalMeshedGearDesign)

        @property
        def gear_design_component(self):
            from mastapy.gears.gear_designs import _943
            
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
        def hypoid_meshed_gear_design(self):
            from mastapy.gears.gear_designs.hypoid import _983
            
            return self._parent._cast(_983.HypoidMeshedGearDesign)

        @property
        def bevel_meshed_gear_design(self):
            from mastapy.gears.gear_designs.bevel import _1177
            
            return self._parent._cast(_1177.BevelMeshedGearDesign)

        @property
        def agma_gleason_conical_meshed_gear_design(self) -> 'AGMAGleasonConicalMeshedGearDesign':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AGMAGleasonConicalMeshedGearDesign.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def mean_normal_topland(self) -> 'float':
        """float: 'MeanNormalTopland' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeanNormalTopland

        if temp is None:
            return 0.0

        return temp

    @property
    def minimum_topland_to_module_factor(self) -> 'float':
        """float: 'MinimumToplandToModuleFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MinimumToplandToModuleFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def required_mean_normal_topland(self) -> 'float':
        """float: 'RequiredMeanNormalTopland' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RequiredMeanNormalTopland

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self) -> 'AGMAGleasonConicalMeshedGearDesign._Cast_AGMAGleasonConicalMeshedGearDesign':
        return self._Cast_AGMAGleasonConicalMeshedGearDesign(self)
