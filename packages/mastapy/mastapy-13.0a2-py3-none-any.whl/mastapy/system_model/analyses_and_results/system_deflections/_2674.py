"""_2674.py

BearingDynamicPostAnalysisResultWrapper
"""
from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEARING_DYNAMIC_POST_ANALYSIS_RESULT_WRAPPER = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections', 'BearingDynamicPostAnalysisResultWrapper')


__docformat__ = 'restructuredtext en'
__all__ = ('BearingDynamicPostAnalysisResultWrapper',)


class BearingDynamicPostAnalysisResultWrapper(_0.APIBase):
    """BearingDynamicPostAnalysisResultWrapper

    This is a mastapy class.
    """

    TYPE = _BEARING_DYNAMIC_POST_ANALYSIS_RESULT_WRAPPER

    class _Cast_BearingDynamicPostAnalysisResultWrapper:
        """Special nested class for casting BearingDynamicPostAnalysisResultWrapper to subclasses."""

        def __init__(self, parent: 'BearingDynamicPostAnalysisResultWrapper'):
            self._parent = parent

        @property
        def bearing_dynamic_post_analysis_result_wrapper(self) -> 'BearingDynamicPostAnalysisResultWrapper':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'BearingDynamicPostAnalysisResultWrapper.TYPE'):
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
    def plot(self) -> 'bool':
        """bool: 'Plot' is the original name of this property."""

        temp = self.wrapped.Plot

        if temp is None:
            return False

        return temp

    @plot.setter
    def plot(self, value: 'bool'):
        self.wrapped.Plot = bool(value) if value else False

    @property
    def cast_to(self) -> 'BearingDynamicPostAnalysisResultWrapper._Cast_BearingDynamicPostAnalysisResultWrapper':
        return self._Cast_BearingDynamicPostAnalysisResultWrapper(self)
