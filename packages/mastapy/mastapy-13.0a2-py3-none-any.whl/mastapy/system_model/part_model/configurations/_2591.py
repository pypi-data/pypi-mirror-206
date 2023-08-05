"""_2591.py

ActiveFESubstructureSelectionGroup
"""
from mastapy.system_model.part_model.configurations import _2596, _2590
from mastapy.system_model.part_model import _2433
from mastapy.system_model.fe import _2363
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ACTIVE_FE_SUBSTRUCTURE_SELECTION_GROUP = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Configurations', 'ActiveFESubstructureSelectionGroup')


__docformat__ = 'restructuredtext en'
__all__ = ('ActiveFESubstructureSelectionGroup',)


class ActiveFESubstructureSelectionGroup(_2596.PartDetailConfiguration['_2590.ActiveFESubstructureSelection', '_2433.FEPart', '_2363.FESubstructure']):
    """ActiveFESubstructureSelectionGroup

    This is a mastapy class.
    """

    TYPE = _ACTIVE_FE_SUBSTRUCTURE_SELECTION_GROUP

    class _Cast_ActiveFESubstructureSelectionGroup:
        """Special nested class for casting ActiveFESubstructureSelectionGroup to subclasses."""

        def __init__(self, parent: 'ActiveFESubstructureSelectionGroup'):
            self._parent = parent

        @property
        def part_detail_configuration(self):
            return self._parent._cast(_2596.PartDetailConfiguration)

        @property
        def active_fe_substructure_selection_group(self) -> 'ActiveFESubstructureSelectionGroup':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ActiveFESubstructureSelectionGroup.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'ActiveFESubstructureSelectionGroup._Cast_ActiveFESubstructureSelectionGroup':
        return self._Cast_ActiveFESubstructureSelectionGroup(self)
