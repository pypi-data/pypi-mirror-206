"""_2217.py

MeasuredAndFactorViewModel
"""
from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MEASURED_AND_FACTOR_VIEW_MODEL = python_net_import('SMT.MastaAPI.SystemModel.Optimization', 'MeasuredAndFactorViewModel')


__docformat__ = 'restructuredtext en'
__all__ = ('MeasuredAndFactorViewModel',)


class MeasuredAndFactorViewModel(_0.APIBase):
    """MeasuredAndFactorViewModel

    This is a mastapy class.
    """

    TYPE = _MEASURED_AND_FACTOR_VIEW_MODEL

    class _Cast_MeasuredAndFactorViewModel:
        """Special nested class for casting MeasuredAndFactorViewModel to subclasses."""

        def __init__(self, parent: 'MeasuredAndFactorViewModel'):
            self._parent = parent

        @property
        def measured_and_factor_view_model(self) -> 'MeasuredAndFactorViewModel':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'MeasuredAndFactorViewModel.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def length(self) -> 'float':
        """float: 'Length' is the original name of this property."""

        temp = self.wrapped.Length

        if temp is None:
            return 0.0

        return temp

    @length.setter
    def length(self, value: 'float'):
        self.wrapped.Length = float(value) if value else 0.0

    @property
    def name(self) -> 'str':
        """str: 'Name' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Name

        if temp is None:
            return ''

        return temp

    @property
    def per_normal_module(self) -> 'float':
        """float: 'PerNormalModule' is the original name of this property."""

        temp = self.wrapped.PerNormalModule

        if temp is None:
            return 0.0

        return temp

    @per_normal_module.setter
    def per_normal_module(self, value: 'float'):
        self.wrapped.PerNormalModule = float(value) if value else 0.0

    @property
    def cast_to(self) -> 'MeasuredAndFactorViewModel._Cast_MeasuredAndFactorViewModel':
        return self._Cast_MeasuredAndFactorViewModel(self)
