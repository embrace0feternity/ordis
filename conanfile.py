from conan import ConanFile
from conan.tools.cmake import cmake_layout


class ExampleRecipe(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "CMakeDeps", "CMakeToolchain"

    build_policy = "missing"

    def requirements(self):
        self.requires("elib_enyo/[2.4]@admin/stable")

    def layout(self):
        cmake_layout(self)
