"""_1213.py

GearImplementationAnalysis
"""
from mastapy.gears.analysis import _1212
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_IMPLEMENTATION_ANALYSIS = python_net_import('SMT.MastaAPI.Gears.Analysis', 'GearImplementationAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('GearImplementationAnalysis',)


class GearImplementationAnalysis(_1212.GearDesignAnalysis):
    """GearImplementationAnalysis

    This is a mastapy class.
    """

    TYPE = _GEAR_IMPLEMENTATION_ANALYSIS

    class _Cast_GearImplementationAnalysis:
        """Special nested class for casting GearImplementationAnalysis to subclasses."""

        def __init__(self, parent: 'GearImplementationAnalysis'):
            self._parent = parent

        @property
        def gear_design_analysis(self):
            return self._parent._cast(_1212.GearDesignAnalysis)

        @property
        def abstract_gear_analysis(self):
            from mastapy.gears.analysis import _1209
            
            return self._parent._cast(_1209.AbstractGearAnalysis)

        @property
        def cylindrical_manufactured_gear_load_case(self):
            from mastapy.gears.manufacturing.cylindrical import _612
            
            return self._parent._cast(_612.CylindricalManufacturedGearLoadCase)

        @property
        def conical_gear_manufacturing_analysis(self):
            from mastapy.gears.manufacturing.bevel import _770
            
            return self._parent._cast(_770.ConicalGearManufacturingAnalysis)

        @property
        def gear_load_distribution_analysis(self):
            from mastapy.gears.ltca import _835
            
            return self._parent._cast(_835.GearLoadDistributionAnalysis)

        @property
        def cylindrical_gear_load_distribution_analysis(self):
            from mastapy.gears.ltca.cylindrical import _851
            
            return self._parent._cast(_851.CylindricalGearLoadDistributionAnalysis)

        @property
        def conical_gear_load_distribution_analysis(self):
            from mastapy.gears.ltca.conical import _862
            
            return self._parent._cast(_862.ConicalGearLoadDistributionAnalysis)

        @property
        def gear_implementation_analysis(self) -> 'GearImplementationAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GearImplementationAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'GearImplementationAnalysis._Cast_GearImplementationAnalysis':
        return self._Cast_GearImplementationAnalysis(self)
