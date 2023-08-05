"""_2013.py

LoadedRollerBearingElement
"""
from typing import List

from mastapy._internal import constructor, conversion
from mastapy.bearings.bearing_results.rolling import _2052, _1999
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_ROLLER_BEARING_ELEMENT = python_net_import('SMT.MastaAPI.Bearings.BearingResults.Rolling', 'LoadedRollerBearingElement')


__docformat__ = 'restructuredtext en'
__all__ = ('LoadedRollerBearingElement',)


class LoadedRollerBearingElement(_1999.LoadedElement):
    """LoadedRollerBearingElement

    This is a mastapy class.
    """

    TYPE = _LOADED_ROLLER_BEARING_ELEMENT

    class _Cast_LoadedRollerBearingElement:
        """Special nested class for casting LoadedRollerBearingElement to subclasses."""

        def __init__(self, parent: 'LoadedRollerBearingElement'):
            self._parent = parent

        @property
        def loaded_element(self):
            return self._parent._cast(_1999.LoadedElement)

        @property
        def loaded_asymmetric_spherical_roller_bearing_element(self):
            from mastapy.bearings.bearing_results.rolling import _1973
            
            return self._parent._cast(_1973.LoadedAsymmetricSphericalRollerBearingElement)

        @property
        def loaded_axial_thrust_cylindrical_roller_bearing_element(self):
            from mastapy.bearings.bearing_results.rolling import _1978
            
            return self._parent._cast(_1978.LoadedAxialThrustCylindricalRollerBearingElement)

        @property
        def loaded_axial_thrust_needle_roller_bearing_element(self):
            from mastapy.bearings.bearing_results.rolling import _1981
            
            return self._parent._cast(_1981.LoadedAxialThrustNeedleRollerBearingElement)

        @property
        def loaded_crossed_roller_bearing_element(self):
            from mastapy.bearings.bearing_results.rolling import _1989
            
            return self._parent._cast(_1989.LoadedCrossedRollerBearingElement)

        @property
        def loaded_cylindrical_roller_bearing_element(self):
            from mastapy.bearings.bearing_results.rolling import _1993
            
            return self._parent._cast(_1993.LoadedCylindricalRollerBearingElement)

        @property
        def loaded_needle_roller_bearing_element(self):
            from mastapy.bearings.bearing_results.rolling import _2005
            
            return self._parent._cast(_2005.LoadedNeedleRollerBearingElement)

        @property
        def loaded_non_barrel_roller_element(self):
            from mastapy.bearings.bearing_results.rolling import _2012
            
            return self._parent._cast(_2012.LoadedNonBarrelRollerElement)

        @property
        def loaded_spherical_radial_roller_bearing_element(self):
            from mastapy.bearings.bearing_results.rolling import _2023
            
            return self._parent._cast(_2023.LoadedSphericalRadialRollerBearingElement)

        @property
        def loaded_spherical_roller_bearing_element(self):
            from mastapy.bearings.bearing_results.rolling import _2024
            
            return self._parent._cast(_2024.LoadedSphericalRollerBearingElement)

        @property
        def loaded_spherical_thrust_roller_bearing_element(self):
            from mastapy.bearings.bearing_results.rolling import _2030
            
            return self._parent._cast(_2030.LoadedSphericalThrustRollerBearingElement)

        @property
        def loaded_taper_roller_bearing_element(self):
            from mastapy.bearings.bearing_results.rolling import _2032
            
            return self._parent._cast(_2032.LoadedTaperRollerBearingElement)

        @property
        def loaded_toroidal_roller_bearing_element(self):
            from mastapy.bearings.bearing_results.rolling import _2041
            
            return self._parent._cast(_2041.LoadedToroidalRollerBearingElement)

        @property
        def loaded_roller_bearing_element(self) -> 'LoadedRollerBearingElement':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'LoadedRollerBearingElement.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def contact_length_inner(self) -> 'float':
        """float: 'ContactLengthInner' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ContactLengthInner

        if temp is None:
            return 0.0

        return temp

    @property
    def contact_length_outer(self) -> 'float':
        """float: 'ContactLengthOuter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ContactLengthOuter

        if temp is None:
            return 0.0

        return temp

    @property
    def element_tilt(self) -> 'float':
        """float: 'ElementTilt' is the original name of this property."""

        temp = self.wrapped.ElementTilt

        if temp is None:
            return 0.0

        return temp

    @element_tilt.setter
    def element_tilt(self, value: 'float'):
        self.wrapped.ElementTilt = float(value) if value else 0.0

    @property
    def maximum_contact_width_inner(self) -> 'float':
        """float: 'MaximumContactWidthInner' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumContactWidthInner

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_contact_width_outer(self) -> 'float':
        """float: 'MaximumContactWidthOuter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumContactWidthOuter

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_depth_of_maximum_shear_stress_inner(self) -> 'float':
        """float: 'MaximumDepthOfMaximumShearStressInner' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumDepthOfMaximumShearStressInner

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_depth_of_maximum_shear_stress_outer(self) -> 'float':
        """float: 'MaximumDepthOfMaximumShearStressOuter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumDepthOfMaximumShearStressOuter

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_normal_edge_stress_inner(self) -> 'float':
        """float: 'MaximumNormalEdgeStressInner' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumNormalEdgeStressInner

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_normal_edge_stress_outer(self) -> 'float':
        """float: 'MaximumNormalEdgeStressOuter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumNormalEdgeStressOuter

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_normal_stress_inner(self) -> 'float':
        """float: 'MaximumNormalStressInner' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumNormalStressInner

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
    def maximum_shear_stress_inner(self) -> 'float':
        """float: 'MaximumShearStressInner' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumShearStressInner

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_shear_stress_outer(self) -> 'float':
        """float: 'MaximumShearStressOuter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumShearStressOuter

        if temp is None:
            return 0.0

        return temp

    @property
    def rib_load(self) -> 'float':
        """float: 'RibLoad' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RibLoad

        if temp is None:
            return 0.0

        return temp

    @property
    def results_at_roller_offsets(self) -> 'List[_2052.ResultsAtRollerOffset]':
        """List[ResultsAtRollerOffset]: 'ResultsAtRollerOffsets' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ResultsAtRollerOffsets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cast_to(self) -> 'LoadedRollerBearingElement._Cast_LoadedRollerBearingElement':
        return self._Cast_LoadedRollerBearingElement(self)
