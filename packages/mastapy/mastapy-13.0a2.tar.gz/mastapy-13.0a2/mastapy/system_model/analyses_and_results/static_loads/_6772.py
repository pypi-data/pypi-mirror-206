"""_6772.py

AbstractShaftLoadCase
"""
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor
from mastapy.system_model.part_model import _2415
from mastapy.system_model.analyses_and_results.static_loads import _6773
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'AbstractShaftLoadCase')


__docformat__ = 'restructuredtext en'
__all__ = ('AbstractShaftLoadCase',)


class AbstractShaftLoadCase(_6773.AbstractShaftOrHousingLoadCase):
    """AbstractShaftLoadCase

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_LOAD_CASE

    class _Cast_AbstractShaftLoadCase:
        """Special nested class for casting AbstractShaftLoadCase to subclasses."""

        def __init__(self, parent: 'AbstractShaftLoadCase'):
            self._parent = parent

        @property
        def abstract_shaft_or_housing_load_case(self):
            return self._parent._cast(_6773.AbstractShaftOrHousingLoadCase)

        @property
        def component_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6801
            
            return self._parent._cast(_6801.ComponentLoadCase)

        @property
        def part_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6892
            
            return self._parent._cast(_6892.PartLoadCase)

        @property
        def part_analysis(self):
            from mastapy.system_model.analyses_and_results import _2636
            
            return self._parent._cast(_2636.PartAnalysis)

        @property
        def design_entity_single_context_analysis(self):
            from mastapy.system_model.analyses_and_results import _2632
            
            return self._parent._cast(_2632.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(self):
            from mastapy.system_model.analyses_and_results import _2630
            
            return self._parent._cast(_2630.DesignEntityAnalysis)

        @property
        def cycloidal_disc_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6823
            
            return self._parent._cast(_6823.CycloidalDiscLoadCase)

        @property
        def shaft_load_case(self):
            from mastapy.system_model.analyses_and_results.static_loads import _6914
            
            return self._parent._cast(_6914.ShaftLoadCase)

        @property
        def abstract_shaft_load_case(self) -> 'AbstractShaftLoadCase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'AbstractShaftLoadCase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def shaft_temperature(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'ShaftTemperature' is the original name of this property."""

        temp = self.wrapped.ShaftTemperature

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @shaft_temperature.setter
    def shaft_temperature(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.ShaftTemperature = value

    @property
    def component_design(self) -> '_2415.AbstractShaft':
        """AbstractShaft: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'AbstractShaftLoadCase._Cast_AbstractShaftLoadCase':
        return self._Cast_AbstractShaftLoadCase(self)
