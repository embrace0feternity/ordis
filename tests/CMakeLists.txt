
if (NOT DEFINED elib_enyo_FOUND)
     set(CMAKE_MODULE_PATH ${CMAKE_BINARY_DIR}/${CMAKE_BUILD_TYPE}/generators)
endif()
find_package(GTest REQUIRED)
include(GoogleTest)

set(CPP_TESTS ordistests)
file(GLOB ORDIS_TESTS_SRC
     "src/*.h"
     "src/*.cpp"
     )
include_directories(${CMAKE_CURRENT_LIST_DIR}/src)
include_directories(${CMAKE_CURRENT_LIST_DIR}/../src)
     

add_executable(${CPP_TESTS} ${ORDIS_TESTS_SRC})
target_link_libraries(${CPP_TESTS} PUBLIC GTest::gtest_main)
target_link_libraries(${CPP_TESTS} PUBLIC ${ORDIS_LIB})
target_link_libraries(${CPP_TESTS} PUBLIC elib_enyo::elib_enyo)

gtest_discover_tests(${CPP_TESTS})