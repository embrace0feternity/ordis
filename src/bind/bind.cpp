// #include "mock/runner.hpp"
#include <pybind11/pybind11.h>
// #include <enyo/enyo.hpp>
namespace py = pybind11;

int add(int i, int j) {
    return i + j;
}

PYBIND11_MODULE(ordis, m) {
    m.doc() = "pybind11 example plugin"; // optional module docstring

    m.def("add", &add, "A function that adds two numbers");
}


// PYBIND11_MODULE(ordis, m) {
//   py::class_<Runner<t6137>>(m, "Runner")
//         .def(py::init<>())
//         .def("create", &Runner<t6137>::create);
// }
