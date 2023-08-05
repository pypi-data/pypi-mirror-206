"""_6873.py

InformationAtRingPinToDiscContactPointFromGeometry
"""
from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INFORMATION_AT_RING_PIN_TO_DISC_CONTACT_POINT_FROM_GEOMETRY = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'InformationAtRingPinToDiscContactPointFromGeometry')


__docformat__ = 'restructuredtext en'
__all__ = ('InformationAtRingPinToDiscContactPointFromGeometry',)


class InformationAtRingPinToDiscContactPointFromGeometry(_0.APIBase):
    """InformationAtRingPinToDiscContactPointFromGeometry

    This is a mastapy class.
    """

    TYPE = _INFORMATION_AT_RING_PIN_TO_DISC_CONTACT_POINT_FROM_GEOMETRY

    class _Cast_InformationAtRingPinToDiscContactPointFromGeometry:
        """Special nested class for casting InformationAtRingPinToDiscContactPointFromGeometry to subclasses."""

        def __init__(self, parent: 'InformationAtRingPinToDiscContactPointFromGeometry'):
            self._parent = parent

        @property
        def information_at_ring_pin_to_disc_contact_point_from_geometry(self) -> 'InformationAtRingPinToDiscContactPointFromGeometry':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'InformationAtRingPinToDiscContactPointFromGeometry.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def clearance_due_to_disc_profile(self) -> 'float':
        """float: 'ClearanceDueToDiscProfile' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ClearanceDueToDiscProfile

        if temp is None:
            return 0.0

        return temp

    @property
    def clearance_due_to_ring_pin_manufacturing_errors(self) -> 'float':
        """float: 'ClearanceDueToRingPinManufacturingErrors' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ClearanceDueToRingPinManufacturingErrors

        if temp is None:
            return 0.0

        return temp

    @property
    def combined_curvature(self) -> 'float':
        """float: 'CombinedCurvature' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CombinedCurvature

        if temp is None:
            return 0.0

        return temp

    @property
    def combined_radius_of_curvature(self) -> 'float':
        """float: 'CombinedRadiusOfCurvature' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CombinedRadiusOfCurvature

        if temp is None:
            return 0.0

        return temp

    @property
    def disc_radius_of_curvature(self) -> 'float':
        """float: 'DiscRadiusOfCurvature' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DiscRadiusOfCurvature

        if temp is None:
            return 0.0

        return temp

    @property
    def normalised_arc_length_along_half_lobe_to_contact(self) -> 'float':
        """float: 'NormalisedArcLengthAlongHalfLobeToContact' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NormalisedArcLengthAlongHalfLobeToContact

        if temp is None:
            return 0.0

        return temp

    @property
    def pin_index(self) -> 'int':
        """int: 'PinIndex' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PinIndex

        if temp is None:
            return 0

        return temp

    @property
    def ring_pin_radius_of_curvature(self) -> 'float':
        """float: 'RingPinRadiusOfCurvature' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RingPinRadiusOfCurvature

        if temp is None:
            return 0.0

        return temp

    @property
    def total_clearance(self) -> 'float':
        """float: 'TotalClearance' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TotalClearance

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self) -> 'InformationAtRingPinToDiscContactPointFromGeometry._Cast_InformationAtRingPinToDiscContactPointFromGeometry':
        return self._Cast_InformationAtRingPinToDiscContactPointFromGeometry(self)
