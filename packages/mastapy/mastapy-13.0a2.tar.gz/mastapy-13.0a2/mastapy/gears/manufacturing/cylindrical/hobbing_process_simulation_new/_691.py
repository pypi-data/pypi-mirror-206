"""_691.py

WormGrindingProcessMarkOnShaft
"""
from mastapy._internal import constructor
from mastapy.utility_gui.charts import _1850
from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import _689
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_WORM_GRINDING_PROCESS_MARK_ON_SHAFT = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Cylindrical.HobbingProcessSimulationNew', 'WormGrindingProcessMarkOnShaft')


__docformat__ = 'restructuredtext en'
__all__ = ('WormGrindingProcessMarkOnShaft',)


class WormGrindingProcessMarkOnShaft(_689.WormGrindingProcessCalculation):
    """WormGrindingProcessMarkOnShaft

    This is a mastapy class.
    """

    TYPE = _WORM_GRINDING_PROCESS_MARK_ON_SHAFT

    class _Cast_WormGrindingProcessMarkOnShaft:
        """Special nested class for casting WormGrindingProcessMarkOnShaft to subclasses."""

        def __init__(self, parent: 'WormGrindingProcessMarkOnShaft'):
            self._parent = parent

        @property
        def worm_grinding_process_calculation(self):
            return self._parent._cast(_689.WormGrindingProcessCalculation)

        @property
        def process_calculation(self):
            from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import _675
            
            return self._parent._cast(_675.ProcessCalculation)

        @property
        def worm_grinding_process_mark_on_shaft(self) -> 'WormGrindingProcessMarkOnShaft':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'WormGrindingProcessMarkOnShaft.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

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
    def number_of_transverse_plane(self) -> 'int':
        """int: 'NumberOfTransversePlane' is the original name of this property."""

        temp = self.wrapped.NumberOfTransversePlane

        if temp is None:
            return 0

        return temp

    @number_of_transverse_plane.setter
    def number_of_transverse_plane(self, value: 'int'):
        self.wrapped.NumberOfTransversePlane = int(value) if value else 0

    @property
    def shaft_diameter(self) -> 'float':
        """float: 'ShaftDiameter' is the original name of this property."""

        temp = self.wrapped.ShaftDiameter

        if temp is None:
            return 0.0

        return temp

    @shaft_diameter.setter
    def shaft_diameter(self, value: 'float'):
        self.wrapped.ShaftDiameter = float(value) if value else 0.0

    @property
    def shaft_mark_chart(self) -> '_1850.ThreeDChartDefinition':
        """ThreeDChartDefinition: 'ShaftMarkChart' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ShaftMarkChart

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'WormGrindingProcessMarkOnShaft._Cast_WormGrindingProcessMarkOnShaft':
        return self._Cast_WormGrindingProcessMarkOnShaft(self)
