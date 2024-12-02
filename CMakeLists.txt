cmake_minimum_required(VERSION 3.20)
project(ordisapp LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(BIND_TARGET_NAME ordis)

find_package(Python COMPONENTS Interpreter Development)
find_package(pybind11 CONFIG)

if (NOT DEFINED pybind11_FOUND) 
    message(FATAL_ERROR "Pybind hasn't been found!")
endif()

file(GLOB ORDIS_SRC
     "src/bind/*.h"
     "src/bind/*.cpp"
)

pybind11_add_module(${BIND_TARGET_NAME} ${ORDIS_SRC})
set(pybind11_DIR ${CMAKE_CURRENT_BINARY_DIR})
target_compile_definitions(${BIND_TARGET_NAME}
                           PRIVATE VERSION_INFO=${EXAMPLE_VERSION_INFO})
