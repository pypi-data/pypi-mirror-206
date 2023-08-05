"""_5705.py

ElectricMachineRotorYForcePeriodicExcitationDetail
"""
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5702
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ELECTRIC_MACHINE_ROTOR_Y_FORCE_PERIODIC_EXCITATION_DETAIL = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses', 'ElectricMachineRotorYForcePeriodicExcitationDetail')


__docformat__ = 'restructuredtext en'
__all__ = ('ElectricMachineRotorYForcePeriodicExcitationDetail',)


class ElectricMachineRotorYForcePeriodicExcitationDetail(_5702.ElectricMachinePeriodicExcitationDetail):
    """ElectricMachineRotorYForcePeriodicExcitationDetail

    This is a mastapy class.
    """

    TYPE = _ELECTRIC_MACHINE_ROTOR_Y_FORCE_PERIODIC_EXCITATION_DETAIL

    class _Cast_ElectricMachineRotorYForcePeriodicExcitationDetail:
        """Special nested class for casting ElectricMachineRotorYForcePeriodicExcitationDetail to subclasses."""

        def __init__(self, parent: 'ElectricMachineRotorYForcePeriodicExcitationDetail'):
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
        def electric_machine_rotor_y_force_periodic_excitation_detail(self) -> 'ElectricMachineRotorYForcePeriodicExcitationDetail':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ElectricMachineRotorYForcePeriodicExcitationDetail.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'ElectricMachineRotorYForcePeriodicExcitationDetail._Cast_ElectricMachineRotorYForcePeriodicExcitationDetail':
        return self._Cast_ElectricMachineRotorYForcePeriodicExcitationDetail(self)
