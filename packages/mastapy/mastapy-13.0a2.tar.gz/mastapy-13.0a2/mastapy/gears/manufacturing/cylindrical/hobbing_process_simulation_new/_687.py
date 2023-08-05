"""_687.py

WormGrindingCutterCalculation
"""
from mastapy.utility_gui.charts import _1852
from mastapy._internal import constructor
from mastapy.gears.manufacturing.cylindrical.plunge_shaving import _648
from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import _689
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_WORM_GRINDING_CUTTER_CALCULATION = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Cylindrical.HobbingProcessSimulationNew', 'WormGrindingCutterCalculation')


__docformat__ = 'restructuredtext en'
__all__ = ('WormGrindingCutterCalculation',)


class WormGrindingCutterCalculation(_689.WormGrindingProcessCalculation):
    """WormGrindingCutterCalculation

    This is a mastapy class.
    """

    TYPE = _WORM_GRINDING_CUTTER_CALCULATION

    class _Cast_WormGrindingCutterCalculation:
        """Special nested class for casting WormGrindingCutterCalculation to subclasses."""

        def __init__(self, parent: 'WormGrindingCutterCalculation'):
            self._parent = parent

        @property
        def worm_grinding_process_calculation(self):
            return self._parent._cast(_689.WormGrindingProcessCalculation)

        @property
        def process_calculation(self):
            from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import _675
            
            return self._parent._cast(_675.ProcessCalculation)

        @property
        def worm_grinding_cutter_calculation(self) -> 'WormGrindingCutterCalculation':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'WormGrindingCutterCalculation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def grinder_tooth_shape_chart(self) -> '_1852.TwoDChartDefinition':
        """TwoDChartDefinition: 'GrinderToothShapeChart' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GrinderToothShapeChart

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
    def use_design_mode_micro_geometry(self) -> 'bool':
        """bool: 'UseDesignModeMicroGeometry' is the original name of this property."""

        temp = self.wrapped.UseDesignModeMicroGeometry

        if temp is None:
            return False

        return temp

    @use_design_mode_micro_geometry.setter
    def use_design_mode_micro_geometry(self, value: 'bool'):
        self.wrapped.UseDesignModeMicroGeometry = bool(value) if value else False

    @property
    def worm_axial_z(self) -> 'float':
        """float: 'WormAxialZ' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WormAxialZ

        if temp is None:
            return 0.0

        return temp

    @property
    def worm_radius(self) -> 'float':
        """float: 'WormRadius' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WormRadius

        if temp is None:
            return 0.0

        return temp

    @property
    def input_gear_point_of_interest(self) -> '_648.PointOfInterest':
        """PointOfInterest: 'InputGearPointOfInterest' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InputGearPointOfInterest

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    def calculate_grinder_axial_section_tooth_shape(self):
        """ 'CalculateGrinderAxialSectionToothShape' is the original name of this method."""

        self.wrapped.CalculateGrinderAxialSectionToothShape()

    def calculate_point_of_interest(self):
        """ 'CalculatePointOfInterest' is the original name of this method."""

        self.wrapped.CalculatePointOfInterest()

    @property
    def cast_to(self) -> 'WormGrindingCutterCalculation._Cast_WormGrindingCutterCalculation':
        return self._Cast_WormGrindingCutterCalculation(self)
