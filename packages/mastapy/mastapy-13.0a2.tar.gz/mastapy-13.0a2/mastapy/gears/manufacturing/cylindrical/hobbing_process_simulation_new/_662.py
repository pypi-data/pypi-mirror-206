"""_662.py

HobbingProcessGearShape
"""
from mastapy.utility_gui.charts import _1852
from mastapy._internal import constructor
from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import _661
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HOBBING_PROCESS_GEAR_SHAPE = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Cylindrical.HobbingProcessSimulationNew', 'HobbingProcessGearShape')


__docformat__ = 'restructuredtext en'
__all__ = ('HobbingProcessGearShape',)


class HobbingProcessGearShape(_661.HobbingProcessCalculation):
    """HobbingProcessGearShape

    This is a mastapy class.
    """

    TYPE = _HOBBING_PROCESS_GEAR_SHAPE

    class _Cast_HobbingProcessGearShape:
        """Special nested class for casting HobbingProcessGearShape to subclasses."""

        def __init__(self, parent: 'HobbingProcessGearShape'):
            self._parent = parent

        @property
        def hobbing_process_calculation(self):
            return self._parent._cast(_661.HobbingProcessCalculation)

        @property
        def process_calculation(self):
            from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import _675
            
            return self._parent._cast(_675.ProcessCalculation)

        @property
        def hobbing_process_gear_shape(self) -> 'HobbingProcessGearShape':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'HobbingProcessGearShape.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def gear_tooth_shape_chart(self) -> '_1852.TwoDChartDefinition':
        """TwoDChartDefinition: 'GearToothShapeChart' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearToothShapeChart

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def number_of_gear_shape_bands(self) -> 'int':
        """int: 'NumberOfGearShapeBands' is the original name of this property."""

        temp = self.wrapped.NumberOfGearShapeBands

        if temp is None:
            return 0

        return temp

    @number_of_gear_shape_bands.setter
    def number_of_gear_shape_bands(self, value: 'int'):
        self.wrapped.NumberOfGearShapeBands = int(value) if value else 0

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
    def cast_to(self) -> 'HobbingProcessGearShape._Cast_HobbingProcessGearShape':
        return self._Cast_HobbingProcessGearShape(self)
