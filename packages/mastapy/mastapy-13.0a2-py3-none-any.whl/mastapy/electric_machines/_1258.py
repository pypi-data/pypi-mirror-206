"""_1258.py

ElectricMachineMeshingOptionsBase
"""
from mastapy._internal import constructor
from mastapy.nodal_analysis import _61
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ELECTRIC_MACHINE_MESHING_OPTIONS_BASE = python_net_import('SMT.MastaAPI.ElectricMachines', 'ElectricMachineMeshingOptionsBase')


__docformat__ = 'restructuredtext en'
__all__ = ('ElectricMachineMeshingOptionsBase',)


class ElectricMachineMeshingOptionsBase(_61.FEMeshingOptions):
    """ElectricMachineMeshingOptionsBase

    This is a mastapy class.
    """

    TYPE = _ELECTRIC_MACHINE_MESHING_OPTIONS_BASE

    class _Cast_ElectricMachineMeshingOptionsBase:
        """Special nested class for casting ElectricMachineMeshingOptionsBase to subclasses."""

        def __init__(self, parent: 'ElectricMachineMeshingOptionsBase'):
            self._parent = parent

        @property
        def fe_meshing_options(self):
            return self._parent._cast(_61.FEMeshingOptions)

        @property
        def electric_machine_mechanical_analysis_meshing_options(self):
            from mastapy.electric_machines import _1256
            
            return self._parent._cast(_1256.ElectricMachineMechanicalAnalysisMeshingOptions)

        @property
        def electric_machine_meshing_options(self):
            from mastapy.electric_machines import _1257
            
            return self._parent._cast(_1257.ElectricMachineMeshingOptions)

        @property
        def electric_machine_meshing_options_base(self) -> 'ElectricMachineMeshingOptionsBase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ElectricMachineMeshingOptionsBase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def autogenerate_mesh(self) -> 'bool':
        """bool: 'AutogenerateMesh' is the original name of this property."""

        temp = self.wrapped.AutogenerateMesh

        if temp is None:
            return False

        return temp

    @autogenerate_mesh.setter
    def autogenerate_mesh(self, value: 'bool'):
        self.wrapped.AutogenerateMesh = bool(value) if value else False

    @property
    def p_element_order(self) -> 'int':
        """int: 'PElementOrder' is the original name of this property."""

        temp = self.wrapped.PElementOrder

        if temp is None:
            return 0

        return temp

    @p_element_order.setter
    def p_element_order(self, value: 'int'):
        self.wrapped.PElementOrder = int(value) if value else 0

    @property
    def use_p_elements(self) -> 'bool':
        """bool: 'UsePElements' is the original name of this property."""

        temp = self.wrapped.UsePElements

        if temp is None:
            return False

        return temp

    @use_p_elements.setter
    def use_p_elements(self, value: 'bool'):
        self.wrapped.UsePElements = bool(value) if value else False

    @property
    def utilise_periodicity_when_meshing_geometry(self) -> 'bool':
        """bool: 'UtilisePeriodicityWhenMeshingGeometry' is the original name of this property."""

        temp = self.wrapped.UtilisePeriodicityWhenMeshingGeometry

        if temp is None:
            return False

        return temp

    @utilise_periodicity_when_meshing_geometry.setter
    def utilise_periodicity_when_meshing_geometry(self, value: 'bool'):
        self.wrapped.UtilisePeriodicityWhenMeshingGeometry = bool(value) if value else False

    @property
    def cast_to(self) -> 'ElectricMachineMeshingOptionsBase._Cast_ElectricMachineMeshingOptionsBase':
        return self._Cast_ElectricMachineMeshingOptionsBase(self)
