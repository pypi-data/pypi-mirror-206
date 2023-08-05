"""_2115.py

BearingDesign
"""
from typing import List

from mastapy._internal import constructor, conversion
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.math_utility import _1506
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEARING_DESIGN = python_net_import('SMT.MastaAPI.Bearings.BearingDesigns', 'BearingDesign')


__docformat__ = 'restructuredtext en'
__all__ = ('BearingDesign',)


class BearingDesign(_0.APIBase):
    """BearingDesign

    This is a mastapy class.
    """

    TYPE = _BEARING_DESIGN

    class _Cast_BearingDesign:
        """Special nested class for casting BearingDesign to subclasses."""

        def __init__(self, parent: 'BearingDesign'):
            self._parent = parent

        @property
        def detailed_bearing(self):
            from mastapy.bearings.bearing_designs import _2116
            
            return self._parent._cast(_2116.DetailedBearing)

        @property
        def dummy_rolling_bearing(self):
            from mastapy.bearings.bearing_designs import _2117
            
            return self._parent._cast(_2117.DummyRollingBearing)

        @property
        def linear_bearing(self):
            from mastapy.bearings.bearing_designs import _2118
            
            return self._parent._cast(_2118.LinearBearing)

        @property
        def non_linear_bearing(self):
            from mastapy.bearings.bearing_designs import _2119
            
            return self._parent._cast(_2119.NonLinearBearing)

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
        def bearing_design(self) -> 'BearingDesign':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'BearingDesign.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def bore(self) -> 'float':
        """float: 'Bore' is the original name of this property."""

        temp = self.wrapped.Bore

        if temp is None:
            return 0.0

        return temp

    @bore.setter
    def bore(self, value: 'float'):
        self.wrapped.Bore = float(value) if value else 0.0

    @property
    def mass(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'Mass' is the original name of this property."""

        temp = self.wrapped.Mass

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @mass.setter
    def mass(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.Mass = value

    @property
    def outer_diameter(self) -> 'float':
        """float: 'OuterDiameter' is the original name of this property."""

        temp = self.wrapped.OuterDiameter

        if temp is None:
            return 0.0

        return temp

    @outer_diameter.setter
    def outer_diameter(self, value: 'float'):
        self.wrapped.OuterDiameter = float(value) if value else 0.0

    @property
    def type_(self) -> 'str':
        """str: 'Type' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Type

        if temp is None:
            return ''

        return temp

    @property
    def width(self) -> 'float':
        """float: 'Width' is the original name of this property."""

        temp = self.wrapped.Width

        if temp is None:
            return 0.0

        return temp

    @width.setter
    def width(self, value: 'float'):
        self.wrapped.Width = float(value) if value else 0.0

    @property
    def mass_properties_of_elements_from_geometry(self) -> '_1506.MassProperties':
        """MassProperties: 'MassPropertiesOfElementsFromGeometry' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MassPropertiesOfElementsFromGeometry

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def mass_properties_of_inner_ring_from_geometry(self) -> '_1506.MassProperties':
        """MassProperties: 'MassPropertiesOfInnerRingFromGeometry' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MassPropertiesOfInnerRingFromGeometry

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def mass_properties_of_outer_ring_from_geometry(self) -> '_1506.MassProperties':
        """MassProperties: 'MassPropertiesOfOuterRingFromGeometry' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MassPropertiesOfOuterRingFromGeometry

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def total_mass_properties(self) -> '_1506.MassProperties':
        """MassProperties: 'TotalMassProperties' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TotalMassProperties

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def report_names(self) -> 'List[str]':
        """List[str]: 'ReportNames' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ReportNames

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, str)
        return value

    def output_default_report_to(self, file_path: 'str'):
        """ 'OutputDefaultReportTo' is the original name of this method.

        Args:
            file_path (str)
        """

        file_path = str(file_path)
        self.wrapped.OutputDefaultReportTo(file_path if file_path else '')

    def get_default_report_with_encoded_images(self) -> 'str':
        """ 'GetDefaultReportWithEncodedImages' is the original name of this method.

        Returns:
            str
        """

        method_result = self.wrapped.GetDefaultReportWithEncodedImages()
        return method_result

    def output_active_report_to(self, file_path: 'str'):
        """ 'OutputActiveReportTo' is the original name of this method.

        Args:
            file_path (str)
        """

        file_path = str(file_path)
        self.wrapped.OutputActiveReportTo(file_path if file_path else '')

    def output_active_report_as_text_to(self, file_path: 'str'):
        """ 'OutputActiveReportAsTextTo' is the original name of this method.

        Args:
            file_path (str)
        """

        file_path = str(file_path)
        self.wrapped.OutputActiveReportAsTextTo(file_path if file_path else '')

    def get_active_report_with_encoded_images(self) -> 'str':
        """ 'GetActiveReportWithEncodedImages' is the original name of this method.

        Returns:
            str
        """

        method_result = self.wrapped.GetActiveReportWithEncodedImages()
        return method_result

    def output_named_report_to(self, report_name: 'str', file_path: 'str'):
        """ 'OutputNamedReportTo' is the original name of this method.

        Args:
            report_name (str)
            file_path (str)
        """

        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportTo(report_name if report_name else '', file_path if file_path else '')

    def output_named_report_as_masta_report(self, report_name: 'str', file_path: 'str'):
        """ 'OutputNamedReportAsMastaReport' is the original name of this method.

        Args:
            report_name (str)
            file_path (str)
        """

        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsMastaReport(report_name if report_name else '', file_path if file_path else '')

    def output_named_report_as_text_to(self, report_name: 'str', file_path: 'str'):
        """ 'OutputNamedReportAsTextTo' is the original name of this method.

        Args:
            report_name (str)
            file_path (str)
        """

        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsTextTo(report_name if report_name else '', file_path if file_path else '')

    def get_named_report_with_encoded_images(self, report_name: 'str') -> 'str':
        """ 'GetNamedReportWithEncodedImages' is the original name of this method.

        Args:
            report_name (str)

        Returns:
            str
        """

        report_name = str(report_name)
        method_result = self.wrapped.GetNamedReportWithEncodedImages(report_name if report_name else '')
        return method_result

    @property
    def cast_to(self) -> 'BearingDesign._Cast_BearingDesign':
        return self._Cast_BearingDesign(self)
