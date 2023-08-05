"""_2000.py

LoadedFourPointContactBallBearingElement
"""
from mastapy._internal import constructor
from mastapy.bearings.bearing_results.rolling import _2004
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_FOUR_POINT_CONTACT_BALL_BEARING_ELEMENT = python_net_import('SMT.MastaAPI.Bearings.BearingResults.Rolling', 'LoadedFourPointContactBallBearingElement')


__docformat__ = 'restructuredtext en'
__all__ = ('LoadedFourPointContactBallBearingElement',)


class LoadedFourPointContactBallBearingElement(_2004.LoadedMultiPointContactBallBearingElement):
    """LoadedFourPointContactBallBearingElement

    This is a mastapy class.
    """

    TYPE = _LOADED_FOUR_POINT_CONTACT_BALL_BEARING_ELEMENT

    class _Cast_LoadedFourPointContactBallBearingElement:
        """Special nested class for casting LoadedFourPointContactBallBearingElement to subclasses."""

        def __init__(self, parent: 'LoadedFourPointContactBallBearingElement'):
            self._parent = parent

        @property
        def loaded_multi_point_contact_ball_bearing_element(self):
            return self._parent._cast(_2004.LoadedMultiPointContactBallBearingElement)

        @property
        def loaded_ball_bearing_element(self):
            from mastapy.bearings.bearing_results.rolling import _1985
            
            return self._parent._cast(_1985.LoadedBallBearingElement)

        @property
        def loaded_element(self):
            from mastapy.bearings.bearing_results.rolling import _1999
            
            return self._parent._cast(_1999.LoadedElement)

        @property
        def loaded_four_point_contact_ball_bearing_element(self) -> 'LoadedFourPointContactBallBearingElement':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'LoadedFourPointContactBallBearingElement.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def approximate_percentage_of_friction_used_outer_left(self) -> 'float':
        """float: 'ApproximatePercentageOfFrictionUsedOuterLeft' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ApproximatePercentageOfFrictionUsedOuterLeft

        if temp is None:
            return 0.0

        return temp

    @property
    def approximate_percentage_of_friction_used_outer_right(self) -> 'float':
        """float: 'ApproximatePercentageOfFrictionUsedOuterRight' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ApproximatePercentageOfFrictionUsedOuterRight

        if temp is None:
            return 0.0

        return temp

    @property
    def contact_angle_outer_left(self) -> 'float':
        """float: 'ContactAngleOuterLeft' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ContactAngleOuterLeft

        if temp is None:
            return 0.0

        return temp

    @property
    def contact_angle_outer_right(self) -> 'float':
        """float: 'ContactAngleOuterRight' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ContactAngleOuterRight

        if temp is None:
            return 0.0

        return temp

    @property
    def curvature_moment_outer_left(self) -> 'float':
        """float: 'CurvatureMomentOuterLeft' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurvatureMomentOuterLeft

        if temp is None:
            return 0.0

        return temp

    @property
    def curvature_moment_outer_right(self) -> 'float':
        """float: 'CurvatureMomentOuterRight' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurvatureMomentOuterRight

        if temp is None:
            return 0.0

        return temp

    @property
    def hertzian_semi_major_dimension_outer_left(self) -> 'float':
        """float: 'HertzianSemiMajorDimensionOuterLeft' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HertzianSemiMajorDimensionOuterLeft

        if temp is None:
            return 0.0

        return temp

    @property
    def hertzian_semi_major_dimension_outer_right(self) -> 'float':
        """float: 'HertzianSemiMajorDimensionOuterRight' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HertzianSemiMajorDimensionOuterRight

        if temp is None:
            return 0.0

        return temp

    @property
    def hertzian_semi_minor_dimension_outer_left(self) -> 'float':
        """float: 'HertzianSemiMinorDimensionOuterLeft' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HertzianSemiMinorDimensionOuterLeft

        if temp is None:
            return 0.0

        return temp

    @property
    def hertzian_semi_minor_dimension_outer_right(self) -> 'float':
        """float: 'HertzianSemiMinorDimensionOuterRight' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HertzianSemiMinorDimensionOuterRight

        if temp is None:
            return 0.0

        return temp

    @property
    def hydrodynamic_rolling_resistance_force_outer_left(self) -> 'float':
        """float: 'HydrodynamicRollingResistanceForceOuterLeft' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HydrodynamicRollingResistanceForceOuterLeft

        if temp is None:
            return 0.0

        return temp

    @property
    def hydrodynamic_rolling_resistance_force_outer_right(self) -> 'float':
        """float: 'HydrodynamicRollingResistanceForceOuterRight' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HydrodynamicRollingResistanceForceOuterRight

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_normal_stress_outer_left(self) -> 'float':
        """float: 'MaximumNormalStressOuterLeft' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumNormalStressOuterLeft

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_normal_stress_outer_right(self) -> 'float':
        """float: 'MaximumNormalStressOuterRight' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumNormalStressOuterRight

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_normal_stress_outer(self) -> 'float':
        """float: 'MaximumNormalStressOuter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumNormalStressOuter

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_shear_stress_outer_left(self) -> 'float':
        """float: 'MaximumShearStressOuterLeft' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumShearStressOuterLeft

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_shear_stress_outer_right(self) -> 'float':
        """float: 'MaximumShearStressOuterRight' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumShearStressOuterRight

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_smearing_intensity_outer(self) -> 'float':
        """float: 'MaximumSmearingIntensityOuter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumSmearingIntensityOuter

        if temp is None:
            return 0.0

        return temp

    @property
    def minimum_lubricating_film_thickness_outer_left(self) -> 'float':
        """float: 'MinimumLubricatingFilmThicknessOuterLeft' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MinimumLubricatingFilmThicknessOuterLeft

        if temp is None:
            return 0.0

        return temp

    @property
    def minimum_lubricating_film_thickness_outer_right(self) -> 'float':
        """float: 'MinimumLubricatingFilmThicknessOuterRight' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MinimumLubricatingFilmThicknessOuterRight

        if temp is None:
            return 0.0

        return temp

    @property
    def minimum_lubricating_film_thickness_outer(self) -> 'float':
        """float: 'MinimumLubricatingFilmThicknessOuter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MinimumLubricatingFilmThicknessOuter

        if temp is None:
            return 0.0

        return temp

    @property
    def normal_load_outer_left(self) -> 'float':
        """float: 'NormalLoadOuterLeft' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NormalLoadOuterLeft

        if temp is None:
            return 0.0

        return temp

    @property
    def normal_load_outer_right(self) -> 'float':
        """float: 'NormalLoadOuterRight' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NormalLoadOuterRight

        if temp is None:
            return 0.0

        return temp

    @property
    def pivoting_moment_outer_left(self) -> 'float':
        """float: 'PivotingMomentOuterLeft' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PivotingMomentOuterLeft

        if temp is None:
            return 0.0

        return temp

    @property
    def pivoting_moment_outer_right(self) -> 'float':
        """float: 'PivotingMomentOuterRight' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PivotingMomentOuterRight

        if temp is None:
            return 0.0

        return temp

    @property
    def power_loss_outer_left(self) -> 'float':
        """float: 'PowerLossOuterLeft' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerLossOuterLeft

        if temp is None:
            return 0.0

        return temp

    @property
    def power_loss_outer_right(self) -> 'float':
        """float: 'PowerLossOuterRight' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerLossOuterRight

        if temp is None:
            return 0.0

        return temp

    @property
    def power_loss_due_to_elastic_rolling_resistance_outer_left(self) -> 'float':
        """float: 'PowerLossDueToElasticRollingResistanceOuterLeft' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerLossDueToElasticRollingResistanceOuterLeft

        if temp is None:
            return 0.0

        return temp

    @property
    def power_loss_due_to_elastic_rolling_resistance_outer_right(self) -> 'float':
        """float: 'PowerLossDueToElasticRollingResistanceOuterRight' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerLossDueToElasticRollingResistanceOuterRight

        if temp is None:
            return 0.0

        return temp

    @property
    def power_loss_due_to_hydrodynamic_rolling_resistance_outer_left(self) -> 'float':
        """float: 'PowerLossDueToHydrodynamicRollingResistanceOuterLeft' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerLossDueToHydrodynamicRollingResistanceOuterLeft

        if temp is None:
            return 0.0

        return temp

    @property
    def power_loss_due_to_hydrodynamic_rolling_resistance_outer_right(self) -> 'float':
        """float: 'PowerLossDueToHydrodynamicRollingResistanceOuterRight' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerLossDueToHydrodynamicRollingResistanceOuterRight

        if temp is None:
            return 0.0

        return temp

    @property
    def power_loss_parallel_to_major_axis_outer_left(self) -> 'float':
        """float: 'PowerLossParallelToMajorAxisOuterLeft' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerLossParallelToMajorAxisOuterLeft

        if temp is None:
            return 0.0

        return temp

    @property
    def power_loss_parallel_to_major_axis_outer_right(self) -> 'float':
        """float: 'PowerLossParallelToMajorAxisOuterRight' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerLossParallelToMajorAxisOuterRight

        if temp is None:
            return 0.0

        return temp

    @property
    def power_loss_parallel_to_minor_axis_outer_left(self) -> 'float':
        """float: 'PowerLossParallelToMinorAxisOuterLeft' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerLossParallelToMinorAxisOuterLeft

        if temp is None:
            return 0.0

        return temp

    @property
    def power_loss_parallel_to_minor_axis_outer_right(self) -> 'float':
        """float: 'PowerLossParallelToMinorAxisOuterRight' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerLossParallelToMinorAxisOuterRight

        if temp is None:
            return 0.0

        return temp

    @property
    def sliding_force_parallel_to_the_major_axis_outer_left(self) -> 'float':
        """float: 'SlidingForceParallelToTheMajorAxisOuterLeft' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SlidingForceParallelToTheMajorAxisOuterLeft

        if temp is None:
            return 0.0

        return temp

    @property
    def sliding_force_parallel_to_the_major_axis_outer_right(self) -> 'float':
        """float: 'SlidingForceParallelToTheMajorAxisOuterRight' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SlidingForceParallelToTheMajorAxisOuterRight

        if temp is None:
            return 0.0

        return temp

    @property
    def sliding_force_parallel_to_the_minor_axis_outer_left(self) -> 'float':
        """float: 'SlidingForceParallelToTheMinorAxisOuterLeft' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SlidingForceParallelToTheMinorAxisOuterLeft

        if temp is None:
            return 0.0

        return temp

    @property
    def sliding_force_parallel_to_the_minor_axis_outer_right(self) -> 'float':
        """float: 'SlidingForceParallelToTheMinorAxisOuterRight' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SlidingForceParallelToTheMinorAxisOuterRight

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self) -> 'LoadedFourPointContactBallBearingElement._Cast_LoadedFourPointContactBallBearingElement':
        return self._Cast_LoadedFourPointContactBallBearingElement(self)
