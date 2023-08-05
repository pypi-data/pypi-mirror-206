"""_2593.py

ActiveShaftDesignSelectionGroup
"""
from mastapy.system_model.part_model.configurations import _2596, _2592
from mastapy.system_model.part_model.shaft_model import _2462
from mastapy.shafts import _43
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ACTIVE_SHAFT_DESIGN_SELECTION_GROUP = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Configurations', 'ActiveShaftDesignSelectionGroup')


__docformat__ = 'restructuredtext en'
__all__ = ('ActiveShaftDesignSelectionGroup',)


class ActiveShaftDesignSelectionGroup(_2596.PartDetailConfiguration['_2592.ActiveShaftDesignSelection', '_2462.Shaft', '_43.SimpleShaftDefinition']):
    """ActiveShaftDesignSelectionGroup

    This is a mastapy class.
    """

    TYPE = _ACTIVE_SHAFT_DESIGN_SELECTION_GROUP

    class _Cast_ActiveShaftDesignSelectionGroup:
        """Special nested class for casting ActiveShaftDesignSelectionGroup to subclasses."""

        def __init__(self, parent: 'ActiveShaftDesignSelectionGroup'):
            self._parent = parent

        @property
        def part_detail_configuration(self):
            return self._parent._cast(_2596.PartDetailConfiguration)

        @property
        def active_shaft_design_selection_group(self) -> 'ActiveShaftDesignSelectionGroup':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ActiveShaftDesignSelectionGroup.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'ActiveShaftDesignSelectionGroup._Cast_ActiveShaftDesignSelectionGroup':
        return self._Cast_ActiveShaftDesignSelectionGroup(self)
