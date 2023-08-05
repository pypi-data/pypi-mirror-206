"""_863.py

ConicalGearSetLoadDistributionAnalysis
"""
from mastapy.gears.ltca import _841
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_SET_LOAD_DISTRIBUTION_ANALYSIS = python_net_import('SMT.MastaAPI.Gears.LTCA.Conical', 'ConicalGearSetLoadDistributionAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('ConicalGearSetLoadDistributionAnalysis',)


class ConicalGearSetLoadDistributionAnalysis(_841.GearSetLoadDistributionAnalysis):
    """ConicalGearSetLoadDistributionAnalysis

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_SET_LOAD_DISTRIBUTION_ANALYSIS

    class _Cast_ConicalGearSetLoadDistributionAnalysis:
        """Special nested class for casting ConicalGearSetLoadDistributionAnalysis to subclasses."""

        def __init__(self, parent: 'ConicalGearSetLoadDistributionAnalysis'):
            self._parent = parent

        @property
        def gear_set_load_distribution_analysis(self):
            return self._parent._cast(_841.GearSetLoadDistributionAnalysis)

        @property
        def gear_set_implementation_analysis(self):
            from mastapy.gears.analysis import _1222
            
            return self._parent._cast(_1222.GearSetImplementationAnalysis)

        @property
        def gear_set_implementation_analysis_abstract(self):
            from mastapy.gears.analysis import _1223
            
            return self._parent._cast(_1223.GearSetImplementationAnalysisAbstract)

        @property
        def gear_set_design_analysis(self):
            from mastapy.gears.analysis import _1220
            
            return self._parent._cast(_1220.GearSetDesignAnalysis)

        @property
        def abstract_gear_set_analysis(self):
            from mastapy.gears.analysis import _1211
            
            return self._parent._cast(_1211.AbstractGearSetAnalysis)

        @property
        def conical_gear_set_load_distribution_analysis(self) -> 'ConicalGearSetLoadDistributionAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConicalGearSetLoadDistributionAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'ConicalGearSetLoadDistributionAnalysis._Cast_ConicalGearSetLoadDistributionAnalysis':
        return self._Cast_ConicalGearSetLoadDistributionAnalysis(self)
