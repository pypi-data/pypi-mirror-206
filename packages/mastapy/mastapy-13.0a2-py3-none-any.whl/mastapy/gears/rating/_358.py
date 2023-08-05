"""_358.py

GearSetDutyCycleRating
"""
from typing import List

from mastapy._internal import constructor, conversion
from mastapy.gears.gear_designs import _945
from mastapy.gears.rating import _354, _361, _351
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_SET_DUTY_CYCLE_RATING = python_net_import('SMT.MastaAPI.Gears.Rating', 'GearSetDutyCycleRating')


__docformat__ = 'restructuredtext en'
__all__ = ('GearSetDutyCycleRating',)


class GearSetDutyCycleRating(_351.AbstractGearSetRating):
    """GearSetDutyCycleRating

    This is a mastapy class.
    """

    TYPE = _GEAR_SET_DUTY_CYCLE_RATING

    class _Cast_GearSetDutyCycleRating:
        """Special nested class for casting GearSetDutyCycleRating to subclasses."""

        def __init__(self, parent: 'GearSetDutyCycleRating'):
            self._parent = parent

        @property
        def abstract_gear_set_rating(self):
            return self._parent._cast(_351.AbstractGearSetRating)

        @property
        def abstract_gear_set_analysis(self):
            from mastapy.gears.analysis import _1211
            
            return self._parent._cast(_1211.AbstractGearSetAnalysis)

        @property
        def worm_gear_set_duty_cycle_rating(self):
            from mastapy.gears.rating.worm import _371
            
            return self._parent._cast(_371.WormGearSetDutyCycleRating)

        @property
        def face_gear_set_duty_cycle_rating(self):
            from mastapy.gears.rating.face import _445
            
            return self._parent._cast(_445.FaceGearSetDutyCycleRating)

        @property
        def cylindrical_gear_set_duty_cycle_rating(self):
            from mastapy.gears.rating.cylindrical import _459
            
            return self._parent._cast(_459.CylindricalGearSetDutyCycleRating)

        @property
        def conical_gear_set_duty_cycle_rating(self):
            from mastapy.gears.rating.conical import _536
            
            return self._parent._cast(_536.ConicalGearSetDutyCycleRating)

        @property
        def concept_gear_set_duty_cycle_rating(self):
            from mastapy.gears.rating.concept import _547
            
            return self._parent._cast(_547.ConceptGearSetDutyCycleRating)

        @property
        def gear_set_duty_cycle_rating(self) -> 'GearSetDutyCycleRating':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GearSetDutyCycleRating.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def duty_cycle_name(self) -> 'str':
        """str: 'DutyCycleName' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DutyCycleName

        if temp is None:
            return ''

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
    def total_duty_cycle_gear_set_reliability(self) -> 'float':
        """float: 'TotalDutyCycleGearSetReliability' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TotalDutyCycleGearSetReliability

        if temp is None:
            return 0.0

        return temp

    @property
    def gear_set_design(self) -> '_945.GearSetDesign':
        """GearSetDesign: 'GearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSetDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_ratings(self) -> 'List[_354.GearDutyCycleRating]':
        """List[GearDutyCycleRating]: 'GearRatings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def gear_duty_cycle_ratings(self) -> 'List[_354.GearDutyCycleRating]':
        """List[GearDutyCycleRating]: 'GearDutyCycleRatings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearDutyCycleRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def gear_mesh_ratings(self) -> 'List[_361.MeshDutyCycleRating]':
        """List[MeshDutyCycleRating]: 'GearMeshRatings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearMeshRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def gear_mesh_duty_cycle_ratings(self) -> 'List[_361.MeshDutyCycleRating]':
        """List[MeshDutyCycleRating]: 'GearMeshDutyCycleRatings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearMeshDutyCycleRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    def set_face_widths_for_specified_safety_factors(self):
        """ 'SetFaceWidthsForSpecifiedSafetyFactors' is the original name of this method."""

        self.wrapped.SetFaceWidthsForSpecifiedSafetyFactors()

    @property
    def cast_to(self) -> 'GearSetDutyCycleRating._Cast_GearSetDutyCycleRating':
        return self._Cast_GearSetDutyCycleRating(self)
