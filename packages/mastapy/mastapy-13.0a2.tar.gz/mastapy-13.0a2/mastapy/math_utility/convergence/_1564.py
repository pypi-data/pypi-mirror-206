"""_1564.py

DataLogger
"""
from typing import List

from mastapy._internal import constructor, conversion
from mastapy._math.vector_3d import Vector3D
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DATA_LOGGER = python_net_import('SMT.MastaAPI.MathUtility.Convergence', 'DataLogger')


__docformat__ = 'restructuredtext en'
__all__ = ('DataLogger',)


class DataLogger(_0.APIBase):
    """DataLogger

    This is a mastapy class.
    """

    TYPE = _DATA_LOGGER

    class _Cast_DataLogger:
        """Special nested class for casting DataLogger to subclasses."""

        def __init__(self, parent: 'DataLogger'):
            self._parent = parent

        @property
        def convergence_logger(self):
            from mastapy.math_utility.convergence import _1563
            
            return self._parent._cast(_1563.ConvergenceLogger)

        @property
        def data_logger_with_charts(self):
            from mastapy.utility_gui import _1836
            
            return self._parent._cast(_1836.DataLoggerWithCharts)

        @property
        def data_logger(self) -> 'DataLogger':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'DataLogger.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def available_properties(self) -> 'List[str]':
        """List[str]: 'AvailableProperties' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AvailableProperties

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, str)
        return value

    @property
    def has_logged_data(self) -> 'bool':
        """bool: 'HasLoggedData' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HasLoggedData

        if temp is None:
            return False

        return temp

    def get_double_data_for(self, property_name: 'str') -> 'List[float]':
        """ 'GetDoubleDataFor' is the original name of this method.

        Args:
            property_name (str)

        Returns:
            List[float]
        """

        property_name = str(property_name)
        return conversion.pn_to_mp_objects_in_list(self.wrapped.GetDoubleDataFor(property_name if property_name else ''), float)

    def get_int_data_for(self, property_name: 'str') -> 'List[int]':
        """ 'GetIntDataFor' is the original name of this method.

        Args:
            property_name (str)

        Returns:
            List[int]
        """

        property_name = str(property_name)
        return conversion.pn_to_mp_objects_in_list(self.wrapped.GetIntDataFor(property_name if property_name else ''), int)

    def get_vector_data_for(self, property_name: 'str') -> 'List[Vector3D]':
        """ 'GetVectorDataFor' is the original name of this method.

        Args:
            property_name (str)

        Returns:
            List[Vector3D]
        """

        property_name = str(property_name)
        return conversion.pn_to_mp_objects_in_list(self.wrapped.GetVectorDataFor(property_name if property_name else ''))

    @property
    def cast_to(self) -> 'DataLogger._Cast_DataLogger':
        return self._Cast_DataLogger(self)
