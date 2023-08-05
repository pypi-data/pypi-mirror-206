"""_889.py

CylindricalGearMeshTIFFAnalysis
"""
from mastapy.gears.analysis import _1216
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_MESH_TIFF_ANALYSIS = python_net_import('SMT.MastaAPI.Gears.GearTwoDFEAnalysis', 'CylindricalGearMeshTIFFAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearMeshTIFFAnalysis',)


class CylindricalGearMeshTIFFAnalysis(_1216.GearMeshDesignAnalysis):
    """CylindricalGearMeshTIFFAnalysis

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_MESH_TIFF_ANALYSIS

    class _Cast_CylindricalGearMeshTIFFAnalysis:
        """Special nested class for casting CylindricalGearMeshTIFFAnalysis to subclasses."""

        def __init__(self, parent: 'CylindricalGearMeshTIFFAnalysis'):
            self._parent = parent

        @property
        def gear_mesh_design_analysis(self):
            return self._parent._cast(_1216.GearMeshDesignAnalysis)

        @property
        def abstract_gear_mesh_analysis(self):
            from mastapy.gears.analysis import _1210
            
            return self._parent._cast(_1210.AbstractGearMeshAnalysis)

        @property
        def cylindrical_gear_mesh_tiff_analysis(self) -> 'CylindricalGearMeshTIFFAnalysis':
            return self._parent

        def __getattr__(self, name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = ''.join(n.capitalize() for n in name.split('_'))
                raise CastException(f'Detected an invalid cast. Cannot cast to type "{class_name}"') from None

    def __init__(self, instance_to_wrap: 'CylindricalGearMeshTIFFAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self) -> 'CylindricalGearMeshTIFFAnalysis._Cast_CylindricalGearMeshTIFFAnalysis':
        return self._Cast_CylindricalGearMeshTIFFAnalysis(self)
