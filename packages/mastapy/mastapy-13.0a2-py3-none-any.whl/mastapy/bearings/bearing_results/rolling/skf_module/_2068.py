"""_2068.py

Friction
"""
from mastapy._internal import constructor
from mastapy.bearings.bearing_results.rolling.skf_module import _2070, _2069, _2081
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FRICTION = python_net_import('SMT.MastaAPI.Bearings.BearingResults.Rolling.SkfModule', 'Friction')


__docformat__ = 'restructuredtext en'
__all__ = ('Friction',)


class Friction(_2081.SKFCalculationResult):
    """Friction

    This is a mastapy class.
    """

    TYPE = _FRICTION

    class _Cast_Friction:
        """Special nested class for casting Friction to subclasses."""

        def __init__(self, parent: 'Friction'):
            self._parent = parent

        @property
        def skf_calculation_result(self):
            return self._parent._cast(_2081.SKFCalculationResult)

        @property
        def friction(self) -> 'Friction':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'Friction.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def power_loss(self) -> 'float':
        """float: 'PowerLoss' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerLoss

        if temp is None:
            return 0.0

        return temp

    @property
    def friction_sources(self) -> '_2070.FrictionSources':
        """FrictionSources: 'FrictionSources' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FrictionSources

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def frictional_moment(self) -> '_2069.FrictionalMoment':
        """FrictionalMoment: 'FrictionalMoment' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FrictionalMoment

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'Friction._Cast_Friction':
        return self._Cast_Friction(self)
