"""_504.py

CylindricalGearToothFatigueFractureResultsN1457
"""
from typing import List

from mastapy.utility_gui.charts import _1850
from mastapy._internal import constructor, conversion
from mastapy.gears.rating.cylindrical.iso6336 import _525, _522
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_TOOTH_FATIGUE_FRACTURE_RESULTS_N1457 = python_net_import('SMT.MastaAPI.Gears.Rating.Cylindrical.ISO6336', 'CylindricalGearToothFatigueFractureResultsN1457')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearToothFatigueFractureResultsN1457',)


class CylindricalGearToothFatigueFractureResultsN1457(_0.APIBase):
    """CylindricalGearToothFatigueFractureResultsN1457

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_TOOTH_FATIGUE_FRACTURE_RESULTS_N1457

    class _Cast_CylindricalGearToothFatigueFractureResultsN1457:
        """Special nested class for casting CylindricalGearToothFatigueFractureResultsN1457 to subclasses."""

        def __init__(self, parent: 'CylindricalGearToothFatigueFractureResultsN1457'):
            self._parent = parent

        @property
        def cylindrical_gear_tooth_fatigue_fracture_results_n1457(self) -> 'CylindricalGearToothFatigueFractureResultsN1457':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CylindricalGearToothFatigueFractureResultsN1457.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def fatigue_damage_chart(self) -> '_1850.ThreeDChartDefinition':
        """ThreeDChartDefinition: 'FatigueDamageChart' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FatigueDamageChart

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def maximum_fatigue_damage(self) -> 'float':
        """float: 'MaximumFatigueDamage' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumFatigueDamage

        if temp is None:
            return 0.0

        return temp

    @property
    def critical_section(self) -> '_525.ToothFlankFractureAnalysisRowN1457':
        """ToothFlankFractureAnalysisRowN1457: 'CriticalSection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CriticalSection

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def mesh_contact_point_a_section(self) -> '_525.ToothFlankFractureAnalysisRowN1457':
        """ToothFlankFractureAnalysisRowN1457: 'MeshContactPointASection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeshContactPointASection

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def mesh_contact_point_ab_section(self) -> '_522.ToothFlankFractureAnalysisContactPointN1457':
        """ToothFlankFractureAnalysisContactPointN1457: 'MeshContactPointABSection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeshContactPointABSection

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def mesh_contact_point_b_section(self) -> '_522.ToothFlankFractureAnalysisContactPointN1457':
        """ToothFlankFractureAnalysisContactPointN1457: 'MeshContactPointBSection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeshContactPointBSection

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def mesh_contact_point_c_section(self) -> '_522.ToothFlankFractureAnalysisContactPointN1457':
        """ToothFlankFractureAnalysisContactPointN1457: 'MeshContactPointCSection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeshContactPointCSection

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def mesh_contact_point_d_section(self) -> '_522.ToothFlankFractureAnalysisContactPointN1457':
        """ToothFlankFractureAnalysisContactPointN1457: 'MeshContactPointDSection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeshContactPointDSection

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def mesh_contact_point_de_section(self) -> '_522.ToothFlankFractureAnalysisContactPointN1457':
        """ToothFlankFractureAnalysisContactPointN1457: 'MeshContactPointDESection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeshContactPointDESection

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def mesh_contact_point_e_section(self) -> '_522.ToothFlankFractureAnalysisContactPointN1457':
        """ToothFlankFractureAnalysisContactPointN1457: 'MeshContactPointESection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeshContactPointESection

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def analysis_rows(self) -> 'List[_525.ToothFlankFractureAnalysisRowN1457]':
        """List[ToothFlankFractureAnalysisRowN1457]: 'AnalysisRows' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AnalysisRows

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def contact_points(self) -> 'List[_522.ToothFlankFractureAnalysisContactPointN1457]':
        """List[ToothFlankFractureAnalysisContactPointN1457]: 'ContactPoints' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ContactPoints

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'CylindricalGearToothFatigueFractureResultsN1457._Cast_CylindricalGearToothFatigueFractureResultsN1457':
        return self._Cast_CylindricalGearToothFatigueFractureResultsN1457(self)
