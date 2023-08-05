"""_5734.py

HarmonicAnalysisRootAssemblyExportOptions
"""
from typing import List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5731
from mastapy.system_model.analyses_and_results import _2634
from mastapy.system_model.part_model import _2454
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HARMONIC_ANALYSIS_ROOT_ASSEMBLY_EXPORT_OPTIONS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses', 'HarmonicAnalysisRootAssemblyExportOptions')


__docformat__ = 'restructuredtext en'
__all__ = ('HarmonicAnalysisRootAssemblyExportOptions',)


class HarmonicAnalysisRootAssemblyExportOptions(_5731.HarmonicAnalysisExportOptions['_2634.IHaveRootHarmonicAnalysisResults', '_2454.RootAssembly']):
    """HarmonicAnalysisRootAssemblyExportOptions

    This is a mastapy class.
    """

    TYPE = _HARMONIC_ANALYSIS_ROOT_ASSEMBLY_EXPORT_OPTIONS

    class _Cast_HarmonicAnalysisRootAssemblyExportOptions:
        """Special nested class for casting HarmonicAnalysisRootAssemblyExportOptions to subclasses."""

        def __init__(self, parent: 'HarmonicAnalysisRootAssemblyExportOptions'):
            self._parent = parent

        @property
        def harmonic_analysis_export_options(self):
            return self._parent._cast(_5731.HarmonicAnalysisExportOptions)

        @property
        def harmonic_analysis_root_assembly_export_options(self) -> 'HarmonicAnalysisRootAssemblyExportOptions':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'HarmonicAnalysisRootAssemblyExportOptions.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def include_all_fe_models(self) -> 'bool':
        """bool: 'IncludeAllFEModels' is the original name of this property."""

        temp = self.wrapped.IncludeAllFEModels

        if temp is None:
            return False

        return temp

    @include_all_fe_models.setter
    def include_all_fe_models(self, value: 'bool'):
        self.wrapped.IncludeAllFEModels = bool(value) if value else False

    @property
    def include_all_shafts(self) -> 'bool':
        """bool: 'IncludeAllShafts' is the original name of this property."""

        temp = self.wrapped.IncludeAllShafts

        if temp is None:
            return False

        return temp

    @include_all_shafts.setter
    def include_all_shafts(self, value: 'bool'):
        self.wrapped.IncludeAllShafts = bool(value) if value else False

    @property
    def status_message_for_export(self) -> 'str':
        """str: 'StatusMessageForExport' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StatusMessageForExport

        if temp is None:
            return ''

        return temp

    def export_to_folder(self, folder_path: 'str') -> 'List[str]':
        """ 'ExportToFolder' is the original name of this method.

        Args:
            folder_path (str)

        Returns:
            List[str]
        """

        folder_path = str(folder_path)
        return conversion.pn_to_mp_objects_in_list(self.wrapped.ExportToFolder(folder_path if folder_path else ''), str)

    @property
    def cast_to(self) -> 'HarmonicAnalysisRootAssemblyExportOptions._Cast_HarmonicAnalysisRootAssemblyExportOptions':
        return self._Cast_HarmonicAnalysisRootAssemblyExportOptions(self)
