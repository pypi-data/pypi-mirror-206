"""_5759.py

PeriodicExcitationWithReferenceShaft
"""
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5649
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PERIODIC_EXCITATION_WITH_REFERENCE_SHAFT = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses', 'PeriodicExcitationWithReferenceShaft')


__docformat__ = 'restructuredtext en'
__all__ = ('PeriodicExcitationWithReferenceShaft',)


class PeriodicExcitationWithReferenceShaft(_5649.AbstractPeriodicExcitationDetail):
    """PeriodicExcitationWithReferenceShaft

    This is a mastapy class.
    """

    TYPE = _PERIODIC_EXCITATION_WITH_REFERENCE_SHAFT

    class _Cast_PeriodicExcitationWithReferenceShaft:
        """Special nested class for casting PeriodicExcitationWithReferenceShaft to subclasses."""

        def __init__(self, parent: 'PeriodicExcitationWithReferenceShaft'):
            self._parent = parent

        @property
        def abstract_periodic_excitation_detail(self):
            return self._parent._cast(_5649.AbstractPeriodicExcitationDetail)

        @property
        def electric_machine_periodic_excitation_detail(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5702
            
            return self._parent._cast(_5702.ElectricMachinePeriodicExcitationDetail)

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
        def general_periodic_excitation_detail(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5728
            
            return self._parent._cast(_5728.GeneralPeriodicExcitationDetail)

        @property
        def single_node_periodic_excitation_with_reference_shaft(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5776
            
            return self._parent._cast(_5776.SingleNodePeriodicExcitationWithReferenceShaft)

        @property
        def unbalanced_mass_excitation_detail(self):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import _5802
            
            return self._parent._cast(_5802.UnbalancedMassExcitationDetail)

        @property
        def periodic_excitation_with_reference_shaft(self) -> 'PeriodicExcitationWithReferenceShaft':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'PeriodicExcitationWithReferenceShaft.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'PeriodicExcitationWithReferenceShaft._Cast_PeriodicExcitationWithReferenceShaft':
        return self._Cast_PeriodicExcitationWithReferenceShaft(self)
