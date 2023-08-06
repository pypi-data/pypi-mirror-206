cmake_minimum_required(VERSION 3.12 FATAL_ERROR)

project(inference-cpp LANGUAGES C CXX)

# C++ configurations.
set(CMAKE_CXX_STANDARD 17)

# Shared library settings
if(APPLE)
  set(CMAKE_SHARED_LIBRARY_SUFFIX ".so")
elseif(WIN32)
  message(FATAL_ERROR "Windows is not supported")
endif()

# Finds PyTorch and Python libraries.
find_package(Torch REQUIRED)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} ${TORCH_CXX_FLAGS}")
find_package(PythonLibs REQUIRED)
find_package(pybind11 REQUIRED)

# Links relevant directories.
link_directories(${TORCH_INSTALL_PREFIX}/lib)
if(DEFINED ENV{CONDA_PREFIX})
  link_directories($ENV{CONDA_PREFIX}/lib)
endif()

macro(build_torch_extension)
  set(LIBRARY_NAME ${ARGV0})

  # Gets all source files.
  file(GLOB_RECURSE SRC_FILES *.c *.cpp)

  add_library(${LIBRARY_NAME} SHARED ${SRC_FILES})

  # Sets shared library properties.
  set_target_properties(${LIBRARY_NAME} PROPERTIES LIBRARY_OUTPUT_DIRECTORY
                                                   ${CMAKE_CURRENT_SOURCE_DIR})
  set_target_properties(${LIBRARY_NAME} PROPERTIES PREFIX "")
  set_target_properties(${LIBRARY_NAME} PROPERTIES OUTPUT_NAME ${LIBRARY_NAME})

  # Links with Torch directories.
  target_include_directories(
    ${LIBRARY_NAME}
    PUBLIC ${TORCH_INCLUDE_DIRS}
    PUBLIC ${PYTHON_INCLUDE_DIRS}
    PUBLIC ${pybind11_INCLUDE_DIRS})
  target_link_libraries(
    ${LIBRARY_NAME}
    PUBLIC c10
    PUBLIC torch
    PUBLIC torch_cpu
    PUBLIC torch_python
    PUBLIC ${TORCH_PYTHON_LIBRARY}
    PUBLIC ${pybind11_LIBRARIES})
endmacro()

# Subprojects.
add_subdirectory(torch_ops)
add_subdirectory(inference)
