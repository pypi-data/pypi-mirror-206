"""_4698.py

ShaftPerModeResult
"""
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses.reporting import _4691
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_PER_MODE_RESULT = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Reporting', 'ShaftPerModeResult')


__docformat__ = 'restructuredtext en'
__all__ = ('ShaftPerModeResult',)


class ShaftPerModeResult(_4691.ComponentPerModeResult):
    """ShaftPerModeResult

    This is a mastapy class.
    """

    TYPE = _SHAFT_PER_MODE_RESULT

    class _Cast_ShaftPerModeResult:
        """Special nested class for casting ShaftPerModeResult to subclasses."""

        def __init__(self, parent: 'ShaftPerModeResult'):
            self._parent = parent

        @property
        def component_per_mode_result(self):
            return self._parent._cast(_4691.ComponentPerModeResult)

        @property
        def shaft_per_mode_result(self) -> 'ShaftPerModeResult':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ShaftPerModeResult.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def torsional_mode_shape(self) -> 'float':
        """float: 'TorsionalModeShape' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TorsionalModeShape

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self) -> 'ShaftPerModeResult._Cast_ShaftPerModeResult':
        return self._Cast_ShaftPerModeResult(self)
