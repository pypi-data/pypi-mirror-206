"""_1531.py

Optimisable
"""
from mastapy.math_utility.optimisation import _1527
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_OPTIMISABLE = python_net_import('SMT.MastaAPI.MathUtility.Optimisation', 'Optimisable')


__docformat__ = 'restructuredtext en'
__all__ = ('Optimisable',)


class Optimisable(_1527.AbstractOptimisable):
    """Optimisable

    This is a mastapy class.
    """

    TYPE = _OPTIMISABLE

    class _Cast_Optimisable:
        """Special nested class for casting Optimisable to subclasses."""

        def __init__(self, parent: 'Optimisable'):
            self._parent = parent

        @property
        def abstract_optimisable(self):
            return self._parent._cast(_1527.AbstractOptimisable)

        @property
        def optimisable(self) -> 'Optimisable':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'Optimisable.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'Optimisable._Cast_Optimisable':
        return self._Cast_Optimisable(self)
