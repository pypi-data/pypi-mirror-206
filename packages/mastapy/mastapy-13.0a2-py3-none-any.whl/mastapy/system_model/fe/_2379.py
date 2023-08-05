"""_2379.py

MaterialPropertiesWithSelection
"""
from mastapy.nodal_analysis.dev_tools_analyses.full_fe_reporting import _214
from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MATERIAL_PROPERTIES_WITH_SELECTION = python_net_import('SMT.MastaAPI.SystemModel.FE', 'MaterialPropertiesWithSelection')


__docformat__ = 'restructuredtext en'
__all__ = ('MaterialPropertiesWithSelection',)


class MaterialPropertiesWithSelection(_0.APIBase):
    """MaterialPropertiesWithSelection

    This is a mastapy class.
    """

    TYPE = _MATERIAL_PROPERTIES_WITH_SELECTION

    class _Cast_MaterialPropertiesWithSelection:
        """Special nested class for casting MaterialPropertiesWithSelection to subclasses."""

        def __init__(self, parent: 'MaterialPropertiesWithSelection'):
            self._parent = parent

        @property
        def material_properties_with_selection(self) -> 'MaterialPropertiesWithSelection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'MaterialPropertiesWithSelection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def material_properties(self) -> '_214.MaterialPropertiesReporting':
        """MaterialPropertiesReporting: 'MaterialProperties' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaterialProperties

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    def select_nodes(self):
        """ 'SelectNodes' is the original name of this method."""

        self.wrapped.SelectNodes()

    @property
    def cast_to(self) -> 'MaterialPropertiesWithSelection._Cast_MaterialPropertiesWithSelection':
        return self._Cast_MaterialPropertiesWithSelection(self)
