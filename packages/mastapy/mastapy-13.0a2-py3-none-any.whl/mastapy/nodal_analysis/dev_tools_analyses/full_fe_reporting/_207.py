"""_207.py

ElementPropertiesInterface
"""
from mastapy.nodal_analysis.dev_tools_analyses.full_fe_reporting import _205
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ELEMENT_PROPERTIES_INTERFACE = python_net_import('SMT.MastaAPI.NodalAnalysis.DevToolsAnalyses.FullFEReporting', 'ElementPropertiesInterface')


__docformat__ = 'restructuredtext en'
__all__ = ('ElementPropertiesInterface',)


class ElementPropertiesInterface(_205.ElementPropertiesBase):
    """ElementPropertiesInterface

    This is a mastapy class.
    """

    TYPE = _ELEMENT_PROPERTIES_INTERFACE

    class _Cast_ElementPropertiesInterface:
        """Special nested class for casting ElementPropertiesInterface to subclasses."""

        def __init__(self, parent: 'ElementPropertiesInterface'):
            self._parent = parent

        @property
        def element_properties_base(self):
            return self._parent._cast(_205.ElementPropertiesBase)

        @property
        def element_properties_interface(self) -> 'ElementPropertiesInterface':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ElementPropertiesInterface.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'ElementPropertiesInterface._Cast_ElementPropertiesInterface':
        return self._Cast_ElementPropertiesInterface(self)
