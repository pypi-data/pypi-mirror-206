"""_771.py

ConicalGearManufacturingConfig
"""
from mastapy.gears.manufacturing.bevel import _773
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_MANUFACTURING_CONFIG = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Bevel', 'ConicalGearManufacturingConfig')


__docformat__ = 'restructuredtext en'
__all__ = ('ConicalGearManufacturingConfig',)


class ConicalGearManufacturingConfig(_773.ConicalGearMicroGeometryConfigBase):
    """ConicalGearManufacturingConfig

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_MANUFACTURING_CONFIG

    class _Cast_ConicalGearManufacturingConfig:
        """Special nested class for casting ConicalGearManufacturingConfig to subclasses."""

        def __init__(self, parent: 'ConicalGearManufacturingConfig'):
            self._parent = parent

        @property
        def conical_gear_micro_geometry_config_base(self):
            return self._parent._cast(_773.ConicalGearMicroGeometryConfigBase)

        @property
        def gear_implementation_detail(self):
            from mastapy.gears.analysis import _1215
            
            return self._parent._cast(_1215.GearImplementationDetail)

        @property
        def gear_design_analysis(self):
            from mastapy.gears.analysis import _1212
            
            return self._parent._cast(_1212.GearDesignAnalysis)

        @property
        def abstract_gear_analysis(self):
            from mastapy.gears.analysis import _1209
            
            return self._parent._cast(_1209.AbstractGearAnalysis)

        @property
        def conical_pinion_manufacturing_config(self):
            from mastapy.gears.manufacturing.bevel import _783
            
            return self._parent._cast(_783.ConicalPinionManufacturingConfig)

        @property
        def conical_wheel_manufacturing_config(self):
            from mastapy.gears.manufacturing.bevel import _789
            
            return self._parent._cast(_789.ConicalWheelManufacturingConfig)

        @property
        def conical_gear_manufacturing_config(self) -> 'ConicalGearManufacturingConfig':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConicalGearManufacturingConfig.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'ConicalGearManufacturingConfig._Cast_ConicalGearManufacturingConfig':
        return self._Cast_ConicalGearManufacturingConfig(self)
