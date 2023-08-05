"""_826.py

CylindricalGearRootFilletStressResults
"""
from mastapy.gears.ltca import _840
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_ROOT_FILLET_STRESS_RESULTS = python_net_import('SMT.MastaAPI.Gears.LTCA', 'CylindricalGearRootFilletStressResults')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearRootFilletStressResults',)


class CylindricalGearRootFilletStressResults(_840.GearRootFilletStressResults):
    """CylindricalGearRootFilletStressResults

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_ROOT_FILLET_STRESS_RESULTS

    class _Cast_CylindricalGearRootFilletStressResults:
        """Special nested class for casting CylindricalGearRootFilletStressResults to subclasses."""

        def __init__(self, parent: 'CylindricalGearRootFilletStressResults'):
            self._parent = parent

        @property
        def gear_root_fillet_stress_results(self):
            return self._parent._cast(_840.GearRootFilletStressResults)

        @property
        def cylindrical_gear_root_fillet_stress_results(self) -> 'CylindricalGearRootFilletStressResults':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CylindricalGearRootFilletStressResults.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'CylindricalGearRootFilletStressResults._Cast_CylindricalGearRootFilletStressResults':
        return self._Cast_CylindricalGearRootFilletStressResults(self)
