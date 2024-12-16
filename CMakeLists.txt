cmake_minimum_required(VERSION 3.20)
project(ordisapp LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(ORDIS_LIB ordis_lib)

find_package(Python COMPONENTS Interpreter Development)
find_package(pybind11 CONFIG)
find_package(elib_enyo CONFIG)

set(BIND_TARGET ordis)

pybind11_add_module(${BIND_TARGET} 
    src/bind/bind.cpp)

target_link_libraries(${BIND_TARGET} PUBLIC elib_enyo::elib_enyo)

# if (NOT DEFINED elib_enyo_FOUND) 
#     message(STATUS "ENYO hasn't been found!
#     \   Create mock enyo library")
# endif()


# set(ORDIS_TESTS ON CACHE BOOL "enable/disable tests")
# set(ORDIS_TESTS OFF)
# if (${ORDIS_TESTS})
#     enable_testing()
#     add_subdirectory(${CMAKE_CURRENT_SOURCE_DIR}/tests)
# endif()