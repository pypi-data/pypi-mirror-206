"""_1365.py

Temperatures
"""
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor
from mastapy.utility import _1575
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TEMPERATURES = python_net_import('SMT.MastaAPI.ElectricMachines.LoadCasesAndAnalyses', 'Temperatures')


__docformat__ = 'restructuredtext en'
__all__ = ('Temperatures',)


class Temperatures(_1575.IndependentReportablePropertiesBase['Temperatures']):
    """Temperatures

    This is a mastapy class.
    """

    TYPE = _TEMPERATURES

    class _Cast_Temperatures:
        """Special nested class for casting Temperatures to subclasses."""

        def __init__(self, parent: 'Temperatures'):
            self._parent = parent

        @property
        def independent_reportable_properties_base(self):
            from mastapy.electric_machines.load_cases_and_analyses import _1365
            
            return self._parent._cast(_1575.IndependentReportablePropertiesBase)

        @property
        def temperatures(self) -> 'Temperatures':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'Temperatures.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def magnet_temperature(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'MagnetTemperature' is the original name of this property."""

        temp = self.wrapped.MagnetTemperature

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @magnet_temperature.setter
    def magnet_temperature(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.MagnetTemperature = value

    @property
    def windings_temperature(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'WindingsTemperature' is the original name of this property."""

        temp = self.wrapped.WindingsTemperature

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @windings_temperature.setter
    def windings_temperature(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.WindingsTemperature = value

    @property
    def cast_to(self) -> 'Temperatures._Cast_Temperatures':
        return self._Cast_Temperatures(self)
