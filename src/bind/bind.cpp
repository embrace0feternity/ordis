#include "runner.hpp"
#include <pybind11/pybind11.h>

namespace py = pybind11;

PYBIND11_MODULE(ordis, m) {
  py::class_<Runner<t6137>>(m, "Runner").def(py::init<>());
}
