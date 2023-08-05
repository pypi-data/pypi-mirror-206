"""_2568.py

PartToPartShearCouplingHalf
"""
from mastapy.system_model.part_model.couplings import _2563
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_TO_PART_SHEAR_COUPLING_HALF = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Couplings', 'PartToPartShearCouplingHalf')


__docformat__ = 'restructuredtext en'
__all__ = ('PartToPartShearCouplingHalf',)


class PartToPartShearCouplingHalf(_2563.CouplingHalf):
    """PartToPartShearCouplingHalf

    This is a mastapy class.
    """

    TYPE = _PART_TO_PART_SHEAR_COUPLING_HALF

    class _Cast_PartToPartShearCouplingHalf:
        """Special nested class for casting PartToPartShearCouplingHalf to subclasses."""

        def __init__(self, parent: 'PartToPartShearCouplingHalf'):
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
        def part_to_part_shear_coupling_half(self) -> 'PartToPartShearCouplingHalf':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'PartToPartShearCouplingHalf.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'PartToPartShearCouplingHalf._Cast_PartToPartShearCouplingHalf':
        return self._Cast_PartToPartShearCouplingHalf(self)
