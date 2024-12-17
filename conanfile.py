from conan import ConanFile
from conan.tools.cmake import cmake_layout, CMake

#       Base conan recipe for ordis.
#   To install dependencies of internal packages (like enyo),
#   use option mock=True
#
#       conan install 'conan-recipe' -o mock=true
#
#   Set mock=False if you won't work with internal packages


class ExampleRecipe(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "CMakeDeps", "CMakeToolchain"
    options = {"mock": [True, False]}
    default_options = {"mock": False}
    build_policy = "missing"

    def requirements(self):
        self.requires("gtest/1.15.0")
        print("+++++", self.options)
        if (self.options.mock == False):
            self.requires("elib_enyo/[2.4]@admin/stable")

    def layout(self):
        cmake_layout(self)
