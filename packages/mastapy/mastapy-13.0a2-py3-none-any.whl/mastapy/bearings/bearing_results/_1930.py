"""_1930.py

EquivalentLoadFactors
"""
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor
from mastapy.utility import _1575
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_EQUIVALENT_LOAD_FACTORS = python_net_import('SMT.MastaAPI.Bearings.BearingResults', 'EquivalentLoadFactors')


__docformat__ = 'restructuredtext en'
__all__ = ('EquivalentLoadFactors',)


class EquivalentLoadFactors(_1575.IndependentReportablePropertiesBase['EquivalentLoadFactors']):
    """EquivalentLoadFactors

    This is a mastapy class.
    """

    TYPE = _EQUIVALENT_LOAD_FACTORS

    class _Cast_EquivalentLoadFactors:
        """Special nested class for casting EquivalentLoadFactors to subclasses."""

        def __init__(self, parent: 'EquivalentLoadFactors'):
            self._parent = parent

        @property
        def independent_reportable_properties_base(self):
            from mastapy.bearings.bearing_results import _1930
            
            return self._parent._cast(_1575.IndependentReportablePropertiesBase)

        @property
        def equivalent_load_factors(self) -> 'EquivalentLoadFactors':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'EquivalentLoadFactors.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def axial_load_factor(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'AxialLoadFactor' is the original name of this property."""

        temp = self.wrapped.AxialLoadFactor

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @axial_load_factor.setter
    def axial_load_factor(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.AxialLoadFactor = value

    @property
    def radial_load_factor(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'RadialLoadFactor' is the original name of this property."""

        temp = self.wrapped.RadialLoadFactor

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @radial_load_factor.setter
    def radial_load_factor(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.RadialLoadFactor = value

    @property
    def cast_to(self) -> 'EquivalentLoadFactors._Cast_EquivalentLoadFactors':
        return self._Cast_EquivalentLoadFactors(self)
