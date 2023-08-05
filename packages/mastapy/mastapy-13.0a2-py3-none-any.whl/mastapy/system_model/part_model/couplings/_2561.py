"""_2561.py

ConceptCouplingHalf
"""
from mastapy.system_model.part_model.couplings import _2563
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_COUPLING_HALF = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Couplings', 'ConceptCouplingHalf')


__docformat__ = 'restructuredtext en'
__all__ = ('ConceptCouplingHalf',)


class ConceptCouplingHalf(_2563.CouplingHalf):
    """ConceptCouplingHalf

    This is a mastapy class.
    """

    TYPE = _CONCEPT_COUPLING_HALF

    class _Cast_ConceptCouplingHalf:
        """Special nested class for casting ConceptCouplingHalf to subclasses."""

        def __init__(self, parent: 'ConceptCouplingHalf'):
            self._parent = parent

        @property
        def coupling_half(self):
            return self._parent._cast(_2563.CouplingHalf)

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
        def concept_coupling_half(self) -> 'ConceptCouplingHalf':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConceptCouplingHalf.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'ConceptCouplingHalf._Cast_ConceptCouplingHalf':
        return self._Cast_ConceptCouplingHalf(self)
