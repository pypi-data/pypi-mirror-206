"""_1404.py

SplineMaterial
"""
from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy.detailed_rigid_connectors.splines import _1386
from mastapy.materials import _265
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPLINE_MATERIAL = python_net_import('SMT.MastaAPI.DetailedRigidConnectors.Splines', 'SplineMaterial')


__docformat__ = 'restructuredtext en'
__all__ = ('SplineMaterial',)


class SplineMaterial(_265.Material):
    """SplineMaterial

    This is a mastapy class.
    """

    TYPE = _SPLINE_MATERIAL

    class _Cast_SplineMaterial:
        """Special nested class for casting SplineMaterial to subclasses."""

        def __init__(self, parent: 'SplineMaterial'):
            self._parent = parent

        @property
        def material(self):
            return self._parent._cast(_265.Material)

        @property
        def named_database_item(self):
            from mastapy.utility.databases import _1816
            
            return self._parent._cast(_1816.NamedDatabaseItem)

        @property
        def spline_material(self) -> 'SplineMaterial':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'SplineMaterial.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def core_hardness_h_rc(self) -> 'float':
        """float: 'CoreHardnessHRc' is the original name of this property."""

        temp = self.wrapped.CoreHardnessHRc

        if temp is None:
            return 0.0

        return temp

    @core_hardness_h_rc.setter
    def core_hardness_h_rc(self, value: 'float'):
        self.wrapped.CoreHardnessHRc = float(value) if value else 0.0

    @property
    def heat_treatment_type(self) -> '_1386.HeatTreatmentTypes':
        """HeatTreatmentTypes: 'HeatTreatmentType' is the original name of this property."""

        temp = self.wrapped.HeatTreatmentType

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, _1386.HeatTreatmentTypes)
        return constructor.new_from_mastapy_type(_1386.HeatTreatmentTypes)(value) if value is not None else None

    @heat_treatment_type.setter
    def heat_treatment_type(self, value: '_1386.HeatTreatmentTypes'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value, _1386.HeatTreatmentTypes.type_())
        self.wrapped.HeatTreatmentType = value

    @property
    def cast_to(self) -> 'SplineMaterial._Cast_SplineMaterial':
        return self._Cast_SplineMaterial(self)
