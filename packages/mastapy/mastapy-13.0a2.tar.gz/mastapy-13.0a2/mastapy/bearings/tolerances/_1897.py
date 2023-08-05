"""_1897.py

OuterRingTolerance
"""
from mastapy.bearings.tolerances import _1902
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_OUTER_RING_TOLERANCE = python_net_import('SMT.MastaAPI.Bearings.Tolerances', 'OuterRingTolerance')


__docformat__ = 'restructuredtext en'
__all__ = ('OuterRingTolerance',)


class OuterRingTolerance(_1902.RingTolerance):
    """OuterRingTolerance

    This is a mastapy class.
    """

    TYPE = _OUTER_RING_TOLERANCE

    class _Cast_OuterRingTolerance:
        """Special nested class for casting OuterRingTolerance to subclasses."""

        def __init__(self, parent: 'OuterRingTolerance'):
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
        def outer_ring_tolerance(self) -> 'OuterRingTolerance':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'OuterRingTolerance.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'OuterRingTolerance._Cast_OuterRingTolerance':
        return self._Cast_OuterRingTolerance(self)
