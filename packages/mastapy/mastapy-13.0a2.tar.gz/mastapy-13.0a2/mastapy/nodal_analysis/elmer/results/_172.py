"""_172.py

Data
"""
from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DATA = python_net_import('SMT.MastaAPI.NodalAnalysis.Elmer.Results', 'Data')


__docformat__ = 'restructuredtext en'
__all__ = ('Data',)


class Data(_0.APIBase):
    """Data

    This is a mastapy class.
    """

    TYPE = _DATA

    class _Cast_Data:
        """Special nested class for casting Data to subclasses."""

        def __init__(self, parent: 'Data'):
            self._parent = parent

        @property
        def data_1d(self):
            from mastapy.nodal_analysis.elmer.results import _173
            
            return self._parent._cast(_173.Data1D)

        @property
        def data_3d(self):
            from mastapy.nodal_analysis.elmer.results import _174
            
            return self._parent._cast(_174.Data3D)

        @property
        def data(self) -> 'Data':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'Data.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def quantity_name(self) -> 'str':
        """str: 'QuantityName' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.QuantityName

        if temp is None:
            return ''

        return temp

    @property
    def cast_to(self) -> 'Data._Cast_Data':
        return self._Cast_Data(self)
