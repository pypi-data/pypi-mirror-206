"""_755.py

PlungeShavingDynamicsViewModel
"""
from mastapy._internal import constructor
from mastapy.gears.manufacturing.cylindrical.axial_and_plunge_shaving_dynamics import _751, _765, _750
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLUNGE_SHAVING_DYNAMICS_VIEW_MODEL = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Cylindrical.AxialAndPlungeShavingDynamics', 'PlungeShavingDynamicsViewModel')


__docformat__ = 'restructuredtext en'
__all__ = ('PlungeShavingDynamicsViewModel',)


class PlungeShavingDynamicsViewModel(_765.ShavingDynamicsViewModel['_750.PlungeShaverDynamics']):
    """PlungeShavingDynamicsViewModel

    This is a mastapy class.
    """

    TYPE = _PLUNGE_SHAVING_DYNAMICS_VIEW_MODEL

    class _Cast_PlungeShavingDynamicsViewModel:
        """Special nested class for casting PlungeShavingDynamicsViewModel to subclasses."""

        def __init__(self, parent: 'PlungeShavingDynamicsViewModel'):
            self._parent = parent

        @property
        def shaving_dynamics_view_model(self):
            return self._parent._cast(_765.ShavingDynamicsViewModel)

        @property
        def shaving_dynamics_view_model_base(self):
            from mastapy.gears.manufacturing.cylindrical.axial_and_plunge_shaving_dynamics import _766
            
            return self._parent._cast(_766.ShavingDynamicsViewModelBase)

        @property
        def gear_manufacturing_configuration_view_model(self):
            from mastapy.gears.manufacturing.cylindrical import _623
            
            return self._parent._cast(_623.GearManufacturingConfigurationViewModel)

        @property
        def plunge_shaving_dynamics_view_model(self) -> 'PlungeShavingDynamicsViewModel':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'PlungeShavingDynamicsViewModel.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def transverse_plane_on_gear_for_analysis(self) -> 'float':
        """float: 'TransversePlaneOnGearForAnalysis' is the original name of this property."""

        temp = self.wrapped.TransversePlaneOnGearForAnalysis

        if temp is None:
            return 0.0

        return temp

    @transverse_plane_on_gear_for_analysis.setter
    def transverse_plane_on_gear_for_analysis(self, value: 'float'):
        self.wrapped.TransversePlaneOnGearForAnalysis = float(value) if value else 0.0

    @property
    def settings(self) -> '_751.PlungeShaverDynamicSettings':
        """PlungeShaverDynamicSettings: 'Settings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Settings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'PlungeShavingDynamicsViewModel._Cast_PlungeShavingDynamicsViewModel':
        return self._Cast_PlungeShavingDynamicsViewModel(self)
