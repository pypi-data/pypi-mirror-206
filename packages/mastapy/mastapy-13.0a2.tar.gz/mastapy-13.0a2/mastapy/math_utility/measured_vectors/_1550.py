"""_1550.py

ForceResults
"""
from mastapy.math_utility.measured_vectors import _1548
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FORCE_RESULTS = python_net_import('SMT.MastaAPI.MathUtility.MeasuredVectors', 'ForceResults')


__docformat__ = 'restructuredtext en'
__all__ = ('ForceResults',)


class ForceResults(_1548.AbstractForceAndDisplacementResults):
    """ForceResults

    This is a mastapy class.
    """

    TYPE = _FORCE_RESULTS

    class _Cast_ForceResults:
        """Special nested class for casting ForceResults to subclasses."""

        def __init__(self, parent: 'ForceResults'):
            self._parent = parent

        @property
        def abstract_force_and_displacement_results(self):
            return self._parent._cast(_1548.AbstractForceAndDisplacementResults)

        @property
        def force_results(self) -> 'ForceResults':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ForceResults.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'ForceResults._Cast_ForceResults':
        return self._Cast_ForceResults(self)
