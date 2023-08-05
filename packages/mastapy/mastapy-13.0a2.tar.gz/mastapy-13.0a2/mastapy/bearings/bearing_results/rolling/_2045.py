"""_2045.py

MaximumStaticContactStress
"""
from mastapy.bearings.bearing_results.rolling import _2047
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MAXIMUM_STATIC_CONTACT_STRESS = python_net_import('SMT.MastaAPI.Bearings.BearingResults.Rolling', 'MaximumStaticContactStress')


__docformat__ = 'restructuredtext en'
__all__ = ('MaximumStaticContactStress',)


class MaximumStaticContactStress(_2047.MaximumStaticContactStressResultsAbstract):
    """MaximumStaticContactStress

    This is a mastapy class.
    """

    TYPE = _MAXIMUM_STATIC_CONTACT_STRESS

    class _Cast_MaximumStaticContactStress:
        """Special nested class for casting MaximumStaticContactStress to subclasses."""

        def __init__(self, parent: 'MaximumStaticContactStress'):
            self._parent = parent

        @property
        def maximum_static_contact_stress_results_abstract(self):
            return self._parent._cast(_2047.MaximumStaticContactStressResultsAbstract)

        @property
        def maximum_static_contact_stress(self) -> 'MaximumStaticContactStress':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'MaximumStaticContactStress.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'MaximumStaticContactStress._Cast_MaximumStaticContactStress':
        return self._Cast_MaximumStaticContactStress(self)
