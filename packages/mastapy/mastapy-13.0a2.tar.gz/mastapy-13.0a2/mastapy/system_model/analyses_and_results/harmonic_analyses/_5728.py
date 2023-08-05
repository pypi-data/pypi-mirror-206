"""_5728.py

GeneralPeriodicExcitationDetail
"""
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5776
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GENERAL_PERIODIC_EXCITATION_DETAIL = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses', 'GeneralPeriodicExcitationDetail')


__docformat__ = 'restructuredtext en'
__all__ = ('GeneralPeriodicExcitationDetail',)


class GeneralPeriodicExcitationDetail(_5776.SingleNodePeriodicExcitationWithReferenceShaft):
    """GeneralPeriodicExcitationDetail

    This is a mastapy class.
    """

    TYPE = _GENERAL_PERIODIC_EXCITATION_DETAIL

    class _Cast_GeneralPeriodicExcitationDetail:
        """Special nested class for casting GeneralPeriodicExcitationDetail to subclasses."""

        def __init__(self, parent: 'GeneralPeriodicExcitationDetail'):
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
        def general_periodic_excitation_detail(self) -> 'GeneralPeriodicExcitationDetail':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GeneralPeriodicExcitationDetail.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'GeneralPeriodicExcitationDetail._Cast_GeneralPeriodicExcitationDetail':
        return self._Cast_GeneralPeriodicExcitationDetail(self)
