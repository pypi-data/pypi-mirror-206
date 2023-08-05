"""_1548.py

AbstractForceAndDisplacementResults
"""
from mastapy._internal import constructor, conversion
from mastapy.math_utility.measured_vectors import _1553
from mastapy._math.vector_3d import Vector3D
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_FORCE_AND_DISPLACEMENT_RESULTS = python_net_import('SMT.MastaAPI.MathUtility.MeasuredVectors', 'AbstractForceAndDisplacementResults')


__docformat__ = 'restructuredtext en'
__all__ = ('AbstractForceAndDisplacementResults',)


class AbstractForceAndDisplacementResults(_0.APIBase):
    """AbstractForceAndDisplacementResults

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_FORCE_AND_DISPLACEMENT_RESULTS

    class _Cast_AbstractForceAndDisplacementResults:
        """Special nested class for casting AbstractForceAndDisplacementResults to subclasses."""

        def __init__(self, parent: 'AbstractForceAndDisplacementResults'):
            self._parent = parent

        @property
        def force_and_displacement_results(self):
            from mastapy.math_utility.measured_vectors import _1549
            
            return self._parent._cast(_1549.ForceAndDisplacementResults)

        @property
        def force_results(self):
            from mastapy.math_utility.measured_vectors import _1550
            
            return self._parent._cast(_1550.ForceResults)

        @property
        def abstract_force_and_displacement_results(self) -> 'AbstractForceAndDisplacementResults':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AbstractForceAndDisplacementResults.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def node(self) -> 'str':
        """str: 'Node' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Node

        if temp is None:
            return ''

        return temp

    @property
    def force(self) -> '_1553.VectorWithLinearAndAngularComponents':
        """VectorWithLinearAndAngularComponents: 'Force' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Force

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def location(self) -> 'Vector3D':
        """Vector3D: 'Location' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Location

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)
        return value

    @property
    def cast_to(self) -> 'AbstractForceAndDisplacementResults._Cast_AbstractForceAndDisplacementResults':
        return self._Cast_AbstractForceAndDisplacementResults(self)
