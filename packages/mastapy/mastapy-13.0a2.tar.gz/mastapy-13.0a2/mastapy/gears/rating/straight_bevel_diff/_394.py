"""_394.py

StraightBevelDiffGearMeshRating
"""
from typing import List

from mastapy._internal import constructor, conversion
from mastapy.gears.gear_designs.straight_bevel_diff import _961
from mastapy.gears.rating.straight_bevel_diff import _397, _395
from mastapy.gears.rating.conical import _534
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_DIFF_GEAR_MESH_RATING = python_net_import('SMT.MastaAPI.Gears.Rating.StraightBevelDiff', 'StraightBevelDiffGearMeshRating')


__docformat__ = 'restructuredtext en'
__all__ = ('StraightBevelDiffGearMeshRating',)


class StraightBevelDiffGearMeshRating(_534.ConicalGearMeshRating):
    """StraightBevelDiffGearMeshRating

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_DIFF_GEAR_MESH_RATING

    class _Cast_StraightBevelDiffGearMeshRating:
        """Special nested class for casting StraightBevelDiffGearMeshRating to subclasses."""

        def __init__(self, parent: 'StraightBevelDiffGearMeshRating'):
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
        def straight_bevel_diff_gear_mesh_rating(self) -> 'StraightBevelDiffGearMeshRating':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'StraightBevelDiffGearMeshRating.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def derating_factor(self) -> 'float':
        """float: 'DeratingFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DeratingFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def inertia_factor_bending(self) -> 'float':
        """float: 'InertiaFactorBending' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InertiaFactorBending

        if temp is None:
            return 0.0

        return temp

    @property
    def load_distribution_factor(self) -> 'float':
        """float: 'LoadDistributionFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LoadDistributionFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def rating_result(self) -> 'str':
        """str: 'RatingResult' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RatingResult

        if temp is None:
            return ''

        return temp

    @property
    def straight_bevel_diff_gear_mesh(self) -> '_961.StraightBevelDiffGearMeshDesign':
        """StraightBevelDiffGearMeshDesign: 'StraightBevelDiffGearMesh' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StraightBevelDiffGearMesh

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def meshed_gears(self) -> 'List[_397.StraightBevelDiffMeshedGearRating]':
        """List[StraightBevelDiffMeshedGearRating]: 'MeshedGears' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeshedGears

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def gears_in_mesh(self) -> 'List[_397.StraightBevelDiffMeshedGearRating]':
        """List[StraightBevelDiffMeshedGearRating]: 'GearsInMesh' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearsInMesh

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def straight_bevel_diff_gear_ratings(self) -> 'List[_395.StraightBevelDiffGearRating]':
        """List[StraightBevelDiffGearRating]: 'StraightBevelDiffGearRatings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StraightBevelDiffGearRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'StraightBevelDiffGearMeshRating._Cast_StraightBevelDiffGearMeshRating':
        return self._Cast_StraightBevelDiffGearMeshRating(self)
