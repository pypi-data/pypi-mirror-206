"""_2567.py

PartToPartShearCoupling
"""
from mastapy.system_model.connections_and_sockets.couplings import _2329
from mastapy._internal import constructor
from mastapy.system_model.part_model.couplings import _2562
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_TO_PART_SHEAR_COUPLING = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Couplings', 'PartToPartShearCoupling')


__docformat__ = 'restructuredtext en'
__all__ = ('PartToPartShearCoupling',)


class PartToPartShearCoupling(_2562.Coupling):
    """PartToPartShearCoupling

    This is a mastapy class.
    """

    TYPE = _PART_TO_PART_SHEAR_COUPLING

    class _Cast_PartToPartShearCoupling:
        """Special nested class for casting PartToPartShearCoupling to subclasses."""

        def __init__(self, parent: 'PartToPartShearCoupling'):
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
        def part_to_part_shear_coupling(self) -> 'PartToPartShearCoupling':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'PartToPartShearCoupling.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def part_to_part_shear_coupling_connection(self) -> '_2329.PartToPartShearCouplingConnection':
        """PartToPartShearCouplingConnection: 'PartToPartShearCouplingConnection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PartToPartShearCouplingConnection

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'PartToPartShearCoupling._Cast_PartToPartShearCoupling':
        return self._Cast_PartToPartShearCoupling(self)
