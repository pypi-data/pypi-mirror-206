"""_7272.py

ContactChartPerToothPass
"""
from PIL.Image import Image

from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONTACT_CHART_PER_TOOTH_PASS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections', 'ContactChartPerToothPass')


__docformat__ = 'restructuredtext en'
__all__ = ('ContactChartPerToothPass',)


class ContactChartPerToothPass(_0.APIBase):
    """ContactChartPerToothPass

    This is a mastapy class.
    """

    TYPE = _CONTACT_CHART_PER_TOOTH_PASS

    class _Cast_ContactChartPerToothPass:
        """Special nested class for casting ContactChartPerToothPass to subclasses."""

        def __init__(self, parent: 'ContactChartPerToothPass'):
            self._parent = parent

        @property
        def contact_chart_per_tooth_pass(self) -> 'ContactChartPerToothPass':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ContactChartPerToothPass.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def max_pressure(self) -> 'Image':
        """Image: 'MaxPressure' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaxPressure

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)
        return value

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
    def cast_to(self) -> 'ContactChartPerToothPass._Cast_ContactChartPerToothPass':
        return self._Cast_ContactChartPerToothPass(self)
