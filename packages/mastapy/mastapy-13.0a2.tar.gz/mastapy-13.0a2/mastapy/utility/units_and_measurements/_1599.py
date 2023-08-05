"""_1599.py

Unit
"""
from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_UNIT = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements', 'Unit')


__docformat__ = 'restructuredtext en'
__all__ = ('Unit',)


class Unit(_0.APIBase):
    """Unit

    This is a mastapy class.
    """

    TYPE = _UNIT

    class _Cast_Unit:
        """Special nested class for casting Unit to subclasses."""

        def __init__(self, parent: 'Unit'):
            self._parent = parent

        @property
        def degrees_minutes_seconds(self):
            from mastapy.utility.units_and_measurements import _1591
            
            return self._parent._cast(_1591.DegreesMinutesSeconds)

        @property
        def enum_unit(self):
            from mastapy.utility.units_and_measurements import _1592
            
            return self._parent._cast(_1592.EnumUnit)

        @property
        def inverse_unit(self):
            from mastapy.utility.units_and_measurements import _1593
            
            return self._parent._cast(_1593.InverseUnit)

        @property
        def safety_factor_unit(self):
            from mastapy.utility.units_and_measurements import _1597
            
            return self._parent._cast(_1597.SafetyFactorUnit)

        @property
        def time_unit(self):
            from mastapy.utility.units_and_measurements import _1598
            
            return self._parent._cast(_1598.TimeUnit)

        @property
        def unit_gradient(self):
            from mastapy.utility.units_and_measurements import _1600
            
            return self._parent._cast(_1600.UnitGradient)

        @property
        def unit(self) -> 'Unit':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'Unit.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def html_symbol(self) -> 'str':
        """str: 'HTMLSymbol' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HTMLSymbol

        if temp is None:
            return ''

        return temp

    @property
    def name(self) -> 'str':
        """str: 'Name' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Name

        if temp is None:
            return ''

        return temp

    @property
    def offset(self) -> 'float':
        """float: 'Offset' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Offset

        if temp is None:
            return 0.0

        return temp

    @property
    def scale(self) -> 'float':
        """float: 'Scale' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Scale

        if temp is None:
            return 0.0

        return temp

    @property
    def symbol(self) -> 'str':
        """str: 'Symbol' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Symbol

        if temp is None:
            return ''

        return temp

    def convert_from_si_unit(self, d: 'float') -> 'float':
        """ 'ConvertFromSIUnit' is the original name of this method.

        Args:
            d (float)

        Returns:
            float
        """

        d = float(d)
        method_result = self.wrapped.ConvertFromSIUnit(d if d else 0.0)
        return method_result

    def convert_to_si_unit(self, d: 'float') -> 'float':
        """ 'ConvertToSIUnit' is the original name of this method.

        Args:
            d (float)

        Returns:
            float
        """

        d = float(d)
        method_result = self.wrapped.ConvertToSIUnit(d if d else 0.0)
        return method_result

    @property
    def cast_to(self) -> 'Unit._Cast_Unit':
        return self._Cast_Unit(self)
