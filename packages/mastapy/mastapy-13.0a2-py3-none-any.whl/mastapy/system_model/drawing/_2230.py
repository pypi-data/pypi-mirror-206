"""_2230.py

HarmonicAnalysisViewable
"""
from mastapy._internal.implicit import list_with_selected_item, enum_with_selected_value
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5649, _5737
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy.utility.generics import _1797
from mastapy.math_utility import _1517
from mastapy.system_model.analyses_and_results.system_deflections import _2738
from mastapy.system_model.drawing.options import _2243
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6295
from mastapy.system_model.drawing import _2229
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HARMONIC_ANALYSIS_VIEWABLE = python_net_import('SMT.MastaAPI.SystemModel.Drawing', 'HarmonicAnalysisViewable')


__docformat__ = 'restructuredtext en'
__all__ = ('HarmonicAnalysisViewable',)


class HarmonicAnalysisViewable(_2229.DynamicAnalysisViewable):
    """HarmonicAnalysisViewable

    This is a mastapy class.
    """

    TYPE = _HARMONIC_ANALYSIS_VIEWABLE

    class _Cast_HarmonicAnalysisViewable:
        """Special nested class for casting HarmonicAnalysisViewable to subclasses."""

        def __init__(self, parent: 'HarmonicAnalysisViewable'):
            self._parent = parent

        @property
        def dynamic_analysis_viewable(self):
            return self._parent._cast(_2229.DynamicAnalysisViewable)

        @property
        def part_analysis_case_with_contour_viewable(self):
            from mastapy.system_model.drawing import _2234
            
            return self._parent._cast(_2234.PartAnalysisCaseWithContourViewable)

        @property
        def harmonic_analysis_viewable(self) -> 'HarmonicAnalysisViewable':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'HarmonicAnalysisViewable.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def excitation(self) -> 'list_with_selected_item.ListWithSelectedItem_AbstractPeriodicExcitationDetail':
        """list_with_selected_item.ListWithSelectedItem_AbstractPeriodicExcitationDetail: 'Excitation' is the original name of this property."""

        temp = self.wrapped.Excitation

        if temp is None:
            return None

        return constructor.new_from_mastapy_type(list_with_selected_item.ListWithSelectedItem_AbstractPeriodicExcitationDetail)(temp) if temp is not None else None

    @excitation.setter
    def excitation(self, value: 'list_with_selected_item.ListWithSelectedItem_AbstractPeriodicExcitationDetail.implicit_type()'):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_AbstractPeriodicExcitationDetail.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_AbstractPeriodicExcitationDetail.implicit_type()
        value = wrapper_type[enclosed_type](value.wrapped if value is not None else None)
        self.wrapped.Excitation = value

    @property
    def frequency(self) -> 'float':
        """float: 'Frequency' is the original name of this property."""

        temp = self.wrapped.Frequency

        if temp is None:
            return 0.0

        return temp

    @frequency.setter
    def frequency(self, value: 'float'):
        self.wrapped.Frequency = float(value) if value else 0.0

    @property
    def harmonic(self) -> 'int':
        """int: 'Harmonic' is the original name of this property."""

        temp = self.wrapped.Harmonic

        if temp is None:
            return 0

        return temp

    @harmonic.setter
    def harmonic(self, value: 'int'):
        self.wrapped.Harmonic = int(value) if value else 0

    @property
    def harmonic_analysis_with_varying_stiffness_step(self) -> 'list_with_selected_item.ListWithSelectedItem_HarmonicAnalysisWithVaryingStiffnessStaticLoadCase':
        """list_with_selected_item.ListWithSelectedItem_HarmonicAnalysisWithVaryingStiffnessStaticLoadCase: 'HarmonicAnalysisWithVaryingStiffnessStep' is the original name of this property."""

        temp = self.wrapped.HarmonicAnalysisWithVaryingStiffnessStep

        if temp is None:
            return None

        return constructor.new_from_mastapy_type(list_with_selected_item.ListWithSelectedItem_HarmonicAnalysisWithVaryingStiffnessStaticLoadCase)(temp) if temp is not None else None

    @harmonic_analysis_with_varying_stiffness_step.setter
    def harmonic_analysis_with_varying_stiffness_step(self, value: 'list_with_selected_item.ListWithSelectedItem_HarmonicAnalysisWithVaryingStiffnessStaticLoadCase.implicit_type()'):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_HarmonicAnalysisWithVaryingStiffnessStaticLoadCase.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_HarmonicAnalysisWithVaryingStiffnessStaticLoadCase.implicit_type()
        value = wrapper_type[enclosed_type](value.wrapped if value is not None else None)
        self.wrapped.HarmonicAnalysisWithVaryingStiffnessStep = value

    @property
    def order(self) -> 'list_with_selected_item.ListWithSelectedItem_NamedTuple1_RoundedOrder':
        """list_with_selected_item.ListWithSelectedItem_NamedTuple1_RoundedOrder: 'Order' is the original name of this property."""

        temp = self.wrapped.Order

        if temp is None:
            return None

        return constructor.new_from_mastapy_type(list_with_selected_item.ListWithSelectedItem_NamedTuple1_RoundedOrder)(temp) if temp is not None else None

    @order.setter
    def order(self, value: 'list_with_selected_item.ListWithSelectedItem_NamedTuple1_RoundedOrder.implicit_type()'):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_NamedTuple1_RoundedOrder.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_NamedTuple1_RoundedOrder.implicit_type()
        value = wrapper_type[enclosed_type](value.wrapped if value is not None else None)
        self.wrapped.Order = value

    @property
    def reference_power_load_speed(self) -> 'float':
        """float: 'ReferencePowerLoadSpeed' is the original name of this property."""

        temp = self.wrapped.ReferencePowerLoadSpeed

        if temp is None:
            return 0.0

        return temp

    @reference_power_load_speed.setter
    def reference_power_load_speed(self, value: 'float'):
        self.wrapped.ReferencePowerLoadSpeed = float(value) if value else 0.0

    @property
    def uncoupled_mesh(self) -> 'list_with_selected_item.ListWithSelectedItem_GearMeshSystemDeflection':
        """list_with_selected_item.ListWithSelectedItem_GearMeshSystemDeflection: 'UncoupledMesh' is the original name of this property."""

        temp = self.wrapped.UncoupledMesh

        if temp is None:
            return None

        return constructor.new_from_mastapy_type(list_with_selected_item.ListWithSelectedItem_GearMeshSystemDeflection)(temp) if temp is not None else None

    @uncoupled_mesh.setter
    def uncoupled_mesh(self, value: 'list_with_selected_item.ListWithSelectedItem_GearMeshSystemDeflection.implicit_type()'):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_GearMeshSystemDeflection.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_GearMeshSystemDeflection.implicit_type()
        value = wrapper_type[enclosed_type](value.wrapped if value is not None else None)
        self.wrapped.UncoupledMesh = value

    @property
    def view_type(self) -> 'enum_with_selected_value.EnumWithSelectedValue_ExcitationAnalysisViewOption':
        """enum_with_selected_value.EnumWithSelectedValue_ExcitationAnalysisViewOption: 'ViewType' is the original name of this property."""

        temp = self.wrapped.ViewType

        if temp is None:
            return None

        value = enum_with_selected_value.EnumWithSelectedValue_ExcitationAnalysisViewOption.wrapped_type()
        return enum_with_selected_value_runtime.create(temp, value) if temp is not None else None

    @view_type.setter
    def view_type(self, value: 'enum_with_selected_value.EnumWithSelectedValue_ExcitationAnalysisViewOption.implicit_type()'):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = enum_with_selected_value.EnumWithSelectedValue_ExcitationAnalysisViewOption.implicit_type()
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.ViewType = value

    @property
    def dynamic_analysis_draw_style(self) -> '_6295.DynamicAnalysisDrawStyle':
        """DynamicAnalysisDrawStyle: 'DynamicAnalysisDrawStyle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DynamicAnalysisDrawStyle

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'HarmonicAnalysisViewable._Cast_HarmonicAnalysisViewable':
        return self._Cast_HarmonicAnalysisViewable(self)
