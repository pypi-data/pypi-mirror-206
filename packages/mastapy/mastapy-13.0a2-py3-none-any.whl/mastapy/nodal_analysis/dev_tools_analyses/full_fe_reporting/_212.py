"""_212.py

ElementPropertiesSpringDashpot
"""
from mastapy._internal import constructor, conversion
from mastapy._math.vector_3d import Vector3D
from mastapy.nodal_analysis.dev_tools_analyses.full_fe_reporting import _205
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ELEMENT_PROPERTIES_SPRING_DASHPOT = python_net_import('SMT.MastaAPI.NodalAnalysis.DevToolsAnalyses.FullFEReporting', 'ElementPropertiesSpringDashpot')


__docformat__ = 'restructuredtext en'
__all__ = ('ElementPropertiesSpringDashpot',)


class ElementPropertiesSpringDashpot(_205.ElementPropertiesBase):
    """ElementPropertiesSpringDashpot

    This is a mastapy class.
    """

    TYPE = _ELEMENT_PROPERTIES_SPRING_DASHPOT

    class _Cast_ElementPropertiesSpringDashpot:
        """Special nested class for casting ElementPropertiesSpringDashpot to subclasses."""

        def __init__(self, parent: 'ElementPropertiesSpringDashpot'):
            self._parent = parent

        @property
        def element_properties_base(self):
            return self._parent._cast(_205.ElementPropertiesBase)

        @property
        def element_properties_spring_dashpot(self) -> 'ElementPropertiesSpringDashpot':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ElementPropertiesSpringDashpot.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def degree_of_freedom_1(self) -> 'int':
        """int: 'DegreeOfFreedom1' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DegreeOfFreedom1

        if temp is None:
            return 0

        return temp

    @property
    def degree_of_freedom_2(self) -> 'int':
        """int: 'DegreeOfFreedom2' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DegreeOfFreedom2

        if temp is None:
            return 0

        return temp

    @property
    def stiffness(self) -> 'float':
        """float: 'Stiffness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Stiffness

        if temp is None:
            return 0.0

        return temp

    @property
    def stiffness_matrix_lower_triangle(self) -> 'str':
        """str: 'StiffnessMatrixLowerTriangle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StiffnessMatrixLowerTriangle

        if temp is None:
            return ''

        return temp

    @property
    def stiffness_rotation(self) -> 'Vector3D':
        """Vector3D: 'StiffnessRotation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StiffnessRotation

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)
        return value

    @property
    def stiffness_translation(self) -> 'Vector3D':
        """Vector3D: 'StiffnessTranslation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StiffnessTranslation

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)
        return value

    @property
    def cast_to(self) -> 'ElementPropertiesSpringDashpot._Cast_ElementPropertiesSpringDashpot':
        return self._Cast_ElementPropertiesSpringDashpot(self)
