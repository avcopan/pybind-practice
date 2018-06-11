#include <iostream>
#include <pybind11/pybind11.h>

namespace py = pybind11;


int add(int i, int j) {
    return i + j;
}


void greet() {
    std::cout << "Hello world!" << std::endl;
}


PYBIND11_MODULE(pybind_example, module) {
    module.def("add", &add, "A function which adds two numbers",
               py::arg("i") = 0, py::arg("j") = 0);
}
