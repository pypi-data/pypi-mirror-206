"""_1092.py

CylindricalGearMeshMicroGeometry
"""
from typing import List

from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy.utility_gui.charts import _1852
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.gears.gear_designs.cylindrical import _1021, _1013
from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1101, _1095, _1098
from mastapy.gears.analysis import _1219
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_MESH_MICRO_GEOMETRY = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Cylindrical.MicroGeometry', 'CylindricalGearMeshMicroGeometry')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearMeshMicroGeometry',)


class CylindricalGearMeshMicroGeometry(_1219.GearMeshImplementationDetail):
    """CylindricalGearMeshMicroGeometry

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_MESH_MICRO_GEOMETRY

    class _Cast_CylindricalGearMeshMicroGeometry:
        """Special nested class for casting CylindricalGearMeshMicroGeometry to subclasses."""

        def __init__(self, parent: 'CylindricalGearMeshMicroGeometry'):
            self._parent = parent

        @property
        def gear_mesh_implementation_detail(self):
            return self._parent._cast(_1219.GearMeshImplementationDetail)

        @property
        def gear_mesh_design_analysis(self):
            from mastapy.gears.analysis import _1216
            
            return self._parent._cast(_1216.GearMeshDesignAnalysis)

        @property
        def abstract_gear_mesh_analysis(self):
            from mastapy.gears.analysis import _1210
            
            return self._parent._cast(_1210.AbstractGearMeshAnalysis)

        @property
        def cylindrical_gear_mesh_micro_geometry(self) -> 'CylindricalGearMeshMicroGeometry':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CylindricalGearMeshMicroGeometry.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def has_gears_specifying_micro_geometry_per_tooth(self) -> 'bool':
        """bool: 'HasGearsSpecifyingMicroGeometryPerTooth' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HasGearsSpecifyingMicroGeometryPerTooth

        if temp is None:
            return False

        return temp

    @property
    def left_flank_lead_modification_chart(self) -> '_1852.TwoDChartDefinition':
        """TwoDChartDefinition: 'LeftFlankLeadModificationChart' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LeftFlankLeadModificationChart

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def left_flank_profile_modification_chart(self) -> '_1852.TwoDChartDefinition':
        """TwoDChartDefinition: 'LeftFlankProfileModificationChart' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LeftFlankProfileModificationChart

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def number_of_tooth_passes_for_ltca(self) -> 'overridable.Overridable_int':
        """overridable.Overridable_int: 'NumberOfToothPassesForLTCA' is the original name of this property."""

        temp = self.wrapped.NumberOfToothPassesForLTCA

        if temp is None:
            return 0

        return constructor.new_from_mastapy_type(overridable.Overridable_int)(temp) if temp is not None else 0

    @number_of_tooth_passes_for_ltca.setter
    def number_of_tooth_passes_for_ltca(self, value: 'overridable.Overridable_int.implicit_type()'):
        wrapper_type = overridable.Overridable_int.wrapper_type()
        enclosed_type = overridable.Overridable_int.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0, is_overridden)
        self.wrapped.NumberOfToothPassesForLTCA = value

    @property
    def profile_measured_as(self) -> '_1021.CylindricalGearProfileMeasurementType':
        """CylindricalGearProfileMeasurementType: 'ProfileMeasuredAs' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ProfileMeasuredAs

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, _1021.CylindricalGearProfileMeasurementType)
        return constructor.new_from_mastapy_type(_1021.CylindricalGearProfileMeasurementType)(value) if value is not None else None

    @property
    def right_flank_lead_modification_chart(self) -> '_1852.TwoDChartDefinition':
        """TwoDChartDefinition: 'RightFlankLeadModificationChart' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RightFlankLeadModificationChart

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def right_flank_profile_modification_chart(self) -> '_1852.TwoDChartDefinition':
        """TwoDChartDefinition: 'RightFlankProfileModificationChart' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RightFlankProfileModificationChart

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cylindrical_gear_set_micro_geometry(self) -> '_1101.CylindricalGearSetMicroGeometry':
        """CylindricalGearSetMicroGeometry: 'CylindricalGearSetMicroGeometry' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalGearSetMicroGeometry

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cylindrical_mesh(self) -> '_1013.CylindricalGearMeshDesign':
        """CylindricalGearMeshDesign: 'CylindricalMesh' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalMesh

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cylindrical_gear_micro_geometries(self) -> 'List[_1095.CylindricalGearMicroGeometryBase]':
        """List[CylindricalGearMicroGeometryBase]: 'CylindricalGearMicroGeometries' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalGearMicroGeometries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cylindrical_gear_micro_geometries_specified_per_tooth(self) -> 'List[_1098.CylindricalGearMicroGeometryPerTooth]':
        """List[CylindricalGearMicroGeometryPerTooth]: 'CylindricalGearMicroGeometriesSpecifiedPerTooth' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalGearMicroGeometriesSpecifiedPerTooth

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def gear_a(self) -> '_1095.CylindricalGearMicroGeometryBase':
        """CylindricalGearMicroGeometryBase: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b(self) -> '_1095.CylindricalGearMicroGeometryBase':
        """CylindricalGearMicroGeometryBase: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'CylindricalGearMeshMicroGeometry._Cast_CylindricalGearMeshMicroGeometry':
        return self._Cast_CylindricalGearMeshMicroGeometry(self)
