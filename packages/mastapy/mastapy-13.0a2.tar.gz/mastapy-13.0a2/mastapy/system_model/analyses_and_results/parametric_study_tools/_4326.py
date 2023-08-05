"""_4326.py

DutyCycleResultsForAllGearSets
"""
from mastapy.gears.analysis import _1221
from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DUTY_CYCLE_RESULTS_FOR_ALL_GEAR_SETS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools', 'DutyCycleResultsForAllGearSets')


__docformat__ = 'restructuredtext en'
__all__ = ('DutyCycleResultsForAllGearSets',)


class DutyCycleResultsForAllGearSets(_0.APIBase):
    """DutyCycleResultsForAllGearSets

    This is a mastapy class.
    """

    TYPE = _DUTY_CYCLE_RESULTS_FOR_ALL_GEAR_SETS

    class _Cast_DutyCycleResultsForAllGearSets:
        """Special nested class for casting DutyCycleResultsForAllGearSets to subclasses."""

        def __init__(self, parent: 'DutyCycleResultsForAllGearSets'):
            self._parent = parent

        @property
        def duty_cycle_results_for_all_gear_sets(self) -> 'DutyCycleResultsForAllGearSets':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'DutyCycleResultsForAllGearSets.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def duty_cycle_results(self) -> '_1221.GearSetGroupDutyCycle':
        """GearSetGroupDutyCycle: 'DutyCycleResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DutyCycleResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'DutyCycleResultsForAllGearSets._Cast_DutyCycleResultsForAllGearSets':
        return self._Cast_DutyCycleResultsForAllGearSets(self)
