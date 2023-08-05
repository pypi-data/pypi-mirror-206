"""_1257.py

ElectricMachineMeshingOptions
"""
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor
from mastapy.electric_machines import _1258
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ELECTRIC_MACHINE_MESHING_OPTIONS = python_net_import('SMT.MastaAPI.ElectricMachines', 'ElectricMachineMeshingOptions')


__docformat__ = 'restructuredtext en'
__all__ = ('ElectricMachineMeshingOptions',)


class ElectricMachineMeshingOptions(_1258.ElectricMachineMeshingOptionsBase):
    """ElectricMachineMeshingOptions

    This is a mastapy class.
    """

    TYPE = _ELECTRIC_MACHINE_MESHING_OPTIONS

    class _Cast_ElectricMachineMeshingOptions:
        """Special nested class for casting ElectricMachineMeshingOptions to subclasses."""

        def __init__(self, parent: 'ElectricMachineMeshingOptions'):
            self._parent = parent

        @property
        def electric_machine_meshing_options_base(self):
            return self._parent._cast(_1258.ElectricMachineMeshingOptionsBase)

        @property
        def fe_meshing_options(self):
            from mastapy.nodal_analysis import _61
            
            return self._parent._cast(_61.FEMeshingOptions)

        @property
        def electric_machine_meshing_options(self) -> 'ElectricMachineMeshingOptions':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ElectricMachineMeshingOptions.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def air_gap_element_size(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'AirGapElementSize' is the original name of this property."""

        temp = self.wrapped.AirGapElementSize

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @air_gap_element_size.setter
    def air_gap_element_size(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.AirGapElementSize = value

    @property
    def conductor_element_size(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'ConductorElementSize' is the original name of this property."""

        temp = self.wrapped.ConductorElementSize

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @conductor_element_size.setter
    def conductor_element_size(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.ConductorElementSize = value

    @property
    def magnet_element_size(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'MagnetElementSize' is the original name of this property."""

        temp = self.wrapped.MagnetElementSize

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @magnet_element_size.setter
    def magnet_element_size(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.MagnetElementSize = value

    @property
    def number_of_element_layers_in_air_gap(self) -> 'int':
        """int: 'NumberOfElementLayersInAirGap' is the original name of this property."""

        temp = self.wrapped.NumberOfElementLayersInAirGap

        if temp is None:
            return 0

        return temp

    @number_of_element_layers_in_air_gap.setter
    def number_of_element_layers_in_air_gap(self, value: 'int'):
        self.wrapped.NumberOfElementLayersInAirGap = int(value) if value else 0

    @property
    def rotor_element_size(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'RotorElementSize' is the original name of this property."""

        temp = self.wrapped.RotorElementSize

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @rotor_element_size.setter
    def rotor_element_size(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.RotorElementSize = value

    @property
    def slot_element_size(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'SlotElementSize' is the original name of this property."""

        temp = self.wrapped.SlotElementSize

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @slot_element_size.setter
    def slot_element_size(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.SlotElementSize = value

    @property
    def stator_element_size(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'StatorElementSize' is the original name of this property."""

        temp = self.wrapped.StatorElementSize

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @stator_element_size.setter
    def stator_element_size(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.StatorElementSize = value

    @property
    def cast_to(self) -> 'ElectricMachineMeshingOptions._Cast_ElectricMachineMeshingOptions':
        return self._Cast_ElectricMachineMeshingOptions(self)
