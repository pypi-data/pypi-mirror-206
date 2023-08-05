"""_1643.py

HeatTransferCoefficientForPlasticGearTooth
"""
from mastapy.utility.units_and_measurements import _1594
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HEAT_TRANSFER_COEFFICIENT_FOR_PLASTIC_GEAR_TOOTH = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements', 'HeatTransferCoefficientForPlasticGearTooth')


__docformat__ = 'restructuredtext en'
__all__ = ('HeatTransferCoefficientForPlasticGearTooth',)


class HeatTransferCoefficientForPlasticGearTooth(_1594.MeasurementBase):
    """HeatTransferCoefficientForPlasticGearTooth

    This is a mastapy class.
    """

    TYPE = _HEAT_TRANSFER_COEFFICIENT_FOR_PLASTIC_GEAR_TOOTH

    class _Cast_HeatTransferCoefficientForPlasticGearTooth:
        """Special nested class for casting HeatTransferCoefficientForPlasticGearTooth to subclasses."""

        def __init__(self, parent: 'HeatTransferCoefficientForPlasticGearTooth'):
            self._parent = parent

        @property
        def measurement_base(self):
            return self._parent._cast(_1594.MeasurementBase)

        @property
        def heat_transfer_coefficient_for_plastic_gear_tooth(self) -> 'HeatTransferCoefficientForPlasticGearTooth':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'HeatTransferCoefficientForPlasticGearTooth.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'HeatTransferCoefficientForPlasticGearTooth._Cast_HeatTransferCoefficientForPlasticGearTooth':
        return self._Cast_HeatTransferCoefficientForPlasticGearTooth(self)
