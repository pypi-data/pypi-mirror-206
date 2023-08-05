"""_15.py

ProfilePointFilletStressConcentrationFactors
"""
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PROFILE_POINT_FILLET_STRESS_CONCENTRATION_FACTORS = python_net_import('SMT.MastaAPI.Shafts', 'ProfilePointFilletStressConcentrationFactors')


__docformat__ = 'restructuredtext en'
__all__ = ('ProfilePointFilletStressConcentrationFactors',)


class ProfilePointFilletStressConcentrationFactors(_0.APIBase):
    """ProfilePointFilletStressConcentrationFactors

    This is a mastapy class.
    """

    TYPE = _PROFILE_POINT_FILLET_STRESS_CONCENTRATION_FACTORS

    class _Cast_ProfilePointFilletStressConcentrationFactors:
        """Special nested class for casting ProfilePointFilletStressConcentrationFactors to subclasses."""

        def __init__(self, parent: 'ProfilePointFilletStressConcentrationFactors'):
            self._parent = parent

        @property
        def profile_point_fillet_stress_concentration_factors(self) -> 'ProfilePointFilletStressConcentrationFactors':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ProfilePointFilletStressConcentrationFactors.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def bending(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'Bending' is the original name of this property."""

        temp = self.wrapped.Bending

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @bending.setter
    def bending(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.Bending = value

    @property
    def tension(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'Tension' is the original name of this property."""

        temp = self.wrapped.Tension

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @tension.setter
    def tension(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.Tension = value

    @property
    def torsion(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'Torsion' is the original name of this property."""

        temp = self.wrapped.Torsion

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @torsion.setter
    def torsion(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.Torsion = value

    @property
    def cast_to(self) -> 'ProfilePointFilletStressConcentrationFactors._Cast_ProfilePointFilletStressConcentrationFactors':
        return self._Cast_ProfilePointFilletStressConcentrationFactors(self)
