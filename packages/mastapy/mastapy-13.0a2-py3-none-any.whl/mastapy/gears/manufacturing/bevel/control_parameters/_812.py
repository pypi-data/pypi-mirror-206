"""_812.py

ConicalGearManufacturingControlParameters
"""
from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_MANUFACTURING_CONTROL_PARAMETERS = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Bevel.ControlParameters', 'ConicalGearManufacturingControlParameters')


__docformat__ = 'restructuredtext en'
__all__ = ('ConicalGearManufacturingControlParameters',)


class ConicalGearManufacturingControlParameters(_0.APIBase):
    """ConicalGearManufacturingControlParameters

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_MANUFACTURING_CONTROL_PARAMETERS

    class _Cast_ConicalGearManufacturingControlParameters:
        """Special nested class for casting ConicalGearManufacturingControlParameters to subclasses."""

        def __init__(self, parent: 'ConicalGearManufacturingControlParameters'):
            self._parent = parent

        @property
        def conical_manufacturing_sgm_control_parameters(self):
            from mastapy.gears.manufacturing.bevel.control_parameters import _813
            
            return self._parent._cast(_813.ConicalManufacturingSGMControlParameters)

        @property
        def conical_manufacturing_sgt_control_parameters(self):
            from mastapy.gears.manufacturing.bevel.control_parameters import _814
            
            return self._parent._cast(_814.ConicalManufacturingSGTControlParameters)

        @property
        def conical_manufacturing_smt_control_parameters(self):
            from mastapy.gears.manufacturing.bevel.control_parameters import _815
            
            return self._parent._cast(_815.ConicalManufacturingSMTControlParameters)

        @property
        def conical_gear_manufacturing_control_parameters(self) -> 'ConicalGearManufacturingControlParameters':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConicalGearManufacturingControlParameters.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def length_factor_of_contact_pattern(self) -> 'float':
        """float: 'LengthFactorOfContactPattern' is the original name of this property."""

        temp = self.wrapped.LengthFactorOfContactPattern

        if temp is None:
            return 0.0

        return temp

    @length_factor_of_contact_pattern.setter
    def length_factor_of_contact_pattern(self, value: 'float'):
        self.wrapped.LengthFactorOfContactPattern = float(value) if value else 0.0

    @property
    def pinion_root_relief_length(self) -> 'float':
        """float: 'PinionRootReliefLength' is the original name of this property."""

        temp = self.wrapped.PinionRootReliefLength

        if temp is None:
            return 0.0

        return temp

    @pinion_root_relief_length.setter
    def pinion_root_relief_length(self, value: 'float'):
        self.wrapped.PinionRootReliefLength = float(value) if value else 0.0

    @property
    def cast_to(self) -> 'ConicalGearManufacturingControlParameters._Cast_ConicalGearManufacturingControlParameters':
        return self._Cast_ConicalGearManufacturingControlParameters(self)
