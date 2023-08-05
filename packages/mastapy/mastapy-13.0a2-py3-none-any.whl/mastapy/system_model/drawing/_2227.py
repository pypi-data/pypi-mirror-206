"""_2227.py

ContourDrawStyle
"""
from mastapy.utility.enums import _1808
from mastapy._internal import enum_with_selected_value_runtime, constructor, conversion
from mastapy.utility_gui import _1837
from mastapy.system_model.drawing import _2233
from mastapy.geometry import _304
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONTOUR_DRAW_STYLE = python_net_import('SMT.MastaAPI.SystemModel.Drawing', 'ContourDrawStyle')


__docformat__ = 'restructuredtext en'
__all__ = ('ContourDrawStyle',)


class ContourDrawStyle(_304.DrawStyleBase):
    """ContourDrawStyle

    This is a mastapy class.
    """

    TYPE = _CONTOUR_DRAW_STYLE

    class _Cast_ContourDrawStyle:
        """Special nested class for casting ContourDrawStyle to subclasses."""

        def __init__(self, parent: 'ContourDrawStyle'):
            self._parent = parent

        @property
        def draw_style_base(self):
            return self._parent._cast(_304.DrawStyleBase)

        @property
        def system_deflection_draw_style(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2805
            
            return self._parent._cast(_2805.SystemDeflectionDrawStyle)

        @property
        def steady_state_synchronous_response_draw_style(self):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3069
            
            return self._parent._cast(_3069.SteadyStateSynchronousResponseDrawStyle)

        @property
        def stability_analysis_draw_style(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3848
            
            return self._parent._cast(_3848.StabilityAnalysisDrawStyle)

        @property
        def rotor_dynamics_draw_style(self):
            from mastapy.system_model.analyses_and_results.rotor_dynamics import _4003
            
            return self._parent._cast(_4003.RotorDynamicsDrawStyle)

        @property
        def modal_analysis_draw_style(self):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4629
            
            return self._parent._cast(_4629.ModalAnalysisDrawStyle)

        @property
        def mbd_analysis_draw_style(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5431
            
            return self._parent._cast(_5431.MBDAnalysisDrawStyle)

        @property
        def harmonic_analysis_draw_style(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5730
            
            return self._parent._cast(_5730.HarmonicAnalysisDrawStyle)

        @property
        def dynamic_analysis_draw_style(self):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6295
            
            return self._parent._cast(_6295.DynamicAnalysisDrawStyle)

        @property
        def critical_speed_analysis_draw_style(self):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6548
            
            return self._parent._cast(_6548.CriticalSpeedAnalysisDrawStyle)

        @property
        def contour_draw_style(self) -> 'ContourDrawStyle':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ContourDrawStyle.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def contour(self) -> '_1808.ThreeDViewContourOption':
        """ThreeDViewContourOption: 'Contour' is the original name of this property."""

        temp = self.wrapped.Contour

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, _1808.ThreeDViewContourOption)
        return constructor.new_from_mastapy_type(_1808.ThreeDViewContourOption)(value) if value is not None else None

    @contour.setter
    def contour(self, value: '_1808.ThreeDViewContourOption'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value, _1808.ThreeDViewContourOption.type_())
        self.wrapped.Contour = value

    @property
    def minimum_peak_value_displacement(self) -> 'float':
        """float: 'MinimumPeakValueDisplacement' is the original name of this property."""

        temp = self.wrapped.MinimumPeakValueDisplacement

        if temp is None:
            return 0.0

        return temp

    @minimum_peak_value_displacement.setter
    def minimum_peak_value_displacement(self, value: 'float'):
        self.wrapped.MinimumPeakValueDisplacement = float(value) if value else 0.0

    @property
    def minimum_peak_value_stress(self) -> 'float':
        """float: 'MinimumPeakValueStress' is the original name of this property."""

        temp = self.wrapped.MinimumPeakValueStress

        if temp is None:
            return 0.0

        return temp

    @minimum_peak_value_stress.setter
    def minimum_peak_value_stress(self, value: 'float'):
        self.wrapped.MinimumPeakValueStress = float(value) if value else 0.0

    @property
    def show_local_maxima(self) -> 'bool':
        """bool: 'ShowLocalMaxima' is the original name of this property."""

        temp = self.wrapped.ShowLocalMaxima

        if temp is None:
            return False

        return temp

    @show_local_maxima.setter
    def show_local_maxima(self, value: 'bool'):
        self.wrapped.ShowLocalMaxima = bool(value) if value else False

    @property
    def deflection_scaling(self) -> '_1837.ScalingDrawStyle':
        """ScalingDrawStyle: 'DeflectionScaling' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DeflectionScaling

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def model_view_options(self) -> '_2233.ModelViewOptionsDrawStyle':
        """ModelViewOptionsDrawStyle: 'ModelViewOptions' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ModelViewOptions

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'ContourDrawStyle._Cast_ContourDrawStyle':
        return self._Cast_ContourDrawStyle(self)
