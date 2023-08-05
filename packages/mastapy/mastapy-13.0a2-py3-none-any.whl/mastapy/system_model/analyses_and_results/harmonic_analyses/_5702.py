"""_5702.py

ElectricMachinePeriodicExcitationDetail
"""
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5759
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ELECTRIC_MACHINE_PERIODIC_EXCITATION_DETAIL = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses', 'ElectricMachinePeriodicExcitationDetail')


__docformat__ = 'restructuredtext en'
__all__ = ('ElectricMachinePeriodicExcitationDetail',)


class ElectricMachinePeriodicExcitationDetail(_5759.PeriodicExcitationWithReferenceShaft):
    """ElectricMachinePeriodicExcitationDetail

    This is a mastapy class.
    """

    TYPE = _ELECTRIC_MACHINE_PERIODIC_EXCITATION_DETAIL

    class _Cast_ElectricMachinePeriodicExcitationDetail:
        """Special nested class for casting ElectricMachinePeriodicExcitationDetail to subclasses."""

        def __init__(self, parent: 'ElectricMachinePeriodicExcitationDetail'):
            self._parent = parent

        @property
        def periodic_excitation_with_reference_shaft(self):
            return self._parent._cast(_5759.PeriodicExcitationWithReferenceShaft)

        @property
        def abstract_periodic_excitation_detail(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5649
            
            return self._parent._cast(_5649.AbstractPeriodicExcitationDetail)

        @property
        def electric_machine_rotor_x_force_periodic_excitation_detail(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5703
            
            return self._parent._cast(_5703.ElectricMachineRotorXForcePeriodicExcitationDetail)

        @property
        def electric_machine_rotor_x_moment_periodic_excitation_detail(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5704
            
            return self._parent._cast(_5704.ElectricMachineRotorXMomentPeriodicExcitationDetail)

        @property
        def electric_machine_rotor_y_force_periodic_excitation_detail(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5705
            
            return self._parent._cast(_5705.ElectricMachineRotorYForcePeriodicExcitationDetail)

        @property
        def electric_machine_rotor_y_moment_periodic_excitation_detail(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5706
            
            return self._parent._cast(_5706.ElectricMachineRotorYMomentPeriodicExcitationDetail)

        @property
        def electric_machine_rotor_z_force_periodic_excitation_detail(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5707
            
            return self._parent._cast(_5707.ElectricMachineRotorZForcePeriodicExcitationDetail)

        @property
        def electric_machine_stator_tooth_axial_loads_excitation_detail(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5708
            
            return self._parent._cast(_5708.ElectricMachineStatorToothAxialLoadsExcitationDetail)

        @property
        def electric_machine_stator_tooth_loads_excitation_detail(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5709
            
            return self._parent._cast(_5709.ElectricMachineStatorToothLoadsExcitationDetail)

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
        def electric_machine_torque_ripple_periodic_excitation_detail(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5713
            
            return self._parent._cast(_5713.ElectricMachineTorqueRipplePeriodicExcitationDetail)

        @property
        def electric_machine_periodic_excitation_detail(self) -> 'ElectricMachinePeriodicExcitationDetail':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ElectricMachinePeriodicExcitationDetail.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'ElectricMachinePeriodicExcitationDetail._Cast_ElectricMachinePeriodicExcitationDetail':
        return self._Cast_ElectricMachinePeriodicExcitationDetail(self)
