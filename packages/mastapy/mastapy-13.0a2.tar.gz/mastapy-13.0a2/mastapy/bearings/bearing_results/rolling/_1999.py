"""_1999.py

LoadedElement
"""
from typing import List

from mastapy._internal import constructor, conversion
from mastapy.bearings.bearing_results import _1929
from mastapy.bearings.bearing_results.rolling import _1958, _2058
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_ELEMENT = python_net_import('SMT.MastaAPI.Bearings.BearingResults.Rolling', 'LoadedElement')


__docformat__ = 'restructuredtext en'
__all__ = ('LoadedElement',)


class LoadedElement(_0.APIBase):
    """LoadedElement

    This is a mastapy class.
    """

    TYPE = _LOADED_ELEMENT

    class _Cast_LoadedElement:
        """Special nested class for casting LoadedElement to subclasses."""

        def __init__(self, parent: 'LoadedElement'):
            self._parent = parent

        @property
        def loaded_angular_contact_ball_bearing_element(self):
            from mastapy.bearings.bearing_results.rolling import _1967
            
            return self._parent._cast(_1967.LoadedAngularContactBallBearingElement)

        @property
        def loaded_angular_contact_thrust_ball_bearing_element(self):
            from mastapy.bearings.bearing_results.rolling import _1970
            
            return self._parent._cast(_1970.LoadedAngularContactThrustBallBearingElement)

        @property
        def loaded_asymmetric_spherical_roller_bearing_element(self):
            from mastapy.bearings.bearing_results.rolling import _1973
            
            return self._parent._cast(_1973.LoadedAsymmetricSphericalRollerBearingElement)

        @property
        def loaded_axial_thrust_cylindrical_roller_bearing_element(self):
            from mastapy.bearings.bearing_results.rolling import _1978
            
            return self._parent._cast(_1978.LoadedAxialThrustCylindricalRollerBearingElement)

        @property
        def loaded_axial_thrust_needle_roller_bearing_element(self):
            from mastapy.bearings.bearing_results.rolling import _1981
            
            return self._parent._cast(_1981.LoadedAxialThrustNeedleRollerBearingElement)

        @property
        def loaded_ball_bearing_element(self):
            from mastapy.bearings.bearing_results.rolling import _1985
            
            return self._parent._cast(_1985.LoadedBallBearingElement)

        @property
        def loaded_crossed_roller_bearing_element(self):
            from mastapy.bearings.bearing_results.rolling import _1989
            
            return self._parent._cast(_1989.LoadedCrossedRollerBearingElement)

        @property
        def loaded_cylindrical_roller_bearing_element(self):
            from mastapy.bearings.bearing_results.rolling import _1993
            
            return self._parent._cast(_1993.LoadedCylindricalRollerBearingElement)

        @property
        def loaded_deep_groove_ball_bearing_element(self):
            from mastapy.bearings.bearing_results.rolling import _1996
            
            return self._parent._cast(_1996.LoadedDeepGrooveBallBearingElement)

        @property
        def loaded_four_point_contact_ball_bearing_element(self):
            from mastapy.bearings.bearing_results.rolling import _2000
            
            return self._parent._cast(_2000.LoadedFourPointContactBallBearingElement)

        @property
        def loaded_multi_point_contact_ball_bearing_element(self):
            from mastapy.bearings.bearing_results.rolling import _2004
            
            return self._parent._cast(_2004.LoadedMultiPointContactBallBearingElement)

        @property
        def loaded_needle_roller_bearing_element(self):
            from mastapy.bearings.bearing_results.rolling import _2005
            
            return self._parent._cast(_2005.LoadedNeedleRollerBearingElement)

        @property
        def loaded_non_barrel_roller_element(self):
            from mastapy.bearings.bearing_results.rolling import _2012
            
            return self._parent._cast(_2012.LoadedNonBarrelRollerElement)

        @property
        def loaded_roller_bearing_element(self):
            from mastapy.bearings.bearing_results.rolling import _2013
            
            return self._parent._cast(_2013.LoadedRollerBearingElement)

        @property
        def loaded_self_aligning_ball_bearing_element(self):
            from mastapy.bearings.bearing_results.rolling import _2020
            
            return self._parent._cast(_2020.LoadedSelfAligningBallBearingElement)

        @property
        def loaded_spherical_radial_roller_bearing_element(self):
            from mastapy.bearings.bearing_results.rolling import _2023
            
            return self._parent._cast(_2023.LoadedSphericalRadialRollerBearingElement)

        @property
        def loaded_spherical_roller_bearing_element(self):
            from mastapy.bearings.bearing_results.rolling import _2024
            
            return self._parent._cast(_2024.LoadedSphericalRollerBearingElement)

        @property
        def loaded_spherical_thrust_roller_bearing_element(self):
            from mastapy.bearings.bearing_results.rolling import _2030
            
            return self._parent._cast(_2030.LoadedSphericalThrustRollerBearingElement)

        @property
        def loaded_taper_roller_bearing_element(self):
            from mastapy.bearings.bearing_results.rolling import _2032
            
            return self._parent._cast(_2032.LoadedTaperRollerBearingElement)

        @property
        def loaded_three_point_contact_ball_bearing_element(self):
            from mastapy.bearings.bearing_results.rolling import _2035
            
            return self._parent._cast(_2035.LoadedThreePointContactBallBearingElement)

        @property
        def loaded_thrust_ball_bearing_element(self):
            from mastapy.bearings.bearing_results.rolling import _2038
            
            return self._parent._cast(_2038.LoadedThrustBallBearingElement)

        @property
        def loaded_toroidal_roller_bearing_element(self):
            from mastapy.bearings.bearing_results.rolling import _2041
            
            return self._parent._cast(_2041.LoadedToroidalRollerBearingElement)

        @property
        def loaded_element(self) -> 'LoadedElement':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'LoadedElement.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def angle(self) -> 'float':
        """float: 'Angle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Angle

        if temp is None:
            return 0.0

        return temp

    @property
    def axial_loading(self) -> 'float':
        """float: 'AxialLoading' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AxialLoading

        if temp is None:
            return 0.0

        return temp

    @property
    def element_id(self) -> 'str':
        """str: 'ElementId' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ElementId

        if temp is None:
            return ''

        return temp

    @property
    def element_raceway_contact_area_inner(self) -> 'float':
        """float: 'ElementRacewayContactAreaInner' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ElementRacewayContactAreaInner

        if temp is None:
            return 0.0

        return temp

    @property
    def element_raceway_contact_area_left(self) -> 'float':
        """float: 'ElementRacewayContactAreaLeft' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ElementRacewayContactAreaLeft

        if temp is None:
            return 0.0

        return temp

    @property
    def element_raceway_contact_area_outer(self) -> 'float':
        """float: 'ElementRacewayContactAreaOuter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ElementRacewayContactAreaOuter

        if temp is None:
            return 0.0

        return temp

    @property
    def element_raceway_contact_area_right(self) -> 'float':
        """float: 'ElementRacewayContactAreaRight' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ElementRacewayContactAreaRight

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_normal_stress(self) -> 'float':
        """float: 'MaximumNormalStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumNormalStress

        if temp is None:
            return 0.0

        return temp

    @property
    def minimum_lubricating_film_thickness_inner(self) -> 'float':
        """float: 'MinimumLubricatingFilmThicknessInner' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MinimumLubricatingFilmThicknessInner

        if temp is None:
            return 0.0

        return temp

    @property
    def minimum_lubricating_film_thickness_outer(self) -> 'float':
        """float: 'MinimumLubricatingFilmThicknessOuter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MinimumLubricatingFilmThicknessOuter

        if temp is None:
            return 0.0

        return temp

    @property
    def normal_load_inner(self) -> 'float':
        """float: 'NormalLoadInner' is the original name of this property."""

        temp = self.wrapped.NormalLoadInner

        if temp is None:
            return 0.0

        return temp

    @normal_load_inner.setter
    def normal_load_inner(self, value: 'float'):
        self.wrapped.NormalLoadInner = float(value) if value else 0.0

    @property
    def normal_load_outer(self) -> 'float':
        """float: 'NormalLoadOuter' is the original name of this property."""

        temp = self.wrapped.NormalLoadOuter

        if temp is None:
            return 0.0

        return temp

    @normal_load_outer.setter
    def normal_load_outer(self, value: 'float'):
        self.wrapped.NormalLoadOuter = float(value) if value else 0.0

    @property
    def race_deflection_inner(self) -> 'float':
        """float: 'RaceDeflectionInner' is the original name of this property."""

        temp = self.wrapped.RaceDeflectionInner

        if temp is None:
            return 0.0

        return temp

    @race_deflection_inner.setter
    def race_deflection_inner(self, value: 'float'):
        self.wrapped.RaceDeflectionInner = float(value) if value else 0.0

    @property
    def race_deflection_outer(self) -> 'float':
        """float: 'RaceDeflectionOuter' is the original name of this property."""

        temp = self.wrapped.RaceDeflectionOuter

        if temp is None:
            return 0.0

        return temp

    @race_deflection_outer.setter
    def race_deflection_outer(self, value: 'float'):
        self.wrapped.RaceDeflectionOuter = float(value) if value else 0.0

    @property
    def race_deflection_total(self) -> 'float':
        """float: 'RaceDeflectionTotal' is the original name of this property."""

        temp = self.wrapped.RaceDeflectionTotal

        if temp is None:
            return 0.0

        return temp

    @race_deflection_total.setter
    def race_deflection_total(self, value: 'float'):
        self.wrapped.RaceDeflectionTotal = float(value) if value else 0.0

    @property
    def race_separation_at_element_axial(self) -> 'float':
        """float: 'RaceSeparationAtElementAxial' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RaceSeparationAtElementAxial

        if temp is None:
            return 0.0

        return temp

    @property
    def race_separation_at_element_radial(self) -> 'float':
        """float: 'RaceSeparationAtElementRadial' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RaceSeparationAtElementRadial

        if temp is None:
            return 0.0

        return temp

    @property
    def force_from_inner_race(self) -> '_1929.ElementForce':
        """ElementForce: 'ForceFromInnerRace' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ForceFromInnerRace

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def operating_internal_clearance(self) -> '_1958.InternalClearance':
        """InternalClearance: 'OperatingInternalClearance' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OperatingInternalClearance

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def subsurface_shear_stress_distribution_inner(self) -> 'List[_2058.StressAtPosition]':
        """List[StressAtPosition]: 'SubsurfaceShearStressDistributionInner' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SubsurfaceShearStressDistributionInner

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def subsurface_shear_stress_distribution_outer(self) -> 'List[_2058.StressAtPosition]':
        """List[StressAtPosition]: 'SubsurfaceShearStressDistributionOuter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SubsurfaceShearStressDistributionOuter

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
    def cast_to(self) -> 'LoadedElement._Cast_LoadedElement':
        return self._Cast_LoadedElement(self)
