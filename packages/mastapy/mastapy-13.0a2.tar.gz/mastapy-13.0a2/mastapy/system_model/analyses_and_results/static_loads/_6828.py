"""_6828.py

CylindricalGearSetHarmonicLoadData
"""
from mastapy.system_model.analyses_and_results.static_loads import _6858
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_SET_HARMONIC_LOAD_DATA = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'CylindricalGearSetHarmonicLoadData')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearSetHarmonicLoadData',)


class CylindricalGearSetHarmonicLoadData(_6858.GearSetHarmonicLoadData):
    """CylindricalGearSetHarmonicLoadData

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_SET_HARMONIC_LOAD_DATA

    class _Cast_CylindricalGearSetHarmonicLoadData:
        """Special nested class for casting CylindricalGearSetHarmonicLoadData to subclasses."""

        def __init__(self, parent: 'CylindricalGearSetHarmonicLoadData'):
            self._parent = parent

        @property
        def gear_set_harmonic_load_data(self):
            return self._parent._cast(_6858.GearSetHarmonicLoadData)

        @property
        def harmonic_load_data_base(self):
            from mastapy.electric_machines.harmonic_load_data import _1368
            
            return self._parent._cast(_1368.HarmonicLoadDataBase)

        @property
        def cylindrical_gear_set_harmonic_load_data(self) -> 'CylindricalGearSetHarmonicLoadData':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CylindricalGearSetHarmonicLoadData.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'CylindricalGearSetHarmonicLoadData._Cast_CylindricalGearSetHarmonicLoadData':
        return self._Cast_CylindricalGearSetHarmonicLoadData(self)
