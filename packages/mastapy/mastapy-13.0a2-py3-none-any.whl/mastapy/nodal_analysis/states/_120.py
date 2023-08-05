"""_120.py

ElementVectorState
"""
from mastapy.nodal_analysis.states import _121
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ELEMENT_VECTOR_STATE = python_net_import('SMT.MastaAPI.NodalAnalysis.States', 'ElementVectorState')


__docformat__ = 'restructuredtext en'
__all__ = ('ElementVectorState',)


class ElementVectorState(_121.EntityVectorState):
    """ElementVectorState

    This is a mastapy class.
    """

    TYPE = _ELEMENT_VECTOR_STATE

    class _Cast_ElementVectorState:
        """Special nested class for casting ElementVectorState to subclasses."""

        def __init__(self, parent: 'ElementVectorState'):
            self._parent = parent

        @property
        def entity_vector_state(self):
            return self._parent._cast(_121.EntityVectorState)

        @property
        def element_scalar_state(self):
            from mastapy.nodal_analysis.states import _119
            
            return self._parent._cast(_119.ElementScalarState)

        @property
        def element_vector_state(self) -> 'ElementVectorState':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ElementVectorState.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'ElementVectorState._Cast_ElementVectorState':
        return self._Cast_ElementVectorState(self)
