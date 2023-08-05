"""_1477.py

Range
"""
from mastapy._internal import constructor
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_RANGE = python_net_import('SMT.MastaAPI.MathUtility', 'Range')


__docformat__ = 'restructuredtext en'
__all__ = ('Range',)


class Range:
    """Range

    This is a mastapy class.
    """

    TYPE = _RANGE

    class _Cast_Range:
        """Special nested class for casting Range to subclasses."""

        def __init__(self, parent: 'Range'):
            self._parent = parent

        @property
        def range(self) -> 'Range':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'Range.TYPE'):
        self.wrapped = instance_to_wrap
        if not hasattr(self.wrapped, 'reference_count'):
            self.wrapped.reference_count = 0
        self.wrapped.reference_count += 1
        self._freeze()

    __frozen = False

    def __setattr__(self, attr, value):
        prop = getattr(self.__class__, attr, None)
        if isinstance(prop, property):
            prop.fset(self, value)
        else:
            if self.__frozen and attr not in self.__dict__:
                raise AttributeError((
                    'Attempted to set unknown '
                    'attribute: \'{}\''.format(attr))) from None

            super().__setattr__(attr, value)

    def __delattr__(self, name):
        raise AttributeError(
            'Cannot delete the attributes of a mastapy object.') from None

    def _freeze(self):
        self.__frozen = True

    def __eq__(self, other: 'Range') -> 'bool':
        """ 'op_Equality' is the original name of this method.

        Args:
            other (mastapy.math_utility.Range)

        Returns:
            bool
        """

        method_result = self.wrapped.op_Equality(self.wrapped, other.wrapped if other else None)
        return method_result

    def __ne__(self, other: 'Range') -> 'bool':
        """ 'op_Inequality' is the original name of this method.

        Args:
            other (mastapy.math_utility.Range)

        Returns:
            bool
        """

        method_result = self.wrapped.op_Inequality(self.wrapped, other.wrapped if other else None)
        return method_result

    def __hash__(self) -> 'int':
        """ 'GetHashCode' is the original name of this method.

        Returns:
            int
        """

        method_result = self.wrapped.GetHashCode()
        return method_result

    @property
    def cast_to(self) -> 'Range._Cast_Range':
        return self._Cast_Range(self)
