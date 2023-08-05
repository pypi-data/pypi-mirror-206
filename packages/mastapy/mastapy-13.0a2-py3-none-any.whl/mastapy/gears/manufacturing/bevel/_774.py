"""_774.py

ConicalMeshedGearManufacturingAnalysis
"""
from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_MESHED_GEAR_MANUFACTURING_ANALYSIS = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Bevel', 'ConicalMeshedGearManufacturingAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('ConicalMeshedGearManufacturingAnalysis',)


class ConicalMeshedGearManufacturingAnalysis(_0.APIBase):
    """ConicalMeshedGearManufacturingAnalysis

    This is a mastapy class.
    """

    TYPE = _CONICAL_MESHED_GEAR_MANUFACTURING_ANALYSIS

    class _Cast_ConicalMeshedGearManufacturingAnalysis:
        """Special nested class for casting ConicalMeshedGearManufacturingAnalysis to subclasses."""

        def __init__(self, parent: 'ConicalMeshedGearManufacturingAnalysis'):
            self._parent = parent

        @property
        def conical_meshed_gear_manufacturing_analysis(self) -> 'ConicalMeshedGearManufacturingAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ConicalMeshedGearManufacturingAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

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
    def cast_to(self) -> 'ConicalMeshedGearManufacturingAnalysis._Cast_ConicalMeshedGearManufacturingAnalysis':
        return self._Cast_ConicalMeshedGearManufacturingAnalysis(self)
