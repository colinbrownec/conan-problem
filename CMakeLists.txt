project(conan-problem-project)
cmake_minimum_required(VERSION 2.8)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

# Not necessary to specify if using BUILD_SHARED_LIBS
add_library(conan-problem-project src/hello.cpp)

#target_link_libraries(conan-problem-project ${CONAN_LIBS})

install(TARGETS conan-problem-project
        LIBRARY DESTINATION lib
        ARCHIVE DESTINATION lib)

install(DIRECTORY src/
        DESTINATION include/conan-problem-project
        FILES_MATCHING PATTERN "*.hpp")
