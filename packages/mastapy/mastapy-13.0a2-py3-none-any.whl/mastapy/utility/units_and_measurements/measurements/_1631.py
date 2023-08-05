"""_1631.py

Force
"""
from mastapy.utility.units_and_measurements import _1594
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FORCE = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements', 'Force')


__docformat__ = 'restructuredtext en'
__all__ = ('Force',)


class Force(_1594.MeasurementBase):
    """Force

    This is a mastapy class.
    """

    TYPE = _FORCE

    class _Cast_Force:
        """Special nested class for casting Force to subclasses."""

        def __init__(self, parent: 'Force'):
            self._parent = parent

        @property
        def measurement_base(self):
            return self._parent._cast(_1594.MeasurementBase)

        @property
        def force(self) -> 'Force':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'Force.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'Force._Cast_Force':
        return self._Cast_Force(self)
