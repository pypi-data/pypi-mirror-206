"""_1744.py

CustomReportCadDrawing
"""
from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy.utility.cad_export import _1820
from mastapy.utility.report import _1760
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CUSTOM_REPORT_CAD_DRAWING = python_net_import('SMT.MastaAPI.Utility.Report', 'CustomReportCadDrawing')


__docformat__ = 'restructuredtext en'
__all__ = ('CustomReportCadDrawing',)


class CustomReportCadDrawing(_1760.CustomReportNameableItem):
    """CustomReportCadDrawing

    This is a mastapy class.
    """

    TYPE = _CUSTOM_REPORT_CAD_DRAWING

    class _Cast_CustomReportCadDrawing:
        """Special nested class for casting CustomReportCadDrawing to subclasses."""

        def __init__(self, parent: 'CustomReportCadDrawing'):
            self._parent = parent

        @property
        def custom_report_nameable_item(self):
            return self._parent._cast(_1760.CustomReportNameableItem)

        @property
        def custom_report_item(self):
            from mastapy.utility.report import _1752
            
            return self._parent._cast(_1752.CustomReportItem)

        @property
        def custom_report_cad_drawing(self) -> 'CustomReportCadDrawing':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CustomReportCadDrawing.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def scale(self) -> 'float':
        """float: 'Scale' is the original name of this property."""

        temp = self.wrapped.Scale

        if temp is None:
            return 0.0

        return temp

    @scale.setter
    def scale(self, value: 'float'):
        self.wrapped.Scale = float(value) if value else 0.0

    @property
    def stock_drawing(self) -> '_1820.StockDrawings':
        """StockDrawings: 'StockDrawing' is the original name of this property."""

        temp = self.wrapped.StockDrawing

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, _1820.StockDrawings)
        return constructor.new_from_mastapy_type(_1820.StockDrawings)(value) if value is not None else None

    @stock_drawing.setter
    def stock_drawing(self, value: '_1820.StockDrawings'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value, _1820.StockDrawings.type_())
        self.wrapped.StockDrawing = value

    @property
    def use_stock_drawing(self) -> 'bool':
        """bool: 'UseStockDrawing' is the original name of this property."""

        temp = self.wrapped.UseStockDrawing

        if temp is None:
            return False

        return temp

    @use_stock_drawing.setter
    def use_stock_drawing(self, value: 'bool'):
        self.wrapped.UseStockDrawing = bool(value) if value else False

    @property
    def cast_to(self) -> 'CustomReportCadDrawing._Cast_CustomReportCadDrawing':
        return self._Cast_CustomReportCadDrawing(self)
