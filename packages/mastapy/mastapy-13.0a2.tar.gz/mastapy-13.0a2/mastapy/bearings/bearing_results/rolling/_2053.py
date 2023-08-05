"""_2053.py

RingForceAndDisplacement
"""
from mastapy._internal import constructor
from mastapy.math_utility.measured_vectors import _1553
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_RING_FORCE_AND_DISPLACEMENT = python_net_import('SMT.MastaAPI.Bearings.BearingResults.Rolling', 'RingForceAndDisplacement')


__docformat__ = 'restructuredtext en'
__all__ = ('RingForceAndDisplacement',)


class RingForceAndDisplacement(_0.APIBase):
    """RingForceAndDisplacement

    This is a mastapy class.
    """

    TYPE = _RING_FORCE_AND_DISPLACEMENT

    class _Cast_RingForceAndDisplacement:
        """Special nested class for casting RingForceAndDisplacement to subclasses."""

        def __init__(self, parent: 'RingForceAndDisplacement'):
            self._parent = parent

        @property
        def ring_force_and_displacement(self) -> 'RingForceAndDisplacement':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'RingForceAndDisplacement.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def magnitude_of_misalignment_normal_to_load_direction(self) -> 'float':
        """float: 'MagnitudeOfMisalignmentNormalToLoadDirection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MagnitudeOfMisalignmentNormalToLoadDirection

        if temp is None:
            return 0.0

        return temp

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
    def cast_to(self) -> 'RingForceAndDisplacement._Cast_RingForceAndDisplacement':
        return self._Cast_RingForceAndDisplacement(self)
