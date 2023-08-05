"""_2119.py

NonLinearBearing
"""
from mastapy.bearings.bearing_designs import _2115
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_NON_LINEAR_BEARING = python_net_import('SMT.MastaAPI.Bearings.BearingDesigns', 'NonLinearBearing')


__docformat__ = 'restructuredtext en'
__all__ = ('NonLinearBearing',)


class NonLinearBearing(_2115.BearingDesign):
    """NonLinearBearing

    This is a mastapy class.
    """

    TYPE = _NON_LINEAR_BEARING

    class _Cast_NonLinearBearing:
        """Special nested class for casting NonLinearBearing to subclasses."""

        def __init__(self, parent: 'NonLinearBearing'):
            self._parent = parent

        @property
        def bearing_design(self):
            return self._parent._cast(_2115.BearingDesign)

        @property
        def detailed_bearing(self):
            from mastapy.bearings.bearing_designs import _2116
            
            return self._parent._cast(_2116.DetailedBearing)

        @property
        def angular_contact_ball_bearing(self):
            from mastapy.bearings.bearing_designs.rolling import _2120
            
            return self._parent._cast(_2120.AngularContactBallBearing)

        @property
        def angular_contact_thrust_ball_bearing(self):
            from mastapy.bearings.bearing_designs.rolling import _2121
            
            return self._parent._cast(_2121.AngularContactThrustBallBearing)

        @property
        def asymmetric_spherical_roller_bearing(self):
            from mastapy.bearings.bearing_designs.rolling import _2122
            
            return self._parent._cast(_2122.AsymmetricSphericalRollerBearing)

        @property
        def axial_thrust_cylindrical_roller_bearing(self):
            from mastapy.bearings.bearing_designs.rolling import _2123
            
            return self._parent._cast(_2123.AxialThrustCylindricalRollerBearing)

        @property
        def axial_thrust_needle_roller_bearing(self):
            from mastapy.bearings.bearing_designs.rolling import _2124
            
            return self._parent._cast(_2124.AxialThrustNeedleRollerBearing)

        @property
        def ball_bearing(self):
            from mastapy.bearings.bearing_designs.rolling import _2125
            
            return self._parent._cast(_2125.BallBearing)

        @property
        def barrel_roller_bearing(self):
            from mastapy.bearings.bearing_designs.rolling import _2127
            
            return self._parent._cast(_2127.BarrelRollerBearing)

        @property
        def crossed_roller_bearing(self):
            from mastapy.bearings.bearing_designs.rolling import _2133
            
            return self._parent._cast(_2133.CrossedRollerBearing)

        @property
        def cylindrical_roller_bearing(self):
            from mastapy.bearings.bearing_designs.rolling import _2134
            
            return self._parent._cast(_2134.CylindricalRollerBearing)

        @property
        def deep_groove_ball_bearing(self):
            from mastapy.bearings.bearing_designs.rolling import _2135
            
            return self._parent._cast(_2135.DeepGrooveBallBearing)

        @property
        def four_point_contact_ball_bearing(self):
            from mastapy.bearings.bearing_designs.rolling import _2139
            
            return self._parent._cast(_2139.FourPointContactBallBearing)

        @property
        def multi_point_contact_ball_bearing(self):
            from mastapy.bearings.bearing_designs.rolling import _2144
            
            return self._parent._cast(_2144.MultiPointContactBallBearing)

        @property
        def needle_roller_bearing(self):
            from mastapy.bearings.bearing_designs.rolling import _2145
            
            return self._parent._cast(_2145.NeedleRollerBearing)

        @property
        def non_barrel_roller_bearing(self):
            from mastapy.bearings.bearing_designs.rolling import _2146
            
            return self._parent._cast(_2146.NonBarrelRollerBearing)

        @property
        def roller_bearing(self):
            from mastapy.bearings.bearing_designs.rolling import _2147
            
            return self._parent._cast(_2147.RollerBearing)

        @property
        def rolling_bearing(self):
            from mastapy.bearings.bearing_designs.rolling import _2150
            
            return self._parent._cast(_2150.RollingBearing)

        @property
        def self_aligning_ball_bearing(self):
            from mastapy.bearings.bearing_designs.rolling import _2151
            
            return self._parent._cast(_2151.SelfAligningBallBearing)

        @property
        def spherical_roller_bearing(self):
            from mastapy.bearings.bearing_designs.rolling import _2154
            
            return self._parent._cast(_2154.SphericalRollerBearing)

        @property
        def spherical_roller_thrust_bearing(self):
            from mastapy.bearings.bearing_designs.rolling import _2155
            
            return self._parent._cast(_2155.SphericalRollerThrustBearing)

        @property
        def taper_roller_bearing(self):
            from mastapy.bearings.bearing_designs.rolling import _2156
            
            return self._parent._cast(_2156.TaperRollerBearing)

        @property
        def three_point_contact_ball_bearing(self):
            from mastapy.bearings.bearing_designs.rolling import _2157
            
            return self._parent._cast(_2157.ThreePointContactBallBearing)

        @property
        def thrust_ball_bearing(self):
            from mastapy.bearings.bearing_designs.rolling import _2158
            
            return self._parent._cast(_2158.ThrustBallBearing)

        @property
        def toroidal_roller_bearing(self):
            from mastapy.bearings.bearing_designs.rolling import _2159
            
            return self._parent._cast(_2159.ToroidalRollerBearing)

        @property
        def pad_fluid_film_bearing(self):
            from mastapy.bearings.bearing_designs.fluid_film import _2172
            
            return self._parent._cast(_2172.PadFluidFilmBearing)

        @property
        def plain_grease_filled_journal_bearing(self):
            from mastapy.bearings.bearing_designs.fluid_film import _2174
            
            return self._parent._cast(_2174.PlainGreaseFilledJournalBearing)

        @property
        def plain_journal_bearing(self):
            from mastapy.bearings.bearing_designs.fluid_film import _2176
            
            return self._parent._cast(_2176.PlainJournalBearing)

        @property
        def plain_oil_fed_journal_bearing(self):
            from mastapy.bearings.bearing_designs.fluid_film import _2178
            
            return self._parent._cast(_2178.PlainOilFedJournalBearing)

        @property
        def tilting_pad_journal_bearing(self):
            from mastapy.bearings.bearing_designs.fluid_film import _2179
            
            return self._parent._cast(_2179.TiltingPadJournalBearing)

        @property
        def tilting_pad_thrust_bearing(self):
            from mastapy.bearings.bearing_designs.fluid_film import _2180
            
            return self._parent._cast(_2180.TiltingPadThrustBearing)

        @property
        def concept_axial_clearance_bearing(self):
            from mastapy.bearings.bearing_designs.concept import _2182
            
            return self._parent._cast(_2182.ConceptAxialClearanceBearing)

        @property
        def concept_clearance_bearing(self):
            from mastapy.bearings.bearing_designs.concept import _2183
            
            return self._parent._cast(_2183.ConceptClearanceBearing)

        @property
        def concept_radial_clearance_bearing(self):
            from mastapy.bearings.bearing_designs.concept import _2184
            
            return self._parent._cast(_2184.ConceptRadialClearanceBearing)

        @property
        def non_linear_bearing(self) -> 'NonLinearBearing':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'NonLinearBearing.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'NonLinearBearing._Cast_NonLinearBearing':
        return self._Cast_NonLinearBearing(self)
