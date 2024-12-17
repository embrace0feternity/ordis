cmake_minimum_required(VERSION 3.20)
project(ordisapp LANGUAGES CXX)


set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)


find_package(Python COMPONENTS Interpreter Development)
find_package(pybind11 CONFIG)
find_package(elib_enyo CONFIG)


if (NOT ${elib_enyo_FOUND})
    include_directories(mock/)
else()
    set(ENYO elib_enyo::elib_enyo)
endif()

set(BIND ordis)
pybind11_add_module(${BIND} 
    src/bind/wrapper/interfaces.cpp
    src/bind/bind.cpp
)
target_link_libraries(${BIND} PUBLIC ${ENYO})

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