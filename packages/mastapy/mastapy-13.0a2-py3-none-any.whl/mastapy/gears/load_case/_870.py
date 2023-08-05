"""_870.py

MeshLoadCase
"""
from mastapy._internal import constructor
from mastapy.gears.analysis import _1216
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MESH_LOAD_CASE = python_net_import('SMT.MastaAPI.Gears.LoadCase', 'MeshLoadCase')


__docformat__ = 'restructuredtext en'
__all__ = ('MeshLoadCase',)


class MeshLoadCase(_1216.GearMeshDesignAnalysis):
    """MeshLoadCase

    This is a mastapy class.
    """

    TYPE = _MESH_LOAD_CASE

    class _Cast_MeshLoadCase:
        """Special nested class for casting MeshLoadCase to subclasses."""

        def __init__(self, parent: 'MeshLoadCase'):
            self._parent = parent

        @property
        def gear_mesh_design_analysis(self):
            return self._parent._cast(_1216.GearMeshDesignAnalysis)

        @property
        def abstract_gear_mesh_analysis(self):
            from mastapy.gears.analysis import _1210
            
            return self._parent._cast(_1210.AbstractGearMeshAnalysis)

        @property
        def worm_mesh_load_case(self):
            from mastapy.gears.load_case.worm import _873
            
            return self._parent._cast(_873.WormMeshLoadCase)

        @property
        def face_mesh_load_case(self):
            from mastapy.gears.load_case.face import _876
            
            return self._parent._cast(_876.FaceMeshLoadCase)

        @property
        def cylindrical_mesh_load_case(self):
            from mastapy.gears.load_case.cylindrical import _879
            
            return self._parent._cast(_879.CylindricalMeshLoadCase)

        @property
        def conical_mesh_load_case(self):
            from mastapy.gears.load_case.conical import _882
            
            return self._parent._cast(_882.ConicalMeshLoadCase)

        @property
        def concept_mesh_load_case(self):
            from mastapy.gears.load_case.concept import _885
            
            return self._parent._cast(_885.ConceptMeshLoadCase)

        @property
        def bevel_mesh_load_case(self):
            from mastapy.gears.load_case.bevel import _887
            
            return self._parent._cast(_887.BevelMeshLoadCase)

        @property
        def mesh_load_case(self) -> 'MeshLoadCase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'MeshLoadCase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def gear_a_torque(self) -> 'float':
        """float: 'GearATorque' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearATorque

        if temp is None:
            return 0.0

        return temp

    @property
    def gear_b_torque(self) -> 'float':
        """float: 'GearBTorque' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearBTorque

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self) -> 'MeshLoadCase._Cast_MeshLoadCase':
        return self._Cast_MeshLoadCase(self)
