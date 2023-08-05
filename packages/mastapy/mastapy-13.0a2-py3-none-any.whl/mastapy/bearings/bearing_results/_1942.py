"""_1942.py

LoadedNonLinearBearingResults
"""
from mastapy.materials.efficiency import _298, _299
from mastapy._internal import constructor
from mastapy.bearings.bearing_results import _1934
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_NON_LINEAR_BEARING_RESULTS = python_net_import('SMT.MastaAPI.Bearings.BearingResults', 'LoadedNonLinearBearingResults')


__docformat__ = 'restructuredtext en'
__all__ = ('LoadedNonLinearBearingResults',)


class LoadedNonLinearBearingResults(_1934.LoadedBearingResults):
    """LoadedNonLinearBearingResults

    This is a mastapy class.
    """

    TYPE = _LOADED_NON_LINEAR_BEARING_RESULTS

    class _Cast_LoadedNonLinearBearingResults:
        """Special nested class for casting LoadedNonLinearBearingResults to subclasses."""

        def __init__(self, parent: 'LoadedNonLinearBearingResults'):
            self._parent = parent

        @property
        def loaded_bearing_results(self):
            return self._parent._cast(_1934.LoadedBearingResults)

        @property
        def bearing_load_case_results_lightweight(self):
            from mastapy.bearings import _1860
            
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
        def loaded_non_linear_bearing_results(self) -> 'LoadedNonLinearBearingResults':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'LoadedNonLinearBearingResults.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def power_loss(self) -> '_298.PowerLoss':
        """PowerLoss: 'PowerLoss' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerLoss

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def resistive_torque(self) -> '_299.ResistiveTorque':
        """ResistiveTorque: 'ResistiveTorque' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ResistiveTorque

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults':
        return self._Cast_LoadedNonLinearBearingResults(self)
