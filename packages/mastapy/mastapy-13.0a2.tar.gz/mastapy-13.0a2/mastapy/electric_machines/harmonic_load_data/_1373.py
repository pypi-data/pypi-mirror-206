"""_1373.py

StatorToothLoadInterpolator
"""
from mastapy._internal import constructor
from mastapy.electric_machines.harmonic_load_data import _1372
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STATOR_TOOTH_LOAD_INTERPOLATOR = python_net_import('SMT.MastaAPI.ElectricMachines.HarmonicLoadData', 'StatorToothLoadInterpolator')


__docformat__ = 'restructuredtext en'
__all__ = ('StatorToothLoadInterpolator',)


class StatorToothLoadInterpolator(_1372.StatorToothInterpolator):
    """StatorToothLoadInterpolator

    This is a mastapy class.
    """

    TYPE = _STATOR_TOOTH_LOAD_INTERPOLATOR

    class _Cast_StatorToothLoadInterpolator:
        """Special nested class for casting StatorToothLoadInterpolator to subclasses."""

        def __init__(self, parent: 'StatorToothLoadInterpolator'):
            self._parent = parent

        @property
        def stator_tooth_interpolator(self):
            return self._parent._cast(_1372.StatorToothInterpolator)

        @property
        def stator_tooth_load_interpolator(self) -> 'StatorToothLoadInterpolator':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'StatorToothLoadInterpolator.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def spatial_force_absolute_tolerance(self) -> 'float':
        """float: 'SpatialForceAbsoluteTolerance' is the original name of this property."""

        temp = self.wrapped.SpatialForceAbsoluteTolerance

        if temp is None:
            return 0.0

        return temp

    @spatial_force_absolute_tolerance.setter
    def spatial_force_absolute_tolerance(self, value: 'float'):
        self.wrapped.SpatialForceAbsoluteTolerance = float(value) if value else 0.0

    @property
    def spatial_force_relative_tolerance(self) -> 'float':
        """float: 'SpatialForceRelativeTolerance' is the original name of this property."""

        temp = self.wrapped.SpatialForceRelativeTolerance

        if temp is None:
            return 0.0

        return temp

    @spatial_force_relative_tolerance.setter
    def spatial_force_relative_tolerance(self, value: 'float'):
        self.wrapped.SpatialForceRelativeTolerance = float(value) if value else 0.0

    @property
    def cast_to(self) -> 'StatorToothLoadInterpolator._Cast_StatorToothLoadInterpolator':
        return self._Cast_StatorToothLoadInterpolator(self)
