"""_146.py

SimpleBar
"""
from mastapy.nodal_analysis.nodal_entities import _150
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SIMPLE_BAR = python_net_import('SMT.MastaAPI.NodalAnalysis.NodalEntities', 'SimpleBar')


__docformat__ = 'restructuredtext en'
__all__ = ('SimpleBar',)


class SimpleBar(_150.TwoBodyConnectionNodalComponent):
    """SimpleBar

    This is a mastapy class.
    """

    TYPE = _SIMPLE_BAR

    class _Cast_SimpleBar:
        """Special nested class for casting SimpleBar to subclasses."""

        def __init__(self, parent: 'SimpleBar'):
            self._parent = parent

        @property
        def two_body_connection_nodal_component(self):
            return self._parent._cast(_150.TwoBodyConnectionNodalComponent)

        @property
        def component_nodal_composite(self):
            from mastapy.nodal_analysis.nodal_entities import _132
            
            return self._parent._cast(_132.ComponentNodalComposite)

        @property
        def nodal_composite(self):
            from mastapy.nodal_analysis.nodal_entities import _142
            
            return self._parent._cast(_142.NodalComposite)

        @property
        def nodal_entity(self):
            from mastapy.nodal_analysis.nodal_entities import _143
            
            return self._parent._cast(_143.NodalEntity)

        @property
        def simple_bar(self) -> 'SimpleBar':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'SimpleBar.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'SimpleBar._Cast_SimpleBar':
        return self._Cast_SimpleBar(self)
