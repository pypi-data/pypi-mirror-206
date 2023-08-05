"""_1648.py

Integer
"""
from mastapy.utility.units_and_measurements import _1594
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INTEGER = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements', 'Integer')


__docformat__ = 'restructuredtext en'
__all__ = ('Integer',)


class Integer(_1594.MeasurementBase):
    """Integer

    This is a mastapy class.
    """

    TYPE = _INTEGER

    class _Cast_Integer:
        """Special nested class for casting Integer to subclasses."""

        def __init__(self, parent: 'Integer'):
            self._parent = parent

        @property
        def measurement_base(self):
            return self._parent._cast(_1594.MeasurementBase)

        @property
        def integer(self) -> 'Integer':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'Integer.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'Integer._Cast_Integer':
        return self._Cast_Integer(self)
