"""_5826.py

HarmonicAnalysisCombinedForMultipleSurfacesWithinAHarmonic
"""
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results import _5831
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HARMONIC_ANALYSIS_COMBINED_FOR_MULTIPLE_SURFACES_WITHIN_A_HARMONIC = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.ReportablePropertyResults', 'HarmonicAnalysisCombinedForMultipleSurfacesWithinAHarmonic')


__docformat__ = 'restructuredtext en'
__all__ = ('HarmonicAnalysisCombinedForMultipleSurfacesWithinAHarmonic',)


class HarmonicAnalysisCombinedForMultipleSurfacesWithinAHarmonic(_5831.HarmonicAnalysisResultsBrokenDownBySurfaceWithinAHarmonic):
    """HarmonicAnalysisCombinedForMultipleSurfacesWithinAHarmonic

    This is a mastapy class.
    """

    TYPE = _HARMONIC_ANALYSIS_COMBINED_FOR_MULTIPLE_SURFACES_WITHIN_A_HARMONIC

    class _Cast_HarmonicAnalysisCombinedForMultipleSurfacesWithinAHarmonic:
        """Special nested class for casting HarmonicAnalysisCombinedForMultipleSurfacesWithinAHarmonic to subclasses."""

        def __init__(self, parent: 'HarmonicAnalysisCombinedForMultipleSurfacesWithinAHarmonic'):
            self._parent = parent

        @property
        def harmonic_analysis_results_broken_down_by_surface_within_a_harmonic(self):
            return self._parent._cast(_5831.HarmonicAnalysisResultsBrokenDownBySurfaceWithinAHarmonic)

        @property
        def harmonic_analysis_results_broken_down_by_location_within_a_harmonic(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results import _5829
            
            return self._parent._cast(_5829.HarmonicAnalysisResultsBrokenDownByLocationWithinAHarmonic)

        @property
        def harmonic_analysis_combined_for_multiple_surfaces_within_a_harmonic(self) -> 'HarmonicAnalysisCombinedForMultipleSurfacesWithinAHarmonic':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'HarmonicAnalysisCombinedForMultipleSurfacesWithinAHarmonic.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def surface_names(self) -> 'str':
        """str: 'SurfaceNames' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SurfaceNames

        if temp is None:
            return ''

        return temp

    @property
    def cast_to(self) -> 'HarmonicAnalysisCombinedForMultipleSurfacesWithinAHarmonic._Cast_HarmonicAnalysisCombinedForMultipleSurfacesWithinAHarmonic':
        return self._Cast_HarmonicAnalysisCombinedForMultipleSurfacesWithinAHarmonic(self)
