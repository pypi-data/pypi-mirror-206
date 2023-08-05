"""_1527.py

AbstractOptimisable
"""
from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_OPTIMISABLE = python_net_import('SMT.MastaAPI.MathUtility.Optimisation', 'AbstractOptimisable')


__docformat__ = 'restructuredtext en'
__all__ = ('AbstractOptimisable',)


class AbstractOptimisable(_0.APIBase):
    """AbstractOptimisable

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_OPTIMISABLE

    class _Cast_AbstractOptimisable:
        """Special nested class for casting AbstractOptimisable to subclasses."""

        def __init__(self, parent: 'AbstractOptimisable'):
            self._parent = parent

        @property
        def optimisable(self):
            from mastapy.math_utility.optimisation import _1531
            
            return self._parent._cast(_1531.Optimisable)

        @property
        def abstract_optimisable(self) -> 'AbstractOptimisable':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AbstractOptimisable.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def parameter_1(self) -> 'float':
        """float: 'Parameter1' is the original name of this property."""

        temp = self.wrapped.Parameter1

        if temp is None:
            return 0.0

        return temp

    @parameter_1.setter
    def parameter_1(self, value: 'float'):
        self.wrapped.Parameter1 = float(value) if value else 0.0

    @property
    def parameter_2(self) -> 'float':
        """float: 'Parameter2' is the original name of this property."""

        temp = self.wrapped.Parameter2

        if temp is None:
            return 0.0

        return temp

    @parameter_2.setter
    def parameter_2(self, value: 'float'):
        self.wrapped.Parameter2 = float(value) if value else 0.0

    @property
    def cast_to(self) -> 'AbstractOptimisable._Cast_AbstractOptimisable':
        return self._Cast_AbstractOptimisable(self)
