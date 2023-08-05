"""_143.py

NodalEntity
"""
from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_NODAL_ENTITY = python_net_import('SMT.MastaAPI.NodalAnalysis.NodalEntities', 'NodalEntity')


__docformat__ = 'restructuredtext en'
__all__ = ('NodalEntity',)


class NodalEntity(_0.APIBase):
    """NodalEntity

    This is a mastapy class.
    """

    TYPE = _NODAL_ENTITY

    class _Cast_NodalEntity:
        """Special nested class for casting NodalEntity to subclasses."""

        def __init__(self, parent: 'NodalEntity'):
            self._parent = parent

        @property
        def arbitrary_nodal_component(self):
            from mastapy.nodal_analysis.nodal_entities import _124
            
            return self._parent._cast(_124.ArbitraryNodalComponent)

        @property
        def bar(self):
            from mastapy.nodal_analysis.nodal_entities import _125
            
            return self._parent._cast(_125.Bar)

        @property
        def bar_elastic_mbd(self):
            from mastapy.nodal_analysis.nodal_entities import _126
            
            return self._parent._cast(_126.BarElasticMBD)

        @property
        def bar_mbd(self):
            from mastapy.nodal_analysis.nodal_entities import _127
            
            return self._parent._cast(_127.BarMBD)

        @property
        def bar_rigid_mbd(self):
            from mastapy.nodal_analysis.nodal_entities import _128
            
            return self._parent._cast(_128.BarRigidMBD)

        @property
        def bearing_axial_mounting_clearance(self):
            from mastapy.nodal_analysis.nodal_entities import _130
            
            return self._parent._cast(_130.BearingAxialMountingClearance)

        @property
        def cms_nodal_component(self):
            from mastapy.nodal_analysis.nodal_entities import _131
            
            return self._parent._cast(_131.CMSNodalComponent)

        @property
        def component_nodal_composite(self):
            from mastapy.nodal_analysis.nodal_entities import _132
            
            return self._parent._cast(_132.ComponentNodalComposite)

        @property
        def concentric_connection_nodal_component(self):
            from mastapy.nodal_analysis.nodal_entities import _133
            
            return self._parent._cast(_133.ConcentricConnectionNodalComponent)

        @property
        def distributed_rigid_bar_coupling(self):
            from mastapy.nodal_analysis.nodal_entities import _134
            
            return self._parent._cast(_134.DistributedRigidBarCoupling)

        @property
        def friction_nodal_component(self):
            from mastapy.nodal_analysis.nodal_entities import _135
            
            return self._parent._cast(_135.FrictionNodalComponent)

        @property
        def gear_mesh_nodal_component(self):
            from mastapy.nodal_analysis.nodal_entities import _136
            
            return self._parent._cast(_136.GearMeshNodalComponent)

        @property
        def gear_mesh_node_pair(self):
            from mastapy.nodal_analysis.nodal_entities import _137
            
            return self._parent._cast(_137.GearMeshNodePair)

        @property
        def gear_mesh_point_on_flank_contact(self):
            from mastapy.nodal_analysis.nodal_entities import _138
            
            return self._parent._cast(_138.GearMeshPointOnFlankContact)

        @property
        def gear_mesh_single_flank_contact(self):
            from mastapy.nodal_analysis.nodal_entities import _139
            
            return self._parent._cast(_139.GearMeshSingleFlankContact)

        @property
        def line_contact_stiffness_entity(self):
            from mastapy.nodal_analysis.nodal_entities import _140
            
            return self._parent._cast(_140.LineContactStiffnessEntity)

        @property
        def nodal_component(self):
            from mastapy.nodal_analysis.nodal_entities import _141
            
            return self._parent._cast(_141.NodalComponent)

        @property
        def nodal_composite(self):
            from mastapy.nodal_analysis.nodal_entities import _142
            
            return self._parent._cast(_142.NodalComposite)

        @property
        def pid_control_nodal_component(self):
            from mastapy.nodal_analysis.nodal_entities import _144
            
            return self._parent._cast(_144.PIDControlNodalComponent)

        @property
        def rigid_bar(self):
            from mastapy.nodal_analysis.nodal_entities import _145
            
            return self._parent._cast(_145.RigidBar)

        @property
        def simple_bar(self):
            from mastapy.nodal_analysis.nodal_entities import _146
            
            return self._parent._cast(_146.SimpleBar)

        @property
        def surface_to_surface_contact_stiffness_entity(self):
            from mastapy.nodal_analysis.nodal_entities import _147
            
            return self._parent._cast(_147.SurfaceToSurfaceContactStiffnessEntity)

        @property
        def torsional_friction_node_pair(self):
            from mastapy.nodal_analysis.nodal_entities import _148
            
            return self._parent._cast(_148.TorsionalFrictionNodePair)

        @property
        def torsional_friction_node_pair_simple_locked_stiffness(self):
            from mastapy.nodal_analysis.nodal_entities import _149
            
            return self._parent._cast(_149.TorsionalFrictionNodePairSimpleLockedStiffness)

        @property
        def two_body_connection_nodal_component(self):
            from mastapy.nodal_analysis.nodal_entities import _150
            
            return self._parent._cast(_150.TwoBodyConnectionNodalComponent)

        @property
        def shaft_section_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2782
            
            return self._parent._cast(_2782.ShaftSectionSystemDeflection)

        @property
        def nodal_entity(self) -> 'NodalEntity':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'NodalEntity.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def name(self) -> 'str':
        """str: 'Name' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Name

        if temp is None:
            return ''

        return temp

    @property
    def cast_to(self) -> 'NodalEntity._Cast_NodalEntity':
        return self._Cast_NodalEntity(self)
