"""_1034.py

CylindricalMeshLinearBacklashSpecification
"""
from mastapy._internal import constructor
from mastapy.gears.gear_designs.cylindrical import _1077, _994
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_MESH_LINEAR_BACKLASH_SPECIFICATION = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Cylindrical', 'CylindricalMeshLinearBacklashSpecification')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalMeshLinearBacklashSpecification',)


class CylindricalMeshLinearBacklashSpecification(_1077.TolerancedValueSpecification['_994.BacklashSpecification']):
    """CylindricalMeshLinearBacklashSpecification

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_MESH_LINEAR_BACKLASH_SPECIFICATION

    class _Cast_CylindricalMeshLinearBacklashSpecification:
        """Special nested class for casting CylindricalMeshLinearBacklashSpecification to subclasses."""

        def __init__(self, parent: 'CylindricalMeshLinearBacklashSpecification'):
            self._parent = parent

        @property
        def toleranced_value_specification(self):
            return self._parent._cast(_1077.TolerancedValueSpecification)

        @property
        def relative_measurement_view_model(self):
            from mastapy.gears.gear_designs.cylindrical import _1061
            
            return self._parent._cast(_1061.RelativeMeasurementViewModel)

        @property
        def cylindrical_mesh_angular_backlash(self):
            from mastapy.gears.gear_designs.cylindrical import _1031
            
            return self._parent._cast(_1031.CylindricalMeshAngularBacklash)

        @property
        def cylindrical_mesh_linear_backlash_specification(self) -> 'CylindricalMeshLinearBacklashSpecification':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CylindricalMeshLinearBacklashSpecification.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def measurement_type(self) -> 'str':
        """str: 'MeasurementType' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeasurementType

        if temp is None:
            return ''

        return temp

    @property
    def cast_to(self) -> 'CylindricalMeshLinearBacklashSpecification._Cast_CylindricalMeshLinearBacklashSpecification':
        return self._Cast_CylindricalMeshLinearBacklashSpecification(self)
