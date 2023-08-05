"""_1.py

Initialiser
"""
from mastapy._internal import constructor
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INITIALISER = python_net_import('SMT.MastaAPI', 'Initialiser')


__docformat__ = 'restructuredtext en'
__all__ = ('Initialiser',)


class Initialiser:
    """Initialiser

    This is a mastapy class.
    """

    TYPE = _INITIALISER

    class _Cast_Initialiser:
        """Special nested class for casting Initialiser to subclasses."""

        def __init__(self, parent: 'Initialiser'):
            self._parent = parent

        @property
        def initialiser(self) -> 'Initialiser':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'Initialiser.TYPE'):
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

    def initialise_api_access(self, installation_directory: 'str'):
        """ 'InitialiseApiAccess' is the original name of this method.

        Args:
            installation_directory (str)
        """

        installation_directory = str(installation_directory)
        self.wrapped.InitialiseApiAccess(installation_directory if installation_directory else '')

    @property
    def cast_to(self) -> 'Initialiser._Cast_Initialiser':
        return self._Cast_Initialiser(self)
