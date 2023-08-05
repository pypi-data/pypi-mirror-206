"""_2388.py

RaceBearingFEWithSelection
"""
from mastapy.math_utility import _1488
from mastapy._internal import constructor
from mastapy.system_model.fe import _2386, _2341
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_RACE_BEARING_FE_WITH_SELECTION = python_net_import('SMT.MastaAPI.SystemModel.FE', 'RaceBearingFEWithSelection')


__docformat__ = 'restructuredtext en'
__all__ = ('RaceBearingFEWithSelection',)


class RaceBearingFEWithSelection(_2341.BaseFEWithSelection):
    """RaceBearingFEWithSelection

    This is a mastapy class.
    """

    TYPE = _RACE_BEARING_FE_WITH_SELECTION

    class _Cast_RaceBearingFEWithSelection:
        """Special nested class for casting RaceBearingFEWithSelection to subclasses."""

        def __init__(self, parent: 'RaceBearingFEWithSelection'):
            self._parent = parent

        @property
        def base_fe_with_selection(self):
            return self._parent._cast(_2341.BaseFEWithSelection)

        @property
        def race_bearing_fe_with_selection(self) -> 'RaceBearingFEWithSelection':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'RaceBearingFEWithSelection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def manual_alignment(self) -> '_1488.CoordinateSystemEditor':
        """CoordinateSystemEditor: 'ManualAlignment' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ManualAlignment

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def race_bearing(self) -> '_2386.RaceBearingFE':
        """RaceBearingFE: 'RaceBearing' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RaceBearing

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'RaceBearingFEWithSelection._Cast_RaceBearingFEWithSelection':
        return self._Cast_RaceBearingFEWithSelection(self)
