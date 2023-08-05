"""_1667.py

MagneticFlux
"""
from mastapy.utility.units_and_measurements import _1594
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MAGNETIC_FLUX = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements', 'MagneticFlux')


__docformat__ = 'restructuredtext en'
__all__ = ('MagneticFlux',)


class MagneticFlux(_1594.MeasurementBase):
    """MagneticFlux

    This is a mastapy class.
    """

    TYPE = _MAGNETIC_FLUX

    class _Cast_MagneticFlux:
        """Special nested class for casting MagneticFlux to subclasses."""

        def __init__(self, parent: 'MagneticFlux'):
            self._parent = parent

        @property
        def measurement_base(self):
            return self._parent._cast(_1594.MeasurementBase)

        @property
        def magnetic_flux(self) -> 'MagneticFlux':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'MagneticFlux.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'MagneticFlux._Cast_MagneticFlux':
        return self._Cast_MagneticFlux(self)
