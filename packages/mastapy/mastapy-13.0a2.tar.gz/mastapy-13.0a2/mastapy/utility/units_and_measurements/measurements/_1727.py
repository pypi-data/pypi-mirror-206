"""_1727.py

Yank
"""
from mastapy.utility.units_and_measurements import _1594
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_YANK = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements', 'Yank')


__docformat__ = 'restructuredtext en'
__all__ = ('Yank',)


class Yank(_1594.MeasurementBase):
    """Yank

    This is a mastapy class.
    """

    TYPE = _YANK

    class _Cast_Yank:
        """Special nested class for casting Yank to subclasses."""

        def __init__(self, parent: 'Yank'):
            self._parent = parent

        @property
        def measurement_base(self):
            return self._parent._cast(_1594.MeasurementBase)

        @property
        def yank(self) -> 'Yank':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'Yank.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'Yank._Cast_Yank':
        return self._Cast_Yank(self)
