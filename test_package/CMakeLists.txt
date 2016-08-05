project(conan-problem-test-project)
cmake_minimum_required(VERSION 2.8.12)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

add_executable(conan-problem-test-project main.cpp)
target_link_libraries(conan-problem-test-project ${CONAN_LIBS})
