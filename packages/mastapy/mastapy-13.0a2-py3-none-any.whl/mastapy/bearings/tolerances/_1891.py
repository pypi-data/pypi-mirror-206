"""_1891.py

InnerRingTolerance
"""
from mastapy.bearings.tolerances import _1902
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INNER_RING_TOLERANCE = python_net_import('SMT.MastaAPI.Bearings.Tolerances', 'InnerRingTolerance')


__docformat__ = 'restructuredtext en'
__all__ = ('InnerRingTolerance',)


class InnerRingTolerance(_1902.RingTolerance):
    """InnerRingTolerance

    This is a mastapy class.
    """

    TYPE = _INNER_RING_TOLERANCE

    class _Cast_InnerRingTolerance:
        """Special nested class for casting InnerRingTolerance to subclasses."""

        def __init__(self, parent: 'InnerRingTolerance'):
            self._parent = parent

        @property
        def ring_tolerance(self):
            return self._parent._cast(_1902.RingTolerance)

        @property
        def interference_tolerance(self):
            from mastapy.bearings.tolerances import _1894
            
            return self._parent._cast(_1894.InterferenceTolerance)

        @property
        def bearing_connection_component(self):
            from mastapy.bearings.tolerances import _1886
            
            return self._parent._cast(_1886.BearingConnectionComponent)

        @property
        def inner_ring_tolerance(self) -> 'InnerRingTolerance':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'InnerRingTolerance.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'InnerRingTolerance._Cast_InnerRingTolerance':
        return self._Cast_InnerRingTolerance(self)
