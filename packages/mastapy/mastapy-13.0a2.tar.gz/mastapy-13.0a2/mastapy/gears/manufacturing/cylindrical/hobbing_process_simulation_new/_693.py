"""_693.py

WormGrindingProcessProfileCalculation
"""
from mastapy.gears.gear_designs.cylindrical import _1021
from mastapy._internal import enum_with_selected_value_runtime, constructor, conversion
from mastapy.utility_gui.charts import _1852
from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import _657, _689
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_WORM_GRINDING_PROCESS_PROFILE_CALCULATION = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Cylindrical.HobbingProcessSimulationNew', 'WormGrindingProcessProfileCalculation')


__docformat__ = 'restructuredtext en'
__all__ = ('WormGrindingProcessProfileCalculation',)


class WormGrindingProcessProfileCalculation(_689.WormGrindingProcessCalculation):
    """WormGrindingProcessProfileCalculation

    This is a mastapy class.
    """

    TYPE = _WORM_GRINDING_PROCESS_PROFILE_CALCULATION

    class _Cast_WormGrindingProcessProfileCalculation:
        """Special nested class for casting WormGrindingProcessProfileCalculation to subclasses."""

        def __init__(self, parent: 'WormGrindingProcessProfileCalculation'):
            self._parent = parent

        @property
        def worm_grinding_process_calculation(self):
            return self._parent._cast(_689.WormGrindingProcessCalculation)

        @property
        def process_calculation(self):
            from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import _675
            
            return self._parent._cast(_675.ProcessCalculation)

        @property
        def worm_grinding_process_profile_calculation(self) -> 'WormGrindingProcessProfileCalculation':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'WormGrindingProcessProfileCalculation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def chart_display_method(self) -> '_1021.CylindricalGearProfileMeasurementType':
        """CylindricalGearProfileMeasurementType: 'ChartDisplayMethod' is the original name of this property."""

        temp = self.wrapped.ChartDisplayMethod

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, _1021.CylindricalGearProfileMeasurementType)
        return constructor.new_from_mastapy_type(_1021.CylindricalGearProfileMeasurementType)(value) if value is not None else None

    @chart_display_method.setter
    def chart_display_method(self, value: '_1021.CylindricalGearProfileMeasurementType'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value, _1021.CylindricalGearProfileMeasurementType.type_())
        self.wrapped.ChartDisplayMethod = value

    @property
    def left_flank_profile_modification_chart(self) -> '_1852.TwoDChartDefinition':
        """TwoDChartDefinition: 'LeftFlankProfileModificationChart' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LeftFlankProfileModificationChart

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def number_of_profile_bands(self) -> 'int':
        """int: 'NumberOfProfileBands' is the original name of this property."""

        temp = self.wrapped.NumberOfProfileBands

        if temp is None:
            return 0

        return temp

    @number_of_profile_bands.setter
    def number_of_profile_bands(self, value: 'int'):
        self.wrapped.NumberOfProfileBands = int(value) if value else 0

    @property
    def result_z_plane(self) -> 'float':
        """float: 'ResultZPlane' is the original name of this property."""

        temp = self.wrapped.ResultZPlane

        if temp is None:
            return 0.0

        return temp

    @result_z_plane.setter
    def result_z_plane(self, value: 'float'):
        self.wrapped.ResultZPlane = float(value) if value else 0.0

    @property
    def right_flank_profile_modification_chart(self) -> '_1852.TwoDChartDefinition':
        """TwoDChartDefinition: 'RightFlankProfileModificationChart' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RightFlankProfileModificationChart

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def left_flank(self) -> '_657.CalculateProfileDeviationAccuracy':
        """CalculateProfileDeviationAccuracy: 'LeftFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LeftFlank

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def right_flank(self) -> '_657.CalculateProfileDeviationAccuracy':
        """CalculateProfileDeviationAccuracy: 'RightFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RightFlank

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'WormGrindingProcessProfileCalculation._Cast_WormGrindingProcessProfileCalculation':
        return self._Cast_WormGrindingProcessProfileCalculation(self)
