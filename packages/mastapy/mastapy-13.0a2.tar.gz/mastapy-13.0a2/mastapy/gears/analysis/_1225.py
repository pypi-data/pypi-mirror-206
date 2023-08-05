"""_1225.py

GearSetImplementationDetail
"""
from mastapy._internal import constructor
from mastapy.utility.scripting import _1730
from mastapy.gears.analysis import _1220
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_SET_IMPLEMENTATION_DETAIL = python_net_import('SMT.MastaAPI.Gears.Analysis', 'GearSetImplementationDetail')


__docformat__ = 'restructuredtext en'
__all__ = ('GearSetImplementationDetail',)


class GearSetImplementationDetail(_1220.GearSetDesignAnalysis):
    """GearSetImplementationDetail

    This is a mastapy class.
    """

    TYPE = _GEAR_SET_IMPLEMENTATION_DETAIL

    class _Cast_GearSetImplementationDetail:
        """Special nested class for casting GearSetImplementationDetail to subclasses."""

        def __init__(self, parent: 'GearSetImplementationDetail'):
            self._parent = parent

        @property
        def gear_set_design_analysis(self):
            return self._parent._cast(_1220.GearSetDesignAnalysis)

        @property
        def abstract_gear_set_analysis(self):
            from mastapy.gears.analysis import _1211
            
            return self._parent._cast(_1211.AbstractGearSetAnalysis)

        @property
        def cylindrical_set_manufacturing_config(self):
            from mastapy.gears.manufacturing.cylindrical import _620
            
            return self._parent._cast(_620.CylindricalSetManufacturingConfig)

        @property
        def conical_set_manufacturing_config(self):
            from mastapy.gears.manufacturing.bevel import _786
            
            return self._parent._cast(_786.ConicalSetManufacturingConfig)

        @property
        def conical_set_micro_geometry_config(self):
            from mastapy.gears.manufacturing.bevel import _787
            
            return self._parent._cast(_787.ConicalSetMicroGeometryConfig)

        @property
        def conical_set_micro_geometry_config_base(self):
            from mastapy.gears.manufacturing.bevel import _788
            
            return self._parent._cast(_788.ConicalSetMicroGeometryConfigBase)

        @property
        def face_gear_set_micro_geometry(self):
            from mastapy.gears.gear_designs.face import _991
            
            return self._parent._cast(_991.FaceGearSetMicroGeometry)

        @property
        def cylindrical_gear_set_micro_geometry(self):
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1101
            
            return self._parent._cast(_1101.CylindricalGearSetMicroGeometry)

        @property
        def gear_set_fe_model(self):
            from mastapy.gears.fe_model import _1194
            
            return self._parent._cast(_1194.GearSetFEModel)

        @property
        def cylindrical_gear_set_fe_model(self):
            from mastapy.gears.fe_model.cylindrical import _1197
            
            return self._parent._cast(_1197.CylindricalGearSetFEModel)

        @property
        def conical_set_fe_model(self):
            from mastapy.gears.fe_model.conical import _1200
            
            return self._parent._cast(_1200.ConicalSetFEModel)

        @property
        def gear_set_implementation_detail(self) -> 'GearSetImplementationDetail':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GearSetImplementationDetail.TYPE'):
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
    def user_specified_data(self) -> '_1730.UserSpecifiedData':
        """UserSpecifiedData: 'UserSpecifiedData' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.UserSpecifiedData

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'GearSetImplementationDetail._Cast_GearSetImplementationDetail':
        return self._Cast_GearSetImplementationDetail(self)
