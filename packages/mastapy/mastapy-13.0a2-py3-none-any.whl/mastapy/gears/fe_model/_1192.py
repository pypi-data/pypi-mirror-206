"""_1192.py

GearMeshFEModel
"""
from mastapy._internal import constructor
from mastapy.gears.analysis import _1219
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_MESH_FE_MODEL = python_net_import('SMT.MastaAPI.Gears.FEModel', 'GearMeshFEModel')


__docformat__ = 'restructuredtext en'
__all__ = ('GearMeshFEModel',)


class GearMeshFEModel(_1219.GearMeshImplementationDetail):
    """GearMeshFEModel

    This is a mastapy class.
    """

    TYPE = _GEAR_MESH_FE_MODEL

    class _Cast_GearMeshFEModel:
        """Special nested class for casting GearMeshFEModel to subclasses."""

        def __init__(self, parent: 'GearMeshFEModel'):
            self._parent = parent

        @property
        def gear_mesh_implementation_detail(self):
            return self._parent._cast(_1219.GearMeshImplementationDetail)

        @property
        def gear_mesh_design_analysis(self):
            from mastapy.gears.analysis import _1216
            
            return self._parent._cast(_1216.GearMeshDesignAnalysis)

        @property
        def abstract_gear_mesh_analysis(self):
            from mastapy.gears.analysis import _1210
            
            return self._parent._cast(_1210.AbstractGearMeshAnalysis)

        @property
        def cylindrical_gear_mesh_fe_model(self):
            from mastapy.gears.fe_model.cylindrical import _1196
            
            return self._parent._cast(_1196.CylindricalGearMeshFEModel)

        @property
        def conical_mesh_fe_model(self):
            from mastapy.gears.fe_model.conical import _1199
            
            return self._parent._cast(_1199.ConicalMeshFEModel)

        @property
        def gear_mesh_fe_model(self) -> 'GearMeshFEModel':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GearMeshFEModel.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def number_of_loads_per_contact(self) -> 'int':
        """int: 'NumberOfLoadsPerContact' is the original name of this property."""

        temp = self.wrapped.NumberOfLoadsPerContact

        if temp is None:
            return 0

        return temp

    @number_of_loads_per_contact.setter
    def number_of_loads_per_contact(self, value: 'int'):
        self.wrapped.NumberOfLoadsPerContact = int(value) if value else 0

    @property
    def number_of_rotations(self) -> 'int':
        """int: 'NumberOfRotations' is the original name of this property."""

        temp = self.wrapped.NumberOfRotations

        if temp is None:
            return 0

        return temp

    @number_of_rotations.setter
    def number_of_rotations(self, value: 'int'):
        self.wrapped.NumberOfRotations = int(value) if value else 0

    @property
    def cast_to(self) -> 'GearMeshFEModel._Cast_GearMeshFEModel':
        return self._Cast_GearMeshFEModel(self)
