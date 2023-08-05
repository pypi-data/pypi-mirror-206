"""_1166.py

ConicalGearBiasModification
"""
from mastapy._internal import constructor
from mastapy.gears.micro_geometry import _564
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_BIAS_MODIFICATION = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Conical.MicroGeometry', 'ConicalGearBiasModification')


__docformat__ = 'restructuredtext en'
__all__ = ('ConicalGearBiasModification',)


class ConicalGearBiasModification(_564.BiasModification):
    """ConicalGearBiasModification

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_BIAS_MODIFICATION

    class _Cast_ConicalGearBiasModification:
        """Special nested class for casting ConicalGearBiasModification to subclasses."""

        def __init__(self, parent: 'ConicalGearBiasModification'):
            self._parent = parent

        @property
        def bias_modification(self):
            return self._parent._cast(_564.BiasModification)

        @property
        def modification(self):
            from mastapy.gears.micro_geometry import _574
            
            return self._parent._cast(_574.Modification)

        @property
        def conical_gear_bias_modification(self) -> 'ConicalGearBiasModification':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConicalGearBiasModification.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def constant_relief(self) -> 'float':
        """float: 'ConstantRelief' is the original name of this property."""

        temp = self.wrapped.ConstantRelief

        if temp is None:
            return 0.0

        return temp

    @constant_relief.setter
    def constant_relief(self, value: 'float'):
        self.wrapped.ConstantRelief = float(value) if value else 0.0

    @property
    def cast_to(self) -> 'ConicalGearBiasModification._Cast_ConicalGearBiasModification':
        return self._Cast_ConicalGearBiasModification(self)
