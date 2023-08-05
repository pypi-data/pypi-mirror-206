"""_4327.py

DutyCycleResultsForRootAssembly
"""
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2882
from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DUTY_CYCLE_RESULTS_FOR_ROOT_ASSEMBLY = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools', 'DutyCycleResultsForRootAssembly')


__docformat__ = 'restructuredtext en'
__all__ = ('DutyCycleResultsForRootAssembly',)


class DutyCycleResultsForRootAssembly(_0.APIBase):
    """DutyCycleResultsForRootAssembly

    This is a mastapy class.
    """

    TYPE = _DUTY_CYCLE_RESULTS_FOR_ROOT_ASSEMBLY

    class _Cast_DutyCycleResultsForRootAssembly:
        """Special nested class for casting DutyCycleResultsForRootAssembly to subclasses."""

        def __init__(self, parent: 'DutyCycleResultsForRootAssembly'):
            self._parent = parent

        @property
        def duty_cycle_results_for_root_assembly(self) -> 'DutyCycleResultsForRootAssembly':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'DutyCycleResultsForRootAssembly.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def duty_cycle_efficiency_results(self) -> '_2882.DutyCycleEfficiencyResults':
        """DutyCycleEfficiencyResults: 'DutyCycleEfficiencyResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DutyCycleEfficiencyResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'DutyCycleResultsForRootAssembly._Cast_DutyCycleResultsForRootAssembly':
        return self._Cast_DutyCycleResultsForRootAssembly(self)
