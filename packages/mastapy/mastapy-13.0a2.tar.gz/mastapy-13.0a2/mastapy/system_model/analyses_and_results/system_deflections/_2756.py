"""_2756.py

LoadCaseOverallEfficiencyResult
"""
from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOAD_CASE_OVERALL_EFFICIENCY_RESULT = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections', 'LoadCaseOverallEfficiencyResult')


__docformat__ = 'restructuredtext en'
__all__ = ('LoadCaseOverallEfficiencyResult',)


class LoadCaseOverallEfficiencyResult(_0.APIBase):
    """LoadCaseOverallEfficiencyResult

    This is a mastapy class.
    """

    TYPE = _LOAD_CASE_OVERALL_EFFICIENCY_RESULT

    class _Cast_LoadCaseOverallEfficiencyResult:
        """Special nested class for casting LoadCaseOverallEfficiencyResult to subclasses."""

        def __init__(self, parent: 'LoadCaseOverallEfficiencyResult'):
            self._parent = parent

        @property
        def load_case_overall_efficiency_result(self) -> 'LoadCaseOverallEfficiencyResult':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'LoadCaseOverallEfficiencyResult.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def duration(self) -> 'float':
        """float: 'Duration' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Duration

        if temp is None:
            return 0.0

        return temp

    @property
    def efficiency(self) -> 'float':
        """float: 'Efficiency' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Efficiency

        if temp is None:
            return 0.0

        return temp

    @property
    def energy_input(self) -> 'float':
        """float: 'EnergyInput' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.EnergyInput

        if temp is None:
            return 0.0

        return temp

    @property
    def energy_lost(self) -> 'float':
        """float: 'EnergyLost' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.EnergyLost

        if temp is None:
            return 0.0

        return temp

    @property
    def energy_output(self) -> 'float':
        """float: 'EnergyOutput' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.EnergyOutput

        if temp is None:
            return 0.0

        return temp

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
    def cast_to(self) -> 'LoadCaseOverallEfficiencyResult._Cast_LoadCaseOverallEfficiencyResult':
        return self._Cast_LoadCaseOverallEfficiencyResult(self)
