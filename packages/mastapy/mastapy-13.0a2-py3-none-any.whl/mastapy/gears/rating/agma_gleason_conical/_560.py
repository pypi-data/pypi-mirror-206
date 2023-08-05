"""_560.py

AGMAGleasonConicalGearMeshRating
"""
from mastapy.gears.gear_designs.conical import _1163
from mastapy._internal import enum_with_selected_value_runtime, constructor, conversion
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.gears.rating.conical import _534
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_MESH_RATING = python_net_import('SMT.MastaAPI.Gears.Rating.AGMAGleasonConical', 'AGMAGleasonConicalGearMeshRating')


__docformat__ = 'restructuredtext en'
__all__ = ('AGMAGleasonConicalGearMeshRating',)


class AGMAGleasonConicalGearMeshRating(_534.ConicalGearMeshRating):
    """AGMAGleasonConicalGearMeshRating

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_MESH_RATING

    class _Cast_AGMAGleasonConicalGearMeshRating:
        """Special nested class for casting AGMAGleasonConicalGearMeshRating to subclasses."""

        def __init__(self, parent: 'AGMAGleasonConicalGearMeshRating'):
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
        def zerol_bevel_gear_mesh_rating(self):
            from mastapy.gears.rating.zerol_bevel import _365
            
            return self._parent._cast(_365.ZerolBevelGearMeshRating)

        @property
        def straight_bevel_gear_mesh_rating(self):
            from mastapy.gears.rating.straight_bevel import _391
            
            return self._parent._cast(_391.StraightBevelGearMeshRating)

        @property
        def spiral_bevel_gear_mesh_rating(self):
            from mastapy.gears.rating.spiral_bevel import _398
            
            return self._parent._cast(_398.SpiralBevelGearMeshRating)

        @property
        def hypoid_gear_mesh_rating(self):
            from mastapy.gears.rating.hypoid import _434
            
            return self._parent._cast(_434.HypoidGearMeshRating)

        @property
        def bevel_gear_mesh_rating(self):
            from mastapy.gears.rating.bevel import _549
            
            return self._parent._cast(_549.BevelGearMeshRating)

        @property
        def agma_gleason_conical_gear_mesh_rating(self) -> 'AGMAGleasonConicalGearMeshRating':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AGMAGleasonConicalGearMeshRating.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def load_distribution_factor_method(self) -> '_1163.LoadDistributionFactorMethods':
        """LoadDistributionFactorMethods: 'LoadDistributionFactorMethod' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LoadDistributionFactorMethod

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, _1163.LoadDistributionFactorMethods)
        return constructor.new_from_mastapy_type(_1163.LoadDistributionFactorMethods)(value) if value is not None else None

    @property
    def maximum_relative_displacement(self) -> 'float':
        """float: 'MaximumRelativeDisplacement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumRelativeDisplacement

        if temp is None:
            return 0.0

        return temp

    @property
    def overload_factor_bending(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'OverloadFactorBending' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OverloadFactorBending

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @property
    def overload_factor_contact(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'OverloadFactorContact' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OverloadFactorContact

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @property
    def cast_to(self) -> 'AGMAGleasonConicalGearMeshRating._Cast_AGMAGleasonConicalGearMeshRating':
        return self._Cast_AGMAGleasonConicalGearMeshRating(self)
