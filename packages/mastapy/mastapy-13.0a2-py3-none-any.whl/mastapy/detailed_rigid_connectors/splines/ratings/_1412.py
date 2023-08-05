"""_1412.py

AGMA6123SplineJointRating
"""
from mastapy._internal import constructor
from mastapy.detailed_rigid_connectors.splines.ratings import _1420
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA6123_SPLINE_JOINT_RATING = python_net_import('SMT.MastaAPI.DetailedRigidConnectors.Splines.Ratings', 'AGMA6123SplineJointRating')


__docformat__ = 'restructuredtext en'
__all__ = ('AGMA6123SplineJointRating',)


class AGMA6123SplineJointRating(_1420.SplineJointRating):
    """AGMA6123SplineJointRating

    This is a mastapy class.
    """

    TYPE = _AGMA6123_SPLINE_JOINT_RATING

    class _Cast_AGMA6123SplineJointRating:
        """Special nested class for casting AGMA6123SplineJointRating to subclasses."""

        def __init__(self, parent: 'AGMA6123SplineJointRating'):
            self._parent = parent

        @property
        def spline_joint_rating(self):
            return self._parent._cast(_1420.SplineJointRating)

        @property
        def shaft_hub_connection_rating(self):
            from mastapy.detailed_rigid_connectors.rating import _1424
            
            return self._parent._cast(_1424.ShaftHubConnectionRating)

        @property
        def agma6123_spline_joint_rating(self) -> 'AGMA6123SplineJointRating':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AGMA6123SplineJointRating.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

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
    def allowable_ring_bursting_stress(self) -> 'float':
        """float: 'AllowableRingBurstingStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AllowableRingBurstingStress

        if temp is None:
            return 0.0

        return temp

    @property
    def allowable_stress_for_shearing(self) -> 'float':
        """float: 'AllowableStressForShearing' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AllowableStressForShearing

        if temp is None:
            return 0.0

        return temp

    @property
    def allowable_torque_for_torsional_failure(self) -> 'float':
        """float: 'AllowableTorqueForTorsionalFailure' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AllowableTorqueForTorsionalFailure

        if temp is None:
            return 0.0

        return temp

    @property
    def allowable_torque_for_wear_and_fretting(self) -> 'float':
        """float: 'AllowableTorqueForWearAndFretting' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AllowableTorqueForWearAndFretting

        if temp is None:
            return 0.0

        return temp

    @property
    def bursting_stress(self) -> 'float':
        """float: 'BurstingStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BurstingStress

        if temp is None:
            return 0.0

        return temp

    @property
    def centrifugal_hoop_stress(self) -> 'float':
        """float: 'CentrifugalHoopStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CentrifugalHoopStress

        if temp is None:
            return 0.0

        return temp

    @property
    def diameter_at_half_the_working_depth(self) -> 'float':
        """float: 'DiameterAtHalfTheWorkingDepth' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DiameterAtHalfTheWorkingDepth

        if temp is None:
            return 0.0

        return temp

    @property
    def load_distribution_factor(self) -> 'float':
        """float: 'LoadDistributionFactor' is the original name of this property."""

        temp = self.wrapped.LoadDistributionFactor

        if temp is None:
            return 0.0

        return temp

    @load_distribution_factor.setter
    def load_distribution_factor(self, value: 'float'):
        self.wrapped.LoadDistributionFactor = float(value) if value else 0.0

    @property
    def name(self) -> 'str':
        """str: 'Name' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Name

        if temp is None:
            return ''

        return temp

    @property
    def safety_factor_for_ring_bursting(self) -> 'float':
        """float: 'SafetyFactorForRingBursting' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SafetyFactorForRingBursting

        if temp is None:
            return 0.0

        return temp

    @property
    def safety_factor_for_shearing(self) -> 'float':
        """float: 'SafetyFactorForShearing' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SafetyFactorForShearing

        if temp is None:
            return 0.0

        return temp

    @property
    def safety_factor_for_torsional_failure(self) -> 'float':
        """float: 'SafetyFactorForTorsionalFailure' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SafetyFactorForTorsionalFailure

        if temp is None:
            return 0.0

        return temp

    @property
    def safety_factor_for_wear_and_fretting(self) -> 'float':
        """float: 'SafetyFactorForWearAndFretting' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SafetyFactorForWearAndFretting

        if temp is None:
            return 0.0

        return temp

    @property
    def tensile_tooth_bending_stress(self) -> 'float':
        """float: 'TensileToothBendingStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TensileToothBendingStress

        if temp is None:
            return 0.0

        return temp

    @property
    def total_tensile_stress(self) -> 'float':
        """float: 'TotalTensileStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TotalTensileStress

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self) -> 'AGMA6123SplineJointRating._Cast_AGMA6123SplineJointRating':
        return self._Cast_AGMA6123SplineJointRating(self)
