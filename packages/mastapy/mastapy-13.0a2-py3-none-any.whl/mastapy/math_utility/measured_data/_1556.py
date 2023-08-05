"""_1556.py

OnedimensionalFunctionLookupTable
"""
from mastapy.math_utility import _1523
from mastapy._internal import constructor
from mastapy.math_utility.measured_data import _1555
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ONEDIMENSIONAL_FUNCTION_LOOKUP_TABLE = python_net_import('SMT.MastaAPI.MathUtility.MeasuredData', 'OnedimensionalFunctionLookupTable')


__docformat__ = 'restructuredtext en'
__all__ = ('OnedimensionalFunctionLookupTable',)


class OnedimensionalFunctionLookupTable(_1555.LookupTableBase['OnedimensionalFunctionLookupTable']):
    """OnedimensionalFunctionLookupTable

    This is a mastapy class.
    """

    TYPE = _ONEDIMENSIONAL_FUNCTION_LOOKUP_TABLE

    class _Cast_OnedimensionalFunctionLookupTable:
        """Special nested class for casting OnedimensionalFunctionLookupTable to subclasses."""

        def __init__(self, parent: 'OnedimensionalFunctionLookupTable'):
            self._parent = parent

        @property
        def lookup_table_base(self):
            from mastapy.math_utility.measured_data import _1556
            
            return self._parent._cast(_1555.LookupTableBase)

        @property
        def independent_reportable_properties_base(self):
            from mastapy.utility import _1575
            from mastapy.math_utility.measured_data import _1556
            
            return self._parent._cast(_1575.IndependentReportablePropertiesBase)

        @property
        def onedimensional_function_lookup_table(self) -> 'OnedimensionalFunctionLookupTable':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'OnedimensionalFunctionLookupTable.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def lookup_table(self) -> '_1523.Vector2DListAccessor':
        """Vector2DListAccessor: 'LookupTable' is the original name of this property."""

        temp = self.wrapped.LookupTable

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @lookup_table.setter
    def lookup_table(self, value: '_1523.Vector2DListAccessor'):
        value = value.wrapped if value else None
        self.wrapped.LookupTable = value

    @property
    def cast_to(self) -> 'OnedimensionalFunctionLookupTable._Cast_OnedimensionalFunctionLookupTable':
        return self._Cast_OnedimensionalFunctionLookupTable(self)
