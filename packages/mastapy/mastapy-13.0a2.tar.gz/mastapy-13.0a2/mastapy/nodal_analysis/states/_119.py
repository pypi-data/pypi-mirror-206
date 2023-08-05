"""_119.py

ElementScalarState
"""
from mastapy.nodal_analysis.states import _120
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ELEMENT_SCALAR_STATE = python_net_import('SMT.MastaAPI.NodalAnalysis.States', 'ElementScalarState')


__docformat__ = 'restructuredtext en'
__all__ = ('ElementScalarState',)


class ElementScalarState(_120.ElementVectorState):
    """ElementScalarState

    This is a mastapy class.
    """

    TYPE = _ELEMENT_SCALAR_STATE

    class _Cast_ElementScalarState:
        """Special nested class for casting ElementScalarState to subclasses."""

        def __init__(self, parent: 'ElementScalarState'):
            self._parent = parent

        @property
        def element_vector_state(self):
            return self._parent._cast(_120.ElementVectorState)

        @property
        def entity_vector_state(self):
            from mastapy.nodal_analysis.states import _121
            
            return self._parent._cast(_121.EntityVectorState)

        @property
        def element_scalar_state(self) -> 'ElementScalarState':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ElementScalarState.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'ElementScalarState._Cast_ElementScalarState':
        return self._Cast_ElementScalarState(self)
