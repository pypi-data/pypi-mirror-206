"""_906.py

GearSetOptimiserCandidate
"""
from mastapy.gears.rating import _351
from mastapy._internal import constructor
from mastapy.gears.gear_set_pareto_optimiser import _902
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_SET_OPTIMISER_CANDIDATE = python_net_import('SMT.MastaAPI.Gears.GearSetParetoOptimiser', 'GearSetOptimiserCandidate')


__docformat__ = 'restructuredtext en'
__all__ = ('GearSetOptimiserCandidate',)


class GearSetOptimiserCandidate(_902.DesignSpaceSearchCandidateBase['_351.AbstractGearSetRating', 'GearSetOptimiserCandidate']):
    """GearSetOptimiserCandidate

    This is a mastapy class.
    """

    TYPE = _GEAR_SET_OPTIMISER_CANDIDATE

    class _Cast_GearSetOptimiserCandidate:
        """Special nested class for casting GearSetOptimiserCandidate to subclasses."""

        def __init__(self, parent: 'GearSetOptimiserCandidate'):
            self._parent = parent

        @property
        def design_space_search_candidate_base(self):
            from mastapy.gears.gear_set_pareto_optimiser import _906
            
            return self._parent._cast(_902.DesignSpaceSearchCandidateBase)

        @property
        def gear_set_optimiser_candidate(self) -> 'GearSetOptimiserCandidate':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GearSetOptimiserCandidate.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def candidate(self) -> '_351.AbstractGearSetRating':
        """AbstractGearSetRating: 'Candidate' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Candidate

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    def add_design(self):
        """ 'AddDesign' is the original name of this method."""

        self.wrapped.AddDesign()

    @property
    def cast_to(self) -> 'GearSetOptimiserCandidate._Cast_GearSetOptimiserCandidate':
        return self._Cast_GearSetOptimiserCandidate(self)
