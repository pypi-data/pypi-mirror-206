"""_2019.py

LoadedRollingBearingRow
"""
from typing import List

from PIL.Image import Image

from mastapy._internal import constructor, conversion
from mastapy.utility_gui.charts import _1852
from mastapy.bearings.bearing_results.rolling import (
    _2018, _1958, _1999, _2017,
    _2053, _2058
)
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_ROLLING_BEARING_ROW = python_net_import('SMT.MastaAPI.Bearings.BearingResults.Rolling', 'LoadedRollingBearingRow')


__docformat__ = 'restructuredtext en'
__all__ = ('LoadedRollingBearingRow',)


class LoadedRollingBearingRow(_0.APIBase):
    """LoadedRollingBearingRow

    This is a mastapy class.
    """

    TYPE = _LOADED_ROLLING_BEARING_ROW

    class _Cast_LoadedRollingBearingRow:
        """Special nested class for casting LoadedRollingBearingRow to subclasses."""

        def __init__(self, parent: 'LoadedRollingBearingRow'):
            self._parent = parent

        @property
        def loaded_angular_contact_ball_bearing_row(self):
            from mastapy.bearings.bearing_results.rolling import _1969
            
            return self._parent._cast(_1969.LoadedAngularContactBallBearingRow)

        @property
        def loaded_angular_contact_thrust_ball_bearing_row(self):
            from mastapy.bearings.bearing_results.rolling import _1972
            
            return self._parent._cast(_1972.LoadedAngularContactThrustBallBearingRow)

        @property
        def loaded_asymmetric_spherical_roller_bearing_row(self):
            from mastapy.bearings.bearing_results.rolling import _1975
            
            return self._parent._cast(_1975.LoadedAsymmetricSphericalRollerBearingRow)

        @property
        def loaded_axial_thrust_cylindrical_roller_bearing_row(self):
            from mastapy.bearings.bearing_results.rolling import _1980
            
            return self._parent._cast(_1980.LoadedAxialThrustCylindricalRollerBearingRow)

        @property
        def loaded_axial_thrust_needle_roller_bearing_row(self):
            from mastapy.bearings.bearing_results.rolling import _1983
            
            return self._parent._cast(_1983.LoadedAxialThrustNeedleRollerBearingRow)

        @property
        def loaded_ball_bearing_row(self):
            from mastapy.bearings.bearing_results.rolling import _1988
            
            return self._parent._cast(_1988.LoadedBallBearingRow)

        @property
        def loaded_crossed_roller_bearing_row(self):
            from mastapy.bearings.bearing_results.rolling import _1991
            
            return self._parent._cast(_1991.LoadedCrossedRollerBearingRow)

        @property
        def loaded_cylindrical_roller_bearing_row(self):
            from mastapy.bearings.bearing_results.rolling import _1995
            
            return self._parent._cast(_1995.LoadedCylindricalRollerBearingRow)

        @property
        def loaded_deep_groove_ball_bearing_row(self):
            from mastapy.bearings.bearing_results.rolling import _1998
            
            return self._parent._cast(_1998.LoadedDeepGrooveBallBearingRow)

        @property
        def loaded_four_point_contact_ball_bearing_row(self):
            from mastapy.bearings.bearing_results.rolling import _2003
            
            return self._parent._cast(_2003.LoadedFourPointContactBallBearingRow)

        @property
        def loaded_needle_roller_bearing_row(self):
            from mastapy.bearings.bearing_results.rolling import _2007
            
            return self._parent._cast(_2007.LoadedNeedleRollerBearingRow)

        @property
        def loaded_non_barrel_roller_bearing_row(self):
            from mastapy.bearings.bearing_results.rolling import _2010
            
            return self._parent._cast(_2010.LoadedNonBarrelRollerBearingRow)

        @property
        def loaded_roller_bearing_row(self):
            from mastapy.bearings.bearing_results.rolling import _2015
            
            return self._parent._cast(_2015.LoadedRollerBearingRow)

        @property
        def loaded_self_aligning_ball_bearing_row(self):
            from mastapy.bearings.bearing_results.rolling import _2022
            
            return self._parent._cast(_2022.LoadedSelfAligningBallBearingRow)

        @property
        def loaded_spherical_roller_radial_bearing_row(self):
            from mastapy.bearings.bearing_results.rolling import _2026
            
            return self._parent._cast(_2026.LoadedSphericalRollerRadialBearingRow)

        @property
        def loaded_spherical_roller_thrust_bearing_row(self):
            from mastapy.bearings.bearing_results.rolling import _2029
            
            return self._parent._cast(_2029.LoadedSphericalRollerThrustBearingRow)

        @property
        def loaded_taper_roller_bearing_row(self):
            from mastapy.bearings.bearing_results.rolling import _2034
            
            return self._parent._cast(_2034.LoadedTaperRollerBearingRow)

        @property
        def loaded_three_point_contact_ball_bearing_row(self):
            from mastapy.bearings.bearing_results.rolling import _2037
            
            return self._parent._cast(_2037.LoadedThreePointContactBallBearingRow)

        @property
        def loaded_thrust_ball_bearing_row(self):
            from mastapy.bearings.bearing_results.rolling import _2040
            
            return self._parent._cast(_2040.LoadedThrustBallBearingRow)

        @property
        def loaded_toroidal_roller_bearing_row(self):
            from mastapy.bearings.bearing_results.rolling import _2043
            
            return self._parent._cast(_2043.LoadedToroidalRollerBearingRow)

        @property
        def loaded_rolling_bearing_row(self) -> 'LoadedRollingBearingRow':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'LoadedRollingBearingRow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def dynamic_equivalent_reference_load(self) -> 'float':
        """float: 'DynamicEquivalentReferenceLoad' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DynamicEquivalentReferenceLoad

        if temp is None:
            return 0.0

        return temp

    @property
    def life_modification_factor_for_systems_approach(self) -> 'float':
        """float: 'LifeModificationFactorForSystemsApproach' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LifeModificationFactorForSystemsApproach

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_element_normal_stress(self) -> 'float':
        """float: 'MaximumElementNormalStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumElementNormalStress

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_element_normal_stress_inner(self) -> 'float':
        """float: 'MaximumElementNormalStressInner' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumElementNormalStressInner

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_element_normal_stress_outer(self) -> 'float':
        """float: 'MaximumElementNormalStressOuter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumElementNormalStressOuter

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_normal_load_inner(self) -> 'float':
        """float: 'MaximumNormalLoadInner' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumNormalLoadInner

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_normal_load_outer(self) -> 'float':
        """float: 'MaximumNormalLoadOuter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumNormalLoadOuter

        if temp is None:
            return 0.0

        return temp

    @property
    def normal_contact_stress_chart_inner(self) -> 'Image':
        """Image: 'NormalContactStressChartInner' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NormalContactStressChartInner

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)
        return value

    @property
    def normal_contact_stress_chart_left(self) -> 'Image':
        """Image: 'NormalContactStressChartLeft' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NormalContactStressChartLeft

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)
        return value

    @property
    def normal_contact_stress_chart_outer(self) -> 'Image':
        """Image: 'NormalContactStressChartOuter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NormalContactStressChartOuter

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)
        return value

    @property
    def normal_contact_stress_chart_right(self) -> 'Image':
        """Image: 'NormalContactStressChartRight' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NormalContactStressChartRight

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)
        return value

    @property
    def row_id(self) -> 'str':
        """str: 'RowID' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RowID

        if temp is None:
            return ''

        return temp

    @property
    def subsurface_shear_stress_chart_inner(self) -> '_1852.TwoDChartDefinition':
        """TwoDChartDefinition: 'SubsurfaceShearStressChartInner' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SubsurfaceShearStressChartInner

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def subsurface_shear_stress_chart_outer(self) -> '_1852.TwoDChartDefinition':
        """TwoDChartDefinition: 'SubsurfaceShearStressChartOuter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SubsurfaceShearStressChartOuter

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def loaded_bearing(self) -> '_2018.LoadedRollingBearingResults':
        """LoadedRollingBearingResults: 'LoadedBearing' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LoadedBearing

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def maximum_operating_internal_clearance(self) -> '_1958.InternalClearance':
        """InternalClearance: 'MaximumOperatingInternalClearance' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumOperatingInternalClearance

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def minimum_operating_internal_clearance(self) -> '_1958.InternalClearance':
        """InternalClearance: 'MinimumOperatingInternalClearance' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MinimumOperatingInternalClearance

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def elements(self) -> 'List[_1999.LoadedElement]':
        """List[LoadedElement]: 'Elements' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Elements

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def race_results(self) -> 'List[_2017.LoadedRollingBearingRaceResults]':
        """List[LoadedRollingBearingRaceResults]: 'RaceResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RaceResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def ring_force_and_displacement_results(self) -> 'List[_2053.RingForceAndDisplacement]':
        """List[RingForceAndDisplacement]: 'RingForceAndDisplacementResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RingForceAndDisplacementResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def subsurface_shear_stress_for_most_heavily_loaded_element_inner(self) -> 'List[_2058.StressAtPosition]':
        """List[StressAtPosition]: 'SubsurfaceShearStressForMostHeavilyLoadedElementInner' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SubsurfaceShearStressForMostHeavilyLoadedElementInner

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def subsurface_shear_stress_for_most_heavily_loaded_element_outer(self) -> 'List[_2058.StressAtPosition]':
        """List[StressAtPosition]: 'SubsurfaceShearStressForMostHeavilyLoadedElementOuter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SubsurfaceShearStressForMostHeavilyLoadedElementOuter

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

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
    def cast_to(self) -> 'LoadedRollingBearingRow._Cast_LoadedRollingBearingRow':
        return self._Cast_LoadedRollingBearingRow(self)
