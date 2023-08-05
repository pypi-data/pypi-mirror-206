"""_1240.py

CADElectricMachineDetail
"""
from mastapy.nodal_analysis.geometry_modeller_link import _156
from mastapy._internal import constructor
from mastapy.electric_machines import _1242, _1243, _1254
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CAD_ELECTRIC_MACHINE_DETAIL = python_net_import('SMT.MastaAPI.ElectricMachines', 'CADElectricMachineDetail')


__docformat__ = 'restructuredtext en'
__all__ = ('CADElectricMachineDetail',)


class CADElectricMachineDetail(_1254.ElectricMachineDetail):
    """CADElectricMachineDetail

    This is a mastapy class.
    """

    TYPE = _CAD_ELECTRIC_MACHINE_DETAIL

    class _Cast_CADElectricMachineDetail:
        """Special nested class for casting CADElectricMachineDetail to subclasses."""

        def __init__(self, parent: 'CADElectricMachineDetail'):
            self._parent = parent

        @property
        def electric_machine_detail(self):
            return self._parent._cast(_1254.ElectricMachineDetail)

        @property
        def cad_electric_machine_detail(self) -> 'CADElectricMachineDetail':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CADElectricMachineDetail.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def geometry_modeller_dimensions(self) -> '_156.GeometryModellerDimensions':
        """GeometryModellerDimensions: 'GeometryModellerDimensions' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GeometryModellerDimensions

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def rotor(self) -> '_1242.CADRotor':
        """CADRotor: 'Rotor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Rotor

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def stator(self) -> '_1243.CADStator':
        """CADStator: 'Stator' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Stator

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    def embed_geometry_modeller_file(self):
        """ 'EmbedGeometryModellerFile' is the original name of this method."""

        self.wrapped.EmbedGeometryModellerFile()

    def open_embedded_geometry_modeller_file(self):
        """ 'OpenEmbeddedGeometryModellerFile' is the original name of this method."""

        self.wrapped.OpenEmbeddedGeometryModellerFile()

    def reread_geometry_from_geometry_modeller(self):
        """ 'RereadGeometryFromGeometryModeller' is the original name of this method."""

        self.wrapped.RereadGeometryFromGeometryModeller()

    @property
    def cast_to(self) -> 'CADElectricMachineDetail._Cast_CADElectricMachineDetail':
        return self._Cast_CADElectricMachineDetail(self)
