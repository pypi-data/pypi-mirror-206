"""_1015.py

CylindricalGearMicroGeometrySettings
"""
from mastapy.gears.micro_geometry import _566
from mastapy._internal import enum_with_selected_value_runtime, constructor, conversion
from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1116
from mastapy.gears.gear_designs.cylindrical import _1039
from mastapy.utility import _1575
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_MICRO_GEOMETRY_SETTINGS = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Cylindrical', 'CylindricalGearMicroGeometrySettings')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearMicroGeometrySettings',)


class CylindricalGearMicroGeometrySettings(_1575.IndependentReportablePropertiesBase['CylindricalGearMicroGeometrySettings']):
    """CylindricalGearMicroGeometrySettings

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_MICRO_GEOMETRY_SETTINGS

    class _Cast_CylindricalGearMicroGeometrySettings:
        """Special nested class for casting CylindricalGearMicroGeometrySettings to subclasses."""

        def __init__(self, parent: 'CylindricalGearMicroGeometrySettings'):
            self._parent = parent

        @property
        def independent_reportable_properties_base(self):
            from mastapy.gears.gear_designs.cylindrical import _1015
            
            return self._parent._cast(_1575.IndependentReportablePropertiesBase)

        @property
        def cylindrical_gear_micro_geometry_settings(self) -> 'CylindricalGearMicroGeometrySettings':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CylindricalGearMicroGeometrySettings.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def flank_side_with_zero_face_width(self) -> '_566.FlankSide':
        """FlankSide: 'FlankSideWithZeroFaceWidth' is the original name of this property."""

        temp = self.wrapped.FlankSideWithZeroFaceWidth

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, _566.FlankSide)
        return constructor.new_from_mastapy_type(_566.FlankSide)(value) if value is not None else None

    @flank_side_with_zero_face_width.setter
    def flank_side_with_zero_face_width(self, value: '_566.FlankSide'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value, _566.FlankSide.type_())
        self.wrapped.FlankSideWithZeroFaceWidth = value

    @property
    def micro_geometry_lead_tolerance_chart_view(self) -> '_1116.MicroGeometryLeadToleranceChartView':
        """MicroGeometryLeadToleranceChartView: 'MicroGeometryLeadToleranceChartView' is the original name of this property."""

        temp = self.wrapped.MicroGeometryLeadToleranceChartView

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, _1116.MicroGeometryLeadToleranceChartView)
        return constructor.new_from_mastapy_type(_1116.MicroGeometryLeadToleranceChartView)(value) if value is not None else None

    @micro_geometry_lead_tolerance_chart_view.setter
    def micro_geometry_lead_tolerance_chart_view(self, value: '_1116.MicroGeometryLeadToleranceChartView'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value, _1116.MicroGeometryLeadToleranceChartView.type_())
        self.wrapped.MicroGeometryLeadToleranceChartView = value

    @property
    def scale_and_range_of_flank_relief_axes_for_micro_geometry_tolerance_charts(self) -> '_1039.DoubleAxisScaleAndRange':
        """DoubleAxisScaleAndRange: 'ScaleAndRangeOfFlankReliefAxesForMicroGeometryToleranceCharts' is the original name of this property."""

        temp = self.wrapped.ScaleAndRangeOfFlankReliefAxesForMicroGeometryToleranceCharts

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, _1039.DoubleAxisScaleAndRange)
        return constructor.new_from_mastapy_type(_1039.DoubleAxisScaleAndRange)(value) if value is not None else None

    @scale_and_range_of_flank_relief_axes_for_micro_geometry_tolerance_charts.setter
    def scale_and_range_of_flank_relief_axes_for_micro_geometry_tolerance_charts(self, value: '_1039.DoubleAxisScaleAndRange'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value, _1039.DoubleAxisScaleAndRange.type_())
        self.wrapped.ScaleAndRangeOfFlankReliefAxesForMicroGeometryToleranceCharts = value

    @property
    def cast_to(self) -> 'CylindricalGearMicroGeometrySettings._Cast_CylindricalGearMicroGeometrySettings':
        return self._Cast_CylindricalGearMicroGeometrySettings(self)
