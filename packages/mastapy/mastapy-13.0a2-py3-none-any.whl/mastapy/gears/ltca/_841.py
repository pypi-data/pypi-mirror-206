"""_841.py

GearSetLoadDistributionAnalysis
"""
from mastapy._internal import constructor
from mastapy.gears.analysis import _1222
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_SET_LOAD_DISTRIBUTION_ANALYSIS = python_net_import('SMT.MastaAPI.Gears.LTCA', 'GearSetLoadDistributionAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('GearSetLoadDistributionAnalysis',)


class GearSetLoadDistributionAnalysis(_1222.GearSetImplementationAnalysis):
    """GearSetLoadDistributionAnalysis

    This is a mastapy class.
    """

    TYPE = _GEAR_SET_LOAD_DISTRIBUTION_ANALYSIS

    class _Cast_GearSetLoadDistributionAnalysis:
        """Special nested class for casting GearSetLoadDistributionAnalysis to subclasses."""

        def __init__(self, parent: 'GearSetLoadDistributionAnalysis'):
            self._parent = parent

        @property
        def gear_set_implementation_analysis(self):
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
        def cylindrical_gear_set_load_distribution_analysis(self):
            from mastapy.gears.ltca.cylindrical import _855
            
            return self._parent._cast(_855.CylindricalGearSetLoadDistributionAnalysis)

        @property
        def face_gear_set_load_distribution_analysis(self):
            from mastapy.gears.ltca.cylindrical import _857
            
            return self._parent._cast(_857.FaceGearSetLoadDistributionAnalysis)

        @property
        def conical_gear_set_load_distribution_analysis(self):
            from mastapy.gears.ltca.conical import _863
            
            return self._parent._cast(_863.ConicalGearSetLoadDistributionAnalysis)

        @property
        def gear_set_load_distribution_analysis(self) -> 'GearSetLoadDistributionAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GearSetLoadDistributionAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def is_a_system_deflection_analysis(self) -> 'bool':
        """bool: 'IsASystemDeflectionAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.IsASystemDeflectionAnalysis

        if temp is None:
            return False

        return temp

    @property
    def cast_to(self) -> 'GearSetLoadDistributionAnalysis._Cast_GearSetLoadDistributionAnalysis':
        return self._Cast_GearSetLoadDistributionAnalysis(self)
