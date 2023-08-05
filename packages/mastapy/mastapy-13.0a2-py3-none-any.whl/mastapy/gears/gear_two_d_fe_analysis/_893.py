"""_893.py

CylindricalGearTIFFAnalysis
"""
from mastapy.gears.gear_two_d_fe_analysis import _895
from mastapy._internal import constructor
from mastapy.gears.analysis import _1212
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_TIFF_ANALYSIS = python_net_import('SMT.MastaAPI.Gears.GearTwoDFEAnalysis', 'CylindricalGearTIFFAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearTIFFAnalysis',)


class CylindricalGearTIFFAnalysis(_1212.GearDesignAnalysis):
    """CylindricalGearTIFFAnalysis

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_TIFF_ANALYSIS

    class _Cast_CylindricalGearTIFFAnalysis:
        """Special nested class for casting CylindricalGearTIFFAnalysis to subclasses."""

        def __init__(self, parent: 'CylindricalGearTIFFAnalysis'):
            self._parent = parent

        @property
        def gear_design_analysis(self):
            return self._parent._cast(_1212.GearDesignAnalysis)

        @property
        def abstract_gear_analysis(self):
            from mastapy.gears.analysis import _1209
            
            return self._parent._cast(_1209.AbstractGearAnalysis)

        @property
        def cylindrical_gear_tiff_analysis(self) -> 'CylindricalGearTIFFAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CylindricalGearTIFFAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def analysis(self) -> '_895.CylindricalGearTwoDimensionalFEAnalysis':
        """CylindricalGearTwoDimensionalFEAnalysis: 'Analysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Analysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cast_to(self) -> 'CylindricalGearTIFFAnalysis._Cast_CylindricalGearTIFFAnalysis':
        return self._Cast_CylindricalGearTIFFAnalysis(self)
