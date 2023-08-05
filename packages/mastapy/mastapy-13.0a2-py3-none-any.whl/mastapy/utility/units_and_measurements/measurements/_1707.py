"""_1707.py

Text
"""
from mastapy.utility.units_and_measurements import _1594
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TEXT = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements', 'Text')


__docformat__ = 'restructuredtext en'
__all__ = ('Text',)


class Text(_1594.MeasurementBase):
    """Text

    This is a mastapy class.
    """

    TYPE = _TEXT

    class _Cast_Text:
        """Special nested class for casting Text to subclasses."""

        def __init__(self, parent: 'Text'):
            self._parent = parent

        @property
        def measurement_base(self):
            return self._parent._cast(_1594.MeasurementBase)

        @property
        def text(self) -> 'Text':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'Text.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'Text._Cast_Text':
        return self._Cast_Text(self)
