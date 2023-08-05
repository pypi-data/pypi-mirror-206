"""_1222.py

GearSetImplementationAnalysis
"""
from typing import Optional

from mastapy._internal import constructor
from mastapy import _7521
from mastapy.gears.analysis import _1223
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_SET_IMPLEMENTATION_ANALYSIS = python_net_import('SMT.MastaAPI.Gears.Analysis', 'GearSetImplementationAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('GearSetImplementationAnalysis',)


class GearSetImplementationAnalysis(_1223.GearSetImplementationAnalysisAbstract):
    """GearSetImplementationAnalysis

    This is a mastapy class.
    """

    TYPE = _GEAR_SET_IMPLEMENTATION_ANALYSIS

    class _Cast_GearSetImplementationAnalysis:
        """Special nested class for casting GearSetImplementationAnalysis to subclasses."""

        def __init__(self, parent: 'GearSetImplementationAnalysis'):
            self._parent = parent

        @property
        def gear_set_implementation_analysis_abstract(self):
            return self._parent._cast(_1223.GearSetImplementationAnalysisAbstract)

        @property
        def gear_set_design_analysis(self):
            from mastapy.gears.analysis import _1220
            
            return self._parent._cast(_1220.GearSetDesignAnalysis)

        @property
        def abstract_gear_set_analysis(self):
            from mastapy.gears.analysis import _1211
            
            return self._parent._cast(_1211.AbstractGearSetAnalysis)

        @property
        def cylindrical_manufactured_gear_set_load_case(self):
            from mastapy.gears.manufacturing.cylindrical import _616
            
            return self._parent._cast(_616.CylindricalManufacturedGearSetLoadCase)

        @property
        def conical_set_manufacturing_analysis(self):
            from mastapy.gears.manufacturing.bevel import _785
            
            return self._parent._cast(_785.ConicalSetManufacturingAnalysis)

        @property
        def gear_set_load_distribution_analysis(self):
            from mastapy.gears.ltca import _841
            
            return self._parent._cast(_841.GearSetLoadDistributionAnalysis)

        @property
        def cylindrical_gear_set_load_distribution_analysis(self):
            from mastapy.gears.ltca.cylindrical import _855
            
            return self._parent._cast(_855.CylindricalGearSetLoadDistributionAnalysis)

        @property
        def face_gear_set_load_distribution_analysis(self):
            from mastapy.gears.ltca.cylindrical import _857
            
            return self._parent._cast(_857.FaceGearSetLoadDistributionAnalysis)

        @property
        def conical_gear_set_load_distribution_analysis(self):
            from mastapy.gears.ltca.conical import _863
            
            return self._parent._cast(_863.ConicalGearSetLoadDistributionAnalysis)

        @property
        def gear_set_implementation_analysis(self) -> 'GearSetImplementationAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GearSetImplementationAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def valid_results_ready(self) -> 'bool':
        """bool: 'ValidResultsReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ValidResultsReady

        if temp is None:
            return False

        return temp

    def perform_analysis(self, run_all_planetary_meshes: Optional['bool'] = True):
        """ 'PerformAnalysis' is the original name of this method.

        Args:
            run_all_planetary_meshes (bool, optional)
        """

        run_all_planetary_meshes = bool(run_all_planetary_meshes)
        self.wrapped.PerformAnalysis(run_all_planetary_meshes if run_all_planetary_meshes else False)

    def perform_analysis_with_progress(self, run_all_planetary_meshes: 'bool', progress: '_7521.TaskProgress'):
        """ 'PerformAnalysisWithProgress' is the original name of this method.

        Args:
            run_all_planetary_meshes (bool)
            progress (mastapy.TaskProgress)
        """

        run_all_planetary_meshes = bool(run_all_planetary_meshes)
        self.wrapped.PerformAnalysisWithProgress(run_all_planetary_meshes if run_all_planetary_meshes else False, progress.wrapped if progress else None)

    def results_ready_for(self, run_all_planetary_meshes: Optional['bool'] = True) -> 'bool':
        """ 'ResultsReadyFor' is the original name of this method.

        Args:
            run_all_planetary_meshes (bool, optional)

        Returns:
            bool
        """

        run_all_planetary_meshes = bool(run_all_planetary_meshes)
        method_result = self.wrapped.ResultsReadyFor(run_all_planetary_meshes if run_all_planetary_meshes else False)
        return method_result

    @property
    def cast_to(self) -> 'GearSetImplementationAnalysis._Cast_GearSetImplementationAnalysis':
        return self._Cast_GearSetImplementationAnalysis(self)
