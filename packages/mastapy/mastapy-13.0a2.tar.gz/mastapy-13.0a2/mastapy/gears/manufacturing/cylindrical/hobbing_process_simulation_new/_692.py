"""_692.py

WormGrindingProcessPitchCalculation
"""
from mastapy.utility_gui.charts import _1852
from mastapy._internal import constructor
from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import _656, _689
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_WORM_GRINDING_PROCESS_PITCH_CALCULATION = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Cylindrical.HobbingProcessSimulationNew', 'WormGrindingProcessPitchCalculation')


__docformat__ = 'restructuredtext en'
__all__ = ('WormGrindingProcessPitchCalculation',)


class WormGrindingProcessPitchCalculation(_689.WormGrindingProcessCalculation):
    """WormGrindingProcessPitchCalculation

    This is a mastapy class.
    """

    TYPE = _WORM_GRINDING_PROCESS_PITCH_CALCULATION

    class _Cast_WormGrindingProcessPitchCalculation:
        """Special nested class for casting WormGrindingProcessPitchCalculation to subclasses."""

        def __init__(self, parent: 'WormGrindingProcessPitchCalculation'):
            self._parent = parent

        @property
        def worm_grinding_process_calculation(self):
            return self._parent._cast(_689.WormGrindingProcessCalculation)

        @property
        def process_calculation(self):
            from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import _675
            
            return self._parent._cast(_675.ProcessCalculation)

        @property
        def worm_grinding_process_pitch_calculation(self) -> 'WormGrindingProcessPitchCalculation':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'WormGrindingProcessPitchCalculation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def pitch_modification_chart(self) -> '_1852.TwoDChartDefinition':
        """TwoDChartDefinition: 'PitchModificationChart' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PitchModificationChart

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

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
    def left_flank(self) -> '_656.CalculatePitchDeviationAccuracy':
        """CalculatePitchDeviationAccuracy: 'LeftFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LeftFlank

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def right_flank(self) -> '_656.CalculatePitchDeviationAccuracy':
        """CalculatePitchDeviationAccuracy: 'RightFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RightFlank

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'WormGrindingProcessPitchCalculation._Cast_WormGrindingProcessPitchCalculation':
        return self._Cast_WormGrindingProcessPitchCalculation(self)
