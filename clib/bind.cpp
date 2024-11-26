#include <pybind11/pybind11.h>
#include <iostream>
#include "ordis.hpp"

PYBIND11_MODULE(ordis, m) {
    m.doc() = "pybind11 example plugin"; // optional module docstring
    m.def("add", &sum, "A function that adds two numbers");
}