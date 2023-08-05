"""_1410.py

SAESplineTolerances
"""
from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SAE_SPLINE_TOLERANCES = python_net_import('SMT.MastaAPI.DetailedRigidConnectors.Splines.TolerancesAndDeviations', 'SAESplineTolerances')


__docformat__ = 'restructuredtext en'
__all__ = ('SAESplineTolerances',)


class SAESplineTolerances(_0.APIBase):
    """SAESplineTolerances

    This is a mastapy class.
    """

    TYPE = _SAE_SPLINE_TOLERANCES

    class _Cast_SAESplineTolerances:
        """Special nested class for casting SAESplineTolerances to subclasses."""

        def __init__(self, parent: 'SAESplineTolerances'):
            self._parent = parent

        @property
        def sae_spline_tolerances(self) -> 'SAESplineTolerances':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'SAESplineTolerances.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def internal_major_diameter_tolerance(self) -> 'float':
        """float: 'InternalMajorDiameterTolerance' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InternalMajorDiameterTolerance

        if temp is None:
            return 0.0

        return temp

    @property
    def lead_variation(self) -> 'float':
        """float: 'LeadVariation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LeadVariation

        if temp is None:
            return 0.0

        return temp

    @property
    def machining_variation(self) -> 'float':
        """float: 'MachiningVariation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MachiningVariation

        if temp is None:
            return 0.0

        return temp

    @property
    def major_diameter_tolerance(self) -> 'float':
        """float: 'MajorDiameterTolerance' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MajorDiameterTolerance

        if temp is None:
            return 0.0

        return temp

    @property
    def minor_diameter_tolerance(self) -> 'float':
        """float: 'MinorDiameterTolerance' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MinorDiameterTolerance

        if temp is None:
            return 0.0

        return temp

    @property
    def multiplier_f(self) -> 'float':
        """float: 'MultiplierF' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MultiplierF

        if temp is None:
            return 0.0

        return temp

    @property
    def profile_variation_f_fm(self) -> 'float':
        """float: 'ProfileVariationF_fm' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ProfileVariationF_fm

        if temp is None:
            return 0.0

        return temp

    @property
    def profile_variation_f_fp(self) -> 'float':
        """float: 'ProfileVariationF_fp' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ProfileVariationF_fp

        if temp is None:
            return 0.0

        return temp

    @property
    def total_index_variation(self) -> 'float':
        """float: 'TotalIndexVariation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TotalIndexVariation

        if temp is None:
            return 0.0

        return temp

    @property
    def variation_tolerance(self) -> 'float':
        """float: 'VariationTolerance' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.VariationTolerance

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self) -> 'SAESplineTolerances._Cast_SAESplineTolerances':
        return self._Cast_SAESplineTolerances(self)
