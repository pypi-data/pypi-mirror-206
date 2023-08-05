"""_5650.py

AbstractShaftHarmonicAnalysis
"""
from mastapy.system_model.part_model import _2415
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2666
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5651
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_HARMONIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses', 'AbstractShaftHarmonicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('AbstractShaftHarmonicAnalysis',)


class AbstractShaftHarmonicAnalysis(_5651.AbstractShaftOrHousingHarmonicAnalysis):
    """AbstractShaftHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_HARMONIC_ANALYSIS

    class _Cast_AbstractShaftHarmonicAnalysis:
        """Special nested class for casting AbstractShaftHarmonicAnalysis to subclasses."""

        def __init__(self, parent: 'AbstractShaftHarmonicAnalysis'):
            self._parent = parent

        @property
        def abstract_shaft_or_housing_harmonic_analysis(self):
            return self._parent._cast(_5651.AbstractShaftOrHousingHarmonicAnalysis)

        @property
        def component_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5675
            
            return self._parent._cast(_5675.ComponentHarmonicAnalysis)

        @property
        def part_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5755
            
            return self._parent._cast(_5755.PartHarmonicAnalysis)

        @property
        def part_static_load_analysis_case(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7510
            
            return self._parent._cast(_7510.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7507
            
            return self._parent._cast(_7507.PartAnalysisCase)

        @property
        def part_analysis(self):
            from mastapy.system_model.analyses_and_results import _2636
            
            return self._parent._cast(_2636.PartAnalysis)

        @property
        def design_entity_single_context_analysis(self):
            from mastapy.system_model.analyses_and_results import _2632
            
            return self._parent._cast(_2632.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(self):
            from mastapy.system_model.analyses_and_results import _2630
            
            return self._parent._cast(_2630.DesignEntityAnalysis)

        @property
        def cycloidal_disc_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5695
            
            return self._parent._cast(_5695.CycloidalDiscHarmonicAnalysis)

        @property
        def shaft_harmonic_analysis(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5773
            
            return self._parent._cast(_5773.ShaftHarmonicAnalysis)

        @property
        def abstract_shaft_harmonic_analysis(self) -> 'AbstractShaftHarmonicAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AbstractShaftHarmonicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2415.AbstractShaft':
        """AbstractShaft: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results(self) -> '_2666.AbstractShaftSystemDeflection':
        """AbstractShaftSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'AbstractShaftHarmonicAnalysis._Cast_AbstractShaftHarmonicAnalysis':
        return self._Cast_AbstractShaftHarmonicAnalysis(self)
