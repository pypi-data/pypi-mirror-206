"""_1337.py

EfficiencyMapAnalysis
"""
from mastapy._internal import constructor
from mastapy.electric_machines.results import _1311
from mastapy.electric_machines.load_cases_and_analyses import _1338, _1339
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_EFFICIENCY_MAP_ANALYSIS = python_net_import('SMT.MastaAPI.ElectricMachines.LoadCasesAndAnalyses', 'EfficiencyMapAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('EfficiencyMapAnalysis',)


class EfficiencyMapAnalysis(_1339.ElectricMachineAnalysis):
    """EfficiencyMapAnalysis

    This is a mastapy class.
    """

    TYPE = _EFFICIENCY_MAP_ANALYSIS

    class _Cast_EfficiencyMapAnalysis:
        """Special nested class for casting EfficiencyMapAnalysis to subclasses."""

        def __init__(self, parent: 'EfficiencyMapAnalysis'):
            self._parent = parent

        @property
        def electric_machine_analysis(self):
            return self._parent._cast(_1339.ElectricMachineAnalysis)

        @property
        def efficiency_map_analysis(self) -> 'EfficiencyMapAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'EfficiencyMapAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def permanent_magnet_flux_linkage_at_reference_temperature(self) -> 'float':
        """float: 'PermanentMagnetFluxLinkageAtReferenceTemperature' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PermanentMagnetFluxLinkageAtReferenceTemperature

        if temp is None:
            return 0.0

        return temp

    @property
    def phase_resistance(self) -> 'float':
        """float: 'PhaseResistance' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PhaseResistance

        if temp is None:
            return 0.0

        return temp

    @property
    def efficiency_map_results(self) -> '_1311.EfficiencyResults':
        """EfficiencyResults: 'EfficiencyMapResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.EfficiencyMapResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def load_case(self) -> '_1338.EfficiencyMapLoadCase':
        """EfficiencyMapLoadCase: 'LoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'EfficiencyMapAnalysis._Cast_EfficiencyMapAnalysis':
        return self._Cast_EfficiencyMapAnalysis(self)
