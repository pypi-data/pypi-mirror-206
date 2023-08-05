"""__init__.py"""


from mastapy._internal.dummy_base_class_importer import _DummyBaseClassImport


with _DummyBaseClassImport():
    from ._874 import FaceGearLoadCase
    from ._875 import FaceGearSetLoadCase
    from ._876 import FaceMeshLoadCase
