"""_1449.py

NamedDiscPhase
"""
from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_NAMED_DISC_PHASE = python_net_import('SMT.MastaAPI.Cycloidal', 'NamedDiscPhase')


__docformat__ = 'restructuredtext en'
__all__ = ('NamedDiscPhase',)


class NamedDiscPhase(_0.APIBase):
    """NamedDiscPhase

    This is a mastapy class.
    """

    TYPE = _NAMED_DISC_PHASE

    class _Cast_NamedDiscPhase:
        """Special nested class for casting NamedDiscPhase to subclasses."""

        def __init__(self, parent: 'NamedDiscPhase'):
            self._parent = parent

        @property
        def named_disc_phase(self) -> 'NamedDiscPhase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'NamedDiscPhase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def disc_phase_angle(self) -> 'float':
        """float: 'DiscPhaseAngle' is the original name of this property."""

        temp = self.wrapped.DiscPhaseAngle

        if temp is None:
            return 0.0

        return temp

    @disc_phase_angle.setter
    def disc_phase_angle(self, value: 'float'):
        self.wrapped.DiscPhaseAngle = float(value) if value else 0.0

    @property
    def cast_to(self) -> 'NamedDiscPhase._Cast_NamedDiscPhase':
        return self._Cast_NamedDiscPhase(self)
