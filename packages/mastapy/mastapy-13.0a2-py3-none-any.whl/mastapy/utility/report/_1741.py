"""_1741.py

CustomGraphic
"""
from mastapy._internal import constructor
from mastapy.utility.report import _1749
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CUSTOM_GRAPHIC = python_net_import('SMT.MastaAPI.Utility.Report', 'CustomGraphic')


__docformat__ = 'restructuredtext en'
__all__ = ('CustomGraphic',)


class CustomGraphic(_1749.CustomReportDefinitionItem):
    """CustomGraphic

    This is a mastapy class.
    """

    TYPE = _CUSTOM_GRAPHIC

    class _Cast_CustomGraphic:
        """Special nested class for casting CustomGraphic to subclasses."""

        def __init__(self, parent: 'CustomGraphic'):
            self._parent = parent

        @property
        def custom_report_definition_item(self):
            return self._parent._cast(_1749.CustomReportDefinitionItem)

        @property
        def custom_report_nameable_item(self):
            from mastapy.utility.report import _1760
            
            return self._parent._cast(_1760.CustomReportNameableItem)

        @property
        def custom_report_item(self):
            from mastapy.utility.report import _1752
            
            return self._parent._cast(_1752.CustomReportItem)

        @property
        def custom_chart(self):
            from mastapy.utility.report import _1739
            
            return self._parent._cast(_1739.CustomChart)

        @property
        def custom_drawing(self):
            from mastapy.utility.report import _1740
            
            return self._parent._cast(_1740.CustomDrawing)

        @property
        def custom_image(self):
            from mastapy.utility.report import _1742
            
            return self._parent._cast(_1742.CustomImage)

        @property
        def loaded_bearing_chart_reporter(self):
            from mastapy.bearings.bearing_results import _1932
            
            return self._parent._cast(_1932.LoadedBearingChartReporter)

        @property
        def custom_graphic(self) -> 'CustomGraphic':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CustomGraphic.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def height(self) -> 'int':
        """int: 'Height' is the original name of this property."""

        temp = self.wrapped.Height

        if temp is None:
            return 0

        return temp

    @height.setter
    def height(self, value: 'int'):
        self.wrapped.Height = int(value) if value else 0

    @property
    def height_for_cad(self) -> 'float':
        """float: 'HeightForCAD' is the original name of this property."""

        temp = self.wrapped.HeightForCAD

        if temp is None:
            return 0.0

        return temp

    @height_for_cad.setter
    def height_for_cad(self, value: 'float'):
        self.wrapped.HeightForCAD = float(value) if value else 0.0

    @property
    def transposed(self) -> 'bool':
        """bool: 'Transposed' is the original name of this property."""

        temp = self.wrapped.Transposed

        if temp is None:
            return False

        return temp

    @transposed.setter
    def transposed(self, value: 'bool'):
        self.wrapped.Transposed = bool(value) if value else False

    @property
    def width(self) -> 'int':
        """int: 'Width' is the original name of this property."""

        temp = self.wrapped.Width

        if temp is None:
            return 0

        return temp

    @width.setter
    def width(self, value: 'int'):
        self.wrapped.Width = int(value) if value else 0

    @property
    def width_for_cad(self) -> 'float':
        """float: 'WidthForCAD' is the original name of this property."""

        temp = self.wrapped.WidthForCAD

        if temp is None:
            return 0.0

        return temp

    @width_for_cad.setter
    def width_for_cad(self, value: 'float'):
        self.wrapped.WidthForCAD = float(value) if value else 0.0

    @property
    def cast_to(self) -> 'CustomGraphic._Cast_CustomGraphic':
        return self._Cast_CustomGraphic(self)
