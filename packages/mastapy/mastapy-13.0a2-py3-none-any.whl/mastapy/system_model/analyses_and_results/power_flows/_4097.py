"""_4097.py

PowerFlow
"""
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2811
from mastapy.system_model.analyses_and_results.analysis_cases import _7512
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows', 'PowerFlow')


__docformat__ = 'restructuredtext en'
__all__ = ('PowerFlow',)


class PowerFlow(_7512.StaticLoadAnalysisCase):
    """PowerFlow

    This is a mastapy class.
    """

    TYPE = _POWER_FLOW

    class _Cast_PowerFlow:
        """Special nested class for casting PowerFlow to subclasses."""

        def __init__(self, parent: 'PowerFlow'):
            self._parent = parent

        @property
        def static_load_analysis_case(self):
            return self._parent._cast(_7512.StaticLoadAnalysisCase)

        @property
        def analysis_case(self):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7497
            
            return self._parent._cast(_7497.AnalysisCase)

        @property
        def context(self):
            from mastapy.system_model.analyses_and_results import _2629
            
            return self._parent._cast(_2629.Context)

        @property
        def power_flow(self) -> 'PowerFlow':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'PowerFlow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def ratio(self) -> 'float':
        """float: 'Ratio' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Ratio

        if temp is None:
            return 0.0

        return temp

    @property
    def torsional_system_deflection(self) -> '_2811.TorsionalSystemDeflection':
        """TorsionalSystemDeflection: 'TorsionalSystemDeflection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TorsionalSystemDeflection

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'PowerFlow._Cast_PowerFlow':
        return self._Cast_PowerFlow(self)
