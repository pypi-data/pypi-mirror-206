"""_559.py

SpiralBevelRateableMesh
"""
from mastapy._internal import constructor
from mastapy.gears.rating.agma_gleason_conical import _563
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPIRAL_BEVEL_RATEABLE_MESH = python_net_import('SMT.MastaAPI.Gears.Rating.Bevel.Standards', 'SpiralBevelRateableMesh')


__docformat__ = 'restructuredtext en'
__all__ = ('SpiralBevelRateableMesh',)


class SpiralBevelRateableMesh(_563.AGMAGleasonConicalRateableMesh):
    """SpiralBevelRateableMesh

    This is a mastapy class.
    """

    TYPE = _SPIRAL_BEVEL_RATEABLE_MESH

    class _Cast_SpiralBevelRateableMesh:
        """Special nested class for casting SpiralBevelRateableMesh to subclasses."""

        def __init__(self, parent: 'SpiralBevelRateableMesh'):
            self._parent = parent

        @property
        def agma_gleason_conical_rateable_mesh(self):
            return self._parent._cast(_563.AGMAGleasonConicalRateableMesh)

        @property
        def conical_rateable_mesh(self):
            from mastapy.gears.rating.conical import _542
            
            return self._parent._cast(_542.ConicalRateableMesh)

        @property
        def rateable_mesh(self):
            from mastapy.gears.rating import _363
            
            return self._parent._cast(_363.RateableMesh)

        @property
        def spiral_bevel_rateable_mesh(self) -> 'SpiralBevelRateableMesh':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'SpiralBevelRateableMesh.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def safety_factor_scoring(self) -> 'float':
        """float: 'SafetyFactorScoring' is the original name of this property."""

        temp = self.wrapped.SafetyFactorScoring

        if temp is None:
            return 0.0

        return temp

    @safety_factor_scoring.setter
    def safety_factor_scoring(self, value: 'float'):
        self.wrapped.SafetyFactorScoring = float(value) if value else 0.0

    @property
    def cast_to(self) -> 'SpiralBevelRateableMesh._Cast_SpiralBevelRateableMesh':
        return self._Cast_SpiralBevelRateableMesh(self)
