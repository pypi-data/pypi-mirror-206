"""_7523.py

MeasurementTypeExtensions
"""
from mastapy.units_and_measurements import _7522
from mastapy._internal import conversion, constructor
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MEASUREMENT_TYPE_EXTENSIONS = python_net_import('SMT.MastaAPIUtility.UnitsAndMeasurements', 'MeasurementTypeExtensions')


__docformat__ = 'restructuredtext en'
__all__ = ('MeasurementTypeExtensions',)


class MeasurementTypeExtensions:
    """MeasurementTypeExtensions

    This is a mastapy class.
    """

    TYPE = _MEASUREMENT_TYPE_EXTENSIONS

    class _Cast_MeasurementTypeExtensions:
        """Special nested class for casting MeasurementTypeExtensions to subclasses."""

        def __init__(self, parent: 'MeasurementTypeExtensions'):
            self._parent = parent

        @property
        def measurement_type_extensions(self) -> 'MeasurementTypeExtensions':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'MeasurementTypeExtensions.TYPE'):
        self.wrapped = instance_to_wrap
        if not hasattr(self.wrapped, 'reference_count'):
            self.wrapped.reference_count = 0
        self.wrapped.reference_count += 1

    @staticmethod
    def is_unmeasurable(measurement_type: '_7522.MeasurementType') -> 'bool':
        """ 'IsUnmeasurable' is the original name of this method.

        Args:
            measurement_type (mastapy.units_and_measurements.MeasurementType)

        Returns:
            bool
        """

        measurement_type = conversion.mp_to_pn_enum(measurement_type, _7522.MeasurementType.type_())
        method_result = MeasurementTypeExtensions.TYPE.IsUnmeasurable(measurement_type)
        return method_result

    @staticmethod
    def is_valid(measurement_type: '_7522.MeasurementType') -> 'bool':
        """ 'IsValid' is the original name of this method.

        Args:
            measurement_type (mastapy.units_and_measurements.MeasurementType)

        Returns:
            bool
        """

        measurement_type = conversion.mp_to_pn_enum(measurement_type, _7522.MeasurementType.type_())
        method_result = MeasurementTypeExtensions.TYPE.IsValid(measurement_type)
        return method_result

    @staticmethod
    def is_angle(measurement_type: '_7522.MeasurementType') -> 'bool':
        """ 'IsAngle' is the original name of this method.

        Args:
            measurement_type (mastapy.units_and_measurements.MeasurementType)

        Returns:
            bool
        """

        measurement_type = conversion.mp_to_pn_enum(measurement_type, _7522.MeasurementType.type_())
        method_result = MeasurementTypeExtensions.TYPE.IsAngle(measurement_type)
        return method_result

    @property
    def cast_to(self) -> 'MeasurementTypeExtensions._Cast_MeasurementTypeExtensions':
        return self._Cast_MeasurementTypeExtensions(self)
