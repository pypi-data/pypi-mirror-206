"""__init__.py"""


from mastapy._internal.dummy_base_class_importer import _DummyBaseClassImport


with _DummyBaseClassImport():
    from ._880 import ConicalGearLoadCase
    from ._881 import ConicalGearSetLoadCase
    from ._882 import ConicalMeshLoadCase
