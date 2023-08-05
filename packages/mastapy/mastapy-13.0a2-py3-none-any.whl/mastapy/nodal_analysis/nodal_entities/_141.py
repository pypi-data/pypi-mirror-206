"""_141.py

NodalComponent
"""
from mastapy.nodal_analysis.nodal_entities import _143
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_NODAL_COMPONENT = python_net_import('SMT.MastaAPI.NodalAnalysis.NodalEntities', 'NodalComponent')


__docformat__ = 'restructuredtext en'
__all__ = ('NodalComponent',)


class NodalComponent(_143.NodalEntity):
    """NodalComponent

    This is a mastapy class.
    """

    TYPE = _NODAL_COMPONENT

    class _Cast_NodalComponent:
        """Special nested class for casting NodalComponent to subclasses."""

        def __init__(self, parent: 'NodalComponent'):
            self._parent = parent

        @property
        def nodal_entity(self):
            return self._parent._cast(_143.NodalEntity)

        @property
        def arbitrary_nodal_component(self):
            from mastapy.nodal_analysis.nodal_entities import _124
            
            return self._parent._cast(_124.ArbitraryNodalComponent)

        @property
        def bar(self):
            from mastapy.nodal_analysis.nodal_entities import _125
            
            return self._parent._cast(_125.Bar)

        @property
        def bearing_axial_mounting_clearance(self):
            from mastapy.nodal_analysis.nodal_entities import _130
            
            return self._parent._cast(_130.BearingAxialMountingClearance)

        @property
        def cms_nodal_component(self):
            from mastapy.nodal_analysis.nodal_entities import _131
            
            return self._parent._cast(_131.CMSNodalComponent)

        @property
        def distributed_rigid_bar_coupling(self):
            from mastapy.nodal_analysis.nodal_entities import _134
            
            return self._parent._cast(_134.DistributedRigidBarCoupling)

        @property
        def friction_nodal_component(self):
            from mastapy.nodal_analysis.nodal_entities import _135
            
            return self._parent._cast(_135.FrictionNodalComponent)

        @property
        def gear_mesh_node_pair(self):
            from mastapy.nodal_analysis.nodal_entities import _137
            
            return self._parent._cast(_137.GearMeshNodePair)

        @property
        def line_contact_stiffness_entity(self):
            from mastapy.nodal_analysis.nodal_entities import _140
            
            return self._parent._cast(_140.LineContactStiffnessEntity)

        @property
        def pid_control_nodal_component(self):
            from mastapy.nodal_analysis.nodal_entities import _144
            
            return self._parent._cast(_144.PIDControlNodalComponent)

        @property
        def rigid_bar(self):
            from mastapy.nodal_analysis.nodal_entities import _145
            
            return self._parent._cast(_145.RigidBar)

        @property
        def surface_to_surface_contact_stiffness_entity(self):
            from mastapy.nodal_analysis.nodal_entities import _147
            
            return self._parent._cast(_147.SurfaceToSurfaceContactStiffnessEntity)

        @property
        def shaft_section_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2782
            
            return self._parent._cast(_2782.ShaftSectionSystemDeflection)

        @property
        def nodal_component(self) -> 'NodalComponent':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'NodalComponent.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'NodalComponent._Cast_NodalComponent':
        return self._Cast_NodalComponent(self)
