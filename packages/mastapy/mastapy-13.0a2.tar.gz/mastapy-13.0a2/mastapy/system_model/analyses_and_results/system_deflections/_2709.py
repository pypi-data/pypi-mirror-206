"""_2709.py

CouplingHalfSystemDeflection
"""
from mastapy.system_model.part_model.couplings import _2563
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4047
from mastapy.system_model.analyses_and_results.system_deflections import _2761
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_HALF_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections', 'CouplingHalfSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('CouplingHalfSystemDeflection',)


class CouplingHalfSystemDeflection(_2761.MountableComponentSystemDeflection):
    """CouplingHalfSystemDeflection

    This is a mastapy class.
    """

    TYPE = _COUPLING_HALF_SYSTEM_DEFLECTION

    class _Cast_CouplingHalfSystemDeflection:
        """Special nested class for casting CouplingHalfSystemDeflection to subclasses."""

        def __init__(self, parent: 'CouplingHalfSystemDeflection'):
            self._parent = parent

        @property
        def mountable_component_system_deflection(self):
            return self._parent._cast(_2761.MountableComponentSystemDeflection)

        @property
        def component_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2694
            
            return self._parent._cast(_2694.ComponentSystemDeflection)

        @property
        def part_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2764
            
            return self._parent._cast(_2764.PartSystemDeflection)

        @property
        def part_fe_analysis(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7509
            
            return self._parent._cast(_7509.PartFEAnalysis)

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
        def clutch_half_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2691
            
            return self._parent._cast(_2691.ClutchHalfSystemDeflection)

        @property
        def concept_coupling_half_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2697
            
            return self._parent._cast(_2697.ConceptCouplingHalfSystemDeflection)

        @property
        def cvt_pulley_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2712
            
            return self._parent._cast(_2712.CVTPulleySystemDeflection)

        @property
        def part_to_part_shear_coupling_half_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2766
            
            return self._parent._cast(_2766.PartToPartShearCouplingHalfSystemDeflection)

        @property
        def pulley_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2772
            
            return self._parent._cast(_2772.PulleySystemDeflection)

        @property
        def rolling_ring_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2778
            
            return self._parent._cast(_2778.RollingRingSystemDeflection)

        @property
        def spring_damper_half_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2790
            
            return self._parent._cast(_2790.SpringDamperHalfSystemDeflection)

        @property
        def synchroniser_half_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2800
            
            return self._parent._cast(_2800.SynchroniserHalfSystemDeflection)

        @property
        def synchroniser_part_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2801
            
            return self._parent._cast(_2801.SynchroniserPartSystemDeflection)

        @property
        def synchroniser_sleeve_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2802
            
            return self._parent._cast(_2802.SynchroniserSleeveSystemDeflection)

        @property
        def torque_converter_pump_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2808
            
            return self._parent._cast(_2808.TorqueConverterPumpSystemDeflection)

        @property
        def torque_converter_turbine_system_deflection(self):
            from mastapy.system_model.analyses_and_results.system_deflections import _2810
            
            return self._parent._cast(_2810.TorqueConverterTurbineSystemDeflection)

        @property
        def coupling_half_system_deflection(self) -> 'CouplingHalfSystemDeflection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CouplingHalfSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2563.CouplingHalf':
        """CouplingHalf: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results(self) -> '_4047.CouplingHalfPowerFlow':
        """CouplingHalfPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'CouplingHalfSystemDeflection._Cast_CouplingHalfSystemDeflection':
        return self._Cast_CouplingHalfSystemDeflection(self)
