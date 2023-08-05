"""_2443.py

MeasurementComponent
"""
from mastapy.system_model.part_model import _2459
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MEASUREMENT_COMPONENT = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'MeasurementComponent')


__docformat__ = 'restructuredtext en'
__all__ = ('MeasurementComponent',)


class MeasurementComponent(_2459.VirtualComponent):
    """MeasurementComponent

    This is a mastapy class.
    """

    TYPE = _MEASUREMENT_COMPONENT

    class _Cast_MeasurementComponent:
        """Special nested class for casting MeasurementComponent to subclasses."""

        def __init__(self, parent: 'MeasurementComponent'):
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
        def measurement_component(self) -> 'MeasurementComponent':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'MeasurementComponent.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'MeasurementComponent._Cast_MeasurementComponent':
        return self._Cast_MeasurementComponent(self)
