"""_2079.py

RotationalFrequency
"""
from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROTATIONAL_FREQUENCY = python_net_import('SMT.MastaAPI.Bearings.BearingResults.Rolling.SkfModule', 'RotationalFrequency')


__docformat__ = 'restructuredtext en'
__all__ = ('RotationalFrequency',)


class RotationalFrequency(_0.APIBase):
    """RotationalFrequency

    This is a mastapy class.
    """

    TYPE = _ROTATIONAL_FREQUENCY

    class _Cast_RotationalFrequency:
        """Special nested class for casting RotationalFrequency to subclasses."""

        def __init__(self, parent: 'RotationalFrequency'):
            self._parent = parent

        @property
        def rotational_frequency(self) -> 'RotationalFrequency':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'RotationalFrequency.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def inner_ring(self) -> 'float':
        """float: 'InnerRing' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerRing

        if temp is None:
            return 0.0

        return temp

    @property
    def outer_ring(self) -> 'float':
        """float: 'OuterRing' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterRing

        if temp is None:
            return 0.0

        return temp

    @property
    def rolling_element_about_its_axis(self) -> 'float':
        """float: 'RollingElementAboutItsAxis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RollingElementAboutItsAxis

        if temp is None:
            return 0.0

        return temp

    @property
    def rolling_element_set_ampersand_cage(self) -> 'float':
        """float: 'RollingElementSetAmpersandCage' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RollingElementSetAmpersandCage

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self) -> 'RotationalFrequency._Cast_RotationalFrequency':
        return self._Cast_RotationalFrequency(self)
