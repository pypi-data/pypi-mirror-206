"""_98.py

VelocityInputComponent
"""
from mastapy._internal import constructor
from mastapy.nodal_analysis.varying_input_components import _92
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_VELOCITY_INPUT_COMPONENT = python_net_import('SMT.MastaAPI.NodalAnalysis.VaryingInputComponents', 'VelocityInputComponent')


__docformat__ = 'restructuredtext en'
__all__ = ('VelocityInputComponent',)


class VelocityInputComponent(_92.AbstractVaryingInputComponent):
    """VelocityInputComponent

    This is a mastapy class.
    """

    TYPE = _VELOCITY_INPUT_COMPONENT

    class _Cast_VelocityInputComponent:
        """Special nested class for casting VelocityInputComponent to subclasses."""

        def __init__(self, parent: 'VelocityInputComponent'):
            self._parent = parent

        @property
        def abstract_varying_input_component(self):
            return self._parent._cast(_92.AbstractVaryingInputComponent)

        @property
        def velocity_input_component(self) -> 'VelocityInputComponent':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'VelocityInputComponent.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def velocity(self) -> 'float':
        """float: 'Velocity' is the original name of this property."""

        temp = self.wrapped.Velocity

        if temp is None:
            return 0.0

        return temp

    @velocity.setter
    def velocity(self, value: 'float'):
        self.wrapped.Velocity = float(value) if value else 0.0

    @property
    def cast_to(self) -> 'VelocityInputComponent._Cast_VelocityInputComponent':
        return self._Cast_VelocityInputComponent(self)
