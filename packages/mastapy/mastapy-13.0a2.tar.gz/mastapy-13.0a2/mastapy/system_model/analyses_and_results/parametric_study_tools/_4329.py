"""_4329.py

DutyCycleResultsForSingleShaft
"""
from mastapy.shafts import _19
from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DUTY_CYCLE_RESULTS_FOR_SINGLE_SHAFT = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools', 'DutyCycleResultsForSingleShaft')


__docformat__ = 'restructuredtext en'
__all__ = ('DutyCycleResultsForSingleShaft',)


class DutyCycleResultsForSingleShaft(_0.APIBase):
    """DutyCycleResultsForSingleShaft

    This is a mastapy class.
    """

    TYPE = _DUTY_CYCLE_RESULTS_FOR_SINGLE_SHAFT

    class _Cast_DutyCycleResultsForSingleShaft:
        """Special nested class for casting DutyCycleResultsForSingleShaft to subclasses."""

        def __init__(self, parent: 'DutyCycleResultsForSingleShaft'):
            self._parent = parent

        @property
        def duty_cycle_results_for_single_shaft(self) -> 'DutyCycleResultsForSingleShaft':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'DutyCycleResultsForSingleShaft.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def duty_cycle_results(self) -> '_19.ShaftDamageResults':
        """ShaftDamageResults: 'DutyCycleResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DutyCycleResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'DutyCycleResultsForSingleShaft._Cast_DutyCycleResultsForSingleShaft':
        return self._Cast_DutyCycleResultsForSingleShaft(self)
