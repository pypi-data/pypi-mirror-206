"""_2592.py

ActiveShaftDesignSelection
"""
from mastapy.system_model.part_model.configurations import _2597
from mastapy.system_model.part_model.shaft_model import _2462
from mastapy.shafts import _43
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ACTIVE_SHAFT_DESIGN_SELECTION = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Configurations', 'ActiveShaftDesignSelection')


__docformat__ = 'restructuredtext en'
__all__ = ('ActiveShaftDesignSelection',)


class ActiveShaftDesignSelection(_2597.PartDetailSelection['_2462.Shaft', '_43.SimpleShaftDefinition']):
    """ActiveShaftDesignSelection

    This is a mastapy class.
    """

    TYPE = _ACTIVE_SHAFT_DESIGN_SELECTION

    class _Cast_ActiveShaftDesignSelection:
        """Special nested class for casting ActiveShaftDesignSelection to subclasses."""

        def __init__(self, parent: 'ActiveShaftDesignSelection'):
            self._parent = parent

        @property
        def part_detail_selection(self):
            return self._parent._cast(_2597.PartDetailSelection)

        @property
        def active_shaft_design_selection(self) -> 'ActiveShaftDesignSelection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ActiveShaftDesignSelection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'ActiveShaftDesignSelection._Cast_ActiveShaftDesignSelection':
        return self._Cast_ActiveShaftDesignSelection(self)
