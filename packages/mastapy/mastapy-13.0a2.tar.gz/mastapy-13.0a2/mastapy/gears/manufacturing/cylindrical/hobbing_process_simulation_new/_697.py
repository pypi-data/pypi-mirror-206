"""_697.py

WormGrindingProcessTotalModificationCalculation
"""
from mastapy._internal import constructor
from mastapy.utility_gui.charts import _1850
from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import _689
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_WORM_GRINDING_PROCESS_TOTAL_MODIFICATION_CALCULATION = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Cylindrical.HobbingProcessSimulationNew', 'WormGrindingProcessTotalModificationCalculation')


__docformat__ = 'restructuredtext en'
__all__ = ('WormGrindingProcessTotalModificationCalculation',)


class WormGrindingProcessTotalModificationCalculation(_689.WormGrindingProcessCalculation):
    """WormGrindingProcessTotalModificationCalculation

    This is a mastapy class.
    """

    TYPE = _WORM_GRINDING_PROCESS_TOTAL_MODIFICATION_CALCULATION

    class _Cast_WormGrindingProcessTotalModificationCalculation:
        """Special nested class for casting WormGrindingProcessTotalModificationCalculation to subclasses."""

        def __init__(self, parent: 'WormGrindingProcessTotalModificationCalculation'):
            self._parent = parent

        @property
        def worm_grinding_process_calculation(self):
            return self._parent._cast(_689.WormGrindingProcessCalculation)

        @property
        def process_calculation(self):
            from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import _675
            
            return self._parent._cast(_675.ProcessCalculation)

        @property
        def worm_grinding_process_total_modification_calculation(self) -> 'WormGrindingProcessTotalModificationCalculation':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'WormGrindingProcessTotalModificationCalculation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def lead_range_max(self) -> 'float':
        """float: 'LeadRangeMax' is the original name of this property."""

        temp = self.wrapped.LeadRangeMax

        if temp is None:
            return 0.0

        return temp

    @lead_range_max.setter
    def lead_range_max(self, value: 'float'):
        self.wrapped.LeadRangeMax = float(value) if value else 0.0

    @property
    def lead_range_min(self) -> 'float':
        """float: 'LeadRangeMin' is the original name of this property."""

        temp = self.wrapped.LeadRangeMin

        if temp is None:
            return 0.0

        return temp

    @lead_range_min.setter
    def lead_range_min(self, value: 'float'):
        self.wrapped.LeadRangeMin = float(value) if value else 0.0

    @property
    def number_of_lead_bands(self) -> 'int':
        """int: 'NumberOfLeadBands' is the original name of this property."""

        temp = self.wrapped.NumberOfLeadBands

        if temp is None:
            return 0

        return temp

    @number_of_lead_bands.setter
    def number_of_lead_bands(self, value: 'int'):
        self.wrapped.NumberOfLeadBands = int(value) if value else 0

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
    def total_errors_chart_left_flank(self) -> '_1850.ThreeDChartDefinition':
        """ThreeDChartDefinition: 'TotalErrorsChartLeftFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TotalErrorsChartLeftFlank

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def total_errors_chart_right_flank(self) -> '_1850.ThreeDChartDefinition':
        """ThreeDChartDefinition: 'TotalErrorsChartRightFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TotalErrorsChartRightFlank

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'WormGrindingProcessTotalModificationCalculation._Cast_WormGrindingProcessTotalModificationCalculation':
        return self._Cast_WormGrindingProcessTotalModificationCalculation(self)
