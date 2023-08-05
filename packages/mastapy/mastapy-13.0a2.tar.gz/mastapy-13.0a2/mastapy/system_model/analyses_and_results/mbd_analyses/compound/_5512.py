"""_5512.py

BevelDifferentialGearSetCompoundMultibodyDynamicsAnalysis
"""
from typing import List

from mastapy.system_model.part_model.gears import _2495
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.mbd_analyses import _5362
from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5510, _5511, _5517
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_GEAR_SET_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound', 'BevelDifferentialGearSetCompoundMultibodyDynamicsAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('BevelDifferentialGearSetCompoundMultibodyDynamicsAnalysis',)


class BevelDifferentialGearSetCompoundMultibodyDynamicsAnalysis(_5517.BevelGearSetCompoundMultibodyDynamicsAnalysis):
    """BevelDifferentialGearSetCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_GEAR_SET_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS

    class _Cast_BevelDifferentialGearSetCompoundMultibodyDynamicsAnalysis:
        """Special nested class for casting BevelDifferentialGearSetCompoundMultibodyDynamicsAnalysis to subclasses."""

        def __init__(self, parent: 'BevelDifferentialGearSetCompoundMultibodyDynamicsAnalysis'):
            self._parent = parent

        @property
        def bevel_gear_set_compound_multibody_dynamics_analysis(self):
            return self._parent._cast(_5517.BevelGearSetCompoundMultibodyDynamicsAnalysis)

        @property
        def agma_gleason_conical_gear_set_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5505
            
            return self._parent._cast(_5505.AGMAGleasonConicalGearSetCompoundMultibodyDynamicsAnalysis)

        @property
        def conical_gear_set_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5533
            
            return self._parent._cast(_5533.ConicalGearSetCompoundMultibodyDynamicsAnalysis)

        @property
        def gear_set_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5559
            
            return self._parent._cast(_5559.GearSetCompoundMultibodyDynamicsAnalysis)

        @property
        def specialised_assembly_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5597
            
            return self._parent._cast(_5597.SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis)

        @property
        def abstract_assembly_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5499
            
            return self._parent._cast(_5499.AbstractAssemblyCompoundMultibodyDynamicsAnalysis)

        @property
        def part_compound_multibody_dynamics_analysis(self):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5578
            
            return self._parent._cast(_5578.PartCompoundMultibodyDynamicsAnalysis)

        @property
        def part_compound_analysis(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7508
            
            return self._parent._cast(_7508.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7505
            
            return self._parent._cast(_7505.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(self):
            from mastapy.system_model.analyses_and_results import _2630
            
            return self._parent._cast(_2630.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_set_compound_multibody_dynamics_analysis(self) -> 'BevelDifferentialGearSetCompoundMultibodyDynamicsAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'BevelDifferentialGearSetCompoundMultibodyDynamicsAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2495.BevelDifferentialGearSet':
        """BevelDifferentialGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_design(self) -> '_2495.BevelDifferentialGearSet':
        """BevelDifferentialGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_5362.BevelDifferentialGearSetMultibodyDynamicsAnalysis]':
        """List[BevelDifferentialGearSetMultibodyDynamicsAnalysis]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def bevel_differential_gears_compound_multibody_dynamics_analysis(self) -> 'List[_5510.BevelDifferentialGearCompoundMultibodyDynamicsAnalysis]':
        """List[BevelDifferentialGearCompoundMultibodyDynamicsAnalysis]: 'BevelDifferentialGearsCompoundMultibodyDynamicsAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BevelDifferentialGearsCompoundMultibodyDynamicsAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def bevel_differential_meshes_compound_multibody_dynamics_analysis(self) -> 'List[_5511.BevelDifferentialGearMeshCompoundMultibodyDynamicsAnalysis]':
        """List[BevelDifferentialGearMeshCompoundMultibodyDynamicsAnalysis]: 'BevelDifferentialMeshesCompoundMultibodyDynamicsAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BevelDifferentialMeshesCompoundMultibodyDynamicsAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_5362.BevelDifferentialGearSetMultibodyDynamicsAnalysis]':
        """List[BevelDifferentialGearSetMultibodyDynamicsAnalysis]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'BevelDifferentialGearSetCompoundMultibodyDynamicsAnalysis._Cast_BevelDifferentialGearSetCompoundMultibodyDynamicsAnalysis':
        return self._Cast_BevelDifferentialGearSetCompoundMultibodyDynamicsAnalysis(self)
