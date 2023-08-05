"""_210.py

ElementPropertiesShell
"""
from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy.fe_tools.vis_tools_global.vis_tools_global_enums import _1231
from mastapy.nodal_analysis.dev_tools_analyses.full_fe_reporting import _213
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ELEMENT_PROPERTIES_SHELL = python_net_import('SMT.MastaAPI.NodalAnalysis.DevToolsAnalyses.FullFEReporting', 'ElementPropertiesShell')


__docformat__ = 'restructuredtext en'
__all__ = ('ElementPropertiesShell',)


class ElementPropertiesShell(_213.ElementPropertiesWithMaterial):
    """ElementPropertiesShell

    This is a mastapy class.
    """

    TYPE = _ELEMENT_PROPERTIES_SHELL

    class _Cast_ElementPropertiesShell:
        """Special nested class for casting ElementPropertiesShell to subclasses."""

        def __init__(self, parent: 'ElementPropertiesShell'):
            self._parent = parent

        @property
        def element_properties_with_material(self):
            return self._parent._cast(_213.ElementPropertiesWithMaterial)

        @property
        def element_properties_base(self):
            from mastapy.nodal_analysis.dev_tools_analyses.full_fe_reporting import _205
            
            return self._parent._cast(_205.ElementPropertiesBase)

        @property
        def element_properties_shell(self) -> 'ElementPropertiesShell':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ElementPropertiesShell.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def effective_shear_ratio(self) -> 'float':
        """float: 'EffectiveShearRatio' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.EffectiveShearRatio

        if temp is None:
            return 0.0

        return temp

    @property
    def layer_thicknesses(self) -> 'str':
        """str: 'LayerThicknesses' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LayerThicknesses

        if temp is None:
            return ''

        return temp

    @property
    def number_of_layers(self) -> 'int':
        """int: 'NumberOfLayers' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NumberOfLayers

        if temp is None:
            return 0

        return temp

    @property
    def thickness(self) -> 'float':
        """float: 'Thickness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Thickness

        if temp is None:
            return 0.0

        return temp

    @property
    def wall_type(self) -> '_1231.ElementPropertiesShellWallType':
        """ElementPropertiesShellWallType: 'WallType' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WallType

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, _1231.ElementPropertiesShellWallType)
        return constructor.new_from_mastapy_type(_1231.ElementPropertiesShellWallType)(value) if value is not None else None

    @property
    def cast_to(self) -> 'ElementPropertiesShell._Cast_ElementPropertiesShell':
        return self._Cast_ElementPropertiesShell(self)
