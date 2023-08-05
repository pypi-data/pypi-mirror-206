"""_46.py

AbstractLinearConnectionProperties
"""
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_LINEAR_CONNECTION_PROPERTIES = python_net_import('SMT.MastaAPI.NodalAnalysis', 'AbstractLinearConnectionProperties')


__docformat__ = 'restructuredtext en'
__all__ = ('AbstractLinearConnectionProperties',)


class AbstractLinearConnectionProperties(_0.APIBase):
    """AbstractLinearConnectionProperties

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_LINEAR_CONNECTION_PROPERTIES

    class _Cast_AbstractLinearConnectionProperties:
        """Special nested class for casting AbstractLinearConnectionProperties to subclasses."""

        def __init__(self, parent: 'AbstractLinearConnectionProperties'):
            self._parent = parent

        @property
        def linear_damping_connection_properties(self):
            from mastapy.nodal_analysis import _72
            
            return self._parent._cast(_72.LinearDampingConnectionProperties)

        @property
        def linear_stiffness_properties(self):
            from mastapy.nodal_analysis import _73
            
            return self._parent._cast(_73.LinearStiffnessProperties)

        @property
        def abstract_linear_connection_properties(self) -> 'AbstractLinearConnectionProperties':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AbstractLinearConnectionProperties.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'AbstractLinearConnectionProperties._Cast_AbstractLinearConnectionProperties':
        return self._Cast_AbstractLinearConnectionProperties(self)
