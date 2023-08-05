"""_2459.py

VirtualComponent
"""
from mastapy.system_model.part_model import _2444
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_VIRTUAL_COMPONENT = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'VirtualComponent')


__docformat__ = 'restructuredtext en'
__all__ = ('VirtualComponent',)


class VirtualComponent(_2444.MountableComponent):
    """VirtualComponent

    This is a mastapy class.
    """

    TYPE = _VIRTUAL_COMPONENT

    class _Cast_VirtualComponent:
        """Special nested class for casting VirtualComponent to subclasses."""

        def __init__(self, parent: 'VirtualComponent'):
            self._parent = parent

        @property
        def mountable_component(self):
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
        def mass_disc(self):
            from mastapy.system_model.part_model import _2442
            
            return self._parent._cast(_2442.MassDisc)

        @property
        def measurement_component(self):
            from mastapy.system_model.part_model import _2443
            
            return self._parent._cast(_2443.MeasurementComponent)

        @property
        def point_load(self):
            from mastapy.system_model.part_model import _2451
            
            return self._parent._cast(_2451.PointLoad)

        @property
        def power_load(self):
            from mastapy.system_model.part_model import _2452
            
            return self._parent._cast(_2452.PowerLoad)

        @property
        def unbalanced_mass(self):
            from mastapy.system_model.part_model import _2457
            
            return self._parent._cast(_2457.UnbalancedMass)

        @property
        def virtual_component(self) -> 'VirtualComponent':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'VirtualComponent.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'VirtualComponent._Cast_VirtualComponent':
        return self._Cast_VirtualComponent(self)
