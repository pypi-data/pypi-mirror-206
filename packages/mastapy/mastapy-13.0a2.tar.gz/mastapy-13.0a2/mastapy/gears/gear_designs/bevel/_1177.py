"""_1177.py

BevelMeshedGearDesign
"""
from mastapy._internal import constructor
from mastapy.gears.gear_designs.agma_gleason_conical import _1190
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_MESHED_GEAR_DESIGN = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Bevel', 'BevelMeshedGearDesign')


__docformat__ = 'restructuredtext en'
__all__ = ('BevelMeshedGearDesign',)


class BevelMeshedGearDesign(_1190.AGMAGleasonConicalMeshedGearDesign):
    """BevelMeshedGearDesign

    This is a mastapy class.
    """

    TYPE = _BEVEL_MESHED_GEAR_DESIGN

    class _Cast_BevelMeshedGearDesign:
        """Special nested class for casting BevelMeshedGearDesign to subclasses."""

        def __init__(self, parent: 'BevelMeshedGearDesign'):
            self._parent = parent

        @property
        def agma_gleason_conical_meshed_gear_design(self):
            return self._parent._cast(_1190.AGMAGleasonConicalMeshedGearDesign)

        @property
        def conical_meshed_gear_design(self):
            from mastapy.gears.gear_designs.conical import _1153
            
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
        def bevel_meshed_gear_design(self) -> 'BevelMeshedGearDesign':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'BevelMeshedGearDesign.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def bending_strength_geometry_factor_concave(self) -> 'float':
        """float: 'BendingStrengthGeometryFactorConcave' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BendingStrengthGeometryFactorConcave

        if temp is None:
            return 0.0

        return temp

    @property
    def bending_strength_geometry_factor_convex(self) -> 'float':
        """float: 'BendingStrengthGeometryFactorConvex' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BendingStrengthGeometryFactorConvex

        if temp is None:
            return 0.0

        return temp

    @property
    def distance_factor(self) -> 'float':
        """float: 'DistanceFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DistanceFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def durability_factor_agma(self) -> 'float':
        """float: 'DurabilityFactorAGMA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DurabilityFactorAGMA

        if temp is None:
            return 0.0

        return temp

    @property
    def durability_factor_gleason(self) -> 'float':
        """float: 'DurabilityFactorGleason' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DurabilityFactorGleason

        if temp is None:
            return 0.0

        return temp

    @property
    def geometry_factor_j_concave(self) -> 'float':
        """float: 'GeometryFactorJConcave' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GeometryFactorJConcave

        if temp is None:
            return 0.0

        return temp

    @property
    def geometry_factor_j_convex(self) -> 'float':
        """float: 'GeometryFactorJConvex' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GeometryFactorJConvex

        if temp is None:
            return 0.0

        return temp

    @property
    def minimum_root_fillet_radius(self) -> 'float':
        """float: 'MinimumRootFilletRadius' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MinimumRootFilletRadius

        if temp is None:
            return 0.0

        return temp

    @property
    def normal_chordal_thickness_at_mean_of_contact(self) -> 'float':
        """float: 'NormalChordalThicknessAtMeanOfContact' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NormalChordalThicknessAtMeanOfContact

        if temp is None:
            return 0.0

        return temp

    @property
    def strength_factor_concave(self) -> 'float':
        """float: 'StrengthFactorConcave' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StrengthFactorConcave

        if temp is None:
            return 0.0

        return temp

    @property
    def strength_factor_convex(self) -> 'float':
        """float: 'StrengthFactorConvex' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StrengthFactorConvex

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self) -> 'BevelMeshedGearDesign._Cast_BevelMeshedGearDesign':
        return self._Cast_BevelMeshedGearDesign(self)
