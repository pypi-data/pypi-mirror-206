"""_813.py

ConicalManufacturingSGMControlParameters
"""
from mastapy._internal import constructor
from mastapy.gears.manufacturing.bevel.control_parameters import _812
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_MANUFACTURING_SGM_CONTROL_PARAMETERS = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Bevel.ControlParameters', 'ConicalManufacturingSGMControlParameters')


__docformat__ = 'restructuredtext en'
__all__ = ('ConicalManufacturingSGMControlParameters',)


class ConicalManufacturingSGMControlParameters(_812.ConicalGearManufacturingControlParameters):
    """ConicalManufacturingSGMControlParameters

    This is a mastapy class.
    """

    TYPE = _CONICAL_MANUFACTURING_SGM_CONTROL_PARAMETERS

    class _Cast_ConicalManufacturingSGMControlParameters:
        """Special nested class for casting ConicalManufacturingSGMControlParameters to subclasses."""

        def __init__(self, parent: 'ConicalManufacturingSGMControlParameters'):
            self._parent = parent

        @property
        def conical_gear_manufacturing_control_parameters(self):
            return self._parent._cast(_812.ConicalGearManufacturingControlParameters)

        @property
        def conical_manufacturing_sgm_control_parameters(self) -> 'ConicalManufacturingSGMControlParameters':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConicalManufacturingSGMControlParameters.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def delta_gamma(self) -> 'float':
        """float: 'DeltaGamma' is the original name of this property."""

        temp = self.wrapped.DeltaGamma

        if temp is None:
            return 0.0

        return temp

    @delta_gamma.setter
    def delta_gamma(self, value: 'float'):
        self.wrapped.DeltaGamma = float(value) if value else 0.0

    @property
    def profile_mismatch_factor(self) -> 'float':
        """float: 'ProfileMismatchFactor' is the original name of this property."""

        temp = self.wrapped.ProfileMismatchFactor

        if temp is None:
            return 0.0

        return temp

    @profile_mismatch_factor.setter
    def profile_mismatch_factor(self, value: 'float'):
        self.wrapped.ProfileMismatchFactor = float(value) if value else 0.0

    @property
    def work_head_offset_change(self) -> 'float':
        """float: 'WorkHeadOffsetChange' is the original name of this property."""

        temp = self.wrapped.WorkHeadOffsetChange

        if temp is None:
            return 0.0

        return temp

    @work_head_offset_change.setter
    def work_head_offset_change(self, value: 'float'):
        self.wrapped.WorkHeadOffsetChange = float(value) if value else 0.0

    @property
    def cast_to(self) -> 'ConicalManufacturingSGMControlParameters._Cast_ConicalManufacturingSGMControlParameters':
        return self._Cast_ConicalManufacturingSGMControlParameters(self)
