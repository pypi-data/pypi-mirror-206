"""_206.py

ElementPropertiesBeam
"""
from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy.fe_tools.vis_tools_global.vis_tools_global_enums import _1228
from mastapy.nodal_analysis.dev_tools_analyses.full_fe_reporting import _213
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ELEMENT_PROPERTIES_BEAM = python_net_import('SMT.MastaAPI.NodalAnalysis.DevToolsAnalyses.FullFEReporting', 'ElementPropertiesBeam')


__docformat__ = 'restructuredtext en'
__all__ = ('ElementPropertiesBeam',)


class ElementPropertiesBeam(_213.ElementPropertiesWithMaterial):
    """ElementPropertiesBeam

    This is a mastapy class.
    """

    TYPE = _ELEMENT_PROPERTIES_BEAM

    class _Cast_ElementPropertiesBeam:
        """Special nested class for casting ElementPropertiesBeam to subclasses."""

        def __init__(self, parent: 'ElementPropertiesBeam'):
            self._parent = parent

        @property
        def element_properties_with_material(self):
            return self._parent._cast(_213.ElementPropertiesWithMaterial)

        @property
        def element_properties_base(self):
            from mastapy.nodal_analysis.dev_tools_analyses.full_fe_reporting import _205
            
            return self._parent._cast(_205.ElementPropertiesBase)

        @property
        def element_properties_beam(self) -> 'ElementPropertiesBeam':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ElementPropertiesBeam.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def section_dimensions(self) -> 'str':
        """str: 'SectionDimensions' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SectionDimensions

        if temp is None:
            return ''

        return temp

    @property
    def section_type(self) -> '_1228.BeamSectionType':
        """BeamSectionType: 'SectionType' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SectionType

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, _1228.BeamSectionType)
        return constructor.new_from_mastapy_type(_1228.BeamSectionType)(value) if value is not None else None

    @property
    def cast_to(self) -> 'ElementPropertiesBeam._Cast_ElementPropertiesBeam':
        return self._Cast_ElementPropertiesBeam(self)
