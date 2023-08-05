"""_2096.py

InterferenceComponents
"""
from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INTERFERENCE_COMPONENTS = python_net_import('SMT.MastaAPI.Bearings.BearingResults.Rolling.Fitting', 'InterferenceComponents')


__docformat__ = 'restructuredtext en'
__all__ = ('InterferenceComponents',)


class InterferenceComponents(_0.APIBase):
    """InterferenceComponents

    This is a mastapy class.
    """

    TYPE = _INTERFERENCE_COMPONENTS

    class _Cast_InterferenceComponents:
        """Special nested class for casting InterferenceComponents to subclasses."""

        def __init__(self, parent: 'InterferenceComponents'):
            self._parent = parent

        @property
        def interference_components(self) -> 'InterferenceComponents':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'InterferenceComponents.TYPE'):
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
    def nominal_interfacial_interference(self) -> 'float':
        """float: 'NominalInterfacialInterference' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NominalInterfacialInterference

        if temp is None:
            return 0.0

        return temp

    @property
    def reduction_in_interference_from_centrifugal_effects(self) -> 'float':
        """float: 'ReductionInInterferenceFromCentrifugalEffects' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ReductionInInterferenceFromCentrifugalEffects

        if temp is None:
            return 0.0

        return temp

    @property
    def total_interfacial_interference(self) -> 'float':
        """float: 'TotalInterfacialInterference' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TotalInterfacialInterference

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self) -> 'InterferenceComponents._Cast_InterferenceComponents':
        return self._Cast_InterferenceComponents(self)
