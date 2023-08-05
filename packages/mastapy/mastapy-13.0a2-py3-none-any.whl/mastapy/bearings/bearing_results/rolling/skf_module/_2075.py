"""_2075.py

LifeModel
"""
from mastapy._internal import constructor
from mastapy.bearings.bearing_results.rolling.skf_module import _2081
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LIFE_MODEL = python_net_import('SMT.MastaAPI.Bearings.BearingResults.Rolling.SkfModule', 'LifeModel')


__docformat__ = 'restructuredtext en'
__all__ = ('LifeModel',)


class LifeModel(_2081.SKFCalculationResult):
    """LifeModel

    This is a mastapy class.
    """

    TYPE = _LIFE_MODEL

    class _Cast_LifeModel:
        """Special nested class for casting LifeModel to subclasses."""

        def __init__(self, parent: 'LifeModel'):
            self._parent = parent

        @property
        def skf_calculation_result(self):
            return self._parent._cast(_2081.SKFCalculationResult)

        @property
        def life_model(self) -> 'LifeModel':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'LifeModel.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def basic(self) -> 'float':
        """float: 'Basic' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Basic

        if temp is None:
            return 0.0

        return temp

    @property
    def skf(self) -> 'float':
        """float: 'SKF' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SKF

        if temp is None:
            return 0.0

        return temp

    @property
    def skfgblm(self) -> 'float':
        """float: 'SKFGBLM' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SKFGBLM

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self) -> 'LifeModel._Cast_LifeModel':
        return self._Cast_LifeModel(self)
