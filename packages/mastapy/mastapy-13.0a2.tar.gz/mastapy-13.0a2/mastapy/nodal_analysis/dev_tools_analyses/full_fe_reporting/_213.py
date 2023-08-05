"""_213.py

ElementPropertiesWithMaterial
"""
from mastapy._internal.implicit import list_with_selected_item
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor
from mastapy.nodal_analysis.dev_tools_analyses.full_fe_reporting import _205
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ELEMENT_PROPERTIES_WITH_MATERIAL = python_net_import('SMT.MastaAPI.NodalAnalysis.DevToolsAnalyses.FullFEReporting', 'ElementPropertiesWithMaterial')


__docformat__ = 'restructuredtext en'
__all__ = ('ElementPropertiesWithMaterial',)


class ElementPropertiesWithMaterial(_205.ElementPropertiesBase):
    """ElementPropertiesWithMaterial

    This is a mastapy class.
    """

    TYPE = _ELEMENT_PROPERTIES_WITH_MATERIAL

    class _Cast_ElementPropertiesWithMaterial:
        """Special nested class for casting ElementPropertiesWithMaterial to subclasses."""

        def __init__(self, parent: 'ElementPropertiesWithMaterial'):
            self._parent = parent

        @property
        def element_properties_base(self):
            return self._parent._cast(_205.ElementPropertiesBase)

        @property
        def element_properties_beam(self):
            from mastapy.nodal_analysis.dev_tools_analyses.full_fe_reporting import _206
            
            return self._parent._cast(_206.ElementPropertiesBeam)

        @property
        def element_properties_shell(self):
            from mastapy.nodal_analysis.dev_tools_analyses.full_fe_reporting import _210
            
            return self._parent._cast(_210.ElementPropertiesShell)

        @property
        def element_properties_solid(self):
            from mastapy.nodal_analysis.dev_tools_analyses.full_fe_reporting import _211
            
            return self._parent._cast(_211.ElementPropertiesSolid)

        @property
        def element_properties_with_material(self) -> 'ElementPropertiesWithMaterial':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ElementPropertiesWithMaterial.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def material_coordinate_system_id(self) -> 'list_with_selected_item.ListWithSelectedItem_int':
        """list_with_selected_item.ListWithSelectedItem_int: 'MaterialCoordinateSystemID' is the original name of this property."""

        temp = self.wrapped.MaterialCoordinateSystemID

        if temp is None:
            return 0

        return constructor.new_from_mastapy_type(list_with_selected_item.ListWithSelectedItem_int)(temp) if temp is not None else 0

    @material_coordinate_system_id.setter
    def material_coordinate_system_id(self, value: 'list_with_selected_item.ListWithSelectedItem_int.implicit_type()'):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_int.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_int.implicit_type()
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0)
        self.wrapped.MaterialCoordinateSystemID = value

    @property
    def material_id(self) -> 'list_with_selected_item.ListWithSelectedItem_int':
        """list_with_selected_item.ListWithSelectedItem_int: 'MaterialID' is the original name of this property."""

        temp = self.wrapped.MaterialID

        if temp is None:
            return 0

        return constructor.new_from_mastapy_type(list_with_selected_item.ListWithSelectedItem_int)(temp) if temp is not None else 0

    @material_id.setter
    def material_id(self, value: 'list_with_selected_item.ListWithSelectedItem_int.implicit_type()'):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_int.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_int.implicit_type()
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0)
        self.wrapped.MaterialID = value

    @property
    def cast_to(self) -> 'ElementPropertiesWithMaterial._Cast_ElementPropertiesWithMaterial':
        return self._Cast_ElementPropertiesWithMaterial(self)
