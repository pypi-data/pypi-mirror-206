"""_1670.py

MagnetomotiveForce
"""
from mastapy.utility.units_and_measurements import _1594
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MAGNETOMOTIVE_FORCE = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements', 'MagnetomotiveForce')


__docformat__ = 'restructuredtext en'
__all__ = ('MagnetomotiveForce',)


class MagnetomotiveForce(_1594.MeasurementBase):
    """MagnetomotiveForce

    This is a mastapy class.
    """

    TYPE = _MAGNETOMOTIVE_FORCE

    class _Cast_MagnetomotiveForce:
        """Special nested class for casting MagnetomotiveForce to subclasses."""

        def __init__(self, parent: 'MagnetomotiveForce'):
            self._parent = parent

        @property
        def measurement_base(self):
            return self._parent._cast(_1594.MeasurementBase)

        @property
        def magnetomotive_force(self) -> 'MagnetomotiveForce':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'MagnetomotiveForce.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'MagnetomotiveForce._Cast_MagnetomotiveForce':
        return self._Cast_MagnetomotiveForce(self)
