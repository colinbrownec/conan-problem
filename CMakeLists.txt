project(conan-problem-project)
cmake_minimum_required(VERSION 2.8)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

if (BUILD_SHARED_LIBS)
  add_library(conan-problem-project SHARED src/hello.cpp)
else()
  add_library(conan-problem-project STATIC src/hello.cpp)
endif()

#target_link_libraries(conan-problem-project ${CONAN_LIBS})

install(TARGETS conan-problem-project
        LIBRARY DESTINATION lib
        ARCHIVE DESTINATION lib)

install(DIRECTORY src/
        DESTINATION include
        FILES_MATCHING PATTERN "*.hpp")
