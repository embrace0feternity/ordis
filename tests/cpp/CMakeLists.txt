
if (NOT DEFINED elib_enyo_FOUND)
     set(CMAKE_MODULE_PATH ${CMAKE_BINARY_DIR}/${CMAKE_BUILD_TYPE}/generators)
endif()
find_package(GTest REQUIRED)
include(GoogleTest)

set(CPP_TESTS ordistests)
file(GLOB ORDIS_TESTS_SRC
     "*.h"
     "*.cpp"
     )

add_executable(${CPP_TESTS} ${ORDIS_TESTS_SRC})
target_link_libraries(${CPP_TESTS} GTest::gtest_main)

gtest_discover_tests(${CPP_TESTS})