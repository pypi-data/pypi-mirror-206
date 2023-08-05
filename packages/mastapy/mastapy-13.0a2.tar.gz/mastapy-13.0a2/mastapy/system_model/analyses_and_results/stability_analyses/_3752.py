"""_3752.py

BeltDriveStabilityAnalysis
"""
from mastapy.system_model.part_model.couplings import _2555
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6786
from mastapy.system_model.analyses_and_results.stability_analyses import _3841
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BELT_DRIVE_STABILITY_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses', 'BeltDriveStabilityAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('BeltDriveStabilityAnalysis',)


class BeltDriveStabilityAnalysis(_3841.SpecialisedAssemblyStabilityAnalysis):
    """BeltDriveStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _BELT_DRIVE_STABILITY_ANALYSIS

    class _Cast_BeltDriveStabilityAnalysis:
        """Special nested class for casting BeltDriveStabilityAnalysis to subclasses."""

        def __init__(self, parent: 'BeltDriveStabilityAnalysis'):
            self._parent = parent

        @property
        def specialised_assembly_stability_analysis(self):
            return self._parent._cast(_3841.SpecialisedAssemblyStabilityAnalysis)

        @property
        def abstract_assembly_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3742
            
            return self._parent._cast(_3742.AbstractAssemblyStabilityAnalysis)

        @property
        def part_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3822
            
            return self._parent._cast(_3822.PartStabilityAnalysis)

        @property
        def part_static_load_analysis_case(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7510
            
            return self._parent._cast(_7510.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7507
            
            return self._parent._cast(_7507.PartAnalysisCase)

        @property
        def part_analysis(self):
            from mastapy.system_model.analyses_and_results import _2636
            
            return self._parent._cast(_2636.PartAnalysis)

        @property
        def design_entity_single_context_analysis(self):
            from mastapy.system_model.analyses_and_results import _2632
            
            return self._parent._cast(_2632.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(self):
            from mastapy.system_model.analyses_and_results import _2630
            
            return self._parent._cast(_2630.DesignEntityAnalysis)

        @property
        def cvt_stability_analysis(self):
            from mastapy.system_model.analyses_and_results.stability_analyses import _3785
            
            return self._parent._cast(_3785.CVTStabilityAnalysis)

        @property
        def belt_drive_stability_analysis(self) -> 'BeltDriveStabilityAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'BeltDriveStabilityAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2555.BeltDrive':
        """BeltDrive: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_load_case(self) -> '_6786.BeltDriveLoadCase':
        """BeltDriveLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'BeltDriveStabilityAnalysis._Cast_BeltDriveStabilityAnalysis':
        return self._Cast_BeltDriveStabilityAnalysis(self)
