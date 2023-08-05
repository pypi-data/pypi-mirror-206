"""_2065.py

DynamicAxialLoadCarryingCapacity
"""
from mastapy.bearings.bearing_results.rolling.skf_module import _2078, _2081
from mastapy._internal import constructor
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DYNAMIC_AXIAL_LOAD_CARRYING_CAPACITY = python_net_import('SMT.MastaAPI.Bearings.BearingResults.Rolling.SkfModule', 'DynamicAxialLoadCarryingCapacity')


__docformat__ = 'restructuredtext en'
__all__ = ('DynamicAxialLoadCarryingCapacity',)


class DynamicAxialLoadCarryingCapacity(_2081.SKFCalculationResult):
    """DynamicAxialLoadCarryingCapacity

    This is a mastapy class.
    """

    TYPE = _DYNAMIC_AXIAL_LOAD_CARRYING_CAPACITY

    class _Cast_DynamicAxialLoadCarryingCapacity:
        """Special nested class for casting DynamicAxialLoadCarryingCapacity to subclasses."""

        def __init__(self, parent: 'DynamicAxialLoadCarryingCapacity'):
            self._parent = parent

        @property
        def skf_calculation_result(self):
            return self._parent._cast(_2081.SKFCalculationResult)

        @property
        def dynamic_axial_load_carrying_capacity(self) -> 'DynamicAxialLoadCarryingCapacity':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'DynamicAxialLoadCarryingCapacity.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def permissible_axial_load(self) -> '_2078.PermissibleAxialLoad':
        """PermissibleAxialLoad: 'PermissibleAxialLoad' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PermissibleAxialLoad

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'DynamicAxialLoadCarryingCapacity._Cast_DynamicAxialLoadCarryingCapacity':
        return self._Cast_DynamicAxialLoadCarryingCapacity(self)
