"""_124.py

ArbitraryNodalComponent
"""
from mastapy.nodal_analysis.nodal_entities import _141
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ARBITRARY_NODAL_COMPONENT = python_net_import('SMT.MastaAPI.NodalAnalysis.NodalEntities', 'ArbitraryNodalComponent')


__docformat__ = 'restructuredtext en'
__all__ = ('ArbitraryNodalComponent',)


class ArbitraryNodalComponent(_141.NodalComponent):
    """ArbitraryNodalComponent

    This is a mastapy class.
    """

    TYPE = _ARBITRARY_NODAL_COMPONENT

    class _Cast_ArbitraryNodalComponent:
        """Special nested class for casting ArbitraryNodalComponent to subclasses."""

        def __init__(self, parent: 'ArbitraryNodalComponent'):
            self._parent = parent

        @property
        def nodal_component(self):
            return self._parent._cast(_141.NodalComponent)

        @property
        def nodal_entity(self):
            from mastapy.nodal_analysis.nodal_entities import _143
            
            return self._parent._cast(_143.NodalEntity)

        @property
        def bearing_axial_mounting_clearance(self):
            from mastapy.nodal_analysis.nodal_entities import _130
            
            return self._parent._cast(_130.BearingAxialMountingClearance)

        @property
        def cms_nodal_component(self):
            from mastapy.nodal_analysis.nodal_entities import _131
            
            return self._parent._cast(_131.CMSNodalComponent)

        @property
        def gear_mesh_node_pair(self):
            from mastapy.nodal_analysis.nodal_entities import _137
            
            return self._parent._cast(_137.GearMeshNodePair)

        @property
        def line_contact_stiffness_entity(self):
            from mastapy.nodal_analysis.nodal_entities import _140
            
            return self._parent._cast(_140.LineContactStiffnessEntity)

        @property
        def surface_to_surface_contact_stiffness_entity(self):
            from mastapy.nodal_analysis.nodal_entities import _147
            
            return self._parent._cast(_147.SurfaceToSurfaceContactStiffnessEntity)

        @property
        def arbitrary_nodal_component(self) -> 'ArbitraryNodalComponent':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ArbitraryNodalComponent.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'ArbitraryNodalComponent._Cast_ArbitraryNodalComponent':
        return self._Cast_ArbitraryNodalComponent(self)
