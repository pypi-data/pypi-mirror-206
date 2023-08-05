"""_2627.py

AnalysisCaseVariable
"""
from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ANALYSIS_CASE_VARIABLE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults', 'AnalysisCaseVariable')


__docformat__ = 'restructuredtext en'
__all__ = ('AnalysisCaseVariable',)


class AnalysisCaseVariable(_0.APIBase):
    """AnalysisCaseVariable

    This is a mastapy class.
    """

    TYPE = _ANALYSIS_CASE_VARIABLE

    class _Cast_AnalysisCaseVariable:
        """Special nested class for casting AnalysisCaseVariable to subclasses."""

        def __init__(self, parent: 'AnalysisCaseVariable'):
            self._parent = parent

        @property
        def parametric_study_variable(self):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import _4367
            
            return self._parent._cast(_4367.ParametricStudyVariable)

        @property
        def analysis_case_variable(self) -> 'AnalysisCaseVariable':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AnalysisCaseVariable.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def entity_name(self) -> 'str':
        """str: 'EntityName' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.EntityName

        if temp is None:
            return ''

        return temp

    @property
    def cast_to(self) -> 'AnalysisCaseVariable._Cast_AnalysisCaseVariable':
        return self._Cast_AnalysisCaseVariable(self)
