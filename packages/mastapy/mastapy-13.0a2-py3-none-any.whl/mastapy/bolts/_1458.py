"""_1458.py

BoltMaterial
"""
from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy.bolts import _1473, _1454
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BOLT_MATERIAL = python_net_import('SMT.MastaAPI.Bolts', 'BoltMaterial')


__docformat__ = 'restructuredtext en'
__all__ = ('BoltMaterial',)


class BoltMaterial(_1454.BoltedJointMaterial):
    """BoltMaterial

    This is a mastapy class.
    """

    TYPE = _BOLT_MATERIAL

    class _Cast_BoltMaterial:
        """Special nested class for casting BoltMaterial to subclasses."""

        def __init__(self, parent: 'BoltMaterial'):
            self._parent = parent

        @property
        def bolted_joint_material(self):
            return self._parent._cast(_1454.BoltedJointMaterial)

        @property
        def material(self):
            from mastapy.materials import _265
            
            return self._parent._cast(_265.Material)

        @property
        def named_database_item(self):
            from mastapy.utility.databases import _1816
            
            return self._parent._cast(_1816.NamedDatabaseItem)

        @property
        def bolt_material(self) -> 'BoltMaterial':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'BoltMaterial.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def minimum_tensile_strength(self) -> 'float':
        """float: 'MinimumTensileStrength' is the original name of this property."""

        temp = self.wrapped.MinimumTensileStrength

        if temp is None:
            return 0.0

        return temp

    @minimum_tensile_strength.setter
    def minimum_tensile_strength(self, value: 'float'):
        self.wrapped.MinimumTensileStrength = float(value) if value else 0.0

    @property
    def proof_stress(self) -> 'float':
        """float: 'ProofStress' is the original name of this property."""

        temp = self.wrapped.ProofStress

        if temp is None:
            return 0.0

        return temp

    @proof_stress.setter
    def proof_stress(self, value: 'float'):
        self.wrapped.ProofStress = float(value) if value else 0.0

    @property
    def shearing_strength(self) -> 'float':
        """float: 'ShearingStrength' is the original name of this property."""

        temp = self.wrapped.ShearingStrength

        if temp is None:
            return 0.0

        return temp

    @shearing_strength.setter
    def shearing_strength(self, value: 'float'):
        self.wrapped.ShearingStrength = float(value) if value else 0.0

    @property
    def strength_grade(self) -> '_1473.StrengthGrades':
        """StrengthGrades: 'StrengthGrade' is the original name of this property."""

        temp = self.wrapped.StrengthGrade

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, _1473.StrengthGrades)
        return constructor.new_from_mastapy_type(_1473.StrengthGrades)(value) if value is not None else None

    @strength_grade.setter
    def strength_grade(self, value: '_1473.StrengthGrades'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value, _1473.StrengthGrades.type_())
        self.wrapped.StrengthGrade = value

    @property
    def cast_to(self) -> 'BoltMaterial._Cast_BoltMaterial':
        return self._Cast_BoltMaterial(self)
