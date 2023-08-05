"""__init__.py"""


from mastapy._internal.dummy_base_class_importer import _DummyBaseClassImport


with _DummyBaseClassImport():
    from ._951 import WormDesign
    from ._952 import WormGearDesign
    from ._953 import WormGearMeshDesign
    from ._954 import WormGearSetDesign
    from ._955 import WormWheelDesign
