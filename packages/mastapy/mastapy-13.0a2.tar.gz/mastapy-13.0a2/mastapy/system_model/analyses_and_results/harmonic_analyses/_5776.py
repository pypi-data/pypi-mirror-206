"""_5776.py

SingleNodePeriodicExcitationWithReferenceShaft
"""
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5759
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SINGLE_NODE_PERIODIC_EXCITATION_WITH_REFERENCE_SHAFT = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses', 'SingleNodePeriodicExcitationWithReferenceShaft')


__docformat__ = 'restructuredtext en'
__all__ = ('SingleNodePeriodicExcitationWithReferenceShaft',)


class SingleNodePeriodicExcitationWithReferenceShaft(_5759.PeriodicExcitationWithReferenceShaft):
    """SingleNodePeriodicExcitationWithReferenceShaft

    This is a mastapy class.
    """

    TYPE = _SINGLE_NODE_PERIODIC_EXCITATION_WITH_REFERENCE_SHAFT

    class _Cast_SingleNodePeriodicExcitationWithReferenceShaft:
        """Special nested class for casting SingleNodePeriodicExcitationWithReferenceShaft to subclasses."""

        def __init__(self, parent: 'SingleNodePeriodicExcitationWithReferenceShaft'):
            self._parent = parent

        @property
        def periodic_excitation_with_reference_shaft(self):
            return self._parent._cast(_5759.PeriodicExcitationWithReferenceShaft)

        @property
        def abstract_periodic_excitation_detail(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5649
            
            return self._parent._cast(_5649.AbstractPeriodicExcitationDetail)

        @property
        def general_periodic_excitation_detail(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5728
            
            return self._parent._cast(_5728.GeneralPeriodicExcitationDetail)

        @property
        def unbalanced_mass_excitation_detail(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5802
            
            return self._parent._cast(_5802.UnbalancedMassExcitationDetail)

        @property
        def single_node_periodic_excitation_with_reference_shaft(self) -> 'SingleNodePeriodicExcitationWithReferenceShaft':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'SingleNodePeriodicExcitationWithReferenceShaft.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'SingleNodePeriodicExcitationWithReferenceShaft._Cast_SingleNodePeriodicExcitationWithReferenceShaft':
        return self._Cast_SingleNodePeriodicExcitationWithReferenceShaft(self)
