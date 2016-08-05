from conans import ConanFile, CMake
import os
import shutil

class ConanProblemProject(ConanFile):
  name = 'ConanProblemProject'
  version = '1.0'

  settings = 'os', 'compiler', 'build_type', 'arch'
  generators = 'cmake'

  requires = 'Eigen3/3.2.8@bilke/stable'

  options = { 'shared': [True, False]}
  default_options = 'shared=False'

  def source(self):
    self.run("git clone https://github.com/colinbrownec/conan-problem.git")

  def build(self):
    cmake = CMake(self.settings)
    args = ' '.join([
      '-DCMAKE_INSTALL_PREFIX=%s' % self.package_folder,
      '-DBUILD_SHARED_LIBS=%s' % ('ON' if self.options.shared else 'OFF')
    ])

    self.run('mkdir build')
    #shutil.copy('conanbuildinfo.cmake', 'build')
    self.run('cd build && cmake %s %s ../conan-problem' % (cmake.command_line, args))
    self.run('cd build && cmake --build . --target install %s' % cmake.build_config)

  def package_info(self):
    self.cpp_info.libs = ['conan-problem-project']
