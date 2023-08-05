"""_836.py

GearMeshLoadDistributionAnalysis
"""
from typing import List

from mastapy._internal import constructor, conversion
from mastapy.math_utility import _1501
from mastapy.gears.ltca import _837, _835
from mastapy.gears import _322
from mastapy.nodal_analysis import _86
from mastapy._internal.python_net import python_net_import
from mastapy.gears.analysis import _1217
from mastapy._internal.cast_exception import CastException

_GEAR_LOAD_DISTRIBUTION_ANALYSIS = python_net_import('SMT.MastaAPI.Gears.LTCA', 'GearLoadDistributionAnalysis')
_GEAR_MESH_LOAD_DISTRIBUTION_ANALYSIS = python_net_import('SMT.MastaAPI.Gears.LTCA', 'GearMeshLoadDistributionAnalysis')
_GEAR_FLANKS = python_net_import('SMT.MastaAPI.Gears', 'GearFlanks')
_STRESS_RESULTS_TYPE = python_net_import('SMT.MastaAPI.NodalAnalysis', 'StressResultsType')


__docformat__ = 'restructuredtext en'
__all__ = ('GearMeshLoadDistributionAnalysis',)


class GearMeshLoadDistributionAnalysis(_1217.GearMeshImplementationAnalysis):
    """GearMeshLoadDistributionAnalysis

    This is a mastapy class.
    """

    TYPE = _GEAR_MESH_LOAD_DISTRIBUTION_ANALYSIS

    class _Cast_GearMeshLoadDistributionAnalysis:
        """Special nested class for casting GearMeshLoadDistributionAnalysis to subclasses."""

        def __init__(self, parent: 'GearMeshLoadDistributionAnalysis'):
            self._parent = parent

        @property
        def gear_mesh_implementation_analysis(self):
            return self._parent._cast(_1217.GearMeshImplementationAnalysis)

        @property
        def gear_mesh_design_analysis(self):
            from mastapy.gears.analysis import _1216
            
            return self._parent._cast(_1216.GearMeshDesignAnalysis)

        @property
        def abstract_gear_mesh_analysis(self):
            from mastapy.gears.analysis import _1210
            
            return self._parent._cast(_1210.AbstractGearMeshAnalysis)

        @property
        def cylindrical_gear_mesh_load_distribution_analysis(self):
            from mastapy.gears.ltca.cylindrical import _852
            
            return self._parent._cast(_852.CylindricalGearMeshLoadDistributionAnalysis)

        @property
        def conical_mesh_load_distribution_analysis(self):
            from mastapy.gears.ltca.conical import _865
            
            return self._parent._cast(_865.ConicalMeshLoadDistributionAnalysis)

        @property
        def gear_mesh_load_distribution_analysis(self) -> 'GearMeshLoadDistributionAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GearMeshLoadDistributionAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def actual_total_contact_ratio(self) -> 'float':
        """float: 'ActualTotalContactRatio' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ActualTotalContactRatio

        if temp is None:
            return 0.0

        return temp

    @property
    def analysis_name(self) -> 'str':
        """str: 'AnalysisName' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AnalysisName

        if temp is None:
            return ''

        return temp

    @property
    def index_of_roll_angle_with_maximum_contact_stress(self) -> 'int':
        """int: 'IndexOfRollAngleWithMaximumContactStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.IndexOfRollAngleWithMaximumContactStress

        if temp is None:
            return 0

        return temp

    @property
    def is_advanced_ltca(self) -> 'bool':
        """bool: 'IsAdvancedLTCA' is the original name of this property."""

        temp = self.wrapped.IsAdvancedLTCA

        if temp is None:
            return False

        return temp

    @is_advanced_ltca.setter
    def is_advanced_ltca(self, value: 'bool'):
        self.wrapped.IsAdvancedLTCA = bool(value) if value else False

    @property
    def load_case_name(self) -> 'str':
        """str: 'LoadCaseName' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LoadCaseName

        if temp is None:
            return ''

        return temp

    @property
    def maximum_contact_stress(self) -> 'float':
        """float: 'MaximumContactStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumContactStress

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_force_per_unit_length(self) -> 'float':
        """float: 'MaximumForcePerUnitLength' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumForcePerUnitLength

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_pressure_velocity(self) -> 'float':
        """float: 'MaximumPressureVelocity' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumPressureVelocity

        if temp is None:
            return 0.0

        return temp

    @property
    def minimum_force_per_unit_length(self) -> 'float':
        """float: 'MinimumForcePerUnitLength' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MinimumForcePerUnitLength

        if temp is None:
            return 0.0

        return temp

    @property
    def number_of_roll_angles(self) -> 'int':
        """int: 'NumberOfRollAngles' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NumberOfRollAngles

        if temp is None:
            return 0

        return temp

    @property
    def peakto_peak_moment_about_centre(self) -> 'float':
        """float: 'PeaktoPeakMomentAboutCentre' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PeaktoPeakMomentAboutCentre

        if temp is None:
            return 0.0

        return temp

    @property
    def moment_about_centre_fourier_series(self) -> '_1501.FourierSeries':
        """FourierSeries: 'MomentAboutCentreFourierSeries' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MomentAboutCentreFourierSeries

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def transmission_error_fourier_series(self) -> '_1501.FourierSeries':
        """FourierSeries: 'TransmissionErrorFourierSeries' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TransmissionErrorFourierSeries

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def load_distribution_analyses_at_single_rotation(self) -> 'List[_837.GearMeshLoadDistributionAtRotation]':
        """List[GearMeshLoadDistributionAtRotation]: 'LoadDistributionAnalysesAtSingleRotation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LoadDistributionAnalysesAtSingleRotation

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    def maximum_root_stress_with_flanks(self, gear: '_835.GearLoadDistributionAnalysis', flank: '_322.GearFlanks', stress_type: '_86.StressResultsType') -> 'float':
        """ 'MaximumRootStress' is the original name of this method.

        Args:
            gear (mastapy.gears.ltca.GearLoadDistributionAnalysis)
            flank (mastapy.gears.GearFlanks)
            stress_type (mastapy.nodal_analysis.StressResultsType)

        Returns:
            float
        """

        flank = conversion.mp_to_pn_enum(flank, _322.GearFlanks.type_())
        stress_type = conversion.mp_to_pn_enum(stress_type, _86.StressResultsType.type_())
        method_result = self.wrapped.MaximumRootStress.Overloads[_GEAR_LOAD_DISTRIBUTION_ANALYSIS, _GEAR_FLANKS, _STRESS_RESULTS_TYPE](gear.wrapped if gear else None, flank, stress_type)
        return method_result

    def maximum_root_stress(self, gear: '_835.GearLoadDistributionAnalysis', stress_type: '_86.StressResultsType') -> 'float':
        """ 'MaximumRootStress' is the original name of this method.

        Args:
            gear (mastapy.gears.ltca.GearLoadDistributionAnalysis)
            stress_type (mastapy.nodal_analysis.StressResultsType)

        Returns:
            float
        """

        stress_type = conversion.mp_to_pn_enum(stress_type, _86.StressResultsType.type_())
        method_result = self.wrapped.MaximumRootStress.Overloads[_GEAR_LOAD_DISTRIBUTION_ANALYSIS, _STRESS_RESULTS_TYPE](gear.wrapped if gear else None, stress_type)
        return method_result

    @property
    def cast_to(self) -> 'GearMeshLoadDistributionAnalysis._Cast_GearMeshLoadDistributionAnalysis':
        return self._Cast_GearMeshLoadDistributionAnalysis(self)
