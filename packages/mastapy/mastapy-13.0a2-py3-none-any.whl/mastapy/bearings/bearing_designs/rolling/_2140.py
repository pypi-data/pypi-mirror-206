"""_2140.py

GeometricConstants
"""
from mastapy.bearings.bearing_designs.rolling import _2141, _2142
from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEOMETRIC_CONSTANTS = python_net_import('SMT.MastaAPI.Bearings.BearingDesigns.Rolling', 'GeometricConstants')


__docformat__ = 'restructuredtext en'
__all__ = ('GeometricConstants',)


class GeometricConstants(_0.APIBase):
    """GeometricConstants

    This is a mastapy class.
    """

    TYPE = _GEOMETRIC_CONSTANTS

    class _Cast_GeometricConstants:
        """Special nested class for casting GeometricConstants to subclasses."""

        def __init__(self, parent: 'GeometricConstants'):
            self._parent = parent

        @property
        def geometric_constants(self) -> 'GeometricConstants':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GeometricConstants.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def geometric_constants_for_rolling_frictional_moments(self) -> '_2141.GeometricConstantsForRollingFrictionalMoments':
        """GeometricConstantsForRollingFrictionalMoments: 'GeometricConstantsForRollingFrictionalMoments' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GeometricConstantsForRollingFrictionalMoments

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def geometric_constants_for_sliding_frictional_moments(self) -> '_2142.GeometricConstantsForSlidingFrictionalMoments':
        """GeometricConstantsForSlidingFrictionalMoments: 'GeometricConstantsForSlidingFrictionalMoments' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GeometricConstantsForSlidingFrictionalMoments

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'GeometricConstants._Cast_GeometricConstants':
        return self._Cast_GeometricConstants(self)
