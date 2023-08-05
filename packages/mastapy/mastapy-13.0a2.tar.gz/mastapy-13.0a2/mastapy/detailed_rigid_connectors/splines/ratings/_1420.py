"""_1420.py

SplineJointRating
"""
from typing import List

from mastapy._internal import constructor, conversion
from mastapy.detailed_rigid_connectors.splines.ratings import _1419
from mastapy.detailed_rigid_connectors.rating import _1424
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPLINE_JOINT_RATING = python_net_import('SMT.MastaAPI.DetailedRigidConnectors.Splines.Ratings', 'SplineJointRating')


__docformat__ = 'restructuredtext en'
__all__ = ('SplineJointRating',)


class SplineJointRating(_1424.ShaftHubConnectionRating):
    """SplineJointRating

    This is a mastapy class.
    """

    TYPE = _SPLINE_JOINT_RATING

    class _Cast_SplineJointRating:
        """Special nested class for casting SplineJointRating to subclasses."""

        def __init__(self, parent: 'SplineJointRating'):
            self._parent = parent

        @property
        def shaft_hub_connection_rating(self):
            return self._parent._cast(_1424.ShaftHubConnectionRating)

        @property
        def agma6123_spline_joint_rating(self):
            from mastapy.detailed_rigid_connectors.splines.ratings import _1412
            
            return self._parent._cast(_1412.AGMA6123SplineJointRating)

        @property
        def din5466_spline_rating(self):
            from mastapy.detailed_rigid_connectors.splines.ratings import _1414
            
            return self._parent._cast(_1414.DIN5466SplineRating)

        @property
        def gbt17855_spline_joint_rating(self):
            from mastapy.detailed_rigid_connectors.splines.ratings import _1416
            
            return self._parent._cast(_1416.GBT17855SplineJointRating)

        @property
        def sae_spline_joint_rating(self):
            from mastapy.detailed_rigid_connectors.splines.ratings import _1418
            
            return self._parent._cast(_1418.SAESplineJointRating)

        @property
        def spline_joint_rating(self) -> 'SplineJointRating':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'SplineJointRating.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def allowable_bending_stress(self) -> 'float':
        """float: 'AllowableBendingStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AllowableBendingStress

        if temp is None:
            return 0.0

        return temp

    @property
    def allowable_bursting_stress(self) -> 'float':
        """float: 'AllowableBurstingStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AllowableBurstingStress

        if temp is None:
            return 0.0

        return temp

    @property
    def allowable_compressive_stress(self) -> 'float':
        """float: 'AllowableCompressiveStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AllowableCompressiveStress

        if temp is None:
            return 0.0

        return temp

    @property
    def allowable_contact_stress(self) -> 'float':
        """float: 'AllowableContactStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AllowableContactStress

        if temp is None:
            return 0.0

        return temp

    @property
    def allowable_shear_stress(self) -> 'float':
        """float: 'AllowableShearStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AllowableShearStress

        if temp is None:
            return 0.0

        return temp

    @property
    def angular_velocity(self) -> 'float':
        """float: 'AngularVelocity' is the original name of this property."""

        temp = self.wrapped.AngularVelocity

        if temp is None:
            return 0.0

        return temp

    @angular_velocity.setter
    def angular_velocity(self, value: 'float'):
        self.wrapped.AngularVelocity = float(value) if value else 0.0

    @property
    def axial_force(self) -> 'float':
        """float: 'AxialForce' is the original name of this property."""

        temp = self.wrapped.AxialForce

        if temp is None:
            return 0.0

        return temp

    @axial_force.setter
    def axial_force(self, value: 'float'):
        self.wrapped.AxialForce = float(value) if value else 0.0

    @property
    def dudley_maximum_effective_length(self) -> 'float':
        """float: 'DudleyMaximumEffectiveLength' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DudleyMaximumEffectiveLength

        if temp is None:
            return 0.0

        return temp

    @property
    def load(self) -> 'float':
        """float: 'Load' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Load

        if temp is None:
            return 0.0

        return temp

    @property
    def moment(self) -> 'float':
        """float: 'Moment' is the original name of this property."""

        temp = self.wrapped.Moment

        if temp is None:
            return 0.0

        return temp

    @moment.setter
    def moment(self, value: 'float'):
        self.wrapped.Moment = float(value) if value else 0.0

    @property
    def number_of_cycles(self) -> 'float':
        """float: 'NumberOfCycles' is the original name of this property."""

        temp = self.wrapped.NumberOfCycles

        if temp is None:
            return 0.0

        return temp

    @number_of_cycles.setter
    def number_of_cycles(self, value: 'float'):
        self.wrapped.NumberOfCycles = float(value) if value else 0.0

    @property
    def radial_load(self) -> 'float':
        """float: 'RadialLoad' is the original name of this property."""

        temp = self.wrapped.RadialLoad

        if temp is None:
            return 0.0

        return temp

    @radial_load.setter
    def radial_load(self, value: 'float'):
        self.wrapped.RadialLoad = float(value) if value else 0.0

    @property
    def torque(self) -> 'float':
        """float: 'Torque' is the original name of this property."""

        temp = self.wrapped.Torque

        if temp is None:
            return 0.0

        return temp

    @torque.setter
    def torque(self, value: 'float'):
        self.wrapped.Torque = float(value) if value else 0.0

    @property
    def spline_half_ratings(self) -> 'List[_1419.SplineHalfRating]':
        """List[SplineHalfRating]: 'SplineHalfRatings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SplineHalfRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'SplineJointRating._Cast_SplineJointRating':
        return self._Cast_SplineJointRating(self)
