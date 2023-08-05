"""_1832.py

MASTAGUI
"""
from typing import List, Dict

from mastapy._internal import constructor, conversion, enum_with_selected_value_runtime
from mastapy.system_model import _2185, _2188
from mastapy._math.color import Color
from mastapy.utility.operation_modes import _1779
from mastapy._math.vector_3d import Vector3D
from mastapy.geometry.two_d import _307
from mastapy.nodal_analysis.geometry_modeller_link import (
    _154, _155, _161, _162
)
from mastapy.math_utility import _1499, _1481
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MASTAGUI = python_net_import('SMT.MastaAPI.SystemModelGUI', 'MASTAGUI')


__docformat__ = 'restructuredtext en'
__all__ = ('MASTAGUI',)


class MASTAGUI(_0.APIBase):
    """MASTAGUI

    This is a mastapy class.
    """

    TYPE = _MASTAGUI

    class _Cast_MASTAGUI:
        """Special nested class for casting MASTAGUI to subclasses."""

        def __init__(self, parent: 'MASTAGUI'):
            self._parent = parent

        @property
        def mastagui(self) -> 'MASTAGUI':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'MASTAGUI.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def is_initialised(self) -> 'bool':
        """bool: 'IsInitialised' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.IsInitialised

        if temp is None:
            return False

        return temp

    @property
    def is_paused(self) -> 'bool':
        """bool: 'IsPaused' is the original name of this property."""

        temp = self.wrapped.IsPaused

        if temp is None:
            return False

        return temp

    @is_paused.setter
    def is_paused(self, value: 'bool'):
        self.wrapped.IsPaused = bool(value) if value else False

    @property
    def is_remoting(self) -> 'bool':
        """bool: 'IsRemoting' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.IsRemoting

        if temp is None:
            return False

        return temp

    @property
    def active_design(self) -> '_2185.Design':
        """Design: 'ActiveDesign' is the original name of this property."""

        temp = self.wrapped.ActiveDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @active_design.setter
    def active_design(self, value: '_2185.Design'):
        value = value.wrapped if value else None
        self.wrapped.ActiveDesign = value

    @property
    def color_of_new_problem_node_group(self) -> 'Color':
        """Color: 'ColorOfNewProblemNodeGroup' is the original name of this property."""

        temp = self.wrapped.ColorOfNewProblemNodeGroup

        if temp is None:
            return None

        value = conversion.pn_to_mp_color(temp)
        return value

    @color_of_new_problem_node_group.setter
    def color_of_new_problem_node_group(self, value: 'Color'):
        value = value if value else None
        value = conversion.mp_to_pn_color(value)
        self.wrapped.ColorOfNewProblemNodeGroup = value

    @property
    def geometry_modeller_file_path_to_open(self) -> 'str':
        """str: 'GeometryModellerFilePathToOpen' is the original name of this property."""

        temp = self.wrapped.GeometryModellerFilePathToOpen

        if temp is None:
            return ''

        return temp

    @geometry_modeller_file_path_to_open.setter
    def geometry_modeller_file_path_to_open(self, value: 'str'):
        self.wrapped.GeometryModellerFilePathToOpen = str(value) if value else ''

    @property
    def geometry_modeller_process_id(self) -> 'int':
        """int: 'GeometryModellerProcessID' is the original name of this property."""

        temp = self.wrapped.GeometryModellerProcessID

        if temp is None:
            return 0

        return temp

    @geometry_modeller_process_id.setter
    def geometry_modeller_process_id(self, value: 'int'):
        self.wrapped.GeometryModellerProcessID = int(value) if value else 0

    @property
    def is_connected_to_geometry_modeller(self) -> 'bool':
        """bool: 'IsConnectedToGeometryModeller' is the original name of this property."""

        temp = self.wrapped.IsConnectedToGeometryModeller

        if temp is None:
            return False

        return temp

    @is_connected_to_geometry_modeller.setter
    def is_connected_to_geometry_modeller(self, value: 'bool'):
        self.wrapped.IsConnectedToGeometryModeller = bool(value) if value else False

    @property
    def name_of_new_problem_node_group(self) -> 'str':
        """str: 'NameOfNewProblemNodeGroup' is the original name of this property."""

        temp = self.wrapped.NameOfNewProblemNodeGroup

        if temp is None:
            return ''

        return temp

    @name_of_new_problem_node_group.setter
    def name_of_new_problem_node_group(self, value: 'str'):
        self.wrapped.NameOfNewProblemNodeGroup = str(value) if value else ''

    @property
    def open_designs(self) -> 'List[_2185.Design]':
        """List[Design]: 'OpenDesigns' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OpenDesigns

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def operation_mode(self) -> '_1779.OperationMode':
        """OperationMode: 'OperationMode' is the original name of this property."""

        temp = self.wrapped.OperationMode

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, _1779.OperationMode)
        return constructor.new_from_mastapy_type(_1779.OperationMode)(value) if value is not None else None

    @operation_mode.setter
    def operation_mode(self, value: '_1779.OperationMode'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value, _1779.OperationMode.type_())
        self.wrapped.OperationMode = value

    @property
    def positions_of_problem_node_group(self) -> 'List[Vector3D]':
        """List[Vector3D]: 'PositionsOfProblemNodeGroup' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PositionsOfProblemNodeGroup

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def process_id(self) -> 'int':
        """int: 'ProcessId' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ProcessId

        if temp is None:
            return 0

        return temp

    @property
    def restart_geometry_modeller_flag(self) -> 'bool':
        """bool: 'RestartGeometryModellerFlag' is the original name of this property."""

        temp = self.wrapped.RestartGeometryModellerFlag

        if temp is None:
            return False

        return temp

    @restart_geometry_modeller_flag.setter
    def restart_geometry_modeller_flag(self, value: 'bool'):
        self.wrapped.RestartGeometryModellerFlag = bool(value) if value else False

    @property
    def restart_geometry_modeller_save_file(self) -> 'str':
        """str: 'RestartGeometryModellerSaveFile' is the original name of this property."""

        temp = self.wrapped.RestartGeometryModellerSaveFile

        if temp is None:
            return ''

        return temp

    @restart_geometry_modeller_save_file.setter
    def restart_geometry_modeller_save_file(self, value: 'str'):
        self.wrapped.RestartGeometryModellerSaveFile = str(value) if value else ''

    @property
    def selected_design_entity(self) -> '_2188.DesignEntity':
        """DesignEntity: 'SelectedDesignEntity' is the original name of this property."""

        temp = self.wrapped.SelectedDesignEntity

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @selected_design_entity.setter
    def selected_design_entity(self, value: '_2188.DesignEntity'):
        value = value.wrapped if value else None
        self.wrapped.SelectedDesignEntity = value

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

    @staticmethod
    def get_mastagui(process_id: 'int') -> 'MASTAGUI':
        """ 'GetMASTAGUI' is the original name of this method.

        Args:
            process_id (int)

        Returns:
            mastapy.system_model_gui.MASTAGUI
        """

        process_id = int(process_id)
        method_result = MASTAGUI.TYPE.GetMASTAGUI(process_id if process_id else 0)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def pause(self):
        """ 'Pause' is the original name of this method."""

        self.wrapped.Pause()

    def resume(self):
        """ 'Resume' is the original name of this method."""

        self.wrapped.Resume()

    def start_remoting(self):
        """ 'StartRemoting' is the original name of this method."""

        self.wrapped.StartRemoting()

    def stop_remoting(self):
        """ 'StopRemoting' is the original name of this method."""

        self.wrapped.StopRemoting()

    def aborted(self):
        """ 'Aborted' is the original name of this method."""

        self.wrapped.Aborted()

    def add_electric_machine_from_cad_face_group(self, cad_face_group: '_307.CADFaceGroup', geometry_modeller_design_information: '_154.GeometryModellerDesignInformation', dimensions: 'Dict[str, _155.GeometryModellerDimension]'):
        """ 'AddElectricMachineFromCADFaceGroup' is the original name of this method.

        Args:
            cad_face_group (mastapy.geometry.two_d.CADFaceGroup)
            geometry_modeller_design_information (mastapy.nodal_analysis.geometry_modeller_link.GeometryModellerDesignInformation)
            dimensions (Dict[str, mastapy.nodal_analysis.geometry_modeller_link.GeometryModellerDimension])
        """

        self.wrapped.AddElectricMachineFromCADFaceGroup(cad_face_group.wrapped if cad_face_group else None, geometry_modeller_design_information.wrapped if geometry_modeller_design_information else None, dimensions)

    def add_fe_substructure_from_data(self, vertices_and_facets: '_1499.FacetedBody', geometry_modeller_design_information: '_154.GeometryModellerDesignInformation', dimensions: 'Dict[str, _155.GeometryModellerDimension]', body_moniker: 'str'):
        """ 'AddFESubstructureFromData' is the original name of this method.

        Args:
            vertices_and_facets (mastapy.math_utility.FacetedBody)
            geometry_modeller_design_information (mastapy.nodal_analysis.geometry_modeller_link.GeometryModellerDesignInformation)
            dimensions (Dict[str, mastapy.nodal_analysis.geometry_modeller_link.GeometryModellerDimension])
            body_moniker (str)
        """

        body_moniker = str(body_moniker)
        self.wrapped.AddFESubstructureFromData(vertices_and_facets.wrapped if vertices_and_facets else None, geometry_modeller_design_information.wrapped if geometry_modeller_design_information else None, dimensions, body_moniker if body_moniker else '')

    def add_fe_substructure_from_file(self, length_scale: 'float', stl_file_name: 'str', dimensions: 'Dict[str, _155.GeometryModellerDimension]'):
        """ 'AddFESubstructureFromFile' is the original name of this method.

        Args:
            length_scale (float)
            stl_file_name (str)
            dimensions (Dict[str, mastapy.nodal_analysis.geometry_modeller_link.GeometryModellerDimension])
        """

        length_scale = float(length_scale)
        stl_file_name = str(stl_file_name)
        self.wrapped.AddFESubstructureFromFile(length_scale if length_scale else 0.0, stl_file_name if stl_file_name else '', dimensions)

    def add_line_from_geometry_modeller(self, circles_on_axis: '_1481.CirclesOnAxis'):
        """ 'AddLineFromGeometryModeller' is the original name of this method.

        Args:
            circles_on_axis (mastapy.math_utility.CirclesOnAxis)
        """

        self.wrapped.AddLineFromGeometryModeller(circles_on_axis.wrapped if circles_on_axis else None)

    def are_new_input_available(self) -> '_161.MeshRequest':
        """ 'AreNewInputAvailable' is the original name of this method.

        Returns:
            mastapy.nodal_analysis.geometry_modeller_link.MeshRequest
        """

        method_result = self.wrapped.AreNewInputAvailable()
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def circle_pairs_from_geometry_modeller(self, preselection_circles: '_1481.CirclesOnAxis', selected_circles: 'List[_1481.CirclesOnAxis]'):
        """ 'CirclePairsFromGeometryModeller' is the original name of this method.

        Args:
            preselection_circles (mastapy.math_utility.CirclesOnAxis)
            selected_circles (List[mastapy.math_utility.CirclesOnAxis])
        """

        selected_circles = conversion.mp_to_pn_objects_in_list(selected_circles)
        self.wrapped.CirclePairsFromGeometryModeller(preselection_circles.wrapped if preselection_circles else None, selected_circles)

    def create_geometry_modeller_design_information(self, file_name: 'str', main_part_moniker: 'str', tab_name: 'str') -> '_154.GeometryModellerDesignInformation':
        """ 'CreateGeometryModellerDesignInformation' is the original name of this method.

        Args:
            file_name (str)
            main_part_moniker (str)
            tab_name (str)

        Returns:
            mastapy.nodal_analysis.geometry_modeller_link.GeometryModellerDesignInformation
        """

        file_name = str(file_name)
        main_part_moniker = str(main_part_moniker)
        tab_name = str(tab_name)
        method_result = self.wrapped.CreateGeometryModellerDesignInformation(file_name if file_name else '', main_part_moniker if main_part_moniker else '', tab_name if tab_name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def create_geometry_modeller_dimension(self) -> '_155.GeometryModellerDimension':
        """ 'CreateGeometryModellerDimension' is the original name of this method.

        Returns:
            mastapy.nodal_analysis.geometry_modeller_link.GeometryModellerDimension
        """

        method_result = self.wrapped.CreateGeometryModellerDimension()
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def create_mesh_request_result(self) -> '_162.MeshRequestResult':
        """ 'CreateMeshRequestResult' is the original name of this method.

        Returns:
            mastapy.nodal_analysis.geometry_modeller_link.MeshRequestResult
        """

        method_result = self.wrapped.CreateMeshRequestResult()
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def create_new_cad_face_group(self) -> '_307.CADFaceGroup':
        """ 'CreateNewCADFaceGroup' is the original name of this method.

        Returns:
            mastapy.geometry.two_d.CADFaceGroup
        """

        method_result = self.wrapped.CreateNewCADFaceGroup()
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def create_new_circles_on_axis(self) -> '_1481.CirclesOnAxis':
        """ 'CreateNewCirclesOnAxis' is the original name of this method.

        Returns:
            mastapy.math_utility.CirclesOnAxis
        """

        method_result = self.wrapped.CreateNewCirclesOnAxis()
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def create_new_faceted_body(self) -> '_1499.FacetedBody':
        """ 'CreateNewFacetedBody' is the original name of this method.

        Returns:
            mastapy.math_utility.FacetedBody
        """

        method_result = self.wrapped.CreateNewFacetedBody()
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def flag_message_received(self):
        """ 'FlagMessageReceived' is the original name of this method."""

        self.wrapped.FlagMessageReceived()

    def geometry_modeller_document_loaded(self):
        """ 'GeometryModellerDocumentLoaded' is the original name of this method."""

        self.wrapped.GeometryModellerDocumentLoaded()

    def move_selected_component(self, origin: 'Vector3D', axis: 'Vector3D'):
        """ 'MoveSelectedComponent' is the original name of this method.

        Args:
            origin (Vector3D)
            axis (Vector3D)
        """

        origin = conversion.mp_to_pn_vector3d(origin)
        axis = conversion.mp_to_pn_vector3d(axis)
        self.wrapped.MoveSelectedComponent(origin, axis)

    def open_design_in_new_tab(self, design: '_2185.Design'):
        """ 'OpenDesignInNewTab' is the original name of this method.

        Args:
            design (mastapy.system_model.Design)
        """

        self.wrapped.OpenDesignInNewTab(design.wrapped if design else None)

    def run_command(self, command: 'str'):
        """ 'RunCommand' is the original name of this method.

        Args:
            command (str)
        """

        command = str(command)
        self.wrapped.RunCommand(command if command else '')

    def select_tab(self, tab_text: 'str'):
        """ 'SelectTab' is the original name of this method.

        Args:
            tab_text (str)
        """

        tab_text = str(tab_text)
        self.wrapped.SelectTab(tab_text if tab_text else '')

    def set_error(self, error: 'str'):
        """ 'SetError' is the original name of this method.

        Args:
            error (str)
        """

        error = str(error)
        self.wrapped.SetError(error if error else '')

    def set_mesh_request_result(self, mesh_request_result: '_162.MeshRequestResult'):
        """ 'SetMeshRequestResult' is the original name of this method.

        Args:
            mesh_request_result (mastapy.nodal_analysis.geometry_modeller_link.MeshRequestResult)
        """

        self.wrapped.SetMeshRequestResult(mesh_request_result.wrapped if mesh_request_result else None)

    def show_boxes(self, small_box: 'List[Vector3D]', big_box: 'List[Vector3D]'):
        """ 'ShowBoxes' is the original name of this method.

        Args:
            small_box (List[Vector3D])
            big_box (List[Vector3D])
        """

        small_box = conversion.mp_to_pn_objects_in_list(small_box)
        big_box = conversion.mp_to_pn_objects_in_list(big_box)
        self.wrapped.ShowBoxes(small_box, big_box)

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
    def cast_to(self) -> 'MASTAGUI._Cast_MASTAGUI':
        return self._Cast_MASTAGUI(self)
