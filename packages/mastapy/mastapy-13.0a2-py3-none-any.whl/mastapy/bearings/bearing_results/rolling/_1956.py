"""_1956.py

ForceAtLaminaReportable
"""
from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FORCE_AT_LAMINA_REPORTABLE = python_net_import('SMT.MastaAPI.Bearings.BearingResults.Rolling', 'ForceAtLaminaReportable')


__docformat__ = 'restructuredtext en'
__all__ = ('ForceAtLaminaReportable',)


class ForceAtLaminaReportable(_0.APIBase):
    """ForceAtLaminaReportable

    This is a mastapy class.
    """

    TYPE = _FORCE_AT_LAMINA_REPORTABLE

    class _Cast_ForceAtLaminaReportable:
        """Special nested class for casting ForceAtLaminaReportable to subclasses."""

        def __init__(self, parent: 'ForceAtLaminaReportable'):
            self._parent = parent

        @property
        def force_at_lamina_reportable(self) -> 'ForceAtLaminaReportable':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ForceAtLaminaReportable.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def dynamic_equivalent_load(self) -> 'float':
        """float: 'DynamicEquivalentLoad' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DynamicEquivalentLoad

        if temp is None:
            return 0.0

        return temp

    @property
    def lamina_index(self) -> 'int':
        """int: 'LaminaIndex' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LaminaIndex

        if temp is None:
            return 0

        return temp

    @property
    def cast_to(self) -> 'ForceAtLaminaReportable._Cast_ForceAtLaminaReportable':
        return self._Cast_ForceAtLaminaReportable(self)
