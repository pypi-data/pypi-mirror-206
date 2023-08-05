"""__init__.py"""


from mastapy._internal.dummy_base_class_importer import _DummyBaseClassImport


with _DummyBaseClassImport():
    from ._980 import HypoidGearDesign
    from ._981 import HypoidGearMeshDesign
    from ._982 import HypoidGearSetDesign
    from ._983 import HypoidMeshedGearDesign
