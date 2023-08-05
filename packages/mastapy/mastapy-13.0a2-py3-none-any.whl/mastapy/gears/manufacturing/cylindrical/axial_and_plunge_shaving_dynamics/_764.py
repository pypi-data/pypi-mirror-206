"""_764.py

ShavingDynamicsConfiguration
"""
from mastapy.gears.manufacturing.cylindrical.axial_and_plunge_shaving_dynamics import _761, _746, _750
from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAVING_DYNAMICS_CONFIGURATION = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Cylindrical.AxialAndPlungeShavingDynamics', 'ShavingDynamicsConfiguration')


__docformat__ = 'restructuredtext en'
__all__ = ('ShavingDynamicsConfiguration',)


class ShavingDynamicsConfiguration(_0.APIBase):
    """ShavingDynamicsConfiguration

    This is a mastapy class.
    """

    TYPE = _SHAVING_DYNAMICS_CONFIGURATION

    class _Cast_ShavingDynamicsConfiguration:
        """Special nested class for casting ShavingDynamicsConfiguration to subclasses."""

        def __init__(self, parent: 'ShavingDynamicsConfiguration'):
            self._parent = parent

        @property
        def shaving_dynamics_configuration(self) -> 'ShavingDynamicsConfiguration':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ShavingDynamicsConfiguration.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def conventional_shaving_dynamics(self) -> '_761.ShavingDynamicsCalculation[_746.ConventionalShavingDynamics]':
        """ShavingDynamicsCalculation[ConventionalShavingDynamics]: 'ConventionalShavingDynamics' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConventionalShavingDynamics

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_746.ConventionalShavingDynamics](temp) if temp is not None else None

    @property
    def plunge_shaving_dynamics(self) -> '_761.ShavingDynamicsCalculation[_750.PlungeShaverDynamics]':
        """ShavingDynamicsCalculation[PlungeShaverDynamics]: 'PlungeShavingDynamics' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PlungeShavingDynamics

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_750.PlungeShaverDynamics](temp) if temp is not None else None

    @property
    def cast_to(self) -> 'ShavingDynamicsConfiguration._Cast_ShavingDynamicsConfiguration':
        return self._Cast_ShavingDynamicsConfiguration(self)
