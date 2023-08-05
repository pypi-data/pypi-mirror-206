"""_5709.py

ElectricMachineStatorToothLoadsExcitationDetail
"""
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5702
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ELECTRIC_MACHINE_STATOR_TOOTH_LOADS_EXCITATION_DETAIL = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses', 'ElectricMachineStatorToothLoadsExcitationDetail')


__docformat__ = 'restructuredtext en'
__all__ = ('ElectricMachineStatorToothLoadsExcitationDetail',)


class ElectricMachineStatorToothLoadsExcitationDetail(_5702.ElectricMachinePeriodicExcitationDetail):
    """ElectricMachineStatorToothLoadsExcitationDetail

    This is a mastapy class.
    """

    TYPE = _ELECTRIC_MACHINE_STATOR_TOOTH_LOADS_EXCITATION_DETAIL

    class _Cast_ElectricMachineStatorToothLoadsExcitationDetail:
        """Special nested class for casting ElectricMachineStatorToothLoadsExcitationDetail to subclasses."""

        def __init__(self, parent: 'ElectricMachineStatorToothLoadsExcitationDetail'):
            self._parent = parent

        @property
        def electric_machine_periodic_excitation_detail(self):
            return self._parent._cast(_5702.ElectricMachinePeriodicExcitationDetail)

        @property
        def periodic_excitation_with_reference_shaft(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5759
            
            return self._parent._cast(_5759.PeriodicExcitationWithReferenceShaft)

        @property
        def abstract_periodic_excitation_detail(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5649
            
            return self._parent._cast(_5649.AbstractPeriodicExcitationDetail)

        @property
        def electric_machine_stator_tooth_axial_loads_excitation_detail(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5708
            
            return self._parent._cast(_5708.ElectricMachineStatorToothAxialLoadsExcitationDetail)

        @property
        def electric_machine_stator_tooth_moments_excitation_detail(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5710
            
            return self._parent._cast(_5710.ElectricMachineStatorToothMomentsExcitationDetail)

        @property
        def electric_machine_stator_tooth_radial_loads_excitation_detail(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5711
            
            return self._parent._cast(_5711.ElectricMachineStatorToothRadialLoadsExcitationDetail)

        @property
        def electric_machine_stator_tooth_tangential_loads_excitation_detail(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5712
            
            return self._parent._cast(_5712.ElectricMachineStatorToothTangentialLoadsExcitationDetail)

        @property
        def electric_machine_stator_tooth_loads_excitation_detail(self) -> 'ElectricMachineStatorToothLoadsExcitationDetail':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ElectricMachineStatorToothLoadsExcitationDetail.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'ElectricMachineStatorToothLoadsExcitationDetail._Cast_ElectricMachineStatorToothLoadsExcitationDetail':
        return self._Cast_ElectricMachineStatorToothLoadsExcitationDetail(self)
