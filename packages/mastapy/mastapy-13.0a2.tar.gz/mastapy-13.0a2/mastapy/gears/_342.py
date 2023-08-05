"""_342.py

SpecificationForTheEffectOfOilKinematicViscosity
"""
from mastapy._internal import constructor
from mastapy.utility import _1575
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPECIFICATION_FOR_THE_EFFECT_OF_OIL_KINEMATIC_VISCOSITY = python_net_import('SMT.MastaAPI.Gears', 'SpecificationForTheEffectOfOilKinematicViscosity')


__docformat__ = 'restructuredtext en'
__all__ = ('SpecificationForTheEffectOfOilKinematicViscosity',)


class SpecificationForTheEffectOfOilKinematicViscosity(_1575.IndependentReportablePropertiesBase['SpecificationForTheEffectOfOilKinematicViscosity']):
    """SpecificationForTheEffectOfOilKinematicViscosity

    This is a mastapy class.
    """

    TYPE = _SPECIFICATION_FOR_THE_EFFECT_OF_OIL_KINEMATIC_VISCOSITY

    class _Cast_SpecificationForTheEffectOfOilKinematicViscosity:
        """Special nested class for casting SpecificationForTheEffectOfOilKinematicViscosity to subclasses."""

        def __init__(self, parent: 'SpecificationForTheEffectOfOilKinematicViscosity'):
            self._parent = parent

        @property
        def independent_reportable_properties_base(self):
            from mastapy.gears import _342
            
            return self._parent._cast(_1575.IndependentReportablePropertiesBase)

        @property
        def specification_for_the_effect_of_oil_kinematic_viscosity(self) -> 'SpecificationForTheEffectOfOilKinematicViscosity':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'SpecificationForTheEffectOfOilKinematicViscosity.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def condition(self) -> 'str':
        """str: 'Condition' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Condition

        if temp is None:
            return ''

        return temp

    @property
    def intercept_of_linear_equation(self) -> 'float':
        """float: 'InterceptOfLinearEquation' is the original name of this property."""

        temp = self.wrapped.InterceptOfLinearEquation

        if temp is None:
            return 0.0

        return temp

    @intercept_of_linear_equation.setter
    def intercept_of_linear_equation(self, value: 'float'):
        self.wrapped.InterceptOfLinearEquation = float(value) if value else 0.0

    @property
    def slope_of_linear_equation(self) -> 'float':
        """float: 'SlopeOfLinearEquation' is the original name of this property."""

        temp = self.wrapped.SlopeOfLinearEquation

        if temp is None:
            return 0.0

        return temp

    @slope_of_linear_equation.setter
    def slope_of_linear_equation(self, value: 'float'):
        self.wrapped.SlopeOfLinearEquation = float(value) if value else 0.0

    @property
    def cast_to(self) -> 'SpecificationForTheEffectOfOilKinematicViscosity._Cast_SpecificationForTheEffectOfOilKinematicViscosity':
        return self._Cast_SpecificationForTheEffectOfOilKinematicViscosity(self)
