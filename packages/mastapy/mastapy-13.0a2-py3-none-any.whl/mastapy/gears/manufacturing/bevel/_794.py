"""_794.py

ManufacturingMachine
"""
from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy.gears.manufacturing.bevel import _793, _807
from mastapy.utility.databases import _1816
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MANUFACTURING_MACHINE = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Bevel', 'ManufacturingMachine')


__docformat__ = 'restructuredtext en'
__all__ = ('ManufacturingMachine',)


class ManufacturingMachine(_1816.NamedDatabaseItem):
    """ManufacturingMachine

    This is a mastapy class.
    """

    TYPE = _MANUFACTURING_MACHINE

    class _Cast_ManufacturingMachine:
        """Special nested class for casting ManufacturingMachine to subclasses."""

        def __init__(self, parent: 'ManufacturingMachine'):
            self._parent = parent

        @property
        def named_database_item(self):
            return self._parent._cast(_1816.NamedDatabaseItem)

        @property
        def manufacturing_machine(self) -> 'ManufacturingMachine':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ManufacturingMachine.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def can_work_for_formate(self) -> 'bool':
        """bool: 'CanWorkForFormate' is the original name of this property."""

        temp = self.wrapped.CanWorkForFormate

        if temp is None:
            return False

        return temp

    @can_work_for_formate.setter
    def can_work_for_formate(self, value: 'bool'):
        self.wrapped.CanWorkForFormate = bool(value) if value else False

    @property
    def can_work_for_generating(self) -> 'bool':
        """bool: 'CanWorkForGenerating' is the original name of this property."""

        temp = self.wrapped.CanWorkForGenerating

        if temp is None:
            return False

        return temp

    @can_work_for_generating.setter
    def can_work_for_generating(self, value: 'bool'):
        self.wrapped.CanWorkForGenerating = bool(value) if value else False

    @property
    def can_work_for_roller_modification(self) -> 'bool':
        """bool: 'CanWorkForRollerModification' is the original name of this property."""

        temp = self.wrapped.CanWorkForRollerModification

        if temp is None:
            return False

        return temp

    @can_work_for_roller_modification.setter
    def can_work_for_roller_modification(self, value: 'bool'):
        self.wrapped.CanWorkForRollerModification = bool(value) if value else False

    @property
    def can_work_for_tilt(self) -> 'bool':
        """bool: 'CanWorkForTilt' is the original name of this property."""

        temp = self.wrapped.CanWorkForTilt

        if temp is None:
            return False

        return temp

    @can_work_for_tilt.setter
    def can_work_for_tilt(self, value: 'bool'):
        self.wrapped.CanWorkForTilt = bool(value) if value else False

    @property
    def eccentric_distance(self) -> 'float':
        """float: 'EccentricDistance' is the original name of this property."""

        temp = self.wrapped.EccentricDistance

        if temp is None:
            return 0.0

        return temp

    @eccentric_distance.setter
    def eccentric_distance(self, value: 'float'):
        self.wrapped.EccentricDistance = float(value) if value else 0.0

    @property
    def machine_type(self) -> '_793.MachineTypes':
        """MachineTypes: 'MachineType' is the original name of this property."""

        temp = self.wrapped.MachineType

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, _793.MachineTypes)
        return constructor.new_from_mastapy_type(_793.MachineTypes)(value) if value is not None else None

    @machine_type.setter
    def machine_type(self, value: '_793.MachineTypes'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value, _793.MachineTypes.type_())
        self.wrapped.MachineType = value

    @property
    def maximum_tilt_angle(self) -> 'float':
        """float: 'MaximumTiltAngle' is the original name of this property."""

        temp = self.wrapped.MaximumTiltAngle

        if temp is None:
            return 0.0

        return temp

    @maximum_tilt_angle.setter
    def maximum_tilt_angle(self, value: 'float'):
        self.wrapped.MaximumTiltAngle = float(value) if value else 0.0

    @property
    def tilt_body_angle(self) -> 'float':
        """float: 'TiltBodyAngle' is the original name of this property."""

        temp = self.wrapped.TiltBodyAngle

        if temp is None:
            return 0.0

        return temp

    @tilt_body_angle.setter
    def tilt_body_angle(self, value: 'float'):
        self.wrapped.TiltBodyAngle = float(value) if value else 0.0

    @property
    def tilt_distance(self) -> 'float':
        """float: 'TiltDistance' is the original name of this property."""

        temp = self.wrapped.TiltDistance

        if temp is None:
            return 0.0

        return temp

    @tilt_distance.setter
    def tilt_distance(self, value: 'float'):
        self.wrapped.TiltDistance = float(value) if value else 0.0

    @property
    def wheel_formate_machine_type(self) -> '_807.WheelFormatMachineTypes':
        """WheelFormatMachineTypes: 'WheelFormateMachineType' is the original name of this property."""

        temp = self.wrapped.WheelFormateMachineType

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, _807.WheelFormatMachineTypes)
        return constructor.new_from_mastapy_type(_807.WheelFormatMachineTypes)(value) if value is not None else None

    @wheel_formate_machine_type.setter
    def wheel_formate_machine_type(self, value: '_807.WheelFormatMachineTypes'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value, _807.WheelFormatMachineTypes.type_())
        self.wrapped.WheelFormateMachineType = value

    @property
    def cast_to(self) -> 'ManufacturingMachine._Cast_ManufacturingMachine':
        return self._Cast_ManufacturingMachine(self)
