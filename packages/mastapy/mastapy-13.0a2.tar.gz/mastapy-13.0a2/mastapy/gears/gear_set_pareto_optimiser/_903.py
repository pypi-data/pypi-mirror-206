"""_903.py

FaceGearSetParetoOptimiser
"""
from typing import List

from mastapy._internal.python_net import python_net_import
from mastapy._internal import constructor, conversion
from mastapy.gears.gear_designs.face import _990
from mastapy.gears.gear_set_pareto_optimiser import _907
from mastapy._internal.cast_exception import CastException

_DATABASE_WITH_SELECTED_ITEM = python_net_import('SMT.MastaAPI.UtilityGUI.Databases', 'DatabaseWithSelectedItem')
_FACE_GEAR_SET_PARETO_OPTIMISER = python_net_import('SMT.MastaAPI.Gears.GearSetParetoOptimiser', 'FaceGearSetParetoOptimiser')


__docformat__ = 'restructuredtext en'
__all__ = ('FaceGearSetParetoOptimiser',)


class FaceGearSetParetoOptimiser(_907.GearSetParetoOptimiser):
    """FaceGearSetParetoOptimiser

    This is a mastapy class.
    """

    TYPE = _FACE_GEAR_SET_PARETO_OPTIMISER

    class _Cast_FaceGearSetParetoOptimiser:
        """Special nested class for casting FaceGearSetParetoOptimiser to subclasses."""

        def __init__(self, parent: 'FaceGearSetParetoOptimiser'):
            self._parent = parent

        @property
        def gear_set_pareto_optimiser(self):
            return self._parent._cast(_907.GearSetParetoOptimiser)

        @property
        def design_space_search_base(self):
            from mastapy.gears.gear_set_pareto_optimiser import _901, _906
            from mastapy.gears.rating import _351
            
            return self._parent._cast(_901.DesignSpaceSearchBase)

        @property
        def face_gear_set_pareto_optimiser(self) -> 'FaceGearSetParetoOptimiser':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'FaceGearSetParetoOptimiser.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def design_space_search_strategy(self) -> 'str':
        """str: 'DesignSpaceSearchStrategy' is the original name of this property."""

        temp = self.wrapped.DesignSpaceSearchStrategy.SelectedItemName

        if temp is None:
            return ''

        return temp

    @design_space_search_strategy.setter
    def design_space_search_strategy(self, value: 'str'):
        self.wrapped.DesignSpaceSearchStrategy.SetSelectedItem(str(value) if value else '')

    @property
    def design_space_search_strategy_duty_cycle(self) -> 'str':
        """str: 'DesignSpaceSearchStrategyDutyCycle' is the original name of this property."""

        temp = self.wrapped.DesignSpaceSearchStrategyDutyCycle.SelectedItemName

        if temp is None:
            return ''

        return temp

    @design_space_search_strategy_duty_cycle.setter
    def design_space_search_strategy_duty_cycle(self, value: 'str'):
        self.wrapped.DesignSpaceSearchStrategyDutyCycle.SetSelectedItem(str(value) if value else '')

    @property
    def selected_candidate_geometry(self) -> '_990.FaceGearSetDesign':
        """FaceGearSetDesign: 'SelectedCandidateGeometry' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SelectedCandidateGeometry

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def all_candidate_gear_sets(self) -> 'List[_990.FaceGearSetDesign]':
        """List[FaceGearSetDesign]: 'AllCandidateGearSets' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AllCandidateGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def candidate_gear_sets(self) -> 'List[_990.FaceGearSetDesign]':
        """List[FaceGearSetDesign]: 'CandidateGearSets' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CandidateGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'FaceGearSetParetoOptimiser._Cast_FaceGearSetParetoOptimiser':
        return self._Cast_FaceGearSetParetoOptimiser(self)
