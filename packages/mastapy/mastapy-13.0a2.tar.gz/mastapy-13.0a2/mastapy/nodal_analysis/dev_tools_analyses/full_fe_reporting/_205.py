"""_205.py

ElementPropertiesBase
"""
from typing import List

from mastapy.fe_tools.enums import _1235
from mastapy._internal import enum_with_selected_value_runtime, constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ELEMENT_PROPERTIES_BASE = python_net_import('SMT.MastaAPI.NodalAnalysis.DevToolsAnalyses.FullFEReporting', 'ElementPropertiesBase')


__docformat__ = 'restructuredtext en'
__all__ = ('ElementPropertiesBase',)


class ElementPropertiesBase(_0.APIBase):
    """ElementPropertiesBase

    This is a mastapy class.
    """

    TYPE = _ELEMENT_PROPERTIES_BASE

    class _Cast_ElementPropertiesBase:
        """Special nested class for casting ElementPropertiesBase to subclasses."""

        def __init__(self, parent: 'ElementPropertiesBase'):
            self._parent = parent

        @property
        def element_properties_beam(self):
            from mastapy.nodal_analysis.dev_tools_analyses.full_fe_reporting import _206
            
            return self._parent._cast(_206.ElementPropertiesBeam)

        @property
        def element_properties_interface(self):
            from mastapy.nodal_analysis.dev_tools_analyses.full_fe_reporting import _207
            
            return self._parent._cast(_207.ElementPropertiesInterface)

        @property
        def element_properties_mass(self):
            from mastapy.nodal_analysis.dev_tools_analyses.full_fe_reporting import _208
            
            return self._parent._cast(_208.ElementPropertiesMass)

        @property
        def element_properties_rigid(self):
            from mastapy.nodal_analysis.dev_tools_analyses.full_fe_reporting import _209
            
            return self._parent._cast(_209.ElementPropertiesRigid)

        @property
        def element_properties_shell(self):
            from mastapy.nodal_analysis.dev_tools_analyses.full_fe_reporting import _210
            
            return self._parent._cast(_210.ElementPropertiesShell)

        @property
        def element_properties_solid(self):
            from mastapy.nodal_analysis.dev_tools_analyses.full_fe_reporting import _211
            
            return self._parent._cast(_211.ElementPropertiesSolid)

        @property
        def element_properties_spring_dashpot(self):
            from mastapy.nodal_analysis.dev_tools_analyses.full_fe_reporting import _212
            
            return self._parent._cast(_212.ElementPropertiesSpringDashpot)

        @property
        def element_properties_with_material(self):
            from mastapy.nodal_analysis.dev_tools_analyses.full_fe_reporting import _213
            
            return self._parent._cast(_213.ElementPropertiesWithMaterial)

        @property
        def element_properties_base(self) -> 'ElementPropertiesBase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ElementPropertiesBase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def class_(self) -> '_1235.ElementPropertyClass':
        """ElementPropertyClass: 'Class' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Class

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, _1235.ElementPropertyClass)
        return constructor.new_from_mastapy_type(_1235.ElementPropertyClass)(value) if value is not None else None

    @property
    def id(self) -> 'int':
        """int: 'ID' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ID

        if temp is None:
            return 0

        return temp

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
    def cast_to(self) -> 'ElementPropertiesBase._Cast_ElementPropertiesBase':
        return self._Cast_ElementPropertiesBase(self)
