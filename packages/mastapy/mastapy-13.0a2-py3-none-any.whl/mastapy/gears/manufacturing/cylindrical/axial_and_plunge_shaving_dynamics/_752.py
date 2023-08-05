"""_752.py

PlungeShaverRedressing
"""
from mastapy.gears.manufacturing.cylindrical.axial_and_plunge_shaving_dynamics import _759, _750
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLUNGE_SHAVER_REDRESSING = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Cylindrical.AxialAndPlungeShavingDynamics', 'PlungeShaverRedressing')


__docformat__ = 'restructuredtext en'
__all__ = ('PlungeShaverRedressing',)


class PlungeShaverRedressing(_759.ShaverRedressing['_750.PlungeShaverDynamics']):
    """PlungeShaverRedressing

    This is a mastapy class.
    """

    TYPE = _PLUNGE_SHAVER_REDRESSING

    class _Cast_PlungeShaverRedressing:
        """Special nested class for casting PlungeShaverRedressing to subclasses."""

        def __init__(self, parent: 'PlungeShaverRedressing'):
            self._parent = parent

        @property
        def shaver_redressing(self):
            return self._parent._cast(_759.ShaverRedressing)

        @property
        def plunge_shaver_redressing(self) -> 'PlungeShaverRedressing':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'PlungeShaverRedressing.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'PlungeShaverRedressing._Cast_PlungeShaverRedressing':
        return self._Cast_PlungeShaverRedressing(self)
