"""_864.py

ConicalMeshedGearLoadDistributionAnalysis
"""
from mastapy._internal import constructor
from mastapy.gears.cylindrical import _1207, _1206
from mastapy.gears.ltca.conical import _862
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_MESHED_GEAR_LOAD_DISTRIBUTION_ANALYSIS = python_net_import('SMT.MastaAPI.Gears.LTCA.Conical', 'ConicalMeshedGearLoadDistributionAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('ConicalMeshedGearLoadDistributionAnalysis',)


class ConicalMeshedGearLoadDistributionAnalysis(_0.APIBase):
    """ConicalMeshedGearLoadDistributionAnalysis

    This is a mastapy class.
    """

    TYPE = _CONICAL_MESHED_GEAR_LOAD_DISTRIBUTION_ANALYSIS

    class _Cast_ConicalMeshedGearLoadDistributionAnalysis:
        """Special nested class for casting ConicalMeshedGearLoadDistributionAnalysis to subclasses."""

        def __init__(self, parent: 'ConicalMeshedGearLoadDistributionAnalysis'):
            self._parent = parent

        @property
        def conical_meshed_gear_load_distribution_analysis(self) -> 'ConicalMeshedGearLoadDistributionAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConicalMeshedGearLoadDistributionAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def estimated_gear_stiffness_from_fe_model(self) -> 'float':
        """float: 'EstimatedGearStiffnessFromFEModel' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.EstimatedGearStiffnessFromFEModel

        if temp is None:
            return 0.0

        return temp

    @property
    def max_tensile_principal_root_stress_compression_side(self) -> 'float':
        """float: 'MaxTensilePrincipalRootStressCompressionSide' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaxTensilePrincipalRootStressCompressionSide

        if temp is None:
            return 0.0

        return temp

    @property
    def max_tensile_principal_root_stress_tension_side(self) -> 'float':
        """float: 'MaxTensilePrincipalRootStressTensionSide' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaxTensilePrincipalRootStressTensionSide

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_von_mises_root_stress_compression_side(self) -> 'float':
        """float: 'MaximumVonMisesRootStressCompressionSide' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumVonMisesRootStressCompressionSide

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_von_mises_root_stress_tension_side(self) -> 'float':
        """float: 'MaximumVonMisesRootStressTensionSide' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumVonMisesRootStressTensionSide

        if temp is None:
            return 0.0

        return temp

    @property
    def name(self) -> 'str':
        """str: 'Name' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Name

        if temp is None:
            return ''

        return temp

    @property
    def torque(self) -> 'float':
        """float: 'Torque' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Torque

        if temp is None:
            return 0.0

        return temp

    @property
    def contact_charts(self) -> '_1207.GearLTCAContactCharts':
        """GearLTCAContactCharts: 'ContactCharts' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ContactCharts

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def contact_charts_as_text_file(self) -> '_1206.GearLTCAContactChartDataAsTextFile':
        """GearLTCAContactChartDataAsTextFile: 'ContactChartsAsTextFile' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ContactChartsAsTextFile

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_load_distribution_analysis(self) -> '_862.ConicalGearLoadDistributionAnalysis':
        """ConicalGearLoadDistributionAnalysis: 'GearLoadDistributionAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearLoadDistributionAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'ConicalMeshedGearLoadDistributionAnalysis._Cast_ConicalMeshedGearLoadDistributionAnalysis':
        return self._Cast_ConicalMeshedGearLoadDistributionAnalysis(self)
