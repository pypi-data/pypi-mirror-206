"""_208.py

ElementPropertiesMass
"""
from mastapy.math_utility import _1505
from mastapy._internal import constructor, conversion
from mastapy._math.vector_3d import Vector3D
from mastapy.nodal_analysis.dev_tools_analyses.full_fe_reporting import _205
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ELEMENT_PROPERTIES_MASS = python_net_import('SMT.MastaAPI.NodalAnalysis.DevToolsAnalyses.FullFEReporting', 'ElementPropertiesMass')


__docformat__ = 'restructuredtext en'
__all__ = ('ElementPropertiesMass',)


class ElementPropertiesMass(_205.ElementPropertiesBase):
    """ElementPropertiesMass

    This is a mastapy class.
    """

    TYPE = _ELEMENT_PROPERTIES_MASS

    class _Cast_ElementPropertiesMass:
        """Special nested class for casting ElementPropertiesMass to subclasses."""

        def __init__(self, parent: 'ElementPropertiesMass'):
            self._parent = parent

        @property
        def element_properties_base(self):
            return self._parent._cast(_205.ElementPropertiesBase)

        @property
        def element_properties_mass(self) -> 'ElementPropertiesMass':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ElementPropertiesMass.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def inertia(self) -> '_1505.InertiaTensor':
        """InertiaTensor: 'Inertia' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Inertia

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def mass(self) -> 'Vector3D':
        """Vector3D: 'Mass' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Mass

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)
        return value

    @property
    def cast_to(self) -> 'ElementPropertiesMass._Cast_ElementPropertiesMass':
        return self._Cast_ElementPropertiesMass(self)
