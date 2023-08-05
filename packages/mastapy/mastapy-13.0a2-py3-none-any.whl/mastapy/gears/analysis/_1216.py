"""_1216.py

GearMeshDesignAnalysis
"""
from mastapy.gears.analysis import _1212, _1210
from mastapy._internal import constructor
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_MESH_DESIGN_ANALYSIS = python_net_import('SMT.MastaAPI.Gears.Analysis', 'GearMeshDesignAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('GearMeshDesignAnalysis',)


class GearMeshDesignAnalysis(_1210.AbstractGearMeshAnalysis):
    """GearMeshDesignAnalysis

    This is a mastapy class.
    """

    TYPE = _GEAR_MESH_DESIGN_ANALYSIS

    class _Cast_GearMeshDesignAnalysis:
        """Special nested class for casting GearMeshDesignAnalysis to subclasses."""

        def __init__(self, parent: 'GearMeshDesignAnalysis'):
            self._parent = parent

        @property
        def abstract_gear_mesh_analysis(self):
            return self._parent._cast(_1210.AbstractGearMeshAnalysis)

        @property
        def cylindrical_manufactured_gear_mesh_duty_cycle(self):
            from mastapy.gears.manufacturing.cylindrical import _613
            
            return self._parent._cast(_613.CylindricalManufacturedGearMeshDutyCycle)

        @property
        def cylindrical_manufactured_gear_mesh_load_case(self):
            from mastapy.gears.manufacturing.cylindrical import _614
            
            return self._parent._cast(_614.CylindricalManufacturedGearMeshLoadCase)

        @property
        def cylindrical_mesh_manufacturing_config(self):
            from mastapy.gears.manufacturing.cylindrical import _617
            
            return self._parent._cast(_617.CylindricalMeshManufacturingConfig)

        @property
        def conical_mesh_manufacturing_analysis(self):
            from mastapy.gears.manufacturing.bevel import _779
            
            return self._parent._cast(_779.ConicalMeshManufacturingAnalysis)

        @property
        def conical_mesh_manufacturing_config(self):
            from mastapy.gears.manufacturing.bevel import _780
            
            return self._parent._cast(_780.ConicalMeshManufacturingConfig)

        @property
        def conical_mesh_micro_geometry_config(self):
            from mastapy.gears.manufacturing.bevel import _781
            
            return self._parent._cast(_781.ConicalMeshMicroGeometryConfig)

        @property
        def conical_mesh_micro_geometry_config_base(self):
            from mastapy.gears.manufacturing.bevel import _782
            
            return self._parent._cast(_782.ConicalMeshMicroGeometryConfigBase)

        @property
        def gear_mesh_load_distribution_analysis(self):
            from mastapy.gears.ltca import _836
            
            return self._parent._cast(_836.GearMeshLoadDistributionAnalysis)

        @property
        def cylindrical_gear_mesh_load_distribution_analysis(self):
            from mastapy.gears.ltca.cylindrical import _852
            
            return self._parent._cast(_852.CylindricalGearMeshLoadDistributionAnalysis)

        @property
        def conical_mesh_load_distribution_analysis(self):
            from mastapy.gears.ltca.conical import _865
            
            return self._parent._cast(_865.ConicalMeshLoadDistributionAnalysis)

        @property
        def mesh_load_case(self):
            from mastapy.gears.load_case import _870
            
            return self._parent._cast(_870.MeshLoadCase)

        @property
        def worm_mesh_load_case(self):
            from mastapy.gears.load_case.worm import _873
            
            return self._parent._cast(_873.WormMeshLoadCase)

        @property
        def face_mesh_load_case(self):
            from mastapy.gears.load_case.face import _876
            
            return self._parent._cast(_876.FaceMeshLoadCase)

        @property
        def cylindrical_mesh_load_case(self):
            from mastapy.gears.load_case.cylindrical import _879
            
            return self._parent._cast(_879.CylindricalMeshLoadCase)

        @property
        def conical_mesh_load_case(self):
            from mastapy.gears.load_case.conical import _882
            
            return self._parent._cast(_882.ConicalMeshLoadCase)

        @property
        def concept_mesh_load_case(self):
            from mastapy.gears.load_case.concept import _885
            
            return self._parent._cast(_885.ConceptMeshLoadCase)

        @property
        def bevel_mesh_load_case(self):
            from mastapy.gears.load_case.bevel import _887
            
            return self._parent._cast(_887.BevelMeshLoadCase)

        @property
        def cylindrical_gear_mesh_tiff_analysis(self):
            from mastapy.gears.gear_two_d_fe_analysis import _889
            
            return self._parent._cast(_889.CylindricalGearMeshTIFFAnalysis)

        @property
        def cylindrical_gear_mesh_tiff_analysis_duty_cycle(self):
            from mastapy.gears.gear_two_d_fe_analysis import _890
            
            return self._parent._cast(_890.CylindricalGearMeshTIFFAnalysisDutyCycle)

        @property
        def face_gear_mesh_micro_geometry(self):
            from mastapy.gears.gear_designs.face import _987
            
            return self._parent._cast(_987.FaceGearMeshMicroGeometry)

        @property
        def cylindrical_gear_mesh_micro_geometry(self):
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1092
            
            return self._parent._cast(_1092.CylindricalGearMeshMicroGeometry)

        @property
        def cylindrical_gear_mesh_micro_geometry_duty_cycle(self):
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1093
            
            return self._parent._cast(_1093.CylindricalGearMeshMicroGeometryDutyCycle)

        @property
        def gear_mesh_fe_model(self):
            from mastapy.gears.fe_model import _1192
            
            return self._parent._cast(_1192.GearMeshFEModel)

        @property
        def cylindrical_gear_mesh_fe_model(self):
            from mastapy.gears.fe_model.cylindrical import _1196
            
            return self._parent._cast(_1196.CylindricalGearMeshFEModel)

        @property
        def conical_mesh_fe_model(self):
            from mastapy.gears.fe_model.conical import _1199
            
            return self._parent._cast(_1199.ConicalMeshFEModel)

        @property
        def gear_mesh_implementation_analysis(self):
            from mastapy.gears.analysis import _1217
            
            return self._parent._cast(_1217.GearMeshImplementationAnalysis)

        @property
        def gear_mesh_implementation_analysis_duty_cycle(self):
            from mastapy.gears.analysis import _1218
            
            return self._parent._cast(_1218.GearMeshImplementationAnalysisDutyCycle)

        @property
        def gear_mesh_implementation_detail(self):
            from mastapy.gears.analysis import _1219
            
            return self._parent._cast(_1219.GearMeshImplementationDetail)

        @property
        def gear_mesh_design_analysis(self) -> 'GearMeshDesignAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GearMeshDesignAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def gear_a(self) -> '_1212.GearDesignAnalysis':
        """GearDesignAnalysis: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b(self) -> '_1212.GearDesignAnalysis':
        """GearDesignAnalysis: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'GearMeshDesignAnalysis._Cast_GearMeshDesignAnalysis':
        return self._Cast_GearMeshDesignAnalysis(self)
