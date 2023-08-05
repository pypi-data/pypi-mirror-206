"""__init__.py"""


from mastapy._internal.dummy_base_class_importer import _DummyBaseClassImport


with _DummyBaseClassImport():
    from ._1431 import AssemblyMethods
    from ._1432 import CalculationMethods
    from ._1433 import InterferenceFitDesign
    from ._1434 import InterferenceFitHalfDesign
    from ._1435 import StressRegions
    from ._1436 import Table4JointInterfaceTypes
