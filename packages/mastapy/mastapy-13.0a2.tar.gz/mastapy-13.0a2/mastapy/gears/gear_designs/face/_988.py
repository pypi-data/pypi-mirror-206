"""_988.py

FaceGearMicroGeometry
"""
from mastapy.gears.gear_designs.face import _984
from mastapy._internal import constructor
from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1095
from mastapy.gears.analysis import _1215
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_MICRO_GEOMETRY = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Face', 'FaceGearMicroGeometry')


__docformat__ = 'restructuredtext en'
__all__ = ('FaceGearMicroGeometry',)


class FaceGearMicroGeometry(_1215.GearImplementationDetail):
    """FaceGearMicroGeometry

    This is a mastapy class.
    """

    TYPE = _FACE_GEAR_MICRO_GEOMETRY

    class _Cast_FaceGearMicroGeometry:
        """Special nested class for casting FaceGearMicroGeometry to subclasses."""

        def __init__(self, parent: 'FaceGearMicroGeometry'):
            self._parent = parent

        @property
        def gear_implementation_detail(self):
            return self._parent._cast(_1215.GearImplementationDetail)

        @property
        def gear_design_analysis(self):
            from mastapy.gears.analysis import _1212
            
            return self._parent._cast(_1212.GearDesignAnalysis)

        @property
        def abstract_gear_analysis(self):
            from mastapy.gears.analysis import _1209
            
            return self._parent._cast(_1209.AbstractGearAnalysis)

        @property
        def face_gear_micro_geometry(self) -> 'FaceGearMicroGeometry':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'FaceGearMicroGeometry.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def face_gear(self) -> '_984.FaceGearDesign':
        """FaceGearDesign: 'FaceGear' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FaceGear

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def micro_geometry(self) -> '_1095.CylindricalGearMicroGeometryBase':
        """CylindricalGearMicroGeometryBase: 'MicroGeometry' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MicroGeometry

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'FaceGearMicroGeometry._Cast_FaceGearMicroGeometry':
        return self._Cast_FaceGearMicroGeometry(self)
