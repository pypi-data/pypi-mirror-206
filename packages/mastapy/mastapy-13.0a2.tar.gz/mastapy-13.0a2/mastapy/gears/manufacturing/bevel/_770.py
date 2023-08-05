"""_770.py

ConicalGearManufacturingAnalysis
"""
from mastapy.gears.analysis import _1213
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_MANUFACTURING_ANALYSIS = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Bevel', 'ConicalGearManufacturingAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('ConicalGearManufacturingAnalysis',)


class ConicalGearManufacturingAnalysis(_1213.GearImplementationAnalysis):
    """ConicalGearManufacturingAnalysis

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_MANUFACTURING_ANALYSIS

    class _Cast_ConicalGearManufacturingAnalysis:
        """Special nested class for casting ConicalGearManufacturingAnalysis to subclasses."""

        def __init__(self, parent: 'ConicalGearManufacturingAnalysis'):
            self._parent = parent

        @property
        def gear_implementation_analysis(self):
            return self._parent._cast(_1213.GearImplementationAnalysis)

        @property
        def gear_design_analysis(self):
            from mastapy.gears.analysis import _1212
            
            return self._parent._cast(_1212.GearDesignAnalysis)

        @property
        def abstract_gear_analysis(self):
            from mastapy.gears.analysis import _1209
            
            return self._parent._cast(_1209.AbstractGearAnalysis)

        @property
        def conical_gear_manufacturing_analysis(self) -> 'ConicalGearManufacturingAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConicalGearManufacturingAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'ConicalGearManufacturingAnalysis._Cast_ConicalGearManufacturingAnalysis':
        return self._Cast_ConicalGearManufacturingAnalysis(self)
