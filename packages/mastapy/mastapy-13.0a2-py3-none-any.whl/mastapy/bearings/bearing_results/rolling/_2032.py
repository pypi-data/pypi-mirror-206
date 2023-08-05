"""_2032.py

LoadedTaperRollerBearingElement
"""
from mastapy._internal import constructor
from mastapy.bearings.bearing_results.rolling import _2012
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_TAPER_ROLLER_BEARING_ELEMENT = python_net_import('SMT.MastaAPI.Bearings.BearingResults.Rolling', 'LoadedTaperRollerBearingElement')


__docformat__ = 'restructuredtext en'
__all__ = ('LoadedTaperRollerBearingElement',)


class LoadedTaperRollerBearingElement(_2012.LoadedNonBarrelRollerElement):
    """LoadedTaperRollerBearingElement

    This is a mastapy class.
    """

    TYPE = _LOADED_TAPER_ROLLER_BEARING_ELEMENT

    class _Cast_LoadedTaperRollerBearingElement:
        """Special nested class for casting LoadedTaperRollerBearingElement to subclasses."""

        def __init__(self, parent: 'LoadedTaperRollerBearingElement'):
            self._parent = parent

        @property
        def loaded_non_barrel_roller_element(self):
            return self._parent._cast(_2012.LoadedNonBarrelRollerElement)

        @property
        def loaded_roller_bearing_element(self):
            from mastapy.bearings.bearing_results.rolling import _2013
            
            return self._parent._cast(_2013.LoadedRollerBearingElement)

        @property
        def loaded_element(self):
            from mastapy.bearings.bearing_results.rolling import _1999
            
            return self._parent._cast(_1999.LoadedElement)

        @property
        def loaded_taper_roller_bearing_element(self) -> 'LoadedTaperRollerBearingElement':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'LoadedTaperRollerBearingElement.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def height_of_rib_roller_contact_above_race_inner_left(self) -> 'float':
        """float: 'HeightOfRibRollerContactAboveRaceInnerLeft' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HeightOfRibRollerContactAboveRaceInnerLeft

        if temp is None:
            return 0.0

        return temp

    @property
    def height_of_rib_roller_contact_above_race_inner_right(self) -> 'float':
        """float: 'HeightOfRibRollerContactAboveRaceInnerRight' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HeightOfRibRollerContactAboveRaceInnerRight

        if temp is None:
            return 0.0

        return temp

    @property
    def height_of_rib_roller_contact_above_race_outer_left(self) -> 'float':
        """float: 'HeightOfRibRollerContactAboveRaceOuterLeft' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HeightOfRibRollerContactAboveRaceOuterLeft

        if temp is None:
            return 0.0

        return temp

    @property
    def height_of_rib_roller_contact_above_race_outer_right(self) -> 'float':
        """float: 'HeightOfRibRollerContactAboveRaceOuterRight' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HeightOfRibRollerContactAboveRaceOuterRight

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_rib_stress_inner_left(self) -> 'float':
        """float: 'MaximumRibStressInnerLeft' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumRibStressInnerLeft

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_rib_stress_inner_right(self) -> 'float':
        """float: 'MaximumRibStressInnerRight' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumRibStressInnerRight

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_rib_stress_outer_left(self) -> 'float':
        """float: 'MaximumRibStressOuterLeft' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumRibStressOuterLeft

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_rib_stress_outer_right(self) -> 'float':
        """float: 'MaximumRibStressOuterRight' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumRibStressOuterRight

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self) -> 'LoadedTaperRollerBearingElement._Cast_LoadedTaperRollerBearingElement':
        return self._Cast_LoadedTaperRollerBearingElement(self)
