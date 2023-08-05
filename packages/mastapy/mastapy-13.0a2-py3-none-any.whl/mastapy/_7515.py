"""_7515.py

MarshalByRefObjectPermanent
"""
from mastapy._internal import constructor
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MARSHAL_BY_REF_OBJECT_PERMANENT = python_net_import('SMT.MastaAPIUtility', 'MarshalByRefObjectPermanent')


__docformat__ = 'restructuredtext en'
__all__ = ('MarshalByRefObjectPermanent',)


class MarshalByRefObjectPermanent:
    """MarshalByRefObjectPermanent

    This is a mastapy class.
    """

    TYPE = _MARSHAL_BY_REF_OBJECT_PERMANENT

    class _Cast_MarshalByRefObjectPermanent:
        """Special nested class for casting MarshalByRefObjectPermanent to subclasses."""

        def __init__(self, parent: 'MarshalByRefObjectPermanent'):
            self._parent = parent

        @property
        def marshal_by_ref_object_permanent(self) -> 'MarshalByRefObjectPermanent':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'MarshalByRefObjectPermanent.TYPE'):
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

    def initialize_lifetime_service(self) -> 'object':
        """ 'InitializeLifetimeService' is the original name of this method.

        Returns:
            object
        """

        method_result = self.wrapped.InitializeLifetimeService()
        return method_result

    @property
    def cast_to(self) -> 'MarshalByRefObjectPermanent._Cast_MarshalByRefObjectPermanent':
        return self._Cast_MarshalByRefObjectPermanent(self)
