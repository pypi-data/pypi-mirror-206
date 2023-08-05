"""_2387.py

RaceBearingFESystemDeflection
"""
from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_RACE_BEARING_FE_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.FE', 'RaceBearingFESystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('RaceBearingFESystemDeflection',)


class RaceBearingFESystemDeflection(_0.APIBase):
    """RaceBearingFESystemDeflection

    This is a mastapy class.
    """

    TYPE = _RACE_BEARING_FE_SYSTEM_DEFLECTION

    class _Cast_RaceBearingFESystemDeflection:
        """Special nested class for casting RaceBearingFESystemDeflection to subclasses."""

        def __init__(self, parent: 'RaceBearingFESystemDeflection'):
            self._parent = parent

        @property
        def race_bearing_fe_system_deflection(self) -> 'RaceBearingFESystemDeflection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'RaceBearingFESystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

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
    def cast_to(self) -> 'RaceBearingFESystemDeflection._Cast_RaceBearingFESystemDeflection':
        return self._Cast_RaceBearingFESystemDeflection(self)
