"""_2341.py

BaseFEWithSelection
"""
from typing import List

from mastapy._internal import constructor, conversion
from mastapy.nodal_analysis.dev_tools_analyses import (
    _182, _175, _191, _190
)
from mastapy.system_model.part_model import _2424
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BASE_FE_WITH_SELECTION = python_net_import('SMT.MastaAPI.SystemModel.FE', 'BaseFEWithSelection')


__docformat__ = 'restructuredtext en'
__all__ = ('BaseFEWithSelection',)


class BaseFEWithSelection(_0.APIBase):
    """BaseFEWithSelection

    This is a mastapy class.
    """

    TYPE = _BASE_FE_WITH_SELECTION

    class _Cast_BaseFEWithSelection:
        """Special nested class for casting BaseFEWithSelection to subclasses."""

        def __init__(self, parent: 'BaseFEWithSelection'):
            self._parent = parent

        @property
        def fe_substructure_with_selection(self):
            from mastapy.system_model.fe import _2370
            
            return self._parent._cast(_2370.FESubstructureWithSelection)

        @property
        def fe_substructure_with_selection_components(self):
            from mastapy.system_model.fe import _2371
            
            return self._parent._cast(_2371.FESubstructureWithSelectionComponents)

        @property
        def fe_substructure_with_selection_for_harmonic_analysis(self):
            from mastapy.system_model.fe import _2372
            
            return self._parent._cast(_2372.FESubstructureWithSelectionForHarmonicAnalysis)

        @property
        def fe_substructure_with_selection_for_modal_analysis(self):
            from mastapy.system_model.fe import _2373
            
            return self._parent._cast(_2373.FESubstructureWithSelectionForModalAnalysis)

        @property
        def fe_substructure_with_selection_for_static_analysis(self):
            from mastapy.system_model.fe import _2374
            
            return self._parent._cast(_2374.FESubstructureWithSelectionForStaticAnalysis)

        @property
        def race_bearing_fe_with_selection(self):
            from mastapy.system_model.fe import _2388
            
            return self._parent._cast(_2388.RaceBearingFEWithSelection)

        @property
        def base_fe_with_selection(self) -> 'BaseFEWithSelection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'BaseFEWithSelection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def number_of_selected_faces(self) -> 'int':
        """int: 'NumberOfSelectedFaces' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NumberOfSelectedFaces

        if temp is None:
            return 0

        return temp

    @property
    def number_of_selected_nodes(self) -> 'int':
        """int: 'NumberOfSelectedNodes' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NumberOfSelectedNodes

        if temp is None:
            return 0

        return temp

    @property
    def selected_component(self) -> 'str':
        """str: 'SelectedComponent' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SelectedComponent

        if temp is None:
            return ''

        return temp

    @property
    def component_draw_style(self) -> '_182.FEModelComponentDrawStyle':
        """FEModelComponentDrawStyle: 'ComponentDrawStyle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDrawStyle

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def draw_style(self) -> '_175.DrawStyleForFE':
        """DrawStyleForFE: 'DrawStyle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DrawStyle

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def node_selection(self) -> '_191.FENodeSelectionDrawStyle':
        """FENodeSelectionDrawStyle: 'NodeSelection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NodeSelection

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def transparency_draw_style(self) -> '_190.FEModelTransparencyDrawStyle':
        """FEModelTransparencyDrawStyle: 'TransparencyDrawStyle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TransparencyDrawStyle

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

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

    def select_component(self, component: '_2424.Component'):
        """ 'SelectComponent' is the original name of this method.

        Args:
            component (mastapy.system_model.part_model.Component)
        """

        self.wrapped.SelectComponent(component.wrapped if component else None)

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
    def cast_to(self) -> 'BaseFEWithSelection._Cast_BaseFEWithSelection':
        return self._Cast_BaseFEWithSelection(self)
