"""_685.py

RackMountingError
"""
from mastapy._internal import constructor
from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import _674
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_RACK_MOUNTING_ERROR = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Cylindrical.HobbingProcessSimulationNew', 'RackMountingError')


__docformat__ = 'restructuredtext en'
__all__ = ('RackMountingError',)


class RackMountingError(_674.MountingError):
    """RackMountingError

    This is a mastapy class.
    """

    TYPE = _RACK_MOUNTING_ERROR

    class _Cast_RackMountingError:
        """Special nested class for casting RackMountingError to subclasses."""

        def __init__(self, parent: 'RackMountingError'):
            self._parent = parent

        @property
        def mounting_error(self):
            return self._parent._cast(_674.MountingError)

        @property
        def rack_mounting_error(self) -> 'RackMountingError':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'RackMountingError.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def axial_runout(self) -> 'float':
        """float: 'AxialRunout' is the original name of this property."""

        temp = self.wrapped.AxialRunout

        if temp is None:
            return 0.0

        return temp

    @axial_runout.setter
    def axial_runout(self, value: 'float'):
        self.wrapped.AxialRunout = float(value) if value else 0.0

    @property
    def axial_runout_phase_angle(self) -> 'float':
        """float: 'AxialRunoutPhaseAngle' is the original name of this property."""

        temp = self.wrapped.AxialRunoutPhaseAngle

        if temp is None:
            return 0.0

        return temp

    @axial_runout_phase_angle.setter
    def axial_runout_phase_angle(self, value: 'float'):
        self.wrapped.AxialRunoutPhaseAngle = float(value) if value else 0.0

    @property
    def cast_to(self) -> 'RackMountingError._Cast_RackMountingError':
        return self._Cast_RackMountingError(self)
