"""_746.py

ConventionalShavingDynamics
"""
from mastapy.gears.manufacturing.cylindrical.axial_and_plunge_shaving_dynamics import _760
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONVENTIONAL_SHAVING_DYNAMICS = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Cylindrical.AxialAndPlungeShavingDynamics', 'ConventionalShavingDynamics')


__docformat__ = 'restructuredtext en'
__all__ = ('ConventionalShavingDynamics',)


class ConventionalShavingDynamics(_760.ShavingDynamics):
    """ConventionalShavingDynamics

    This is a mastapy class.
    """

    TYPE = _CONVENTIONAL_SHAVING_DYNAMICS

    class _Cast_ConventionalShavingDynamics:
        """Special nested class for casting ConventionalShavingDynamics to subclasses."""

        def __init__(self, parent: 'ConventionalShavingDynamics'):
            self._parent = parent

        @property
        def shaving_dynamics(self):
            return self._parent._cast(_760.ShavingDynamics)

        @property
        def conventional_shaving_dynamics(self) -> 'ConventionalShavingDynamics':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConventionalShavingDynamics.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'ConventionalShavingDynamics._Cast_ConventionalShavingDynamics':
        return self._Cast_ConventionalShavingDynamics(self)
