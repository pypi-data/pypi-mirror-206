"""_93.py

AngleInputComponent
"""
from mastapy._internal import constructor
from mastapy.nodal_analysis.varying_input_components import _92
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ANGLE_INPUT_COMPONENT = python_net_import('SMT.MastaAPI.NodalAnalysis.VaryingInputComponents', 'AngleInputComponent')


__docformat__ = 'restructuredtext en'
__all__ = ('AngleInputComponent',)


class AngleInputComponent(_92.AbstractVaryingInputComponent):
    """AngleInputComponent

    This is a mastapy class.
    """

    TYPE = _ANGLE_INPUT_COMPONENT

    class _Cast_AngleInputComponent:
        """Special nested class for casting AngleInputComponent to subclasses."""

        def __init__(self, parent: 'AngleInputComponent'):
            self._parent = parent

        @property
        def abstract_varying_input_component(self):
            return self._parent._cast(_92.AbstractVaryingInputComponent)

        @property
        def angle_input_component(self) -> 'AngleInputComponent':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AngleInputComponent.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def angle(self) -> 'float':
        """float: 'Angle' is the original name of this property."""

        temp = self.wrapped.Angle

        if temp is None:
            return 0.0

        return temp

    @angle.setter
    def angle(self, value: 'float'):
        self.wrapped.Angle = float(value) if value else 0.0

    @property
    def cast_to(self) -> 'AngleInputComponent._Cast_AngleInputComponent':
        return self._Cast_AngleInputComponent(self)
