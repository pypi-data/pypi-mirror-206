"""_462.py

CylindricalMeshDutyCycleRating
"""
from typing import List

from mastapy._internal import constructor, conversion
from mastapy.gears.rating.cylindrical import _454
from mastapy.gears.rating import _361
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_MESH_DUTY_CYCLE_RATING = python_net_import('SMT.MastaAPI.Gears.Rating.Cylindrical', 'CylindricalMeshDutyCycleRating')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalMeshDutyCycleRating',)


class CylindricalMeshDutyCycleRating(_361.MeshDutyCycleRating):
    """CylindricalMeshDutyCycleRating

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_MESH_DUTY_CYCLE_RATING

    class _Cast_CylindricalMeshDutyCycleRating:
        """Special nested class for casting CylindricalMeshDutyCycleRating to subclasses."""

        def __init__(self, parent: 'CylindricalMeshDutyCycleRating'):
            self._parent = parent

        @property
        def mesh_duty_cycle_rating(self):
            return self._parent._cast(_361.MeshDutyCycleRating)

        @property
        def abstract_gear_mesh_rating(self):
            from mastapy.gears.rating import _349
            
            return self._parent._cast(_349.AbstractGearMeshRating)

        @property
        def abstract_gear_mesh_analysis(self):
            from mastapy.gears.analysis import _1210
            
            return self._parent._cast(_1210.AbstractGearMeshAnalysis)

        @property
        def cylindrical_mesh_duty_cycle_rating(self) -> 'CylindricalMeshDutyCycleRating':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CylindricalMeshDutyCycleRating.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def maximum_nominal_axial_force(self) -> 'float':
        """float: 'MaximumNominalAxialForce' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumNominalAxialForce

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_nominal_tangential_load(self) -> 'float':
        """float: 'MaximumNominalTangentialLoad' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumNominalTangentialLoad

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_radial_separating_load(self) -> 'float':
        """float: 'MaximumRadialSeparatingLoad' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumRadialSeparatingLoad

        if temp is None:
            return 0.0

        return temp

    @property
    def micropitting_safety_factor(self) -> 'float':
        """float: 'MicropittingSafetyFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MicropittingSafetyFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def permanent_deformation_safety_factor_step_1(self) -> 'float':
        """float: 'PermanentDeformationSafetyFactorStep1' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PermanentDeformationSafetyFactorStep1

        if temp is None:
            return 0.0

        return temp

    @property
    def permanent_deformation_safety_factor_step_2(self) -> 'float':
        """float: 'PermanentDeformationSafetyFactorStep2' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PermanentDeformationSafetyFactorStep2

        if temp is None:
            return 0.0

        return temp

    @property
    def scuffing_load_safety_factor_integral_temperature_method(self) -> 'float':
        """float: 'ScuffingLoadSafetyFactorIntegralTemperatureMethod' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ScuffingLoadSafetyFactorIntegralTemperatureMethod

        if temp is None:
            return 0.0

        return temp

    @property
    def scuffing_safety_factor_flash_temperature_method(self) -> 'float':
        """float: 'ScuffingSafetyFactorFlashTemperatureMethod' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ScuffingSafetyFactorFlashTemperatureMethod

        if temp is None:
            return 0.0

        return temp

    @property
    def scuffing_safety_factor_integral_temperature_method(self) -> 'float':
        """float: 'ScuffingSafetyFactorIntegralTemperatureMethod' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ScuffingSafetyFactorIntegralTemperatureMethod

        if temp is None:
            return 0.0

        return temp

    @property
    def highest_torque_load_case(self) -> '_454.CylindricalGearMeshRating':
        """CylindricalGearMeshRating: 'HighestTorqueLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HighestTorqueLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cylindrical_mesh_ratings(self) -> 'List[_454.CylindricalGearMeshRating]':
        """List[CylindricalGearMeshRating]: 'CylindricalMeshRatings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalMeshRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def loaded_cylindrical_mesh_ratings(self) -> 'List[_454.CylindricalGearMeshRating]':
        """List[CylindricalGearMeshRating]: 'LoadedCylindricalMeshRatings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LoadedCylindricalMeshRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'CylindricalMeshDutyCycleRating._Cast_CylindricalMeshDutyCycleRating':
        return self._Cast_CylindricalMeshDutyCycleRating(self)
