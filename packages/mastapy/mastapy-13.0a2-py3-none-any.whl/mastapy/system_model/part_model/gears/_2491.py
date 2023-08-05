"""_2491.py

ActiveGearSetDesignSelectionGroup
"""
from mastapy._internal import constructor
from mastapy.system_model.part_model.configurations import _2596
from mastapy.system_model.part_model.gears import _2490, _2511
from mastapy.gears.gear_designs import _945
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ACTIVE_GEAR_SET_DESIGN_SELECTION_GROUP = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'ActiveGearSetDesignSelectionGroup')


__docformat__ = 'restructuredtext en'
__all__ = ('ActiveGearSetDesignSelectionGroup',)


class ActiveGearSetDesignSelectionGroup(_2596.PartDetailConfiguration['_2490.ActiveGearSetDesignSelection', '_2511.GearSet', '_945.GearSetDesign']):
    """ActiveGearSetDesignSelectionGroup

    This is a mastapy class.
    """

    TYPE = _ACTIVE_GEAR_SET_DESIGN_SELECTION_GROUP

    class _Cast_ActiveGearSetDesignSelectionGroup:
        """Special nested class for casting ActiveGearSetDesignSelectionGroup to subclasses."""

        def __init__(self, parent: 'ActiveGearSetDesignSelectionGroup'):
            self._parent = parent

        @property
        def part_detail_configuration(self):
            return self._parent._cast(_2596.PartDetailConfiguration)

        @property
        def active_gear_set_design_selection_group(self) -> 'ActiveGearSetDesignSelectionGroup':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'ActiveGearSetDesignSelectionGroup.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def axial_contact_ratio_rating_for_nvh(self) -> 'float':
        """float: 'AxialContactRatioRatingForNVH' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AxialContactRatioRatingForNVH

        if temp is None:
            return 0.0

        return temp

    @property
    def face_width_of_widest_cylindrical_gear(self) -> 'float':
        """float: 'FaceWidthOfWidestCylindricalGear' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FaceWidthOfWidestCylindricalGear

        if temp is None:
            return 0.0

        return temp

    @property
    def minimum_cylindrical_axial_contact_ratio(self) -> 'float':
        """float: 'MinimumCylindricalAxialContactRatio' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MinimumCylindricalAxialContactRatio

        if temp is None:
            return 0.0

        return temp

    @property
    def minimum_cylindrical_transverse_contact_ratio(self) -> 'float':
        """float: 'MinimumCylindricalTransverseContactRatio' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MinimumCylindricalTransverseContactRatio

        if temp is None:
            return 0.0

        return temp

    @property
    def minimum_tip_thickness(self) -> 'float':
        """float: 'MinimumTipThickness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MinimumTipThickness

        if temp is None:
            return 0.0

        return temp

    @property
    def simple_mass_of_cylindrical_gears(self) -> 'float':
        """float: 'SimpleMassOfCylindricalGears' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SimpleMassOfCylindricalGears

        if temp is None:
            return 0.0

        return temp

    @property
    def total_face_width_of_cylindrical_gears(self) -> 'float':
        """float: 'TotalFaceWidthOfCylindricalGears' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TotalFaceWidthOfCylindricalGears

        if temp is None:
            return 0.0

        return temp

    @property
    def transverse_contact_ratio_rating_for_nvh(self) -> 'float':
        """float: 'TransverseContactRatioRatingForNVH' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TransverseContactRatioRatingForNVH

        if temp is None:
            return 0.0

        return temp

    @property
    def transverse_and_axial_contact_ratio_rating_for_nvh(self) -> 'float':
        """float: 'TransverseAndAxialContactRatioRatingForNVH' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TransverseAndAxialContactRatioRatingForNVH

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self) -> 'ActiveGearSetDesignSelectionGroup._Cast_ActiveGearSetDesignSelectionGroup':
        return self._Cast_ActiveGearSetDesignSelectionGroup(self)
