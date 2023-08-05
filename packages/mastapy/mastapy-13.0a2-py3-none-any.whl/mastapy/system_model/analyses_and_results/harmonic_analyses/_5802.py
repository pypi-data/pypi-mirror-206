"""_5802.py

UnbalancedMassExcitationDetail
"""
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5776
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_UNBALANCED_MASS_EXCITATION_DETAIL = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses', 'UnbalancedMassExcitationDetail')


__docformat__ = 'restructuredtext en'
__all__ = ('UnbalancedMassExcitationDetail',)


class UnbalancedMassExcitationDetail(_5776.SingleNodePeriodicExcitationWithReferenceShaft):
    """UnbalancedMassExcitationDetail

    This is a mastapy class.
    """

    TYPE = _UNBALANCED_MASS_EXCITATION_DETAIL

    class _Cast_UnbalancedMassExcitationDetail:
        """Special nested class for casting UnbalancedMassExcitationDetail to subclasses."""

        def __init__(self, parent: 'UnbalancedMassExcitationDetail'):
            self._parent = parent

        @property
        def single_node_periodic_excitation_with_reference_shaft(self):
            return self._parent._cast(_5776.SingleNodePeriodicExcitationWithReferenceShaft)

        @property
        def periodic_excitation_with_reference_shaft(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5759
            
            return self._parent._cast(_5759.PeriodicExcitationWithReferenceShaft)

        @property
        def abstract_periodic_excitation_detail(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5649
            
            return self._parent._cast(_5649.AbstractPeriodicExcitationDetail)

        @property
        def unbalanced_mass_excitation_detail(self) -> 'UnbalancedMassExcitationDetail':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'UnbalancedMassExcitationDetail.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'UnbalancedMassExcitationDetail._Cast_UnbalancedMassExcitationDetail':
        return self._Cast_UnbalancedMassExcitationDetail(self)
