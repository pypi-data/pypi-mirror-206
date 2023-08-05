"""_7516.py

MarshalByRefObjects
"""
from mastapy._internal import constructor
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MARSHAL_BY_REF_OBJECTS = python_net_import('SMT.MastaAPIUtility', 'MarshalByRefObjects')


__docformat__ = 'restructuredtext en'
__all__ = ('MarshalByRefObjects',)


class MarshalByRefObjects:
    """MarshalByRefObjects

    This is a mastapy class.
    """

    TYPE = _MARSHAL_BY_REF_OBJECTS

    class _Cast_MarshalByRefObjects:
        """Special nested class for casting MarshalByRefObjects to subclasses."""

        def __init__(self, parent: 'MarshalByRefObjects'):
            self._parent = parent

        @property
        def marshal_by_ref_objects(self) -> 'MarshalByRefObjects':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'MarshalByRefObjects.TYPE'):
        self.wrapped = instance_to_wrap
        if not hasattr(self.wrapped, 'reference_count'):
            self.wrapped.reference_count = 0
        self.wrapped.reference_count += 1

    @staticmethod
    def add(item: 'object'):
        """ 'Add' is the original name of this method.

        Args:
            item (object)
        """

        MarshalByRefObjects.TYPE.Add(item)

    @staticmethod
    def remove(item: 'object'):
        """ 'Remove' is the original name of this method.

        Args:
            item (object)
        """

        MarshalByRefObjects.TYPE.Remove(item)

    @staticmethod
    def disconnect(item: 'object'):
        """ 'Disconnect' is the original name of this method.

        Args:
            item (object)
        """

        MarshalByRefObjects.TYPE.Disconnect(item)

    @staticmethod
    def clear():
        """ 'Clear' is the original name of this method."""

        MarshalByRefObjects.TYPE.Clear()

    @property
    def cast_to(self) -> 'MarshalByRefObjects._Cast_MarshalByRefObjects':
        return self._Cast_MarshalByRefObjects(self)
