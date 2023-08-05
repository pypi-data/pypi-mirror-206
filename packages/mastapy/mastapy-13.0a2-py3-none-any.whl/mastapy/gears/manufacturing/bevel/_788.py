"""_788.py

ConicalSetMicroGeometryConfigBase
"""
from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy.gears import _321
from mastapy.gears.analysis import _1225
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_SET_MICRO_GEOMETRY_CONFIG_BASE = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Bevel', 'ConicalSetMicroGeometryConfigBase')


__docformat__ = 'restructuredtext en'
__all__ = ('ConicalSetMicroGeometryConfigBase',)


class ConicalSetMicroGeometryConfigBase(_1225.GearSetImplementationDetail):
    """ConicalSetMicroGeometryConfigBase

    This is a mastapy class.
    """

    TYPE = _CONICAL_SET_MICRO_GEOMETRY_CONFIG_BASE

    class _Cast_ConicalSetMicroGeometryConfigBase:
        """Special nested class for casting ConicalSetMicroGeometryConfigBase to subclasses."""

        def __init__(self, parent: 'ConicalSetMicroGeometryConfigBase'):
            self._parent = parent

        @property
        def gear_set_implementation_detail(self):
            return self._parent._cast(_1225.GearSetImplementationDetail)

        @property
        def gear_set_design_analysis(self):
            from mastapy.gears.analysis import _1220
            
            return self._parent._cast(_1220.GearSetDesignAnalysis)

        @property
        def abstract_gear_set_analysis(self):
            from mastapy.gears.analysis import _1211
            
            return self._parent._cast(_1211.AbstractGearSetAnalysis)

        @property
        def conical_set_manufacturing_config(self):
            from mastapy.gears.manufacturing.bevel import _786
            
            return self._parent._cast(_786.ConicalSetManufacturingConfig)

        @property
        def conical_set_micro_geometry_config(self):
            from mastapy.gears.manufacturing.bevel import _787
            
            return self._parent._cast(_787.ConicalSetMicroGeometryConfig)

        @property
        def conical_set_micro_geometry_config_base(self) -> 'ConicalSetMicroGeometryConfigBase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConicalSetMicroGeometryConfigBase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def compound_layer_thickness(self) -> 'float':
        """float: 'CompoundLayerThickness' is the original name of this property."""

        temp = self.wrapped.CompoundLayerThickness

        if temp is None:
            return 0.0

        return temp

    @compound_layer_thickness.setter
    def compound_layer_thickness(self, value: 'float'):
        self.wrapped.CompoundLayerThickness = float(value) if value else 0.0

    @property
    def deflection_from_bending_option(self) -> '_321.DeflectionFromBendingOption':
        """DeflectionFromBendingOption: 'DeflectionFromBendingOption' is the original name of this property."""

        temp = self.wrapped.DeflectionFromBendingOption

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, _321.DeflectionFromBendingOption)
        return constructor.new_from_mastapy_type(_321.DeflectionFromBendingOption)(value) if value is not None else None

    @deflection_from_bending_option.setter
    def deflection_from_bending_option(self, value: '_321.DeflectionFromBendingOption'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value, _321.DeflectionFromBendingOption.type_())
        self.wrapped.DeflectionFromBendingOption = value

    @property
    def file_location_for_contact_chart(self) -> 'str':
        """str: 'FileLocationForContactChart' is the original name of this property."""

        temp = self.wrapped.FileLocationForContactChart

        if temp is None:
            return ''

        return temp

    @file_location_for_contact_chart.setter
    def file_location_for_contact_chart(self, value: 'str'):
        self.wrapped.FileLocationForContactChart = str(value) if value else ''

    @property
    def number_of_columns_for_grid(self) -> 'int':
        """int: 'NumberOfColumnsForGrid' is the original name of this property."""

        temp = self.wrapped.NumberOfColumnsForGrid

        if temp is None:
            return 0

        return temp

    @number_of_columns_for_grid.setter
    def number_of_columns_for_grid(self, value: 'int'):
        self.wrapped.NumberOfColumnsForGrid = int(value) if value else 0

    @property
    def number_of_points_for_interpolated_surface_u(self) -> 'int':
        """int: 'NumberOfPointsForInterpolatedSurfaceU' is the original name of this property."""

        temp = self.wrapped.NumberOfPointsForInterpolatedSurfaceU

        if temp is None:
            return 0

        return temp

    @number_of_points_for_interpolated_surface_u.setter
    def number_of_points_for_interpolated_surface_u(self, value: 'int'):
        self.wrapped.NumberOfPointsForInterpolatedSurfaceU = int(value) if value else 0

    @property
    def number_of_points_for_interpolated_surface_v(self) -> 'int':
        """int: 'NumberOfPointsForInterpolatedSurfaceV' is the original name of this property."""

        temp = self.wrapped.NumberOfPointsForInterpolatedSurfaceV

        if temp is None:
            return 0

        return temp

    @number_of_points_for_interpolated_surface_v.setter
    def number_of_points_for_interpolated_surface_v(self, value: 'int'):
        self.wrapped.NumberOfPointsForInterpolatedSurfaceV = int(value) if value else 0

    @property
    def number_of_rows_for_fillet_grid(self) -> 'int':
        """int: 'NumberOfRowsForFilletGrid' is the original name of this property."""

        temp = self.wrapped.NumberOfRowsForFilletGrid

        if temp is None:
            return 0

        return temp

    @number_of_rows_for_fillet_grid.setter
    def number_of_rows_for_fillet_grid(self, value: 'int'):
        self.wrapped.NumberOfRowsForFilletGrid = int(value) if value else 0

    @property
    def number_of_rows_for_flank_grid(self) -> 'int':
        """int: 'NumberOfRowsForFlankGrid' is the original name of this property."""

        temp = self.wrapped.NumberOfRowsForFlankGrid

        if temp is None:
            return 0

        return temp

    @number_of_rows_for_flank_grid.setter
    def number_of_rows_for_flank_grid(self, value: 'int'):
        self.wrapped.NumberOfRowsForFlankGrid = int(value) if value else 0

    @property
    def single_tooth_stiffness(self) -> 'float':
        """float: 'SingleToothStiffness' is the original name of this property."""

        temp = self.wrapped.SingleToothStiffness

        if temp is None:
            return 0.0

        return temp

    @single_tooth_stiffness.setter
    def single_tooth_stiffness(self, value: 'float'):
        self.wrapped.SingleToothStiffness = float(value) if value else 0.0

    @property
    def write_contact_chart_to_file_after_solve(self) -> 'bool':
        """bool: 'WriteContactChartToFileAfterSolve' is the original name of this property."""

        temp = self.wrapped.WriteContactChartToFileAfterSolve

        if temp is None:
            return False

        return temp

    @write_contact_chart_to_file_after_solve.setter
    def write_contact_chart_to_file_after_solve(self, value: 'bool'):
        self.wrapped.WriteContactChartToFileAfterSolve = bool(value) if value else False

    @property
    def cast_to(self) -> 'ConicalSetMicroGeometryConfigBase._Cast_ConicalSetMicroGeometryConfigBase':
        return self._Cast_ConicalSetMicroGeometryConfigBase(self)
