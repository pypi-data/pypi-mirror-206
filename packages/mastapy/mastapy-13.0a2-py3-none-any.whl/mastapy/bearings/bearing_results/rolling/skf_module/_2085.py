"""_2085.py

Viscosities
"""
from mastapy._internal import constructor
from mastapy.bearings.bearing_results.rolling.skf_module import _2077, _2081
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_VISCOSITIES = python_net_import('SMT.MastaAPI.Bearings.BearingResults.Rolling.SkfModule', 'Viscosities')


__docformat__ = 'restructuredtext en'
__all__ = ('Viscosities',)


class Viscosities(_2081.SKFCalculationResult):
    """Viscosities

    This is a mastapy class.
    """

    TYPE = _VISCOSITIES

    class _Cast_Viscosities:
        """Special nested class for casting Viscosities to subclasses."""

        def __init__(self, parent: 'Viscosities'):
            self._parent = parent

        @property
        def skf_calculation_result(self):
            return self._parent._cast(_2081.SKFCalculationResult)

        @property
        def viscosities(self) -> 'Viscosities':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'Viscosities.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def viscosity_ratio(self) -> 'float':
        """float: 'ViscosityRatio' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ViscosityRatio

        if temp is None:
            return 0.0

        return temp

    @property
    def operating_viscosity(self) -> '_2077.OperatingViscosity':
        """OperatingViscosity: 'OperatingViscosity' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OperatingViscosity

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'Viscosities._Cast_Viscosities':
        return self._Cast_Viscosities(self)
