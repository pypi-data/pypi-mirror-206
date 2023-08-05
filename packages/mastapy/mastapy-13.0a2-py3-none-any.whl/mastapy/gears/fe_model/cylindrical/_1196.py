"""_1196.py

CylindricalGearMeshFEModel
"""
from typing import List

from mastapy.gears.fe_model import _1191, _1192
from mastapy.gears import _322
from mastapy._internal import conversion, constructor
from mastapy.gears.ltca import _830
from mastapy import _7521
from mastapy._internal.python_net import python_net_import
from mastapy._internal.cast_exception import CastException

_GEAR_FE_MODEL = python_net_import('SMT.MastaAPI.Gears.FEModel', 'GearFEModel')
_GEAR_FLANKS = python_net_import('SMT.MastaAPI.Gears', 'GearFlanks')
_TASK_PROGRESS = python_net_import('SMT.MastaAPIUtility', 'TaskProgress')
_CYLINDRICAL_GEAR_MESH_FE_MODEL = python_net_import('SMT.MastaAPI.Gears.FEModel.Cylindrical', 'CylindricalGearMeshFEModel')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearMeshFEModel',)


class CylindricalGearMeshFEModel(_1192.GearMeshFEModel):
    """CylindricalGearMeshFEModel

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_MESH_FE_MODEL

    class _Cast_CylindricalGearMeshFEModel:
        """Special nested class for casting CylindricalGearMeshFEModel to subclasses."""

        def __init__(self, parent: 'CylindricalGearMeshFEModel'):
            self._parent = parent

        @property
        def gear_mesh_fe_model(self):
            return self._parent._cast(_1192.GearMeshFEModel)

        @property
        def gear_mesh_implementation_detail(self):
            from mastapy.gears.analysis import _1219
            
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
        def cylindrical_gear_mesh_fe_model(self) -> 'CylindricalGearMeshFEModel':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CylindricalGearMeshFEModel.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    def stiffness_wrt_contacts_for(self, gear: '_1191.GearFEModel', flank: '_322.GearFlanks') -> 'List[_830.GearContactStiffness]':
        """ 'StiffnessWrtContactsFor' is the original name of this method.

        Args:
            gear (mastapy.gears.fe_model.GearFEModel)
            flank (mastapy.gears.GearFlanks)

        Returns:
            List[mastapy.gears.ltca.GearContactStiffness]
        """

        flank = conversion.mp_to_pn_enum(flank, _322.GearFlanks.type_())
        return conversion.pn_to_mp_objects_in_list(self.wrapped.StiffnessWrtContactsFor.Overloads[_GEAR_FE_MODEL, _GEAR_FLANKS](gear.wrapped if gear else None, flank))

    def stiffness_wrt_contacts_for_with_progress(self, gear: '_1191.GearFEModel', flank: '_322.GearFlanks', progress: '_7521.TaskProgress') -> 'List[_830.GearContactStiffness]':
        """ 'StiffnessWrtContactsFor' is the original name of this method.

        Args:
            gear (mastapy.gears.fe_model.GearFEModel)
            flank (mastapy.gears.GearFlanks)
            progress (mastapy.TaskProgress)

        Returns:
            List[mastapy.gears.ltca.GearContactStiffness]
        """

        flank = conversion.mp_to_pn_enum(flank, _322.GearFlanks.type_())
        return conversion.pn_to_mp_objects_in_list(self.wrapped.StiffnessWrtContactsFor.Overloads[_GEAR_FE_MODEL, _GEAR_FLANKS, _TASK_PROGRESS](gear.wrapped if gear else None, flank, progress.wrapped if progress else None))

    def generate_stiffness_wrt_contacts_for(self, progress: '_7521.TaskProgress'):
        """ 'GenerateStiffnessWrtContactsFor' is the original name of this method.

        Args:
            progress (mastapy.TaskProgress)
        """

        self.wrapped.GenerateStiffnessWrtContactsFor.Overloads[_TASK_PROGRESS](progress.wrapped if progress else None)

    def generate_stiffness_wrt_contacts_for_flank(self, flank: '_322.GearFlanks', progress: '_7521.TaskProgress'):
        """ 'GenerateStiffnessWrtContactsFor' is the original name of this method.

        Args:
            flank (mastapy.gears.GearFlanks)
            progress (mastapy.TaskProgress)
        """

        flank = conversion.mp_to_pn_enum(flank, _322.GearFlanks.type_())
        self.wrapped.GenerateStiffnessWrtContactsFor.Overloads[_GEAR_FLANKS, _TASK_PROGRESS](flank, progress.wrapped if progress else None)

    @property
    def cast_to(self) -> 'CylindricalGearMeshFEModel._Cast_CylindricalGearMeshFEModel':
        return self._Cast_CylindricalGearMeshFEModel(self)
