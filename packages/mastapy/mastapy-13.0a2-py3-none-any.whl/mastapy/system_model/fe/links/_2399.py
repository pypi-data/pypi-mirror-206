"""_2399.py

ElectricMachineStatorFELink
"""
from mastapy.system_model.fe import _2355
from mastapy._internal import constructor
from mastapy.system_model.fe.links import _2405
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ELECTRIC_MACHINE_STATOR_FE_LINK = python_net_import('SMT.MastaAPI.SystemModel.FE.Links', 'ElectricMachineStatorFELink')


__docformat__ = 'restructuredtext en'
__all__ = ('ElectricMachineStatorFELink',)


class ElectricMachineStatorFELink(_2405.MultiNodeFELink):
    """ElectricMachineStatorFELink

    This is a mastapy class.
    """

    TYPE = _ELECTRIC_MACHINE_STATOR_FE_LINK

    class _Cast_ElectricMachineStatorFELink:
        """Special nested class for casting ElectricMachineStatorFELink to subclasses."""

        def __init__(self, parent: 'ElectricMachineStatorFELink'):
            self._parent = parent

        @property
        def multi_node_fe_link(self):
            return self._parent._cast(_2405.MultiNodeFELink)

        @property
        def fe_link(self):
            from mastapy.system_model.fe.links import _2398
            
            return self._parent._cast(_2398.FELink)

        @property
        def electric_machine_stator_fe_link(self) -> 'ElectricMachineStatorFELink':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ElectricMachineStatorFELink.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def electric_machine_dynamic_load_data(self) -> '_2355.ElectricMachineDynamicLoadData':
        """ElectricMachineDynamicLoadData: 'ElectricMachineDynamicLoadData' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ElectricMachineDynamicLoadData

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'ElectricMachineStatorFELink._Cast_ElectricMachineStatorFELink':
        return self._Cast_ElectricMachineStatorFELink(self)
