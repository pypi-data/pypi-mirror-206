"""_211.py

ElementPropertiesSolid
"""
from mastapy.nodal_analysis.dev_tools_analyses.full_fe_reporting import _213
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ELEMENT_PROPERTIES_SOLID = python_net_import('SMT.MastaAPI.NodalAnalysis.DevToolsAnalyses.FullFEReporting', 'ElementPropertiesSolid')


__docformat__ = 'restructuredtext en'
__all__ = ('ElementPropertiesSolid',)


class ElementPropertiesSolid(_213.ElementPropertiesWithMaterial):
    """ElementPropertiesSolid

    This is a mastapy class.
    """

    TYPE = _ELEMENT_PROPERTIES_SOLID

    class _Cast_ElementPropertiesSolid:
        """Special nested class for casting ElementPropertiesSolid to subclasses."""

        def __init__(self, parent: 'ElementPropertiesSolid'):
            self._parent = parent

        @property
        def element_properties_with_material(self):
            return self._parent._cast(_213.ElementPropertiesWithMaterial)

        @property
        def element_properties_base(self):
            from mastapy.nodal_analysis.dev_tools_analyses.full_fe_reporting import _205
            
            return self._parent._cast(_205.ElementPropertiesBase)

        @property
        def element_properties_solid(self) -> 'ElementPropertiesSolid':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ElementPropertiesSolid.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'ElementPropertiesSolid._Cast_ElementPropertiesSolid':
        return self._Cast_ElementPropertiesSolid(self)
