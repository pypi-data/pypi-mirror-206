"""_1938.py

LoadedConceptRadialClearanceBearingResults
"""
from mastapy._internal import constructor
from mastapy.bearings.bearing_results import _1937
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_CONCEPT_RADIAL_CLEARANCE_BEARING_RESULTS = python_net_import('SMT.MastaAPI.Bearings.BearingResults', 'LoadedConceptRadialClearanceBearingResults')


__docformat__ = 'restructuredtext en'
__all__ = ('LoadedConceptRadialClearanceBearingResults',)


class LoadedConceptRadialClearanceBearingResults(_1937.LoadedConceptClearanceBearingResults):
    """LoadedConceptRadialClearanceBearingResults

    This is a mastapy class.
    """

    TYPE = _LOADED_CONCEPT_RADIAL_CLEARANCE_BEARING_RESULTS

    class _Cast_LoadedConceptRadialClearanceBearingResults:
        """Special nested class for casting LoadedConceptRadialClearanceBearingResults to subclasses."""

        def __init__(self, parent: 'LoadedConceptRadialClearanceBearingResults'):
            self._parent = parent

        @property
        def loaded_concept_clearance_bearing_results(self):
            return self._parent._cast(_1937.LoadedConceptClearanceBearingResults)

        @property
        def loaded_non_linear_bearing_results(self):
            from mastapy.bearings.bearing_results import _1942
            
            return self._parent._cast(_1942.LoadedNonLinearBearingResults)

        @property
        def loaded_bearing_results(self):
            from mastapy.bearings.bearing_results import _1934
            
            return self._parent._cast(_1934.LoadedBearingResults)

        @property
        def bearing_load_case_results_lightweight(self):
            from mastapy.bearings import _1860
            
            return self._parent._cast(_1860.BearingLoadCaseResultsLightweight)

        @property
        def loaded_concept_radial_clearance_bearing_results(self) -> 'LoadedConceptRadialClearanceBearingResults':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'LoadedConceptRadialClearanceBearingResults.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def contact_stiffness(self) -> 'float':
        """float: 'ContactStiffness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ContactStiffness

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_contact_stress(self) -> 'float':
        """float: 'MaximumContactStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumContactStress

        if temp is None:
            return 0.0

        return temp

    @property
    def surface_penetration_in_middle(self) -> 'float':
        """float: 'SurfacePenetrationInMiddle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SurfacePenetrationInMiddle

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self) -> 'LoadedConceptRadialClearanceBearingResults._Cast_LoadedConceptRadialClearanceBearingResults':
        return self._Cast_LoadedConceptRadialClearanceBearingResults(self)
