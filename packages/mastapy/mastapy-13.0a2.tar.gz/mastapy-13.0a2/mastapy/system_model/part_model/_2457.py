"""_2457.py

UnbalancedMass
"""
from mastapy._internal import constructor
from mastapy.system_model.part_model import _2459
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_UNBALANCED_MASS = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'UnbalancedMass')


__docformat__ = 'restructuredtext en'
__all__ = ('UnbalancedMass',)


class UnbalancedMass(_2459.VirtualComponent):
    """UnbalancedMass

    This is a mastapy class.
    """

    TYPE = _UNBALANCED_MASS

    class _Cast_UnbalancedMass:
        """Special nested class for casting UnbalancedMass to subclasses."""

        def __init__(self, parent: 'UnbalancedMass'):
            self._parent = parent

        @property
        def virtual_component(self):
            return self._parent._cast(_2459.VirtualComponent)

        @property
        def mountable_component(self):
            from mastapy.system_model.part_model import _2444
            
            return self._parent._cast(_2444.MountableComponent)

        @property
        def component(self):
            from mastapy.system_model.part_model import _2424
            
            return self._parent._cast(_2424.Component)

        @property
        def part(self):
            from mastapy.system_model.part_model import _2448
            
            return self._parent._cast(_2448.Part)

        @property
        def design_entity(self):
            from mastapy.system_model import _2188
            
            return self._parent._cast(_2188.DesignEntity)

        @property
        def unbalanced_mass(self) -> 'UnbalancedMass':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'UnbalancedMass.TYPE'):
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
    def radius(self) -> 'float':
        """float: 'Radius' is the original name of this property."""

        temp = self.wrapped.Radius

        if temp is None:
            return 0.0

        return temp

    @radius.setter
    def radius(self, value: 'float'):
        self.wrapped.Radius = float(value) if value else 0.0

    @property
    def cast_to(self) -> 'UnbalancedMass._Cast_UnbalancedMass':
        return self._Cast_UnbalancedMass(self)
