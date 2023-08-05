"""_2584.py

SynchroniserPart
"""
from mastapy.system_model.part_model.couplings import _2563
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_PART = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Couplings', 'SynchroniserPart')


__docformat__ = 'restructuredtext en'
__all__ = ('SynchroniserPart',)


class SynchroniserPart(_2563.CouplingHalf):
    """SynchroniserPart

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_PART

    class _Cast_SynchroniserPart:
        """Special nested class for casting SynchroniserPart to subclasses."""

        def __init__(self, parent: 'SynchroniserPart'):
            self._parent = parent

        @property
        def coupling_half(self):
            return self._parent._cast(_2563.CouplingHalf)

        @property
        def mountable_component(self):
            from mastapy.system_model.part_model import _2444
            
            return self._parent._cast(_2444.MountableComponent)

        @property
        def component(self):
            from mastapy.system_model.part_model import _2424
            
            return self._parent._cast(_2424.Component)

        @property
        def part(self):
            from mastapy.system_model.part_model import _2448
            
            return self._parent._cast(_2448.Part)

        @property
        def design_entity(self):
            from mastapy.system_model import _2188
            
            return self._parent._cast(_2188.DesignEntity)

        @property
        def synchroniser_half(self):
            from mastapy.system_model.part_model.couplings import _2583
            
            return self._parent._cast(_2583.SynchroniserHalf)

        @property
        def synchroniser_sleeve(self):
            from mastapy.system_model.part_model.couplings import _2585
            
            return self._parent._cast(_2585.SynchroniserSleeve)

        @property
        def synchroniser_part(self) -> 'SynchroniserPart':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'SynchroniserPart.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'SynchroniserPart._Cast_SynchroniserPart':
        return self._Cast_SynchroniserPart(self)
