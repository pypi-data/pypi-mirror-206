"""_2438.py

InnerBearingRaceMountingOptions
"""
from mastapy.system_model.part_model import _2421
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INNER_BEARING_RACE_MOUNTING_OPTIONS = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'InnerBearingRaceMountingOptions')


__docformat__ = 'restructuredtext en'
__all__ = ('InnerBearingRaceMountingOptions',)


class InnerBearingRaceMountingOptions(_2421.BearingRaceMountingOptions):
    """InnerBearingRaceMountingOptions

    This is a mastapy class.
    """

    TYPE = _INNER_BEARING_RACE_MOUNTING_OPTIONS

    class _Cast_InnerBearingRaceMountingOptions:
        """Special nested class for casting InnerBearingRaceMountingOptions to subclasses."""

        def __init__(self, parent: 'InnerBearingRaceMountingOptions'):
            self._parent = parent

        @property
        def bearing_race_mounting_options(self):
            return self._parent._cast(_2421.BearingRaceMountingOptions)

        @property
        def inner_bearing_race_mounting_options(self) -> 'InnerBearingRaceMountingOptions':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'InnerBearingRaceMountingOptions.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'InnerBearingRaceMountingOptions._Cast_InnerBearingRaceMountingOptions':
        return self._Cast_InnerBearingRaceMountingOptions(self)
