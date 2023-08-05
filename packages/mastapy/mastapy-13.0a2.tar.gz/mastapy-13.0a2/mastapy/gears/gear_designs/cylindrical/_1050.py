"""_1050.py

ISO6336GeometryForShapedGears
"""
from mastapy._internal import constructor
from mastapy.gears.gear_designs.cylindrical import _1049
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ISO6336_GEOMETRY_FOR_SHAPED_GEARS = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Cylindrical', 'ISO6336GeometryForShapedGears')


__docformat__ = 'restructuredtext en'
__all__ = ('ISO6336GeometryForShapedGears',)


class ISO6336GeometryForShapedGears(_1049.ISO6336GeometryBase):
    """ISO6336GeometryForShapedGears

    This is a mastapy class.
    """

    TYPE = _ISO6336_GEOMETRY_FOR_SHAPED_GEARS

    class _Cast_ISO6336GeometryForShapedGears:
        """Special nested class for casting ISO6336GeometryForShapedGears to subclasses."""

        def __init__(self, parent: 'ISO6336GeometryForShapedGears'):
            self._parent = parent

        @property
        def iso6336_geometry_base(self):
            return self._parent._cast(_1049.ISO6336GeometryBase)

        @property
        def iso6336_geometry_for_shaped_gears(self) -> 'ISO6336GeometryForShapedGears':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ISO6336GeometryForShapedGears.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def auxiliary_angle(self) -> 'float':
        """float: 'AuxiliaryAngle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AuxiliaryAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def base_radius_of_the_tool(self) -> 'float':
        """float: 'BaseRadiusOfTheTool' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BaseRadiusOfTheTool

        if temp is None:
            return 0.0

        return temp

    @property
    def cutting_pitch_radius_of_the_gear(self) -> 'float':
        """float: 'CuttingPitchRadiusOfTheGear' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CuttingPitchRadiusOfTheGear

        if temp is None:
            return 0.0

        return temp

    @property
    def cutting_pitch_radius_of_the_tool(self) -> 'float':
        """float: 'CuttingPitchRadiusOfTheTool' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CuttingPitchRadiusOfTheTool

        if temp is None:
            return 0.0

        return temp

    @property
    def distance_of_the_point_m_to_the_point_of_contact_of_the_pitch_circles(self) -> 'float':
        """float: 'DistanceOfThePointMToThePointOfContactOfThePitchCircles' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DistanceOfThePointMToThePointOfContactOfThePitchCircles

        if temp is None:
            return 0.0

        return temp

    @property
    def equivalent_numbers_of_teeth(self) -> 'float':
        """float: 'EquivalentNumbersOfTeeth' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.EquivalentNumbersOfTeeth

        if temp is None:
            return 0.0

        return temp

    @property
    def half_angle_of_thickness_at_point_m(self) -> 'float':
        """float: 'HalfAngleOfThicknessAtPointM' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HalfAngleOfThicknessAtPointM

        if temp is None:
            return 0.0

        return temp

    @property
    def manufacturing_centre_distance(self) -> 'float':
        """float: 'ManufacturingCentreDistance' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ManufacturingCentreDistance

        if temp is None:
            return 0.0

        return temp

    @property
    def manufacturing_tooth_ratio(self) -> 'float':
        """float: 'ManufacturingToothRatio' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ManufacturingToothRatio

        if temp is None:
            return 0.0

        return temp

    @property
    def radius_of_point_m(self) -> 'float':
        """float: 'RadiusOfPointM' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RadiusOfPointM

        if temp is None:
            return 0.0

        return temp

    @property
    def theta(self) -> 'float':
        """float: 'Theta' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Theta

        if temp is None:
            return 0.0

        return temp

    @property
    def tooth_root_fillet_radius(self) -> 'float':
        """float: 'ToothRootFilletRadius' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ToothRootFilletRadius

        if temp is None:
            return 0.0

        return temp

    @property
    def tooth_root_thickness(self) -> 'float':
        """float: 'ToothRootThickness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ToothRootThickness

        if temp is None:
            return 0.0

        return temp

    @property
    def transverse_pressure_angle_for_radius_of_point_m(self) -> 'float':
        """float: 'TransversePressureAngleForRadiusOfPointM' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TransversePressureAngleForRadiusOfPointM

        if temp is None:
            return 0.0

        return temp

    @property
    def virtual_tip_diameter_of_tool(self) -> 'float':
        """float: 'VirtualTipDiameterOfTool' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.VirtualTipDiameterOfTool

        if temp is None:
            return 0.0

        return temp

    @property
    def working_pressure_angle(self) -> 'float':
        """float: 'WorkingPressureAngle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WorkingPressureAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self) -> 'ISO6336GeometryForShapedGears._Cast_ISO6336GeometryForShapedGears':
        return self._Cast_ISO6336GeometryForShapedGears(self)
