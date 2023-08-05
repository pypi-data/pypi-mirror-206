"""_1899.py

RaceDetail
"""
from mastapy.bearings.tolerances import _1893
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_RACE_DETAIL = python_net_import('SMT.MastaAPI.Bearings.Tolerances', 'RaceDetail')


__docformat__ = 'restructuredtext en'
__all__ = ('RaceDetail',)


class RaceDetail(_1893.InterferenceDetail):
    """RaceDetail

    This is a mastapy class.
    """

    TYPE = _RACE_DETAIL

    class _Cast_RaceDetail:
        """Special nested class for casting RaceDetail to subclasses."""

        def __init__(self, parent: 'RaceDetail'):
            self._parent = parent

        @property
        def interference_detail(self):
            return self._parent._cast(_1893.InterferenceDetail)

        @property
        def bearing_connection_component(self):
            from mastapy.bearings.tolerances import _1886
            
            return self._parent._cast(_1886.BearingConnectionComponent)

        @property
        def race_detail(self) -> 'RaceDetail':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'RaceDetail.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'RaceDetail._Cast_RaceDetail':
        return self._Cast_RaceDetail(self)
