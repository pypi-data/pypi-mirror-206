"""_415.py

KlingelnbergCycloPalloidSpiralBevelMeshSingleFlankRating
"""
from typing import List

from mastapy._internal import constructor, conversion
from mastapy.gears.rating.klingelnberg_conical.kn3030 import _412, _410
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_MESH_SINGLE_FLANK_RATING = python_net_import('SMT.MastaAPI.Gears.Rating.KlingelnbergConical.KN3030', 'KlingelnbergCycloPalloidSpiralBevelMeshSingleFlankRating')


__docformat__ = 'restructuredtext en'
__all__ = ('KlingelnbergCycloPalloidSpiralBevelMeshSingleFlankRating',)


class KlingelnbergCycloPalloidSpiralBevelMeshSingleFlankRating(_410.KlingelnbergConicalMeshSingleFlankRating):
    """KlingelnbergCycloPalloidSpiralBevelMeshSingleFlankRating

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_MESH_SINGLE_FLANK_RATING

    class _Cast_KlingelnbergCycloPalloidSpiralBevelMeshSingleFlankRating:
        """Special nested class for casting KlingelnbergCycloPalloidSpiralBevelMeshSingleFlankRating to subclasses."""

        def __init__(self, parent: 'KlingelnbergCycloPalloidSpiralBevelMeshSingleFlankRating'):
            self._parent = parent

        @property
        def klingelnberg_conical_mesh_single_flank_rating(self):
            return self._parent._cast(_410.KlingelnbergConicalMeshSingleFlankRating)

        @property
        def mesh_single_flank_rating(self):
            from mastapy.gears.rating import _362
            
            return self._parent._cast(_362.MeshSingleFlankRating)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_mesh_single_flank_rating(self) -> 'KlingelnbergCycloPalloidSpiralBevelMeshSingleFlankRating':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'KlingelnbergCycloPalloidSpiralBevelMeshSingleFlankRating.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def angle_factor(self) -> 'float':
        """float: 'AngleFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AngleFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def contact_ratio_factor_scuffing(self) -> 'float':
        """float: 'ContactRatioFactorScuffing' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ContactRatioFactorScuffing

        if temp is None:
            return 0.0

        return temp

    @property
    def curvature_radius(self) -> 'float':
        """float: 'CurvatureRadius' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurvatureRadius

        if temp is None:
            return 0.0

        return temp

    @property
    def dynamic_factor(self) -> 'float':
        """float: 'DynamicFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DynamicFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def friction_coefficient(self) -> 'float':
        """float: 'FrictionCoefficient' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FrictionCoefficient

        if temp is None:
            return 0.0

        return temp

    @property
    def geometry_factor(self) -> 'float':
        """float: 'GeometryFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GeometryFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def integral_flash_temperature(self) -> 'float':
        """float: 'IntegralFlashTemperature' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.IntegralFlashTemperature

        if temp is None:
            return 0.0

        return temp

    @property
    def load_distribution_factor_transverse(self) -> 'float':
        """float: 'LoadDistributionFactorTransverse' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LoadDistributionFactorTransverse

        if temp is None:
            return 0.0

        return temp

    @property
    def relating_factor_for_the_thermal_flash_temperature(self) -> 'float':
        """float: 'RelatingFactorForTheThermalFlashTemperature' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RelatingFactorForTheThermalFlashTemperature

        if temp is None:
            return 0.0

        return temp

    @property
    def tangential_speed_sum(self) -> 'float':
        """float: 'TangentialSpeedSum' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TangentialSpeedSum

        if temp is None:
            return 0.0

        return temp

    @property
    def thermal_flash_factor(self) -> 'float':
        """float: 'ThermalFlashFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ThermalFlashFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def gear_single_flank_ratings(self) -> 'List[_412.KlingelnbergCycloPalloidConicalGearSingleFlankRating]':
        """List[KlingelnbergCycloPalloidConicalGearSingleFlankRating]: 'GearSingleFlankRatings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSingleFlankRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def kn3030_klingelnberg_gear_single_flank_ratings(self) -> 'List[_412.KlingelnbergCycloPalloidConicalGearSingleFlankRating]':
        """List[KlingelnbergCycloPalloidConicalGearSingleFlankRating]: 'KN3030KlingelnbergGearSingleFlankRatings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.KN3030KlingelnbergGearSingleFlankRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'KlingelnbergCycloPalloidSpiralBevelMeshSingleFlankRating._Cast_KlingelnbergCycloPalloidSpiralBevelMeshSingleFlankRating':
        return self._Cast_KlingelnbergCycloPalloidSpiralBevelMeshSingleFlankRating(self)
