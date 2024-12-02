
set(CMAKE_MODULE_PATH ${CMAKE_CURRENT_BINARY_DIR}/${CMAKE_BUILD_TYPE}/generators)
find_package(GTest REQUIRED)

set(CPP_TESTS ordistests)
file(GLOB ORDIS_TESTS_SRC
     "tests/cpp/*.h"
     "tests/cpp/*.cpp"
     )
     
add_executable(${CPP_TESTS} ${ORDIS_TESTS_SRC})
target_link_libraries(${CPP_TESTS} GTest::gtest_main)

include(GoogleTest)
gtest_discover_tests(${CPP_TESTS})