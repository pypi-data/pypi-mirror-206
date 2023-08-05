"""_814.py

ConicalManufacturingSGTControlParameters
"""
from mastapy._internal import constructor
from mastapy.gears.manufacturing.bevel.control_parameters import _812
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_MANUFACTURING_SGT_CONTROL_PARAMETERS = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Bevel.ControlParameters', 'ConicalManufacturingSGTControlParameters')


__docformat__ = 'restructuredtext en'
__all__ = ('ConicalManufacturingSGTControlParameters',)


class ConicalManufacturingSGTControlParameters(_812.ConicalGearManufacturingControlParameters):
    """ConicalManufacturingSGTControlParameters

    This is a mastapy class.
    """

    TYPE = _CONICAL_MANUFACTURING_SGT_CONTROL_PARAMETERS

    class _Cast_ConicalManufacturingSGTControlParameters:
        """Special nested class for casting ConicalManufacturingSGTControlParameters to subclasses."""

        def __init__(self, parent: 'ConicalManufacturingSGTControlParameters'):
            self._parent = parent

        @property
        def conical_gear_manufacturing_control_parameters(self):
            return self._parent._cast(_812.ConicalGearManufacturingControlParameters)

        @property
        def conical_manufacturing_sgt_control_parameters(self) -> 'ConicalManufacturingSGTControlParameters':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConicalManufacturingSGTControlParameters.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def delta_ax(self) -> 'float':
        """float: 'DeltaAX' is the original name of this property."""

        temp = self.wrapped.DeltaAX

        if temp is None:
            return 0.0

        return temp

    @delta_ax.setter
    def delta_ax(self, value: 'float'):
        self.wrapped.DeltaAX = float(value) if value else 0.0

    @property
    def delta_gamma_m(self) -> 'float':
        """float: 'DeltaGammaM' is the original name of this property."""

        temp = self.wrapped.DeltaGammaM

        if temp is None:
            return 0.0

        return temp

    @delta_gamma_m.setter
    def delta_gamma_m(self, value: 'float'):
        self.wrapped.DeltaGammaM = float(value) if value else 0.0

    @property
    def delta_gamma_x(self) -> 'float':
        """float: 'DeltaGammaX' is the original name of this property."""

        temp = self.wrapped.DeltaGammaX

        if temp is None:
            return 0.0

        return temp

    @delta_gamma_x.setter
    def delta_gamma_x(self, value: 'float'):
        self.wrapped.DeltaGammaX = float(value) if value else 0.0

    @property
    def root_angle_of_the_pinion(self) -> 'float':
        """float: 'RootAngleOfThePinion' is the original name of this property."""

        temp = self.wrapped.RootAngleOfThePinion

        if temp is None:
            return 0.0

        return temp

    @root_angle_of_the_pinion.setter
    def root_angle_of_the_pinion(self, value: 'float'):
        self.wrapped.RootAngleOfThePinion = float(value) if value else 0.0

    @property
    def cast_to(self) -> 'ConicalManufacturingSGTControlParameters._Cast_ConicalManufacturingSGTControlParameters':
        return self._Cast_ConicalManufacturingSGTControlParameters(self)
