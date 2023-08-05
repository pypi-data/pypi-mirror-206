"""_946.py

SelectedDesignConstraintsCollection
"""
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SELECTED_DESIGN_CONSTRAINTS_COLLECTION = python_net_import('SMT.MastaAPI.Gears.GearDesigns', 'SelectedDesignConstraintsCollection')


__docformat__ = 'restructuredtext en'
__all__ = ('SelectedDesignConstraintsCollection',)


class SelectedDesignConstraintsCollection(_0.APIBase):
    """SelectedDesignConstraintsCollection

    This is a mastapy class.
    """

    TYPE = _SELECTED_DESIGN_CONSTRAINTS_COLLECTION

    class _Cast_SelectedDesignConstraintsCollection:
        """Special nested class for casting SelectedDesignConstraintsCollection to subclasses."""

        def __init__(self, parent: 'SelectedDesignConstraintsCollection'):
            self._parent = parent

        @property
        def selected_design_constraints_collection(self) -> 'SelectedDesignConstraintsCollection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'SelectedDesignConstraintsCollection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'SelectedDesignConstraintsCollection._Cast_SelectedDesignConstraintsCollection':
        return self._Cast_SelectedDesignConstraintsCollection(self)
