"""_4690.py

CampbellDiagramReport
"""
from mastapy.utility.report import _1745
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CAMPBELL_DIAGRAM_REPORT = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Reporting', 'CampbellDiagramReport')


__docformat__ = 'restructuredtext en'
__all__ = ('CampbellDiagramReport',)


class CampbellDiagramReport(_1745.CustomReportChart):
    """CampbellDiagramReport

    This is a mastapy class.
    """

    TYPE = _CAMPBELL_DIAGRAM_REPORT

    class _Cast_CampbellDiagramReport:
        """Special nested class for casting CampbellDiagramReport to subclasses."""

        def __init__(self, parent: 'CampbellDiagramReport'):
            self._parent = parent

        @property
        def custom_report_chart(self):
            return self._parent._cast(_1745.CustomReportChart)

        @property
        def custom_report_multi_property_item(self):
            from mastapy.utility.report import _1758, _1746
            
            return self._parent._cast(_1758.CustomReportMultiPropertyItem)

        @property
        def custom_report_multi_property_item_base(self):
            from mastapy.utility.report import _1759
            
            return self._parent._cast(_1759.CustomReportMultiPropertyItemBase)

        @property
        def custom_report_nameable_item(self):
            from mastapy.utility.report import _1760
            
            return self._parent._cast(_1760.CustomReportNameableItem)

        @property
        def custom_report_item(self):
            from mastapy.utility.report import _1752
            
            return self._parent._cast(_1752.CustomReportItem)

        @property
        def campbell_diagram_report(self) -> 'CampbellDiagramReport':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CampbellDiagramReport.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'CampbellDiagramReport._Cast_CampbellDiagramReport':
        return self._Cast_CampbellDiagramReport(self)
