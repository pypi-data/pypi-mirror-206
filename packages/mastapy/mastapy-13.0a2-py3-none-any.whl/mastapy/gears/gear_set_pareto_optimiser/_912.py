"""_912.py

MicroGeometryDesignSpaceSearchCandidate
"""
from mastapy.gears.ltca.cylindrical import _855
from mastapy._internal import constructor
from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1101
from mastapy.gears.gear_set_pareto_optimiser import _902
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MICRO_GEOMETRY_DESIGN_SPACE_SEARCH_CANDIDATE = python_net_import('SMT.MastaAPI.Gears.GearSetParetoOptimiser', 'MicroGeometryDesignSpaceSearchCandidate')


__docformat__ = 'restructuredtext en'
__all__ = ('MicroGeometryDesignSpaceSearchCandidate',)


class MicroGeometryDesignSpaceSearchCandidate(_902.DesignSpaceSearchCandidateBase['_855.CylindricalGearSetLoadDistributionAnalysis', 'MicroGeometryDesignSpaceSearchCandidate']):
    """MicroGeometryDesignSpaceSearchCandidate

    This is a mastapy class.
    """

    TYPE = _MICRO_GEOMETRY_DESIGN_SPACE_SEARCH_CANDIDATE

    class _Cast_MicroGeometryDesignSpaceSearchCandidate:
        """Special nested class for casting MicroGeometryDesignSpaceSearchCandidate to subclasses."""

        def __init__(self, parent: 'MicroGeometryDesignSpaceSearchCandidate'):
            self._parent = parent

        @property
        def design_space_search_candidate_base(self):
            from mastapy.gears.gear_set_pareto_optimiser import _912
            
            return self._parent._cast(_902.DesignSpaceSearchCandidateBase)

        @property
        def micro_geometry_design_space_search_candidate(self) -> 'MicroGeometryDesignSpaceSearchCandidate':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'MicroGeometryDesignSpaceSearchCandidate.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def candidate(self) -> '_855.CylindricalGearSetLoadDistributionAnalysis':
        """CylindricalGearSetLoadDistributionAnalysis: 'Candidate' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Candidate

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def candidate_for_slider(self) -> '_1101.CylindricalGearSetMicroGeometry':
        """CylindricalGearSetMicroGeometry: 'CandidateForSlider' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CandidateForSlider

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    def add_design(self):
        """ 'AddDesign' is the original name of this method."""

        self.wrapped.AddDesign()

    @property
    def cast_to(self) -> 'MicroGeometryDesignSpaceSearchCandidate._Cast_MicroGeometryDesignSpaceSearchCandidate':
        return self._Cast_MicroGeometryDesignSpaceSearchCandidate(self)
