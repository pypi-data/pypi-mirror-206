"""_1859.py

BearingLoadCaseResultsForPst
"""
from mastapy._internal import constructor
from mastapy.bearings import _1860
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEARING_LOAD_CASE_RESULTS_FOR_PST = python_net_import('SMT.MastaAPI.Bearings', 'BearingLoadCaseResultsForPst')


__docformat__ = 'restructuredtext en'
__all__ = ('BearingLoadCaseResultsForPst',)


class BearingLoadCaseResultsForPst(_1860.BearingLoadCaseResultsLightweight):
    """BearingLoadCaseResultsForPst

    This is a mastapy class.
    """

    TYPE = _BEARING_LOAD_CASE_RESULTS_FOR_PST

    class _Cast_BearingLoadCaseResultsForPst:
        """Special nested class for casting BearingLoadCaseResultsForPst to subclasses."""

        def __init__(self, parent: 'BearingLoadCaseResultsForPst'):
            self._parent = parent

        @property
        def bearing_load_case_results_lightweight(self):
            return self._parent._cast(_1860.BearingLoadCaseResultsLightweight)

        @property
        def bearing_load_case_results_for_pst(self) -> 'BearingLoadCaseResultsForPst':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'BearingLoadCaseResultsForPst.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def relative_misalignment(self) -> 'float':
        """float: 'RelativeMisalignment' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RelativeMisalignment

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self) -> 'BearingLoadCaseResultsForPst._Cast_BearingLoadCaseResultsForPst':
        return self._Cast_BearingLoadCaseResultsForPst(self)
