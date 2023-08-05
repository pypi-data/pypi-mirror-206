"""_140.py

LineContactStiffnessEntity
"""
from mastapy.nodal_analysis import _78
from mastapy._internal import constructor
from mastapy.nodal_analysis.nodal_entities import _124
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LINE_CONTACT_STIFFNESS_ENTITY = python_net_import('SMT.MastaAPI.NodalAnalysis.NodalEntities', 'LineContactStiffnessEntity')


__docformat__ = 'restructuredtext en'
__all__ = ('LineContactStiffnessEntity',)


class LineContactStiffnessEntity(_124.ArbitraryNodalComponent):
    """LineContactStiffnessEntity

    This is a mastapy class.
    """

    TYPE = _LINE_CONTACT_STIFFNESS_ENTITY

    class _Cast_LineContactStiffnessEntity:
        """Special nested class for casting LineContactStiffnessEntity to subclasses."""

        def __init__(self, parent: 'LineContactStiffnessEntity'):
            self._parent = parent

        @property
        def arbitrary_nodal_component(self):
            return self._parent._cast(_124.ArbitraryNodalComponent)

        @property
        def nodal_component(self):
            from mastapy.nodal_analysis.nodal_entities import _141
            
            return self._parent._cast(_141.NodalComponent)

        @property
        def nodal_entity(self):
            from mastapy.nodal_analysis.nodal_entities import _143
            
            return self._parent._cast(_143.NodalEntity)

        @property
        def line_contact_stiffness_entity(self) -> 'LineContactStiffnessEntity':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'LineContactStiffnessEntity.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def stiffness_in_local_coordinate_system(self) -> '_78.NodalMatrix':
        """NodalMatrix: 'StiffnessInLocalCoordinateSystem' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StiffnessInLocalCoordinateSystem

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'LineContactStiffnessEntity._Cast_LineContactStiffnessEntity':
        return self._Cast_LineContactStiffnessEntity(self)
