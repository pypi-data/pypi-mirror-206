"""_2258.py

DatumMeasurement
"""
from mastapy._internal.implicit import list_with_selected_item
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor
from mastapy.system_model.connections_and_sockets import _2252
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DATUM_MEASUREMENT = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets', 'DatumMeasurement')


__docformat__ = 'restructuredtext en'
__all__ = ('DatumMeasurement',)


class DatumMeasurement(_2252.ComponentMeasurer):
    """DatumMeasurement

    This is a mastapy class.
    """

    TYPE = _DATUM_MEASUREMENT

    class _Cast_DatumMeasurement:
        """Special nested class for casting DatumMeasurement to subclasses."""

        def __init__(self, parent: 'DatumMeasurement'):
            self._parent = parent

        @property
        def component_measurer(self):
            return self._parent._cast(_2252.ComponentMeasurer)

        @property
        def datum_measurement(self) -> 'DatumMeasurement':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'DatumMeasurement.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def measuring_position(self) -> 'list_with_selected_item.ListWithSelectedItem_str':
        """list_with_selected_item.ListWithSelectedItem_str: 'MeasuringPosition' is the original name of this property."""

        temp = self.wrapped.MeasuringPosition

        if temp is None:
            return ''

        return constructor.new_from_mastapy_type(list_with_selected_item.ListWithSelectedItem_str)(temp) if temp is not None else ''

    @measuring_position.setter
    def measuring_position(self, value: 'list_with_selected_item.ListWithSelectedItem_str.implicit_type()'):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_str.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_str.implicit_type()
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else '')
        self.wrapped.MeasuringPosition = value

    @property
    def cast_to(self) -> 'DatumMeasurement._Cast_DatumMeasurement':
        return self._Cast_DatumMeasurement(self)
