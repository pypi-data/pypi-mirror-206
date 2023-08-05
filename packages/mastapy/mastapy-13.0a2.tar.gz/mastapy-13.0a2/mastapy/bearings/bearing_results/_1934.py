"""_1934.py

LoadedBearingResults
"""
from typing import List

from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy.bearings.bearing_results import _1945
from mastapy.bearings.bearing_designs import _2115
from mastapy.math_utility.measured_vectors import _1553
from mastapy.bearings.bearing_results.rolling import _2053
from mastapy.bearings import _1860
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_BEARING_RESULTS = python_net_import('SMT.MastaAPI.Bearings.BearingResults', 'LoadedBearingResults')


__docformat__ = 'restructuredtext en'
__all__ = ('LoadedBearingResults',)


class LoadedBearingResults(_1860.BearingLoadCaseResultsLightweight):
    """LoadedBearingResults

    This is a mastapy class.
    """

    TYPE = _LOADED_BEARING_RESULTS

    class _Cast_LoadedBearingResults:
        """Special nested class for casting LoadedBearingResults to subclasses."""

        def __init__(self, parent: 'LoadedBearingResults'):
            self._parent = parent

        @property
        def bearing_load_case_results_lightweight(self):
            return self._parent._cast(_1860.BearingLoadCaseResultsLightweight)

        @property
        def loaded_concept_axial_clearance_bearing_results(self):
            from mastapy.bearings.bearing_results import _1936
            
            return self._parent._cast(_1936.LoadedConceptAxialClearanceBearingResults)

        @property
        def loaded_concept_clearance_bearing_results(self):
            from mastapy.bearings.bearing_results import _1937
            
            return self._parent._cast(_1937.LoadedConceptClearanceBearingResults)

        @property
        def loaded_concept_radial_clearance_bearing_results(self):
            from mastapy.bearings.bearing_results import _1938
            
            return self._parent._cast(_1938.LoadedConceptRadialClearanceBearingResults)

        @property
        def loaded_detailed_bearing_results(self):
            from mastapy.bearings.bearing_results import _1939
            
            return self._parent._cast(_1939.LoadedDetailedBearingResults)

        @property
        def loaded_linear_bearing_results(self):
            from mastapy.bearings.bearing_results import _1940
            
            return self._parent._cast(_1940.LoadedLinearBearingResults)

        @property
        def loaded_non_linear_bearing_results(self):
            from mastapy.bearings.bearing_results import _1942
            
            return self._parent._cast(_1942.LoadedNonLinearBearingResults)

        @property
        def loaded_angular_contact_ball_bearing_results(self):
            from mastapy.bearings.bearing_results.rolling import _1968
            
            return self._parent._cast(_1968.LoadedAngularContactBallBearingResults)

        @property
        def loaded_angular_contact_thrust_ball_bearing_results(self):
            from mastapy.bearings.bearing_results.rolling import _1971
            
            return self._parent._cast(_1971.LoadedAngularContactThrustBallBearingResults)

        @property
        def loaded_asymmetric_spherical_roller_bearing_results(self):
            from mastapy.bearings.bearing_results.rolling import _1974
            
            return self._parent._cast(_1974.LoadedAsymmetricSphericalRollerBearingResults)

        @property
        def loaded_axial_thrust_cylindrical_roller_bearing_results(self):
            from mastapy.bearings.bearing_results.rolling import _1979
            
            return self._parent._cast(_1979.LoadedAxialThrustCylindricalRollerBearingResults)

        @property
        def loaded_axial_thrust_needle_roller_bearing_results(self):
            from mastapy.bearings.bearing_results.rolling import _1982
            
            return self._parent._cast(_1982.LoadedAxialThrustNeedleRollerBearingResults)

        @property
        def loaded_ball_bearing_results(self):
            from mastapy.bearings.bearing_results.rolling import _1987
            
            return self._parent._cast(_1987.LoadedBallBearingResults)

        @property
        def loaded_crossed_roller_bearing_results(self):
            from mastapy.bearings.bearing_results.rolling import _1990
            
            return self._parent._cast(_1990.LoadedCrossedRollerBearingResults)

        @property
        def loaded_cylindrical_roller_bearing_results(self):
            from mastapy.bearings.bearing_results.rolling import _1994
            
            return self._parent._cast(_1994.LoadedCylindricalRollerBearingResults)

        @property
        def loaded_deep_groove_ball_bearing_results(self):
            from mastapy.bearings.bearing_results.rolling import _1997
            
            return self._parent._cast(_1997.LoadedDeepGrooveBallBearingResults)

        @property
        def loaded_four_point_contact_ball_bearing_results(self):
            from mastapy.bearings.bearing_results.rolling import _2002
            
            return self._parent._cast(_2002.LoadedFourPointContactBallBearingResults)

        @property
        def loaded_needle_roller_bearing_results(self):
            from mastapy.bearings.bearing_results.rolling import _2006
            
            return self._parent._cast(_2006.LoadedNeedleRollerBearingResults)

        @property
        def loaded_non_barrel_roller_bearing_results(self):
            from mastapy.bearings.bearing_results.rolling import _2009
            
            return self._parent._cast(_2009.LoadedNonBarrelRollerBearingResults)

        @property
        def loaded_roller_bearing_results(self):
            from mastapy.bearings.bearing_results.rolling import _2014
            
            return self._parent._cast(_2014.LoadedRollerBearingResults)

        @property
        def loaded_rolling_bearing_results(self):
            from mastapy.bearings.bearing_results.rolling import _2018
            
            return self._parent._cast(_2018.LoadedRollingBearingResults)

        @property
        def loaded_self_aligning_ball_bearing_results(self):
            from mastapy.bearings.bearing_results.rolling import _2021
            
            return self._parent._cast(_2021.LoadedSelfAligningBallBearingResults)

        @property
        def loaded_spherical_roller_radial_bearing_results(self):
            from mastapy.bearings.bearing_results.rolling import _2025
            
            return self._parent._cast(_2025.LoadedSphericalRollerRadialBearingResults)

        @property
        def loaded_spherical_roller_thrust_bearing_results(self):
            from mastapy.bearings.bearing_results.rolling import _2028
            
            return self._parent._cast(_2028.LoadedSphericalRollerThrustBearingResults)

        @property
        def loaded_taper_roller_bearing_results(self):
            from mastapy.bearings.bearing_results.rolling import _2033
            
            return self._parent._cast(_2033.LoadedTaperRollerBearingResults)

        @property
        def loaded_three_point_contact_ball_bearing_results(self):
            from mastapy.bearings.bearing_results.rolling import _2036
            
            return self._parent._cast(_2036.LoadedThreePointContactBallBearingResults)

        @property
        def loaded_thrust_ball_bearing_results(self):
            from mastapy.bearings.bearing_results.rolling import _2039
            
            return self._parent._cast(_2039.LoadedThrustBallBearingResults)

        @property
        def loaded_toroidal_roller_bearing_results(self):
            from mastapy.bearings.bearing_results.rolling import _2042
            
            return self._parent._cast(_2042.LoadedToroidalRollerBearingResults)

        @property
        def loaded_fluid_film_bearing_results(self):
            from mastapy.bearings.bearing_results.fluid_film import _2104
            
            return self._parent._cast(_2104.LoadedFluidFilmBearingResults)

        @property
        def loaded_grease_filled_journal_bearing_results(self):
            from mastapy.bearings.bearing_results.fluid_film import _2105
            
            return self._parent._cast(_2105.LoadedGreaseFilledJournalBearingResults)

        @property
        def loaded_pad_fluid_film_bearing_results(self):
            from mastapy.bearings.bearing_results.fluid_film import _2106
            
            return self._parent._cast(_2106.LoadedPadFluidFilmBearingResults)

        @property
        def loaded_plain_journal_bearing_results(self):
            from mastapy.bearings.bearing_results.fluid_film import _2107
            
            return self._parent._cast(_2107.LoadedPlainJournalBearingResults)

        @property
        def loaded_plain_oil_fed_journal_bearing(self):
            from mastapy.bearings.bearing_results.fluid_film import _2109
            
            return self._parent._cast(_2109.LoadedPlainOilFedJournalBearing)

        @property
        def loaded_tilting_pad_journal_bearing_results(self):
            from mastapy.bearings.bearing_results.fluid_film import _2112
            
            return self._parent._cast(_2112.LoadedTiltingPadJournalBearingResults)

        @property
        def loaded_tilting_pad_thrust_bearing_results(self):
            from mastapy.bearings.bearing_results.fluid_film import _2113
            
            return self._parent._cast(_2113.LoadedTiltingPadThrustBearingResults)

        @property
        def loaded_bearing_results(self) -> 'LoadedBearingResults':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'LoadedBearingResults.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def angle_of_gravity_from_z_axis(self) -> 'float':
        """float: 'AngleOfGravityFromZAxis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AngleOfGravityFromZAxis

        if temp is None:
            return 0.0

        return temp

    @property
    def axial_displacement_preload(self) -> 'float':
        """float: 'AxialDisplacementPreload' is the original name of this property."""

        temp = self.wrapped.AxialDisplacementPreload

        if temp is None:
            return 0.0

        return temp

    @axial_displacement_preload.setter
    def axial_displacement_preload(self, value: 'float'):
        self.wrapped.AxialDisplacementPreload = float(value) if value else 0.0

    @property
    def duration(self) -> 'float':
        """float: 'Duration' is the original name of this property."""

        temp = self.wrapped.Duration

        if temp is None:
            return 0.0

        return temp

    @duration.setter
    def duration(self, value: 'float'):
        self.wrapped.Duration = float(value) if value else 0.0

    @property
    def force_results_are_overridden(self) -> 'bool':
        """bool: 'ForceResultsAreOverridden' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ForceResultsAreOverridden

        if temp is None:
            return False

        return temp

    @property
    def inner_ring_angular_velocity(self) -> 'float':
        """float: 'InnerRingAngularVelocity' is the original name of this property."""

        temp = self.wrapped.InnerRingAngularVelocity

        if temp is None:
            return 0.0

        return temp

    @inner_ring_angular_velocity.setter
    def inner_ring_angular_velocity(self, value: 'float'):
        self.wrapped.InnerRingAngularVelocity = float(value) if value else 0.0

    @property
    def orientation(self) -> '_1945.Orientations':
        """Orientations: 'Orientation' is the original name of this property."""

        temp = self.wrapped.Orientation

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, _1945.Orientations)
        return constructor.new_from_mastapy_type(_1945.Orientations)(value) if value is not None else None

    @orientation.setter
    def orientation(self, value: '_1945.Orientations'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value, _1945.Orientations.type_())
        self.wrapped.Orientation = value

    @property
    def outer_ring_angular_velocity(self) -> 'float':
        """float: 'OuterRingAngularVelocity' is the original name of this property."""

        temp = self.wrapped.OuterRingAngularVelocity

        if temp is None:
            return 0.0

        return temp

    @outer_ring_angular_velocity.setter
    def outer_ring_angular_velocity(self, value: 'float'):
        self.wrapped.OuterRingAngularVelocity = float(value) if value else 0.0

    @property
    def relative_angular_velocity(self) -> 'float':
        """float: 'RelativeAngularVelocity' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RelativeAngularVelocity

        if temp is None:
            return 0.0

        return temp

    @property
    def relative_axial_displacement(self) -> 'float':
        """float: 'RelativeAxialDisplacement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RelativeAxialDisplacement

        if temp is None:
            return 0.0

        return temp

    @property
    def relative_radial_displacement(self) -> 'float':
        """float: 'RelativeRadialDisplacement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RelativeRadialDisplacement

        if temp is None:
            return 0.0

        return temp

    @property
    def signed_relative_angular_velocity(self) -> 'float':
        """float: 'SignedRelativeAngularVelocity' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SignedRelativeAngularVelocity

        if temp is None:
            return 0.0

        return temp

    @property
    def specified_axial_internal_clearance(self) -> 'float':
        """float: 'SpecifiedAxialInternalClearance' is the original name of this property."""

        temp = self.wrapped.SpecifiedAxialInternalClearance

        if temp is None:
            return 0.0

        return temp

    @specified_axial_internal_clearance.setter
    def specified_axial_internal_clearance(self, value: 'float'):
        self.wrapped.SpecifiedAxialInternalClearance = float(value) if value else 0.0

    @property
    def specified_radial_internal_clearance(self) -> 'float':
        """float: 'SpecifiedRadialInternalClearance' is the original name of this property."""

        temp = self.wrapped.SpecifiedRadialInternalClearance

        if temp is None:
            return 0.0

        return temp

    @specified_radial_internal_clearance.setter
    def specified_radial_internal_clearance(self, value: 'float'):
        self.wrapped.SpecifiedRadialInternalClearance = float(value) if value else 0.0

    @property
    def bearing(self) -> '_2115.BearingDesign':
        """BearingDesign: 'Bearing' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Bearing

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def force_on_inner_race(self) -> '_1553.VectorWithLinearAndAngularComponents':
        """VectorWithLinearAndAngularComponents: 'ForceOnInnerRace' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ForceOnInnerRace

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def ring_results(self) -> 'List[_2053.RingForceAndDisplacement]':
        """List[RingForceAndDisplacement]: 'RingResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RingResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'LoadedBearingResults._Cast_LoadedBearingResults':
        return self._Cast_LoadedBearingResults(self)
