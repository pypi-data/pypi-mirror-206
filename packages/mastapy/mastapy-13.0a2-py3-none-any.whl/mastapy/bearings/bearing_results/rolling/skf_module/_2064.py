"""_2064.py

BearingRatingLife
"""
from mastapy._internal import constructor
from mastapy.bearings.bearing_results.rolling.skf_module import _2075, _2081
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEARING_RATING_LIFE = python_net_import('SMT.MastaAPI.Bearings.BearingResults.Rolling.SkfModule', 'BearingRatingLife')


__docformat__ = 'restructuredtext en'
__all__ = ('BearingRatingLife',)


class BearingRatingLife(_2081.SKFCalculationResult):
    """BearingRatingLife

    This is a mastapy class.
    """

    TYPE = _BEARING_RATING_LIFE

    class _Cast_BearingRatingLife:
        """Special nested class for casting BearingRatingLife to subclasses."""

        def __init__(self, parent: 'BearingRatingLife'):
            self._parent = parent

        @property
        def skf_calculation_result(self):
            return self._parent._cast(_2081.SKFCalculationResult)

        @property
        def bearing_rating_life(self) -> 'BearingRatingLife':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'BearingRatingLife.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def contamination_factor(self) -> 'float':
        """float: 'ContaminationFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ContaminationFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def skf_life_modification_factor(self) -> 'float':
        """float: 'SKFLifeModificationFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SKFLifeModificationFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def life_model(self) -> '_2075.LifeModel':
        """LifeModel: 'LifeModel' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LifeModel

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'BearingRatingLife._Cast_BearingRatingLife':
        return self._Cast_BearingRatingLife(self)
