# pybind-practice

Compile with:
```
c++ -O3 -Wall -shared -std=c++11 -fPIC `python3 -m pybind11 --includes`
example.cpp -o example.so
```

Examples:
```
>>> import example
>>> example.add(1, 2)
3
```
