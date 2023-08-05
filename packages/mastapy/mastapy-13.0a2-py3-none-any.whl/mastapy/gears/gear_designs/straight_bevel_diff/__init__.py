"""__init__.py"""


from mastapy._internal.dummy_base_class_importer import _DummyBaseClassImport


with _DummyBaseClassImport():
    from ._960 import StraightBevelDiffGearDesign
    from ._961 import StraightBevelDiffGearMeshDesign
    from ._962 import StraightBevelDiffGearSetDesign
    from ._963 import StraightBevelDiffMeshedGearDesign
