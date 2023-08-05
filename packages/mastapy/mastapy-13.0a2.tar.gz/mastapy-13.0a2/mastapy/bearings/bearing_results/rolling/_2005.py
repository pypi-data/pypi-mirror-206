"""_2005.py

LoadedNeedleRollerBearingElement
"""
from mastapy._internal import constructor
from mastapy.bearings.bearing_results.rolling import _1993
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_NEEDLE_ROLLER_BEARING_ELEMENT = python_net_import('SMT.MastaAPI.Bearings.BearingResults.Rolling', 'LoadedNeedleRollerBearingElement')


__docformat__ = 'restructuredtext en'
__all__ = ('LoadedNeedleRollerBearingElement',)


class LoadedNeedleRollerBearingElement(_1993.LoadedCylindricalRollerBearingElement):
    """LoadedNeedleRollerBearingElement

    This is a mastapy class.
    """

    TYPE = _LOADED_NEEDLE_ROLLER_BEARING_ELEMENT

    class _Cast_LoadedNeedleRollerBearingElement:
        """Special nested class for casting LoadedNeedleRollerBearingElement to subclasses."""

        def __init__(self, parent: 'LoadedNeedleRollerBearingElement'):
            self._parent = parent

        @property
        def loaded_cylindrical_roller_bearing_element(self):
            return self._parent._cast(_1993.LoadedCylindricalRollerBearingElement)

        @property
        def loaded_non_barrel_roller_element(self):
            from mastapy.bearings.bearing_results.rolling import _2012
            
            return self._parent._cast(_2012.LoadedNonBarrelRollerElement)

        @property
        def loaded_roller_bearing_element(self):
            from mastapy.bearings.bearing_results.rolling import _2013
            
            return self._parent._cast(_2013.LoadedRollerBearingElement)

        @property
        def loaded_element(self):
            from mastapy.bearings.bearing_results.rolling import _1999
            
            return self._parent._cast(_1999.LoadedElement)

        @property
        def loaded_needle_roller_bearing_element(self) -> 'LoadedNeedleRollerBearingElement':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'LoadedNeedleRollerBearingElement.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def sliding_power_loss_from_hysteresis(self) -> 'float':
        """float: 'SlidingPowerLossFromHysteresis' is the original name of this property."""

        temp = self.wrapped.SlidingPowerLossFromHysteresis

        if temp is None:
            return 0.0

        return temp

    @sliding_power_loss_from_hysteresis.setter
    def sliding_power_loss_from_hysteresis(self, value: 'float'):
        self.wrapped.SlidingPowerLossFromHysteresis = float(value) if value else 0.0

    @property
    def sliding_power_loss_from_macro_sliding_due_to_roller_skew(self) -> 'float':
        """float: 'SlidingPowerLossFromMacroSlidingDueToRollerSkew' is the original name of this property."""

        temp = self.wrapped.SlidingPowerLossFromMacroSlidingDueToRollerSkew

        if temp is None:
            return 0.0

        return temp

    @sliding_power_loss_from_macro_sliding_due_to_roller_skew.setter
    def sliding_power_loss_from_macro_sliding_due_to_roller_skew(self, value: 'float'):
        self.wrapped.SlidingPowerLossFromMacroSlidingDueToRollerSkew = float(value) if value else 0.0

    @property
    def sliding_power_loss_roller_cage_axial_component(self) -> 'float':
        """float: 'SlidingPowerLossRollerCageAxialComponent' is the original name of this property."""

        temp = self.wrapped.SlidingPowerLossRollerCageAxialComponent

        if temp is None:
            return 0.0

        return temp

    @sliding_power_loss_roller_cage_axial_component.setter
    def sliding_power_loss_roller_cage_axial_component(self, value: 'float'):
        self.wrapped.SlidingPowerLossRollerCageAxialComponent = float(value) if value else 0.0

    @property
    def sliding_power_loss_roller_cage_moment_component(self) -> 'float':
        """float: 'SlidingPowerLossRollerCageMomentComponent' is the original name of this property."""

        temp = self.wrapped.SlidingPowerLossRollerCageMomentComponent

        if temp is None:
            return 0.0

        return temp

    @sliding_power_loss_roller_cage_moment_component.setter
    def sliding_power_loss_roller_cage_moment_component(self, value: 'float'):
        self.wrapped.SlidingPowerLossRollerCageMomentComponent = float(value) if value else 0.0

    @property
    def sliding_power_loss_roller_cage_radial_component(self) -> 'float':
        """float: 'SlidingPowerLossRollerCageRadialComponent' is the original name of this property."""

        temp = self.wrapped.SlidingPowerLossRollerCageRadialComponent

        if temp is None:
            return 0.0

        return temp

    @sliding_power_loss_roller_cage_radial_component.setter
    def sliding_power_loss_roller_cage_radial_component(self, value: 'float'):
        self.wrapped.SlidingPowerLossRollerCageRadialComponent = float(value) if value else 0.0

    @property
    def cast_to(self) -> 'LoadedNeedleRollerBearingElement._Cast_LoadedNeedleRollerBearingElement':
        return self._Cast_LoadedNeedleRollerBearingElement(self)
