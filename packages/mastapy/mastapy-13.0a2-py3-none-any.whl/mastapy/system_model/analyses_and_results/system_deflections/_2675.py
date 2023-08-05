"""_2675.py

BearingDynamicResultsPropertyWrapper
"""
from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEARING_DYNAMIC_RESULTS_PROPERTY_WRAPPER = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections', 'BearingDynamicResultsPropertyWrapper')


__docformat__ = 'restructuredtext en'
__all__ = ('BearingDynamicResultsPropertyWrapper',)


class BearingDynamicResultsPropertyWrapper(_0.APIBase):
    """BearingDynamicResultsPropertyWrapper

    This is a mastapy class.
    """

    TYPE = _BEARING_DYNAMIC_RESULTS_PROPERTY_WRAPPER

    class _Cast_BearingDynamicResultsPropertyWrapper:
        """Special nested class for casting BearingDynamicResultsPropertyWrapper to subclasses."""

        def __init__(self, parent: 'BearingDynamicResultsPropertyWrapper'):
            self._parent = parent

        @property
        def bearing_dynamic_results_property_wrapper(self) -> 'BearingDynamicResultsPropertyWrapper':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'BearingDynamicResultsPropertyWrapper.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def name(self) -> 'str':
        """str: 'Name' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Name

        if temp is None:
            return ''

        return temp

    @property
    def plot_cdf(self) -> 'bool':
        """bool: 'PlotCDF' is the original name of this property."""

        temp = self.wrapped.PlotCDF

        if temp is None:
            return False

        return temp

    @plot_cdf.setter
    def plot_cdf(self, value: 'bool'):
        self.wrapped.PlotCDF = bool(value) if value else False

    @property
    def plot_time_series(self) -> 'bool':
        """bool: 'PlotTimeSeries' is the original name of this property."""

        temp = self.wrapped.PlotTimeSeries

        if temp is None:
            return False

        return temp

    @plot_time_series.setter
    def plot_time_series(self, value: 'bool'):
        self.wrapped.PlotTimeSeries = bool(value) if value else False

    @property
    def cast_to(self) -> 'BearingDynamicResultsPropertyWrapper._Cast_BearingDynamicResultsPropertyWrapper':
        return self._Cast_BearingDynamicResultsPropertyWrapper(self)
