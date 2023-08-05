"""_1584.py

PersistentSingleton
"""
from typing import List

from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PERSISTENT_SINGLETON = python_net_import('SMT.MastaAPI.Utility', 'PersistentSingleton')


__docformat__ = 'restructuredtext en'
__all__ = ('PersistentSingleton',)


class PersistentSingleton(_0.APIBase):
    """PersistentSingleton

    This is a mastapy class.
    """

    TYPE = _PERSISTENT_SINGLETON

    class _Cast_PersistentSingleton:
        """Special nested class for casting PersistentSingleton to subclasses."""

        def __init__(self, parent: 'PersistentSingleton'):
            self._parent = parent

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
        def per_machine_settings(self):
            from mastapy.utility import _1583
            
            return self._parent._cast(_1583.PerMachineSettings)

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
        def persistent_singleton(self) -> 'PersistentSingleton':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'PersistentSingleton.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def report_names(self) -> 'List[str]':
        """List[str]: 'ReportNames' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ReportNames

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, str)
        return value

    def save(self):
        """ 'Save' is the original name of this method."""

        self.wrapped.Save()

    def output_default_report_to(self, file_path: 'str'):
        """ 'OutputDefaultReportTo' is the original name of this method.

        Args:
            file_path (str)
        """

        file_path = str(file_path)
        self.wrapped.OutputDefaultReportTo(file_path if file_path else '')

    def get_default_report_with_encoded_images(self) -> 'str':
        """ 'GetDefaultReportWithEncodedImages' is the original name of this method.

        Returns:
            str
        """

        method_result = self.wrapped.GetDefaultReportWithEncodedImages()
        return method_result

    def output_active_report_to(self, file_path: 'str'):
        """ 'OutputActiveReportTo' is the original name of this method.

        Args:
            file_path (str)
        """

        file_path = str(file_path)
        self.wrapped.OutputActiveReportTo(file_path if file_path else '')

    def output_active_report_as_text_to(self, file_path: 'str'):
        """ 'OutputActiveReportAsTextTo' is the original name of this method.

        Args:
            file_path (str)
        """

        file_path = str(file_path)
        self.wrapped.OutputActiveReportAsTextTo(file_path if file_path else '')

    def get_active_report_with_encoded_images(self) -> 'str':
        """ 'GetActiveReportWithEncodedImages' is the original name of this method.

        Returns:
            str
        """

        method_result = self.wrapped.GetActiveReportWithEncodedImages()
        return method_result

    def output_named_report_to(self, report_name: 'str', file_path: 'str'):
        """ 'OutputNamedReportTo' is the original name of this method.

        Args:
            report_name (str)
            file_path (str)
        """

        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportTo(report_name if report_name else '', file_path if file_path else '')

    def output_named_report_as_masta_report(self, report_name: 'str', file_path: 'str'):
        """ 'OutputNamedReportAsMastaReport' is the original name of this method.

        Args:
            report_name (str)
            file_path (str)
        """

        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsMastaReport(report_name if report_name else '', file_path if file_path else '')

    def output_named_report_as_text_to(self, report_name: 'str', file_path: 'str'):
        """ 'OutputNamedReportAsTextTo' is the original name of this method.

        Args:
            report_name (str)
            file_path (str)
        """

        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsTextTo(report_name if report_name else '', file_path if file_path else '')

    def get_named_report_with_encoded_images(self, report_name: 'str') -> 'str':
        """ 'GetNamedReportWithEncodedImages' is the original name of this method.

        Args:
            report_name (str)

        Returns:
            str
        """

        report_name = str(report_name)
        method_result = self.wrapped.GetNamedReportWithEncodedImages(report_name if report_name else '')
        return method_result

    @property
    def cast_to(self) -> 'PersistentSingleton._Cast_PersistentSingleton':
        return self._Cast_PersistentSingleton(self)
