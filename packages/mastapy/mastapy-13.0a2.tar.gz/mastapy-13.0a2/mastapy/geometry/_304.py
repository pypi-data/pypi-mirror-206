"""_304.py

DrawStyleBase
"""
from typing import List

from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DRAW_STYLE_BASE = python_net_import('SMT.MastaAPI.Geometry', 'DrawStyleBase')


__docformat__ = 'restructuredtext en'
__all__ = ('DrawStyleBase',)


class DrawStyleBase(_0.APIBase):
    """DrawStyleBase

    This is a mastapy class.
    """

    TYPE = _DRAW_STYLE_BASE

    class _Cast_DrawStyleBase:
        """Special nested class for casting DrawStyleBase to subclasses."""

        def __init__(self, parent: 'DrawStyleBase'):
            self._parent = parent

        @property
        def draw_style(self):
            from mastapy.geometry import _303
            
            return self._parent._cast(_303.DrawStyle)

        @property
        def contour_draw_style(self):
            from mastapy.system_model.drawing import _2227
            
            return self._parent._cast(_2227.ContourDrawStyle)

        @property
        def model_view_options_draw_style(self):
            from mastapy.system_model.drawing import _2233
            
            return self._parent._cast(_2233.ModelViewOptionsDrawStyle)

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
        def cylindrical_gear_geometric_entity_draw_style(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4056
            
            return self._parent._cast(_4056.CylindricalGearGeometricEntityDrawStyle)

        @property
        def power_flow_draw_style(self):
            from mastapy.system_model.analyses_and_results.power_flows import _4098
            
            return self._parent._cast(_4098.PowerFlowDrawStyle)

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
        def draw_style_base(self) -> 'DrawStyleBase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'DrawStyleBase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def report_names(self) -> 'List[str]':
        """List[str]: 'ReportNames' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ReportNames

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, str)
        return value

    def output_default_report_to(self, file_path: 'str'):
        """ 'OutputDefaultReportTo' is the original name of this method.

        Args:
            file_path (str)
        """

        file_path = str(file_path)
        self.wrapped.OutputDefaultReportTo(file_path if file_path else '')

    def get_default_report_with_encoded_images(self) -> 'str':
        """ 'GetDefaultReportWithEncodedImages' is the original name of this method.

        Returns:
            str
        """

        method_result = self.wrapped.GetDefaultReportWithEncodedImages()
        return method_result

    def output_active_report_to(self, file_path: 'str'):
        """ 'OutputActiveReportTo' is the original name of this method.

        Args:
            file_path (str)
        """

        file_path = str(file_path)
        self.wrapped.OutputActiveReportTo(file_path if file_path else '')

    def output_active_report_as_text_to(self, file_path: 'str'):
        """ 'OutputActiveReportAsTextTo' is the original name of this method.

        Args:
            file_path (str)
        """

        file_path = str(file_path)
        self.wrapped.OutputActiveReportAsTextTo(file_path if file_path else '')

    def get_active_report_with_encoded_images(self) -> 'str':
        """ 'GetActiveReportWithEncodedImages' is the original name of this method.

        Returns:
            str
        """

        method_result = self.wrapped.GetActiveReportWithEncodedImages()
        return method_result

    def output_named_report_to(self, report_name: 'str', file_path: 'str'):
        """ 'OutputNamedReportTo' is the original name of this method.

        Args:
            report_name (str)
            file_path (str)
        """

        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportTo(report_name if report_name else '', file_path if file_path else '')

    def output_named_report_as_masta_report(self, report_name: 'str', file_path: 'str'):
        """ 'OutputNamedReportAsMastaReport' is the original name of this method.

        Args:
            report_name (str)
            file_path (str)
        """

        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsMastaReport(report_name if report_name else '', file_path if file_path else '')

    def output_named_report_as_text_to(self, report_name: 'str', file_path: 'str'):
        """ 'OutputNamedReportAsTextTo' is the original name of this method.

        Args:
            report_name (str)
            file_path (str)
        """

        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsTextTo(report_name if report_name else '', file_path if file_path else '')

    def get_named_report_with_encoded_images(self, report_name: 'str') -> 'str':
        """ 'GetNamedReportWithEncodedImages' is the original name of this method.

        Args:
            report_name (str)

        Returns:
            str
        """

        report_name = str(report_name)
        method_result = self.wrapped.GetNamedReportWithEncodedImages(report_name if report_name else '')
        return method_result

    @property
    def cast_to(self) -> 'DrawStyleBase._Cast_DrawStyleBase':
        return self._Cast_DrawStyleBase(self)
