"""_790.py

EaseOffBasedTCA
"""
from mastapy._internal import constructor
from mastapy.gears.manufacturing.bevel import _767
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_EASE_OFF_BASED_TCA = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Bevel', 'EaseOffBasedTCA')


__docformat__ = 'restructuredtext en'
__all__ = ('EaseOffBasedTCA',)


class EaseOffBasedTCA(_767.AbstractTCA):
    """EaseOffBasedTCA

    This is a mastapy class.
    """

    TYPE = _EASE_OFF_BASED_TCA

    class _Cast_EaseOffBasedTCA:
        """Special nested class for casting EaseOffBasedTCA to subclasses."""

        def __init__(self, parent: 'EaseOffBasedTCA'):
            self._parent = parent

        @property
        def abstract_tca(self):
            return self._parent._cast(_767.AbstractTCA)

        @property
        def ease_off_based_tca(self) -> 'EaseOffBasedTCA':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'EaseOffBasedTCA.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def current_ease_off_optimisation_wheel_u(self) -> 'float':
        """float: 'CurrentEaseOffOptimisationWheelU' is the original name of this property."""

        temp = self.wrapped.CurrentEaseOffOptimisationWheelU

        if temp is None:
            return 0.0

        return temp

    @current_ease_off_optimisation_wheel_u.setter
    def current_ease_off_optimisation_wheel_u(self, value: 'float'):
        self.wrapped.CurrentEaseOffOptimisationWheelU = float(value) if value else 0.0

    @property
    def current_ease_off_optimisation_wheel_v(self) -> 'float':
        """float: 'CurrentEaseOffOptimisationWheelV' is the original name of this property."""

        temp = self.wrapped.CurrentEaseOffOptimisationWheelV

        if temp is None:
            return 0.0

        return temp

    @current_ease_off_optimisation_wheel_v.setter
    def current_ease_off_optimisation_wheel_v(self, value: 'float'):
        self.wrapped.CurrentEaseOffOptimisationWheelV = float(value) if value else 0.0

    @property
    def cast_to(self) -> 'EaseOffBasedTCA._Cast_EaseOffBasedTCA':
        return self._Cast_EaseOffBasedTCA(self)
