"""_1892.py

InnerSupportTolerance
"""
from mastapy.bearings.tolerances import _1907
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INNER_SUPPORT_TOLERANCE = python_net_import('SMT.MastaAPI.Bearings.Tolerances', 'InnerSupportTolerance')


__docformat__ = 'restructuredtext en'
__all__ = ('InnerSupportTolerance',)


class InnerSupportTolerance(_1907.SupportTolerance):
    """InnerSupportTolerance

    This is a mastapy class.
    """

    TYPE = _INNER_SUPPORT_TOLERANCE

    class _Cast_InnerSupportTolerance:
        """Special nested class for casting InnerSupportTolerance to subclasses."""

        def __init__(self, parent: 'InnerSupportTolerance'):
            self._parent = parent

        @property
        def support_tolerance(self):
            return self._parent._cast(_1907.SupportTolerance)

        @property
        def interference_tolerance(self):
            from mastapy.bearings.tolerances import _1894
            
            return self._parent._cast(_1894.InterferenceTolerance)

        @property
        def bearing_connection_component(self):
            from mastapy.bearings.tolerances import _1886
            
            return self._parent._cast(_1886.BearingConnectionComponent)

        @property
        def inner_support_tolerance(self) -> 'InnerSupportTolerance':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'InnerSupportTolerance.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'InnerSupportTolerance._Cast_InnerSupportTolerance':
        return self._Cast_InnerSupportTolerance(self)
