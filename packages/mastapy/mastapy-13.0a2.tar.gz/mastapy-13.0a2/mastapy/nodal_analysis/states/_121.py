"""_121.py

EntityVectorState
"""
from mastapy._internal import constructor
from mastapy.math_utility import _1514
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ENTITY_VECTOR_STATE = python_net_import('SMT.MastaAPI.NodalAnalysis.States', 'EntityVectorState')


__docformat__ = 'restructuredtext en'
__all__ = ('EntityVectorState',)


class EntityVectorState(_0.APIBase):
    """EntityVectorState

    This is a mastapy class.
    """

    TYPE = _ENTITY_VECTOR_STATE

    class _Cast_EntityVectorState:
        """Special nested class for casting EntityVectorState to subclasses."""

        def __init__(self, parent: 'EntityVectorState'):
            self._parent = parent

        @property
        def element_scalar_state(self):
            from mastapy.nodal_analysis.states import _119
            
            return self._parent._cast(_119.ElementScalarState)

        @property
        def element_vector_state(self):
            from mastapy.nodal_analysis.states import _120
            
            return self._parent._cast(_120.ElementVectorState)

        @property
        def node_scalar_state(self):
            from mastapy.nodal_analysis.states import _122
            
            return self._parent._cast(_122.NodeScalarState)

        @property
        def node_vector_state(self):
            from mastapy.nodal_analysis.states import _123
            
            return self._parent._cast(_123.NodeVectorState)

        @property
        def entity_vector_state(self) -> 'EntityVectorState':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'EntityVectorState.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def degrees_of_freedom_per_entity(self) -> 'int':
        """int: 'DegreesOfFreedomPerEntity' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DegreesOfFreedomPerEntity

        if temp is None:
            return 0

        return temp

    @property
    def number_of_entities(self) -> 'int':
        """int: 'NumberOfEntities' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NumberOfEntities

        if temp is None:
            return 0

        return temp

    @property
    def vector(self) -> '_1514.RealVector':
        """RealVector: 'Vector' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Vector

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'EntityVectorState._Cast_EntityVectorState':
        return self._Cast_EntityVectorState(self)
