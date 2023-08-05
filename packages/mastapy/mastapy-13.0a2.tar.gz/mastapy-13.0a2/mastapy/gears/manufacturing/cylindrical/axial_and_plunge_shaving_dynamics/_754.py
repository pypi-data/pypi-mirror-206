"""_754.py

PlungeShavingDynamicsCalculationForHobbedGears
"""
from mastapy.gears.manufacturing.cylindrical.axial_and_plunge_shaving_dynamics import _763, _750
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLUNGE_SHAVING_DYNAMICS_CALCULATION_FOR_HOBBED_GEARS = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Cylindrical.AxialAndPlungeShavingDynamics', 'PlungeShavingDynamicsCalculationForHobbedGears')


__docformat__ = 'restructuredtext en'
__all__ = ('PlungeShavingDynamicsCalculationForHobbedGears',)


class PlungeShavingDynamicsCalculationForHobbedGears(_763.ShavingDynamicsCalculationForHobbedGears['_750.PlungeShaverDynamics']):
    """PlungeShavingDynamicsCalculationForHobbedGears

    This is a mastapy class.
    """

    TYPE = _PLUNGE_SHAVING_DYNAMICS_CALCULATION_FOR_HOBBED_GEARS

    class _Cast_PlungeShavingDynamicsCalculationForHobbedGears:
        """Special nested class for casting PlungeShavingDynamicsCalculationForHobbedGears to subclasses."""

        def __init__(self, parent: 'PlungeShavingDynamicsCalculationForHobbedGears'):
            self._parent = parent

        @property
        def shaving_dynamics_calculation_for_hobbed_gears(self):
            return self._parent._cast(_763.ShavingDynamicsCalculationForHobbedGears)

        @property
        def shaving_dynamics_calculation(self):
            from mastapy.gears.manufacturing.cylindrical.axial_and_plunge_shaving_dynamics import _761
            
            return self._parent._cast(_761.ShavingDynamicsCalculation)

        @property
        def plunge_shaving_dynamics_calculation_for_hobbed_gears(self) -> 'PlungeShavingDynamicsCalculationForHobbedGears':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'PlungeShavingDynamicsCalculationForHobbedGears.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'PlungeShavingDynamicsCalculationForHobbedGears._Cast_PlungeShavingDynamicsCalculationForHobbedGears':
        return self._Cast_PlungeShavingDynamicsCalculationForHobbedGears(self)
