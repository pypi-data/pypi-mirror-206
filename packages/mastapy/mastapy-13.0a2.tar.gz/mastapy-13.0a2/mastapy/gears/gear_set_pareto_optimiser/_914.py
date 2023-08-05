"""_914.py

MicroGeometryGearSetDesignSpaceSearch
"""
from mastapy._internal.python_net import python_net_import
from mastapy._internal import constructor
from mastapy.gears.gear_set_pareto_optimiser import _911
from mastapy._internal.cast_exception import CastException

_DATABASE_WITH_SELECTED_ITEM = python_net_import('SMT.MastaAPI.UtilityGUI.Databases', 'DatabaseWithSelectedItem')
_MICRO_GEOMETRY_GEAR_SET_DESIGN_SPACE_SEARCH = python_net_import('SMT.MastaAPI.Gears.GearSetParetoOptimiser', 'MicroGeometryGearSetDesignSpaceSearch')


__docformat__ = 'restructuredtext en'
__all__ = ('MicroGeometryGearSetDesignSpaceSearch',)


class MicroGeometryGearSetDesignSpaceSearch(_911.MicroGeometryDesignSpaceSearch):
    """MicroGeometryGearSetDesignSpaceSearch

    This is a mastapy class.
    """

    TYPE = _MICRO_GEOMETRY_GEAR_SET_DESIGN_SPACE_SEARCH

    class _Cast_MicroGeometryGearSetDesignSpaceSearch:
        """Special nested class for casting MicroGeometryGearSetDesignSpaceSearch to subclasses."""

        def __init__(self, parent: 'MicroGeometryGearSetDesignSpaceSearch'):
            self._parent = parent

        @property
        def micro_geometry_design_space_search(self):
            return self._parent._cast(_911.MicroGeometryDesignSpaceSearch)

        @property
        def design_space_search_base(self):
            from mastapy.gears.gear_set_pareto_optimiser import _901, _912
            from mastapy.gears.ltca.cylindrical import _855
            
            return self._parent._cast(_901.DesignSpaceSearchBase)

        @property
        def micro_geometry_gear_set_design_space_search(self) -> 'MicroGeometryGearSetDesignSpaceSearch':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'MicroGeometryGearSetDesignSpaceSearch.TYPE'):
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
    def cast_to(self) -> 'MicroGeometryGearSetDesignSpaceSearch._Cast_MicroGeometryGearSetDesignSpaceSearch':
        return self._Cast_MicroGeometryGearSetDesignSpaceSearch(self)
