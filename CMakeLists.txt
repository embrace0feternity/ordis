cmake_minimum_required(VERSION 3.20)
project(ordis LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(BIND_TARGET_NAME ordis_lib)

find_package(Python COMPONENTS Interpreter Development)
find_package(pybind11 CONFIG)

if (NOT DEFINED pybind11_FOUND) 
    message(FATAL_ERROR "Pybind hasn't been found!")
endif()

pybind11_add_module(${BIND_TARGET_NAME} clib/bind.cpp)
set(pybind11_DIR ${CMAKE_CURRENT_BINARY_DIR})