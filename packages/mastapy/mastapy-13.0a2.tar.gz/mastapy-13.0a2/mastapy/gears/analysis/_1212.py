"""_1212.py

GearDesignAnalysis
"""
from mastapy.gears.analysis import _1209
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_DESIGN_ANALYSIS = python_net_import('SMT.MastaAPI.Gears.Analysis', 'GearDesignAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('GearDesignAnalysis',)


class GearDesignAnalysis(_1209.AbstractGearAnalysis):
    """GearDesignAnalysis

    This is a mastapy class.
    """

    TYPE = _GEAR_DESIGN_ANALYSIS

    class _Cast_GearDesignAnalysis:
        """Special nested class for casting GearDesignAnalysis to subclasses."""

        def __init__(self, parent: 'GearDesignAnalysis'):
            self._parent = parent

        @property
        def abstract_gear_analysis(self):
            return self._parent._cast(_1209.AbstractGearAnalysis)

        @property
        def cylindrical_gear_manufacturing_config(self):
            from mastapy.gears.manufacturing.cylindrical import _607
            
            return self._parent._cast(_607.CylindricalGearManufacturingConfig)

        @property
        def cylindrical_manufactured_gear_duty_cycle(self):
            from mastapy.gears.manufacturing.cylindrical import _611
            
            return self._parent._cast(_611.CylindricalManufacturedGearDutyCycle)

        @property
        def cylindrical_manufactured_gear_load_case(self):
            from mastapy.gears.manufacturing.cylindrical import _612
            
            return self._parent._cast(_612.CylindricalManufacturedGearLoadCase)

        @property
        def conical_gear_manufacturing_analysis(self):
            from mastapy.gears.manufacturing.bevel import _770
            
            return self._parent._cast(_770.ConicalGearManufacturingAnalysis)

        @property
        def conical_gear_manufacturing_config(self):
            from mastapy.gears.manufacturing.bevel import _771
            
            return self._parent._cast(_771.ConicalGearManufacturingConfig)

        @property
        def conical_gear_micro_geometry_config(self):
            from mastapy.gears.manufacturing.bevel import _772
            
            return self._parent._cast(_772.ConicalGearMicroGeometryConfig)

        @property
        def conical_gear_micro_geometry_config_base(self):
            from mastapy.gears.manufacturing.bevel import _773
            
            return self._parent._cast(_773.ConicalGearMicroGeometryConfigBase)

        @property
        def conical_pinion_manufacturing_config(self):
            from mastapy.gears.manufacturing.bevel import _783
            
            return self._parent._cast(_783.ConicalPinionManufacturingConfig)

        @property
        def conical_pinion_micro_geometry_config(self):
            from mastapy.gears.manufacturing.bevel import _784
            
            return self._parent._cast(_784.ConicalPinionMicroGeometryConfig)

        @property
        def conical_wheel_manufacturing_config(self):
            from mastapy.gears.manufacturing.bevel import _789
            
            return self._parent._cast(_789.ConicalWheelManufacturingConfig)

        @property
        def gear_load_distribution_analysis(self):
            from mastapy.gears.ltca import _835
            
            return self._parent._cast(_835.GearLoadDistributionAnalysis)

        @property
        def cylindrical_gear_load_distribution_analysis(self):
            from mastapy.gears.ltca.cylindrical import _851
            
            return self._parent._cast(_851.CylindricalGearLoadDistributionAnalysis)

        @property
        def conical_gear_load_distribution_analysis(self):
            from mastapy.gears.ltca.conical import _862
            
            return self._parent._cast(_862.ConicalGearLoadDistributionAnalysis)

        @property
        def gear_load_case_base(self):
            from mastapy.gears.load_case import _868
            
            return self._parent._cast(_868.GearLoadCaseBase)

        @property
        def worm_gear_load_case(self):
            from mastapy.gears.load_case.worm import _871
            
            return self._parent._cast(_871.WormGearLoadCase)

        @property
        def face_gear_load_case(self):
            from mastapy.gears.load_case.face import _874
            
            return self._parent._cast(_874.FaceGearLoadCase)

        @property
        def cylindrical_gear_load_case(self):
            from mastapy.gears.load_case.cylindrical import _877
            
            return self._parent._cast(_877.CylindricalGearLoadCase)

        @property
        def conical_gear_load_case(self):
            from mastapy.gears.load_case.conical import _880
            
            return self._parent._cast(_880.ConicalGearLoadCase)

        @property
        def concept_gear_load_case(self):
            from mastapy.gears.load_case.concept import _883
            
            return self._parent._cast(_883.ConceptGearLoadCase)

        @property
        def bevel_load_case(self):
            from mastapy.gears.load_case.bevel import _886
            
            return self._parent._cast(_886.BevelLoadCase)

        @property
        def cylindrical_gear_tiff_analysis(self):
            from mastapy.gears.gear_two_d_fe_analysis import _893
            
            return self._parent._cast(_893.CylindricalGearTIFFAnalysis)

        @property
        def cylindrical_gear_tiff_analysis_duty_cycle(self):
            from mastapy.gears.gear_two_d_fe_analysis import _894
            
            return self._parent._cast(_894.CylindricalGearTIFFAnalysisDutyCycle)

        @property
        def face_gear_micro_geometry(self):
            from mastapy.gears.gear_designs.face import _988
            
            return self._parent._cast(_988.FaceGearMicroGeometry)

        @property
        def cylindrical_gear_micro_geometry(self):
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1094
            
            return self._parent._cast(_1094.CylindricalGearMicroGeometry)

        @property
        def cylindrical_gear_micro_geometry_base(self):
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1095
            
            return self._parent._cast(_1095.CylindricalGearMicroGeometryBase)

        @property
        def cylindrical_gear_micro_geometry_duty_cycle(self):
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1096
            
            return self._parent._cast(_1096.CylindricalGearMicroGeometryDutyCycle)

        @property
        def cylindrical_gear_micro_geometry_per_tooth(self):
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1098
            
            return self._parent._cast(_1098.CylindricalGearMicroGeometryPerTooth)

        @property
        def gear_fe_model(self):
            from mastapy.gears.fe_model import _1191
            
            return self._parent._cast(_1191.GearFEModel)

        @property
        def cylindrical_gear_fe_model(self):
            from mastapy.gears.fe_model.cylindrical import _1195
            
            return self._parent._cast(_1195.CylindricalGearFEModel)

        @property
        def conical_gear_fe_model(self):
            from mastapy.gears.fe_model.conical import _1198
            
            return self._parent._cast(_1198.ConicalGearFEModel)

        @property
        def gear_implementation_analysis(self):
            from mastapy.gears.analysis import _1213
            
            return self._parent._cast(_1213.GearImplementationAnalysis)

        @property
        def gear_implementation_analysis_duty_cycle(self):
            from mastapy.gears.analysis import _1214
            
            return self._parent._cast(_1214.GearImplementationAnalysisDutyCycle)

        @property
        def gear_implementation_detail(self):
            from mastapy.gears.analysis import _1215
            
            return self._parent._cast(_1215.GearImplementationDetail)

        @property
        def gear_design_analysis(self) -> 'GearDesignAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'GearDesignAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'GearDesignAnalysis._Cast_GearDesignAnalysis':
        return self._Cast_GearDesignAnalysis(self)
