"""_1594.py

MeasurementBase
"""
from typing import List

from mastapy._internal.implicit import overridable, list_with_selected_item
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy.utility.units_and_measurements import _1599
from mastapy.utility import _1587
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MEASUREMENT_BASE = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements', 'MeasurementBase')


__docformat__ = 'restructuredtext en'
__all__ = ('MeasurementBase',)


class MeasurementBase(_0.APIBase):
    """MeasurementBase

    This is a mastapy class.
    """

    TYPE = _MEASUREMENT_BASE

    class _Cast_MeasurementBase:
        """Special nested class for casting MeasurementBase to subclasses."""

        def __init__(self, parent: 'MeasurementBase'):
            self._parent = parent

        @property
        def acceleration(self):
            from mastapy.utility.units_and_measurements.measurements import _1601
            
            return self._parent._cast(_1601.Acceleration)

        @property
        def angle(self):
            from mastapy.utility.units_and_measurements.measurements import _1602
            
            return self._parent._cast(_1602.Angle)

        @property
        def angle_per_unit_temperature(self):
            from mastapy.utility.units_and_measurements.measurements import _1603
            
            return self._parent._cast(_1603.AnglePerUnitTemperature)

        @property
        def angle_small(self):
            from mastapy.utility.units_and_measurements.measurements import _1604
            
            return self._parent._cast(_1604.AngleSmall)

        @property
        def angle_very_small(self):
            from mastapy.utility.units_and_measurements.measurements import _1605
            
            return self._parent._cast(_1605.AngleVerySmall)

        @property
        def angular_acceleration(self):
            from mastapy.utility.units_and_measurements.measurements import _1606
            
            return self._parent._cast(_1606.AngularAcceleration)

        @property
        def angular_compliance(self):
            from mastapy.utility.units_and_measurements.measurements import _1607
            
            return self._parent._cast(_1607.AngularCompliance)

        @property
        def angular_jerk(self):
            from mastapy.utility.units_and_measurements.measurements import _1608
            
            return self._parent._cast(_1608.AngularJerk)

        @property
        def angular_stiffness(self):
            from mastapy.utility.units_and_measurements.measurements import _1609
            
            return self._parent._cast(_1609.AngularStiffness)

        @property
        def angular_velocity(self):
            from mastapy.utility.units_and_measurements.measurements import _1610
            
            return self._parent._cast(_1610.AngularVelocity)

        @property
        def area(self):
            from mastapy.utility.units_and_measurements.measurements import _1611
            
            return self._parent._cast(_1611.Area)

        @property
        def area_small(self):
            from mastapy.utility.units_and_measurements.measurements import _1612
            
            return self._parent._cast(_1612.AreaSmall)

        @property
        def carbon_emission_factor(self):
            from mastapy.utility.units_and_measurements.measurements import _1613
            
            return self._parent._cast(_1613.CarbonEmissionFactor)

        @property
        def current_density(self):
            from mastapy.utility.units_and_measurements.measurements import _1614
            
            return self._parent._cast(_1614.CurrentDensity)

        @property
        def current_per_length(self):
            from mastapy.utility.units_and_measurements.measurements import _1615
            
            return self._parent._cast(_1615.CurrentPerLength)

        @property
        def cycles(self):
            from mastapy.utility.units_and_measurements.measurements import _1616
            
            return self._parent._cast(_1616.Cycles)

        @property
        def damage(self):
            from mastapy.utility.units_and_measurements.measurements import _1617
            
            return self._parent._cast(_1617.Damage)

        @property
        def damage_rate(self):
            from mastapy.utility.units_and_measurements.measurements import _1618
            
            return self._parent._cast(_1618.DamageRate)

        @property
        def data_size(self):
            from mastapy.utility.units_and_measurements.measurements import _1619
            
            return self._parent._cast(_1619.DataSize)

        @property
        def decibel(self):
            from mastapy.utility.units_and_measurements.measurements import _1620
            
            return self._parent._cast(_1620.Decibel)

        @property
        def density(self):
            from mastapy.utility.units_and_measurements.measurements import _1621
            
            return self._parent._cast(_1621.Density)

        @property
        def electrical_resistance(self):
            from mastapy.utility.units_and_measurements.measurements import _1622
            
            return self._parent._cast(_1622.ElectricalResistance)

        @property
        def electrical_resistivity(self):
            from mastapy.utility.units_and_measurements.measurements import _1623
            
            return self._parent._cast(_1623.ElectricalResistivity)

        @property
        def electric_current(self):
            from mastapy.utility.units_and_measurements.measurements import _1624
            
            return self._parent._cast(_1624.ElectricCurrent)

        @property
        def energy(self):
            from mastapy.utility.units_and_measurements.measurements import _1625
            
            return self._parent._cast(_1625.Energy)

        @property
        def energy_per_unit_area(self):
            from mastapy.utility.units_and_measurements.measurements import _1626
            
            return self._parent._cast(_1626.EnergyPerUnitArea)

        @property
        def energy_per_unit_area_small(self):
            from mastapy.utility.units_and_measurements.measurements import _1627
            
            return self._parent._cast(_1627.EnergyPerUnitAreaSmall)

        @property
        def energy_small(self):
            from mastapy.utility.units_and_measurements.measurements import _1628
            
            return self._parent._cast(_1628.EnergySmall)

        @property
        def enum(self):
            from mastapy.utility.units_and_measurements.measurements import _1629
            
            return self._parent._cast(_1629.Enum)

        @property
        def flow_rate(self):
            from mastapy.utility.units_and_measurements.measurements import _1630
            
            return self._parent._cast(_1630.FlowRate)

        @property
        def force(self):
            from mastapy.utility.units_and_measurements.measurements import _1631
            
            return self._parent._cast(_1631.Force)

        @property
        def force_per_unit_length(self):
            from mastapy.utility.units_and_measurements.measurements import _1632
            
            return self._parent._cast(_1632.ForcePerUnitLength)

        @property
        def force_per_unit_pressure(self):
            from mastapy.utility.units_and_measurements.measurements import _1633
            
            return self._parent._cast(_1633.ForcePerUnitPressure)

        @property
        def force_per_unit_temperature(self):
            from mastapy.utility.units_and_measurements.measurements import _1634
            
            return self._parent._cast(_1634.ForcePerUnitTemperature)

        @property
        def fraction_measurement_base(self):
            from mastapy.utility.units_and_measurements.measurements import _1635
            
            return self._parent._cast(_1635.FractionMeasurementBase)

        @property
        def fraction_per_temperature(self):
            from mastapy.utility.units_and_measurements.measurements import _1636
            
            return self._parent._cast(_1636.FractionPerTemperature)

        @property
        def frequency(self):
            from mastapy.utility.units_and_measurements.measurements import _1637
            
            return self._parent._cast(_1637.Frequency)

        @property
        def fuel_consumption_engine(self):
            from mastapy.utility.units_and_measurements.measurements import _1638
            
            return self._parent._cast(_1638.FuelConsumptionEngine)

        @property
        def fuel_efficiency_vehicle(self):
            from mastapy.utility.units_and_measurements.measurements import _1639
            
            return self._parent._cast(_1639.FuelEfficiencyVehicle)

        @property
        def gradient(self):
            from mastapy.utility.units_and_measurements.measurements import _1640
            
            return self._parent._cast(_1640.Gradient)

        @property
        def heat_conductivity(self):
            from mastapy.utility.units_and_measurements.measurements import _1641
            
            return self._parent._cast(_1641.HeatConductivity)

        @property
        def heat_transfer(self):
            from mastapy.utility.units_and_measurements.measurements import _1642
            
            return self._parent._cast(_1642.HeatTransfer)

        @property
        def heat_transfer_coefficient_for_plastic_gear_tooth(self):
            from mastapy.utility.units_and_measurements.measurements import _1643
            
            return self._parent._cast(_1643.HeatTransferCoefficientForPlasticGearTooth)

        @property
        def heat_transfer_resistance(self):
            from mastapy.utility.units_and_measurements.measurements import _1644
            
            return self._parent._cast(_1644.HeatTransferResistance)

        @property
        def impulse(self):
            from mastapy.utility.units_and_measurements.measurements import _1645
            
            return self._parent._cast(_1645.Impulse)

        @property
        def index(self):
            from mastapy.utility.units_and_measurements.measurements import _1646
            
            return self._parent._cast(_1646.Index)

        @property
        def inductance(self):
            from mastapy.utility.units_and_measurements.measurements import _1647
            
            return self._parent._cast(_1647.Inductance)

        @property
        def integer(self):
            from mastapy.utility.units_and_measurements.measurements import _1648
            
            return self._parent._cast(_1648.Integer)

        @property
        def inverse_short_length(self):
            from mastapy.utility.units_and_measurements.measurements import _1649
            
            return self._parent._cast(_1649.InverseShortLength)

        @property
        def inverse_short_time(self):
            from mastapy.utility.units_and_measurements.measurements import _1650
            
            return self._parent._cast(_1650.InverseShortTime)

        @property
        def jerk(self):
            from mastapy.utility.units_and_measurements.measurements import _1651
            
            return self._parent._cast(_1651.Jerk)

        @property
        def kinematic_viscosity(self):
            from mastapy.utility.units_and_measurements.measurements import _1652
            
            return self._parent._cast(_1652.KinematicViscosity)

        @property
        def length_long(self):
            from mastapy.utility.units_and_measurements.measurements import _1653
            
            return self._parent._cast(_1653.LengthLong)

        @property
        def length_medium(self):
            from mastapy.utility.units_and_measurements.measurements import _1654
            
            return self._parent._cast(_1654.LengthMedium)

        @property
        def length_per_unit_temperature(self):
            from mastapy.utility.units_and_measurements.measurements import _1655
            
            return self._parent._cast(_1655.LengthPerUnitTemperature)

        @property
        def length_short(self):
            from mastapy.utility.units_and_measurements.measurements import _1656
            
            return self._parent._cast(_1656.LengthShort)

        @property
        def length_to_the_fourth(self):
            from mastapy.utility.units_and_measurements.measurements import _1657
            
            return self._parent._cast(_1657.LengthToTheFourth)

        @property
        def length_very_long(self):
            from mastapy.utility.units_and_measurements.measurements import _1658
            
            return self._parent._cast(_1658.LengthVeryLong)

        @property
        def length_very_short(self):
            from mastapy.utility.units_and_measurements.measurements import _1659
            
            return self._parent._cast(_1659.LengthVeryShort)

        @property
        def length_very_short_per_length_short(self):
            from mastapy.utility.units_and_measurements.measurements import _1660
            
            return self._parent._cast(_1660.LengthVeryShortPerLengthShort)

        @property
        def linear_angular_damping(self):
            from mastapy.utility.units_and_measurements.measurements import _1661
            
            return self._parent._cast(_1661.LinearAngularDamping)

        @property
        def linear_angular_stiffness_cross_term(self):
            from mastapy.utility.units_and_measurements.measurements import _1662
            
            return self._parent._cast(_1662.LinearAngularStiffnessCrossTerm)

        @property
        def linear_damping(self):
            from mastapy.utility.units_and_measurements.measurements import _1663
            
            return self._parent._cast(_1663.LinearDamping)

        @property
        def linear_flexibility(self):
            from mastapy.utility.units_and_measurements.measurements import _1664
            
            return self._parent._cast(_1664.LinearFlexibility)

        @property
        def linear_stiffness(self):
            from mastapy.utility.units_and_measurements.measurements import _1665
            
            return self._parent._cast(_1665.LinearStiffness)

        @property
        def magnetic_field_strength(self):
            from mastapy.utility.units_and_measurements.measurements import _1666
            
            return self._parent._cast(_1666.MagneticFieldStrength)

        @property
        def magnetic_flux(self):
            from mastapy.utility.units_and_measurements.measurements import _1667
            
            return self._parent._cast(_1667.MagneticFlux)

        @property
        def magnetic_flux_density(self):
            from mastapy.utility.units_and_measurements.measurements import _1668
            
            return self._parent._cast(_1668.MagneticFluxDensity)

        @property
        def magnetic_vector_potential(self):
            from mastapy.utility.units_and_measurements.measurements import _1669
            
            return self._parent._cast(_1669.MagneticVectorPotential)

        @property
        def magnetomotive_force(self):
            from mastapy.utility.units_and_measurements.measurements import _1670
            
            return self._parent._cast(_1670.MagnetomotiveForce)

        @property
        def mass(self):
            from mastapy.utility.units_and_measurements.measurements import _1671
            
            return self._parent._cast(_1671.Mass)

        @property
        def mass_per_unit_length(self):
            from mastapy.utility.units_and_measurements.measurements import _1672
            
            return self._parent._cast(_1672.MassPerUnitLength)

        @property
        def mass_per_unit_time(self):
            from mastapy.utility.units_and_measurements.measurements import _1673
            
            return self._parent._cast(_1673.MassPerUnitTime)

        @property
        def moment_of_inertia(self):
            from mastapy.utility.units_and_measurements.measurements import _1674
            
            return self._parent._cast(_1674.MomentOfInertia)

        @property
        def moment_of_inertia_per_unit_length(self):
            from mastapy.utility.units_and_measurements.measurements import _1675
            
            return self._parent._cast(_1675.MomentOfInertiaPerUnitLength)

        @property
        def moment_per_unit_pressure(self):
            from mastapy.utility.units_and_measurements.measurements import _1676
            
            return self._parent._cast(_1676.MomentPerUnitPressure)

        @property
        def number(self):
            from mastapy.utility.units_and_measurements.measurements import _1677
            
            return self._parent._cast(_1677.Number)

        @property
        def percentage(self):
            from mastapy.utility.units_and_measurements.measurements import _1678
            
            return self._parent._cast(_1678.Percentage)

        @property
        def power(self):
            from mastapy.utility.units_and_measurements.measurements import _1679
            
            return self._parent._cast(_1679.Power)

        @property
        def power_per_small_area(self):
            from mastapy.utility.units_and_measurements.measurements import _1680
            
            return self._parent._cast(_1680.PowerPerSmallArea)

        @property
        def power_per_unit_time(self):
            from mastapy.utility.units_and_measurements.measurements import _1681
            
            return self._parent._cast(_1681.PowerPerUnitTime)

        @property
        def power_small(self):
            from mastapy.utility.units_and_measurements.measurements import _1682
            
            return self._parent._cast(_1682.PowerSmall)

        @property
        def power_small_per_area(self):
            from mastapy.utility.units_and_measurements.measurements import _1683
            
            return self._parent._cast(_1683.PowerSmallPerArea)

        @property
        def power_small_per_mass(self):
            from mastapy.utility.units_and_measurements.measurements import _1684
            
            return self._parent._cast(_1684.PowerSmallPerMass)

        @property
        def power_small_per_unit_area_per_unit_time(self):
            from mastapy.utility.units_and_measurements.measurements import _1685
            
            return self._parent._cast(_1685.PowerSmallPerUnitAreaPerUnitTime)

        @property
        def power_small_per_unit_time(self):
            from mastapy.utility.units_and_measurements.measurements import _1686
            
            return self._parent._cast(_1686.PowerSmallPerUnitTime)

        @property
        def power_small_per_volume(self):
            from mastapy.utility.units_and_measurements.measurements import _1687
            
            return self._parent._cast(_1687.PowerSmallPerVolume)

        @property
        def pressure(self):
            from mastapy.utility.units_and_measurements.measurements import _1688
            
            return self._parent._cast(_1688.Pressure)

        @property
        def pressure_per_unit_time(self):
            from mastapy.utility.units_and_measurements.measurements import _1689
            
            return self._parent._cast(_1689.PressurePerUnitTime)

        @property
        def pressure_velocity_product(self):
            from mastapy.utility.units_and_measurements.measurements import _1690
            
            return self._parent._cast(_1690.PressureVelocityProduct)

        @property
        def pressure_viscosity_coefficient(self):
            from mastapy.utility.units_and_measurements.measurements import _1691
            
            return self._parent._cast(_1691.PressureViscosityCoefficient)

        @property
        def price(self):
            from mastapy.utility.units_and_measurements.measurements import _1692
            
            return self._parent._cast(_1692.Price)

        @property
        def price_per_unit_mass(self):
            from mastapy.utility.units_and_measurements.measurements import _1693
            
            return self._parent._cast(_1693.PricePerUnitMass)

        @property
        def quadratic_angular_damping(self):
            from mastapy.utility.units_and_measurements.measurements import _1694
            
            return self._parent._cast(_1694.QuadraticAngularDamping)

        @property
        def quadratic_drag(self):
            from mastapy.utility.units_and_measurements.measurements import _1695
            
            return self._parent._cast(_1695.QuadraticDrag)

        @property
        def rescaled_measurement(self):
            from mastapy.utility.units_and_measurements.measurements import _1696
            
            return self._parent._cast(_1696.RescaledMeasurement)

        @property
        def rotatum(self):
            from mastapy.utility.units_and_measurements.measurements import _1697
            
            return self._parent._cast(_1697.Rotatum)

        @property
        def safety_factor(self):
            from mastapy.utility.units_and_measurements.measurements import _1698
            
            return self._parent._cast(_1698.SafetyFactor)

        @property
        def specific_acoustic_impedance(self):
            from mastapy.utility.units_and_measurements.measurements import _1699
            
            return self._parent._cast(_1699.SpecificAcousticImpedance)

        @property
        def specific_heat(self):
            from mastapy.utility.units_and_measurements.measurements import _1700
            
            return self._parent._cast(_1700.SpecificHeat)

        @property
        def square_root_of_unit_force_per_unit_area(self):
            from mastapy.utility.units_and_measurements.measurements import _1701
            
            return self._parent._cast(_1701.SquareRootOfUnitForcePerUnitArea)

        @property
        def stiffness_per_unit_face_width(self):
            from mastapy.utility.units_and_measurements.measurements import _1702
            
            return self._parent._cast(_1702.StiffnessPerUnitFaceWidth)

        @property
        def stress(self):
            from mastapy.utility.units_and_measurements.measurements import _1703
            
            return self._parent._cast(_1703.Stress)

        @property
        def temperature(self):
            from mastapy.utility.units_and_measurements.measurements import _1704
            
            return self._parent._cast(_1704.Temperature)

        @property
        def temperature_difference(self):
            from mastapy.utility.units_and_measurements.measurements import _1705
            
            return self._parent._cast(_1705.TemperatureDifference)

        @property
        def temperature_per_unit_time(self):
            from mastapy.utility.units_and_measurements.measurements import _1706
            
            return self._parent._cast(_1706.TemperaturePerUnitTime)

        @property
        def text(self):
            from mastapy.utility.units_and_measurements.measurements import _1707
            
            return self._parent._cast(_1707.Text)

        @property
        def thermal_contact_coefficient(self):
            from mastapy.utility.units_and_measurements.measurements import _1708
            
            return self._parent._cast(_1708.ThermalContactCoefficient)

        @property
        def thermal_expansion_coefficient(self):
            from mastapy.utility.units_and_measurements.measurements import _1709
            
            return self._parent._cast(_1709.ThermalExpansionCoefficient)

        @property
        def thermo_elastic_factor(self):
            from mastapy.utility.units_and_measurements.measurements import _1710
            
            return self._parent._cast(_1710.ThermoElasticFactor)

        @property
        def time(self):
            from mastapy.utility.units_and_measurements.measurements import _1711
            
            return self._parent._cast(_1711.Time)

        @property
        def time_short(self):
            from mastapy.utility.units_and_measurements.measurements import _1712
            
            return self._parent._cast(_1712.TimeShort)

        @property
        def time_very_short(self):
            from mastapy.utility.units_and_measurements.measurements import _1713
            
            return self._parent._cast(_1713.TimeVeryShort)

        @property
        def torque(self):
            from mastapy.utility.units_and_measurements.measurements import _1714
            
            return self._parent._cast(_1714.Torque)

        @property
        def torque_converter_inverse_k(self):
            from mastapy.utility.units_and_measurements.measurements import _1715
            
            return self._parent._cast(_1715.TorqueConverterInverseK)

        @property
        def torque_converter_k(self):
            from mastapy.utility.units_and_measurements.measurements import _1716
            
            return self._parent._cast(_1716.TorqueConverterK)

        @property
        def torque_per_current(self):
            from mastapy.utility.units_and_measurements.measurements import _1717
            
            return self._parent._cast(_1717.TorquePerCurrent)

        @property
        def torque_per_square_root_of_power(self):
            from mastapy.utility.units_and_measurements.measurements import _1718
            
            return self._parent._cast(_1718.TorquePerSquareRootOfPower)

        @property
        def torque_per_unit_temperature(self):
            from mastapy.utility.units_and_measurements.measurements import _1719
            
            return self._parent._cast(_1719.TorquePerUnitTemperature)

        @property
        def velocity(self):
            from mastapy.utility.units_and_measurements.measurements import _1720
            
            return self._parent._cast(_1720.Velocity)

        @property
        def velocity_small(self):
            from mastapy.utility.units_and_measurements.measurements import _1721
            
            return self._parent._cast(_1721.VelocitySmall)

        @property
        def viscosity(self):
            from mastapy.utility.units_and_measurements.measurements import _1722
            
            return self._parent._cast(_1722.Viscosity)

        @property
        def voltage(self):
            from mastapy.utility.units_and_measurements.measurements import _1723
            
            return self._parent._cast(_1723.Voltage)

        @property
        def voltage_per_angular_velocity(self):
            from mastapy.utility.units_and_measurements.measurements import _1724
            
            return self._parent._cast(_1724.VoltagePerAngularVelocity)

        @property
        def volume(self):
            from mastapy.utility.units_and_measurements.measurements import _1725
            
            return self._parent._cast(_1725.Volume)

        @property
        def wear_coefficient(self):
            from mastapy.utility.units_and_measurements.measurements import _1726
            
            return self._parent._cast(_1726.WearCoefficient)

        @property
        def yank(self):
            from mastapy.utility.units_and_measurements.measurements import _1727
            
            return self._parent._cast(_1727.Yank)

        @property
        def measurement_base(self) -> 'MeasurementBase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'MeasurementBase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def absolute_tolerance(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'AbsoluteTolerance' is the original name of this property."""

        temp = self.wrapped.AbsoluteTolerance

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @absolute_tolerance.setter
    def absolute_tolerance(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.AbsoluteTolerance = value

    @property
    def default_unit(self) -> 'list_with_selected_item.ListWithSelectedItem_Unit':
        """list_with_selected_item.ListWithSelectedItem_Unit: 'DefaultUnit' is the original name of this property."""

        temp = self.wrapped.DefaultUnit

        if temp is None:
            return None

        return constructor.new_from_mastapy_type(list_with_selected_item.ListWithSelectedItem_Unit)(temp) if temp is not None else None

    @default_unit.setter
    def default_unit(self, value: 'list_with_selected_item.ListWithSelectedItem_Unit.implicit_type()'):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_Unit.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_Unit.implicit_type()
        value = wrapper_type[enclosed_type](value.wrapped if value is not None else None)
        self.wrapped.DefaultUnit = value

    @property
    def name(self) -> 'str':
        """str: 'Name' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Name

        if temp is None:
            return ''

        return temp

    @property
    def percentage_tolerance(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'PercentageTolerance' is the original name of this property."""

        temp = self.wrapped.PercentageTolerance

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @percentage_tolerance.setter
    def percentage_tolerance(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.PercentageTolerance = value

    @property
    def rounding_digits(self) -> 'int':
        """int: 'RoundingDigits' is the original name of this property."""

        temp = self.wrapped.RoundingDigits

        if temp is None:
            return 0

        return temp

    @rounding_digits.setter
    def rounding_digits(self, value: 'int'):
        self.wrapped.RoundingDigits = int(value) if value else 0

    @property
    def rounding_method(self) -> '_1587.RoundingMethods':
        """RoundingMethods: 'RoundingMethod' is the original name of this property."""

        temp = self.wrapped.RoundingMethod

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, _1587.RoundingMethods)
        return constructor.new_from_mastapy_type(_1587.RoundingMethods)(value) if value is not None else None

    @rounding_method.setter
    def rounding_method(self, value: '_1587.RoundingMethods'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value, _1587.RoundingMethods.type_())
        self.wrapped.RoundingMethod = value

    @property
    def current_unit(self) -> '_1599.Unit':
        """Unit: 'CurrentUnit' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentUnit

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_units(self) -> 'List[_1599.Unit]':
        """List[Unit]: 'AvailableUnits' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AvailableUnits

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def report_names(self) -> 'List[str]':
        """List[str]: 'ReportNames' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ReportNames

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, str)
        return value

    def output_default_report_to(self, file_path: 'str'):
        """ 'OutputDefaultReportTo' is the original name of this method.

        Args:
            file_path (str)
        """

        file_path = str(file_path)
        self.wrapped.OutputDefaultReportTo(file_path if file_path else '')

    def get_default_report_with_encoded_images(self) -> 'str':
        """ 'GetDefaultReportWithEncodedImages' is the original name of this method.

        Returns:
            str
        """

        method_result = self.wrapped.GetDefaultReportWithEncodedImages()
        return method_result

    def output_active_report_to(self, file_path: 'str'):
        """ 'OutputActiveReportTo' is the original name of this method.

        Args:
            file_path (str)
        """

        file_path = str(file_path)
        self.wrapped.OutputActiveReportTo(file_path if file_path else '')

    def output_active_report_as_text_to(self, file_path: 'str'):
        """ 'OutputActiveReportAsTextTo' is the original name of this method.

        Args:
            file_path (str)
        """

        file_path = str(file_path)
        self.wrapped.OutputActiveReportAsTextTo(file_path if file_path else '')

    def get_active_report_with_encoded_images(self) -> 'str':
        """ 'GetActiveReportWithEncodedImages' is the original name of this method.

        Returns:
            str
        """

        method_result = self.wrapped.GetActiveReportWithEncodedImages()
        return method_result

    def output_named_report_to(self, report_name: 'str', file_path: 'str'):
        """ 'OutputNamedReportTo' is the original name of this method.

        Args:
            report_name (str)
            file_path (str)
        """

        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportTo(report_name if report_name else '', file_path if file_path else '')

    def output_named_report_as_masta_report(self, report_name: 'str', file_path: 'str'):
        """ 'OutputNamedReportAsMastaReport' is the original name of this method.

        Args:
            report_name (str)
            file_path (str)
        """

        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsMastaReport(report_name if report_name else '', file_path if file_path else '')

    def output_named_report_as_text_to(self, report_name: 'str', file_path: 'str'):
        """ 'OutputNamedReportAsTextTo' is the original name of this method.

        Args:
            report_name (str)
            file_path (str)
        """

        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsTextTo(report_name if report_name else '', file_path if file_path else '')

    def get_named_report_with_encoded_images(self, report_name: 'str') -> 'str':
        """ 'GetNamedReportWithEncodedImages' is the original name of this method.

        Args:
            report_name (str)

        Returns:
            str
        """

        report_name = str(report_name)
        method_result = self.wrapped.GetNamedReportWithEncodedImages(report_name if report_name else '')
        return method_result

    @property
    def cast_to(self) -> 'MeasurementBase._Cast_MeasurementBase':
        return self._Cast_MeasurementBase(self)
