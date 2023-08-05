"""_2579.py

SpringDamper
"""
from mastapy.system_model.connections_and_sockets.couplings import _2331
from mastapy._internal import constructor
from mastapy.system_model.part_model.couplings import _2562
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPRING_DAMPER = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Couplings', 'SpringDamper')


__docformat__ = 'restructuredtext en'
__all__ = ('SpringDamper',)


class SpringDamper(_2562.Coupling):
    """SpringDamper

    This is a mastapy class.
    """

    TYPE = _SPRING_DAMPER

    class _Cast_SpringDamper:
        """Special nested class for casting SpringDamper to subclasses."""

        def __init__(self, parent: 'SpringDamper'):
            self._parent = parent

        @property
        def coupling(self):
            return self._parent._cast(_2562.Coupling)

        @property
        def specialised_assembly(self):
            from mastapy.system_model.part_model import _2456
            
            return self._parent._cast(_2456.SpecialisedAssembly)

        @property
        def abstract_assembly(self):
            from mastapy.system_model.part_model import _2414
            
            return self._parent._cast(_2414.AbstractAssembly)

        @property
        def part(self):
            from mastapy.system_model.part_model import _2448
            
            return self._parent._cast(_2448.Part)

        @property
        def design_entity(self):
            from mastapy.system_model import _2188
            
            return self._parent._cast(_2188.DesignEntity)

        @property
        def spring_damper(self) -> 'SpringDamper':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'SpringDamper.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection(self) -> '_2331.SpringDamperConnection':
        """SpringDamperConnection: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Connection

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'SpringDamper._Cast_SpringDamper':
        return self._Cast_SpringDamper(self)
