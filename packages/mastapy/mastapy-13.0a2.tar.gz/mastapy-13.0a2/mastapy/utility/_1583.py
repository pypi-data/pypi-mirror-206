"""_1583.py

PerMachineSettings
"""
from mastapy._internal import constructor
from mastapy.utility import _1584
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PER_MACHINE_SETTINGS = python_net_import('SMT.MastaAPI.Utility', 'PerMachineSettings')


__docformat__ = 'restructuredtext en'
__all__ = ('PerMachineSettings',)


class PerMachineSettings(_1584.PersistentSingleton):
    """PerMachineSettings

    This is a mastapy class.
    """

    TYPE = _PER_MACHINE_SETTINGS

    class _Cast_PerMachineSettings:
        """Special nested class for casting PerMachineSettings to subclasses."""

        def __init__(self, parent: 'PerMachineSettings'):
            self._parent = parent

        @property
        def persistent_singleton(self):
            return self._parent._cast(_1584.PersistentSingleton)

        @property
        def fe_user_settings(self):
            from mastapy.nodal_analysis import _68
            
            return self._parent._cast(_68.FEUserSettings)

        @property
        def geometry_modeller_settings(self):
            from mastapy.nodal_analysis.geometry_modeller_link import _159
            
            return self._parent._cast(_159.GeometryModellerSettings)

        @property
        def gear_material_expert_system_factor_settings(self):
            from mastapy.gears.materials import _591
            
            return self._parent._cast(_591.GearMaterialExpertSystemFactorSettings)

        @property
        def cylindrical_gear_fe_settings(self):
            from mastapy.gears.ltca.cylindrical import _850
            
            return self._parent._cast(_850.CylindricalGearFESettings)

        @property
        def cylindrical_gear_defaults(self):
            from mastapy.gears.gear_designs.cylindrical import _1006
            
            return self._parent._cast(_1006.CylindricalGearDefaults)

        @property
        def program_settings(self):
            from mastapy.utility import _1585
            
            return self._parent._cast(_1585.ProgramSettings)

        @property
        def pushbullet_settings(self):
            from mastapy.utility import _1586
            
            return self._parent._cast(_1586.PushbulletSettings)

        @property
        def measurement_settings(self):
            from mastapy.utility.units_and_measurements import _1595
            
            return self._parent._cast(_1595.MeasurementSettings)

        @property
        def scripting_setup(self):
            from mastapy.utility.scripting import _1728
            
            return self._parent._cast(_1728.ScriptingSetup)

        @property
        def database_settings(self):
            from mastapy.utility.databases import _1814
            
            return self._parent._cast(_1814.DatabaseSettings)

        @property
        def cad_export_settings(self):
            from mastapy.utility.cad_export import _1819
            
            return self._parent._cast(_1819.CADExportSettings)

        @property
        def skf_settings(self):
            from mastapy.bearings import _1884
            
            return self._parent._cast(_1884.SKFSettings)

        @property
        def planet_carrier_settings(self):
            from mastapy.system_model.part_model import _2450
            
            return self._parent._cast(_2450.PlanetCarrierSettings)

        @property
        def per_machine_settings(self) -> 'PerMachineSettings':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'PerMachineSettings.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    def reset_to_defaults(self):
        """ 'ResetToDefaults' is the original name of this method."""

        self.wrapped.ResetToDefaults()

    @property
    def cast_to(self) -> 'PerMachineSettings._Cast_PerMachineSettings':
        return self._Cast_PerMachineSettings(self)
