"""_1220.py

GearSetDesignAnalysis
"""
from mastapy.gears.analysis import _1211
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_SET_DESIGN_ANALYSIS = python_net_import('SMT.MastaAPI.Gears.Analysis', 'GearSetDesignAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('GearSetDesignAnalysis',)


class GearSetDesignAnalysis(_1211.AbstractGearSetAnalysis):
    """GearSetDesignAnalysis

    This is a mastapy class.
    """

    TYPE = _GEAR_SET_DESIGN_ANALYSIS

    class _Cast_GearSetDesignAnalysis:
        """Special nested class for casting GearSetDesignAnalysis to subclasses."""

        def __init__(self, parent: 'GearSetDesignAnalysis'):
            self._parent = parent

        @property
        def abstract_gear_set_analysis(self):
            return self._parent._cast(_1211.AbstractGearSetAnalysis)

        @property
        def cylindrical_manufactured_gear_set_duty_cycle(self):
            from mastapy.gears.manufacturing.cylindrical import _615
            
            return self._parent._cast(_615.CylindricalManufacturedGearSetDutyCycle)

        @property
        def cylindrical_manufactured_gear_set_load_case(self):
            from mastapy.gears.manufacturing.cylindrical import _616
            
            return self._parent._cast(_616.CylindricalManufacturedGearSetLoadCase)

        @property
        def cylindrical_set_manufacturing_config(self):
            from mastapy.gears.manufacturing.cylindrical import _620
            
            return self._parent._cast(_620.CylindricalSetManufacturingConfig)

        @property
        def conical_set_manufacturing_analysis(self):
            from mastapy.gears.manufacturing.bevel import _785
            
            return self._parent._cast(_785.ConicalSetManufacturingAnalysis)

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
        def gear_set_load_distribution_analysis(self):
            from mastapy.gears.ltca import _841
            
            return self._parent._cast(_841.GearSetLoadDistributionAnalysis)

        @property
        def cylindrical_gear_set_load_distribution_analysis(self):
            from mastapy.gears.ltca.cylindrical import _855
            
            return self._parent._cast(_855.CylindricalGearSetLoadDistributionAnalysis)

        @property
        def face_gear_set_load_distribution_analysis(self):
            from mastapy.gears.ltca.cylindrical import _857
            
            return self._parent._cast(_857.FaceGearSetLoadDistributionAnalysis)

        @property
        def conical_gear_set_load_distribution_analysis(self):
            from mastapy.gears.ltca.conical import _863
            
            return self._parent._cast(_863.ConicalGearSetLoadDistributionAnalysis)

        @property
        def gear_set_load_case_base(self):
            from mastapy.gears.load_case import _869
            
            return self._parent._cast(_869.GearSetLoadCaseBase)

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
        def cylindrical_gear_set_tiff_analysis(self):
            from mastapy.gears.gear_two_d_fe_analysis import _891
            
            return self._parent._cast(_891.CylindricalGearSetTIFFAnalysis)

        @property
        def cylindrical_gear_set_tiff_analysis_duty_cycle(self):
            from mastapy.gears.gear_two_d_fe_analysis import _892
            
            return self._parent._cast(_892.CylindricalGearSetTIFFAnalysisDutyCycle)

        @property
        def face_gear_set_micro_geometry(self):
            from mastapy.gears.gear_designs.face import _991
            
            return self._parent._cast(_991.FaceGearSetMicroGeometry)

        @property
        def cylindrical_gear_set_micro_geometry(self):
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1101
            
            return self._parent._cast(_1101.CylindricalGearSetMicroGeometry)

        @property
        def cylindrical_gear_set_micro_geometry_duty_cycle(self):
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1102
            
            return self._parent._cast(_1102.CylindricalGearSetMicroGeometryDutyCycle)

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
        def gear_set_implementation_analysis(self):
            from mastapy.gears.analysis import _1222
            
            return self._parent._cast(_1222.GearSetImplementationAnalysis)

        @property
        def gear_set_implementation_analysis_abstract(self):
            from mastapy.gears.analysis import _1223
            
            return self._parent._cast(_1223.GearSetImplementationAnalysisAbstract)

        @property
        def gear_set_implementation_analysis_duty_cycle(self):
            from mastapy.gears.analysis import _1224
            
            return self._parent._cast(_1224.GearSetImplementationAnalysisDutyCycle)

        @property
        def gear_set_implementation_detail(self):
            from mastapy.gears.analysis import _1225
            
            return self._parent._cast(_1225.GearSetImplementationDetail)

        @property
        def gear_set_design_analysis(self) -> 'GearSetDesignAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GearSetDesignAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'GearSetDesignAnalysis._Cast_GearSetDesignAnalysis':
        return self._Cast_GearSetDesignAnalysis(self)
