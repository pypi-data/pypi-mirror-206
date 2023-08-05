"""_5827.py

HarmonicAnalysisResultsBrokenDownByComponentWithinAHarmonic
"""
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results import _5840, _5829
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HARMONIC_ANALYSIS_RESULTS_BROKEN_DOWN_BY_COMPONENT_WITHIN_A_HARMONIC = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.ReportablePropertyResults', 'HarmonicAnalysisResultsBrokenDownByComponentWithinAHarmonic')


__docformat__ = 'restructuredtext en'
__all__ = ('HarmonicAnalysisResultsBrokenDownByComponentWithinAHarmonic',)


class HarmonicAnalysisResultsBrokenDownByComponentWithinAHarmonic(_5829.HarmonicAnalysisResultsBrokenDownByLocationWithinAHarmonic):
    """HarmonicAnalysisResultsBrokenDownByComponentWithinAHarmonic

    This is a mastapy class.
    """

    TYPE = _HARMONIC_ANALYSIS_RESULTS_BROKEN_DOWN_BY_COMPONENT_WITHIN_A_HARMONIC

    class _Cast_HarmonicAnalysisResultsBrokenDownByComponentWithinAHarmonic:
        """Special nested class for casting HarmonicAnalysisResultsBrokenDownByComponentWithinAHarmonic to subclasses."""

        def __init__(self, parent: 'HarmonicAnalysisResultsBrokenDownByComponentWithinAHarmonic'):
            self._parent = parent

        @property
        def harmonic_analysis_results_broken_down_by_location_within_a_harmonic(self):
            return self._parent._cast(_5829.HarmonicAnalysisResultsBrokenDownByLocationWithinAHarmonic)

        @property
        def harmonic_analysis_results_broken_down_by_component_within_a_harmonic(self) -> 'HarmonicAnalysisResultsBrokenDownByComponentWithinAHarmonic':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'HarmonicAnalysisResultsBrokenDownByComponentWithinAHarmonic.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_name(self) -> 'str':
        """str: 'ComponentName' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentName

        if temp is None:
            return ''

        return temp

    @property
    def dynamic_mesh_force(self) -> '_5840.ResultsForResponseOfAComponentOrSurfaceInAHarmonic':
        """ResultsForResponseOfAComponentOrSurfaceInAHarmonic: 'DynamicMeshForce' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DynamicMeshForce

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def dynamic_mesh_moment(self) -> '_5840.ResultsForResponseOfAComponentOrSurfaceInAHarmonic':
        """ResultsForResponseOfAComponentOrSurfaceInAHarmonic: 'DynamicMeshMoment' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DynamicMeshMoment

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def dynamic_misalignment(self) -> '_5840.ResultsForResponseOfAComponentOrSurfaceInAHarmonic':
        """ResultsForResponseOfAComponentOrSurfaceInAHarmonic: 'DynamicMisalignment' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DynamicMisalignment

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def dynamic_te(self) -> '_5840.ResultsForResponseOfAComponentOrSurfaceInAHarmonic':
        """ResultsForResponseOfAComponentOrSurfaceInAHarmonic: 'DynamicTE' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DynamicTE

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def kinetic_energy(self) -> '_5840.ResultsForResponseOfAComponentOrSurfaceInAHarmonic':
        """ResultsForResponseOfAComponentOrSurfaceInAHarmonic: 'KineticEnergy' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.KineticEnergy

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def strain_energy(self) -> '_5840.ResultsForResponseOfAComponentOrSurfaceInAHarmonic':
        """ResultsForResponseOfAComponentOrSurfaceInAHarmonic: 'StrainEnergy' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StrainEnergy

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'HarmonicAnalysisResultsBrokenDownByComponentWithinAHarmonic._Cast_HarmonicAnalysisResultsBrokenDownByComponentWithinAHarmonic':
        return self._Cast_HarmonicAnalysisResultsBrokenDownByComponentWithinAHarmonic(self)
