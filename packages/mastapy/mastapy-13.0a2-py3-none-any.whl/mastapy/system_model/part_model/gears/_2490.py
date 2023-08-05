"""_2490.py

ActiveGearSetDesignSelection
"""
from mastapy.system_model.part_model.configurations import _2597
from mastapy.system_model.part_model.gears import _2511
from mastapy.gears.gear_designs import _945
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ACTIVE_GEAR_SET_DESIGN_SELECTION = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'ActiveGearSetDesignSelection')


__docformat__ = 'restructuredtext en'
__all__ = ('ActiveGearSetDesignSelection',)


class ActiveGearSetDesignSelection(_2597.PartDetailSelection['_2511.GearSet', '_945.GearSetDesign']):
    """ActiveGearSetDesignSelection

    This is a mastapy class.
    """

    TYPE = _ACTIVE_GEAR_SET_DESIGN_SELECTION

    class _Cast_ActiveGearSetDesignSelection:
        """Special nested class for casting ActiveGearSetDesignSelection to subclasses."""

        def __init__(self, parent: 'ActiveGearSetDesignSelection'):
            self._parent = parent

        @property
        def part_detail_selection(self):
            return self._parent._cast(_2597.PartDetailSelection)

        @property
        def active_cylindrical_gear_set_design_selection(self):
            from mastapy.system_model.part_model.gears import _2489
            
            return self._parent._cast(_2489.ActiveCylindricalGearSetDesignSelection)

        @property
        def active_gear_set_design_selection(self) -> 'ActiveGearSetDesignSelection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ActiveGearSetDesignSelection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'ActiveGearSetDesignSelection._Cast_ActiveGearSetDesignSelection':
        return self._Cast_ActiveGearSetDesignSelection(self)
