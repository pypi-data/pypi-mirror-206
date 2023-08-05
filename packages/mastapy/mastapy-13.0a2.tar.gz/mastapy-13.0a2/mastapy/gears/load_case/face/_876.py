"""_876.py

FaceMeshLoadCase
"""
from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy.gears import _320
from mastapy.gears.load_case import _870
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FACE_MESH_LOAD_CASE = python_net_import('SMT.MastaAPI.Gears.LoadCase.Face', 'FaceMeshLoadCase')


__docformat__ = 'restructuredtext en'
__all__ = ('FaceMeshLoadCase',)


class FaceMeshLoadCase(_870.MeshLoadCase):
    """FaceMeshLoadCase

    This is a mastapy class.
    """

    TYPE = _FACE_MESH_LOAD_CASE

    class _Cast_FaceMeshLoadCase:
        """Special nested class for casting FaceMeshLoadCase to subclasses."""

        def __init__(self, parent: 'FaceMeshLoadCase'):
            self._parent = parent

        @property
        def mesh_load_case(self):
            return self._parent._cast(_870.MeshLoadCase)

        @property
        def gear_mesh_design_analysis(self):
            from mastapy.gears.analysis import _1216
            
            return self._parent._cast(_1216.GearMeshDesignAnalysis)

        @property
        def abstract_gear_mesh_analysis(self):
            from mastapy.gears.analysis import _1210
            
            return self._parent._cast(_1210.AbstractGearMeshAnalysis)

        @property
        def face_mesh_load_case(self) -> 'FaceMeshLoadCase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'FaceMeshLoadCase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def equivalent_misalignment_due_to_system_deflection(self) -> 'float':
        """float: 'EquivalentMisalignmentDueToSystemDeflection' is the original name of this property."""

        temp = self.wrapped.EquivalentMisalignmentDueToSystemDeflection

        if temp is None:
            return 0.0

        return temp

    @equivalent_misalignment_due_to_system_deflection.setter
    def equivalent_misalignment_due_to_system_deflection(self, value: 'float'):
        self.wrapped.EquivalentMisalignmentDueToSystemDeflection = float(value) if value else 0.0

    @property
    def misalignment_source(self) -> '_320.CylindricalMisalignmentDataSource':
        """CylindricalMisalignmentDataSource: 'MisalignmentSource' is the original name of this property."""

        temp = self.wrapped.MisalignmentSource

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, _320.CylindricalMisalignmentDataSource)
        return constructor.new_from_mastapy_type(_320.CylindricalMisalignmentDataSource)(value) if value is not None else None

    @misalignment_source.setter
    def misalignment_source(self, value: '_320.CylindricalMisalignmentDataSource'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value, _320.CylindricalMisalignmentDataSource.type_())
        self.wrapped.MisalignmentSource = value

    @property
    def cast_to(self) -> 'FaceMeshLoadCase._Cast_FaceMeshLoadCase':
        return self._Cast_FaceMeshLoadCase(self)
