"""_869.py

GearSetLoadCaseBase
"""
from mastapy._internal import constructor
from mastapy.gears.analysis import _1220
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_SET_LOAD_CASE_BASE = python_net_import('SMT.MastaAPI.Gears.LoadCase', 'GearSetLoadCaseBase')


__docformat__ = 'restructuredtext en'
__all__ = ('GearSetLoadCaseBase',)


class GearSetLoadCaseBase(_1220.GearSetDesignAnalysis):
    """GearSetLoadCaseBase

    This is a mastapy class.
    """

    TYPE = _GEAR_SET_LOAD_CASE_BASE

    class _Cast_GearSetLoadCaseBase:
        """Special nested class for casting GearSetLoadCaseBase to subclasses."""

        def __init__(self, parent: 'GearSetLoadCaseBase'):
            self._parent = parent

        @property
        def gear_set_design_analysis(self):
            return self._parent._cast(_1220.GearSetDesignAnalysis)

        @property
        def abstract_gear_set_analysis(self):
            from mastapy.gears.analysis import _1211
            
            return self._parent._cast(_1211.AbstractGearSetAnalysis)

        @property
        def worm_gear_set_load_case(self):
            from mastapy.gears.load_case.worm import _872
            
            return self._parent._cast(_872.WormGearSetLoadCase)

        @property
        def face_gear_set_load_case(self):
            from mastapy.gears.load_case.face import _875
            
            return self._parent._cast(_875.FaceGearSetLoadCase)

        @property
        def cylindrical_gear_set_load_case(self):
            from mastapy.gears.load_case.cylindrical import _878
            
            return self._parent._cast(_878.CylindricalGearSetLoadCase)

        @property
        def conical_gear_set_load_case(self):
            from mastapy.gears.load_case.conical import _881
            
            return self._parent._cast(_881.ConicalGearSetLoadCase)

        @property
        def concept_gear_set_load_case(self):
            from mastapy.gears.load_case.concept import _884
            
            return self._parent._cast(_884.ConceptGearSetLoadCase)

        @property
        def bevel_set_load_case(self):
            from mastapy.gears.load_case.bevel import _888
            
            return self._parent._cast(_888.BevelSetLoadCase)

        @property
        def gear_set_load_case_base(self) -> 'GearSetLoadCaseBase':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GearSetLoadCaseBase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def name(self) -> 'str':
        """str: 'Name' is the original name of this property."""

        temp = self.wrapped.Name

        if temp is None:
            return ''

        return temp

    @name.setter
    def name(self, value: 'str'):
        self.wrapped.Name = str(value) if value else ''

    @property
    def unit_duration(self) -> 'float':
        """float: 'UnitDuration' is the original name of this property."""

        temp = self.wrapped.UnitDuration

        if temp is None:
            return 0.0

        return temp

    @unit_duration.setter
    def unit_duration(self, value: 'float'):
        self.wrapped.UnitDuration = float(value) if value else 0.0

    @property
    def cast_to(self) -> 'GearSetLoadCaseBase._Cast_GearSetLoadCaseBase':
        return self._Cast_GearSetLoadCaseBase(self)
