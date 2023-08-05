"""_835.py

GearLoadDistributionAnalysis
"""
from mastapy.gears.analysis import _1213
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_LOAD_DISTRIBUTION_ANALYSIS = python_net_import('SMT.MastaAPI.Gears.LTCA', 'GearLoadDistributionAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('GearLoadDistributionAnalysis',)


class GearLoadDistributionAnalysis(_1213.GearImplementationAnalysis):
    """GearLoadDistributionAnalysis

    This is a mastapy class.
    """

    TYPE = _GEAR_LOAD_DISTRIBUTION_ANALYSIS

    class _Cast_GearLoadDistributionAnalysis:
        """Special nested class for casting GearLoadDistributionAnalysis to subclasses."""

        def __init__(self, parent: 'GearLoadDistributionAnalysis'):
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
        def cylindrical_gear_load_distribution_analysis(self):
            from mastapy.gears.ltca.cylindrical import _851
            
            return self._parent._cast(_851.CylindricalGearLoadDistributionAnalysis)

        @property
        def conical_gear_load_distribution_analysis(self):
            from mastapy.gears.ltca.conical import _862
            
            return self._parent._cast(_862.ConicalGearLoadDistributionAnalysis)

        @property
        def gear_load_distribution_analysis(self) -> 'GearLoadDistributionAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GearLoadDistributionAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'GearLoadDistributionAnalysis._Cast_GearLoadDistributionAnalysis':
        return self._Cast_GearLoadDistributionAnalysis(self)
