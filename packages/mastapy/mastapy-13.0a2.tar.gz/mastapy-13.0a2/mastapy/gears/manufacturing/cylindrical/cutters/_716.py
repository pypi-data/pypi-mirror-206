"""_716.py

MutatableFillet
"""
from mastapy._internal import constructor
from mastapy.gears.manufacturing.cylindrical.cutters import _714
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MUTATABLE_FILLET = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Cylindrical.Cutters', 'MutatableFillet')


__docformat__ = 'restructuredtext en'
__all__ = ('MutatableFillet',)


class MutatableFillet(_714.MutatableCommon):
    """MutatableFillet

    This is a mastapy class.
    """

    TYPE = _MUTATABLE_FILLET

    class _Cast_MutatableFillet:
        """Special nested class for casting MutatableFillet to subclasses."""

        def __init__(self, parent: 'MutatableFillet'):
            self._parent = parent

        @property
        def mutatable_common(self):
            return self._parent._cast(_714.MutatableCommon)

        @property
        def curve_in_linked_list(self):
            from mastapy.gears.manufacturing.cylindrical.cutters import _698
            
            return self._parent._cast(_698.CurveInLinkedList)

        @property
        def mutatable_fillet(self) -> 'MutatableFillet':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'MutatableFillet.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def radius(self) -> 'float':
        """float: 'Radius' is the original name of this property."""

        temp = self.wrapped.Radius

        if temp is None:
            return 0.0

        return temp

    @radius.setter
    def radius(self, value: 'float'):
        self.wrapped.Radius = float(value) if value else 0.0

    @property
    def cast_to(self) -> 'MutatableFillet._Cast_MutatableFillet':
        return self._Cast_MutatableFillet(self)
