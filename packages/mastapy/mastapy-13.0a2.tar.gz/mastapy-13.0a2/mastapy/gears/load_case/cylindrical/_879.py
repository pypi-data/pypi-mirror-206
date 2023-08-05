"""_879.py

CylindricalMeshLoadCase
"""
from mastapy.gears import _319, _320
from mastapy._internal import enum_with_selected_value_runtime, constructor, conversion
from mastapy.gears.gear_designs.cylindrical import _1053
from mastapy.gears.load_case import _870
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_MESH_LOAD_CASE = python_net_import('SMT.MastaAPI.Gears.LoadCase.Cylindrical', 'CylindricalMeshLoadCase')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalMeshLoadCase',)


class CylindricalMeshLoadCase(_870.MeshLoadCase):
    """CylindricalMeshLoadCase

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_MESH_LOAD_CASE

    class _Cast_CylindricalMeshLoadCase:
        """Special nested class for casting CylindricalMeshLoadCase to subclasses."""

        def __init__(self, parent: 'CylindricalMeshLoadCase'):
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
        def cylindrical_mesh_load_case(self) -> 'CylindricalMeshLoadCase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CylindricalMeshLoadCase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def active_flank(self) -> '_319.CylindricalFlanks':
        """CylindricalFlanks: 'ActiveFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ActiveFlank

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, _319.CylindricalFlanks)
        return constructor.new_from_mastapy_type(_319.CylindricalFlanks)(value) if value is not None else None

    @property
    def equivalent_misalignment(self) -> 'float':
        """float: 'EquivalentMisalignment' is the original name of this property."""

        temp = self.wrapped.EquivalentMisalignment

        if temp is None:
            return 0.0

        return temp

    @equivalent_misalignment.setter
    def equivalent_misalignment(self, value: 'float'):
        self.wrapped.EquivalentMisalignment = float(value) if value else 0.0

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
    def misalignment_due_to_micro_geometry_lead_relief(self) -> 'float':
        """float: 'MisalignmentDueToMicroGeometryLeadRelief' is the original name of this property."""

        temp = self.wrapped.MisalignmentDueToMicroGeometryLeadRelief

        if temp is None:
            return 0.0

        return temp

    @misalignment_due_to_micro_geometry_lead_relief.setter
    def misalignment_due_to_micro_geometry_lead_relief(self, value: 'float'):
        self.wrapped.MisalignmentDueToMicroGeometryLeadRelief = float(value) if value else 0.0

    @property
    def pitch_line_velocity_at_operating_pitch_diameter(self) -> 'float':
        """float: 'PitchLineVelocityAtOperatingPitchDiameter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PitchLineVelocityAtOperatingPitchDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def load_case_modifiable_settings(self) -> '_1053.LTCALoadCaseModifiableSettings':
        """LTCALoadCaseModifiableSettings: 'LoadCaseModifiableSettings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LoadCaseModifiableSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'CylindricalMeshLoadCase._Cast_CylindricalMeshLoadCase':
        return self._Cast_CylindricalMeshLoadCase(self)
