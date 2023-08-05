"""_1567.py

AnalysisRunInformation
"""
from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ANALYSIS_RUN_INFORMATION = python_net_import('SMT.MastaAPI.Utility', 'AnalysisRunInformation')


__docformat__ = 'restructuredtext en'
__all__ = ('AnalysisRunInformation',)


class AnalysisRunInformation(_0.APIBase):
    """AnalysisRunInformation

    This is a mastapy class.
    """

    TYPE = _ANALYSIS_RUN_INFORMATION

    class _Cast_AnalysisRunInformation:
        """Special nested class for casting AnalysisRunInformation to subclasses."""

        def __init__(self, parent: 'AnalysisRunInformation'):
            self._parent = parent

        @property
        def analysis_run_information(self) -> 'AnalysisRunInformation':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AnalysisRunInformation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def masta_version_used(self) -> 'str':
        """str: 'MASTAVersionUsed' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MASTAVersionUsed

        if temp is None:
            return ''

        return temp

    @property
    def specifications_of_computer_used(self) -> 'str':
        """str: 'SpecificationsOfComputerUsed' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SpecificationsOfComputerUsed

        if temp is None:
            return ''

        return temp

    @property
    def time_taken(self) -> 'str':
        """str: 'TimeTaken' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TimeTaken

        if temp is None:
            return ''

        return temp

    @property
    def cast_to(self) -> 'AnalysisRunInformation._Cast_AnalysisRunInformation':
        return self._Cast_AnalysisRunInformation(self)
