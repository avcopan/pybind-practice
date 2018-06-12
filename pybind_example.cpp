#include <iostream>
#include <string>
#include <pybind11/pybind11.h>

namespace py = pybind11;


int add(int i, int j) {
    return i + j;
}


int add_str(const std::string& si, const std::string& sj) {
    int i = std::stoi(si);
    int j = std::stoi(sj);
    return i + j;
}


PYBIND11_MODULE(pybind_example, module) {
    module.def("add", &add);
    module.def("add_str", &add_str);
}
