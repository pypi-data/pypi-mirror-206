"""_1549.py

ForceAndDisplacementResults
"""
from mastapy.math_utility.measured_vectors import _1553, _1548
from mastapy._internal import constructor
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FORCE_AND_DISPLACEMENT_RESULTS = python_net_import('SMT.MastaAPI.MathUtility.MeasuredVectors', 'ForceAndDisplacementResults')


__docformat__ = 'restructuredtext en'
__all__ = ('ForceAndDisplacementResults',)


class ForceAndDisplacementResults(_1548.AbstractForceAndDisplacementResults):
    """ForceAndDisplacementResults

    This is a mastapy class.
    """

    TYPE = _FORCE_AND_DISPLACEMENT_RESULTS

    class _Cast_ForceAndDisplacementResults:
        """Special nested class for casting ForceAndDisplacementResults to subclasses."""

        def __init__(self, parent: 'ForceAndDisplacementResults'):
            self._parent = parent

        @property
        def abstract_force_and_displacement_results(self):
            return self._parent._cast(_1548.AbstractForceAndDisplacementResults)

        @property
        def force_and_displacement_results(self) -> 'ForceAndDisplacementResults':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ForceAndDisplacementResults.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def displacement(self) -> '_1553.VectorWithLinearAndAngularComponents':
        """VectorWithLinearAndAngularComponents: 'Displacement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Displacement

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'ForceAndDisplacementResults._Cast_ForceAndDisplacementResults':
        return self._Cast_ForceAndDisplacementResults(self)
