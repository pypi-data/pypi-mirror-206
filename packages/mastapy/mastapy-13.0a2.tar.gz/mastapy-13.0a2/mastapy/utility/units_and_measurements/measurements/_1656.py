"""_1656.py

LengthShort
"""
from mastapy.utility.units_and_measurements import _1599, _1594
from mastapy._internal import constructor
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LENGTH_SHORT = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements', 'LengthShort')


__docformat__ = 'restructuredtext en'
__all__ = ('LengthShort',)


class LengthShort(_1594.MeasurementBase):
    """LengthShort

    This is a mastapy class.
    """

    TYPE = _LENGTH_SHORT

    class _Cast_LengthShort:
        """Special nested class for casting LengthShort to subclasses."""

        def __init__(self, parent: 'LengthShort'):
            self._parent = parent

        @property
        def measurement_base(self):
            return self._parent._cast(_1594.MeasurementBase)

        @property
        def length_short(self) -> 'LengthShort':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'LengthShort.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def feet(self) -> '_1599.Unit':
        """Unit: 'Feet' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Feet

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def inches(self) -> '_1599.Unit':
        """Unit: 'Inches' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Inches

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def metres(self) -> '_1599.Unit':
        """Unit: 'Metres' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Metres

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def micrometres(self) -> '_1599.Unit':
        """Unit: 'Micrometres' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Micrometres

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def millimetres(self) -> '_1599.Unit':
        """Unit: 'Millimetres' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Millimetres

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def thousandths_of_an_inch(self) -> '_1599.Unit':
        """Unit: 'ThousandthsOfAnInch' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ThousandthsOfAnInch

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'LengthShort._Cast_LengthShort':
        return self._Cast_LengthShort(self)
