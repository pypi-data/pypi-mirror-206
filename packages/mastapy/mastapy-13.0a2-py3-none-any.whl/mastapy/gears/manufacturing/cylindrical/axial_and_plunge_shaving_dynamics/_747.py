"""_747.py

ConventionalShavingDynamicsCalculationForDesignedGears
"""
from mastapy.gears.manufacturing.cylindrical.axial_and_plunge_shaving_dynamics import _762, _746
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONVENTIONAL_SHAVING_DYNAMICS_CALCULATION_FOR_DESIGNED_GEARS = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Cylindrical.AxialAndPlungeShavingDynamics', 'ConventionalShavingDynamicsCalculationForDesignedGears')


__docformat__ = 'restructuredtext en'
__all__ = ('ConventionalShavingDynamicsCalculationForDesignedGears',)


class ConventionalShavingDynamicsCalculationForDesignedGears(_762.ShavingDynamicsCalculationForDesignedGears['_746.ConventionalShavingDynamics']):
    """ConventionalShavingDynamicsCalculationForDesignedGears

    This is a mastapy class.
    """

    TYPE = _CONVENTIONAL_SHAVING_DYNAMICS_CALCULATION_FOR_DESIGNED_GEARS

    class _Cast_ConventionalShavingDynamicsCalculationForDesignedGears:
        """Special nested class for casting ConventionalShavingDynamicsCalculationForDesignedGears to subclasses."""

        def __init__(self, parent: 'ConventionalShavingDynamicsCalculationForDesignedGears'):
            self._parent = parent

        @property
        def shaving_dynamics_calculation_for_designed_gears(self):
            return self._parent._cast(_762.ShavingDynamicsCalculationForDesignedGears)

        @property
        def shaving_dynamics_calculation(self):
            from mastapy.gears.manufacturing.cylindrical.axial_and_plunge_shaving_dynamics import _761
            
            return self._parent._cast(_761.ShavingDynamicsCalculation)

        @property
        def conventional_shaving_dynamics_calculation_for_designed_gears(self) -> 'ConventionalShavingDynamicsCalculationForDesignedGears':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConventionalShavingDynamicsCalculationForDesignedGears.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'ConventionalShavingDynamicsCalculationForDesignedGears._Cast_ConventionalShavingDynamicsCalculationForDesignedGears':
        return self._Cast_ConventionalShavingDynamicsCalculationForDesignedGears(self)
