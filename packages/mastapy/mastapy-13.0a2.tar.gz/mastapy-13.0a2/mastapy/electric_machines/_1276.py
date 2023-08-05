"""_1276.py

NonCADElectricMachineDetail
"""
from mastapy.electric_machines import _1289, _1254
from mastapy._internal import constructor
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_NON_CAD_ELECTRIC_MACHINE_DETAIL = python_net_import('SMT.MastaAPI.ElectricMachines', 'NonCADElectricMachineDetail')


__docformat__ = 'restructuredtext en'
__all__ = ('NonCADElectricMachineDetail',)


class NonCADElectricMachineDetail(_1254.ElectricMachineDetail):
    """NonCADElectricMachineDetail

    This is a mastapy class.
    """

    TYPE = _NON_CAD_ELECTRIC_MACHINE_DETAIL

    class _Cast_NonCADElectricMachineDetail:
        """Special nested class for casting NonCADElectricMachineDetail to subclasses."""

        def __init__(self, parent: 'NonCADElectricMachineDetail'):
            self._parent = parent

        @property
        def electric_machine_detail(self):
            return self._parent._cast(_1254.ElectricMachineDetail)

        @property
        def interior_permanent_magnet_machine(self):
            from mastapy.electric_machines import _1268
            
            return self._parent._cast(_1268.InteriorPermanentMagnetMachine)

        @property
        def permanent_magnet_assisted_synchronous_reluctance_machine(self):
            from mastapy.electric_machines import _1279
            
            return self._parent._cast(_1279.PermanentMagnetAssistedSynchronousReluctanceMachine)

        @property
        def surface_permanent_magnet_machine(self):
            from mastapy.electric_machines import _1293
            
            return self._parent._cast(_1293.SurfacePermanentMagnetMachine)

        @property
        def synchronous_reluctance_machine(self):
            from mastapy.electric_machines import _1295
            
            return self._parent._cast(_1295.SynchronousReluctanceMachine)

        @property
        def wound_field_synchronous_machine(self):
            from mastapy.electric_machines import _1309
            
            return self._parent._cast(_1309.WoundFieldSynchronousMachine)

        @property
        def non_cad_electric_machine_detail(self) -> 'NonCADElectricMachineDetail':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'NonCADElectricMachineDetail.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def stator(self) -> '_1289.Stator':
        """Stator: 'Stator' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Stator

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'NonCADElectricMachineDetail._Cast_NonCADElectricMachineDetail':
        return self._Cast_NonCADElectricMachineDetail(self)
