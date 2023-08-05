"""_1014.py

CylindricalGearMeshFlankDesign
"""
from mastapy._internal import constructor
from mastapy.utility_gui.charts import _1852
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_MESH_FLANK_DESIGN = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Cylindrical', 'CylindricalGearMeshFlankDesign')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearMeshFlankDesign',)


class CylindricalGearMeshFlankDesign(_0.APIBase):
    """CylindricalGearMeshFlankDesign

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_MESH_FLANK_DESIGN

    class _Cast_CylindricalGearMeshFlankDesign:
        """Special nested class for casting CylindricalGearMeshFlankDesign to subclasses."""

        def __init__(self, parent: 'CylindricalGearMeshFlankDesign'):
            self._parent = parent

        @property
        def cylindrical_gear_mesh_flank_design(self) -> 'CylindricalGearMeshFlankDesign':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CylindricalGearMeshFlankDesign.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def degree_of_tooth_loss(self) -> 'float':
        """float: 'DegreeOfToothLoss' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DegreeOfToothLoss

        if temp is None:
            return 0.0

        return temp

    @property
    def flank_name(self) -> 'str':
        """str: 'FlankName' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FlankName

        if temp is None:
            return ''

        return temp

    @property
    def length_of_contact(self) -> 'float':
        """float: 'LengthOfContact' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LengthOfContact

        if temp is None:
            return 0.0

        return temp

    @property
    def specific_sliding_chart(self) -> '_1852.TwoDChartDefinition':
        """TwoDChartDefinition: 'SpecificSlidingChart' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SpecificSlidingChart

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def tooth_loss_factor(self) -> 'float':
        """float: 'ToothLossFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ToothLossFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def total_contact_ratio(self) -> 'float':
        """float: 'TotalContactRatio' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TotalContactRatio

        if temp is None:
            return 0.0

        return temp

    @property
    def transverse_contact_ratio(self) -> 'float':
        """float: 'TransverseContactRatio' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TransverseContactRatio

        if temp is None:
            return 0.0

        return temp

    @property
    def virtual_contact_ratio(self) -> 'float':
        """float: 'VirtualContactRatio' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.VirtualContactRatio

        if temp is None:
            return 0.0

        return temp

    @property
    def working_normal_pressure_angle(self) -> 'float':
        """float: 'WorkingNormalPressureAngle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WorkingNormalPressureAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def working_transverse_pressure_angle(self) -> 'float':
        """float: 'WorkingTransversePressureAngle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WorkingTransversePressureAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self) -> 'CylindricalGearMeshFlankDesign._Cast_CylindricalGearMeshFlankDesign':
        return self._Cast_CylindricalGearMeshFlankDesign(self)
