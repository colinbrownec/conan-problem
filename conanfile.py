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
  exports = "src/*", "CMakeLists.txt"

  def build(self):
    cmake = CMake(self.settings)
    # Small workaround, will fix it in conan 0.12
    destination = self.package_folder if hasattr(self, "package_folder") else "."
    args = ' '.join([
      '-DCMAKE_INSTALL_PREFIX=%s' % destination,
      '-DBUILD_SHARED_LIBS=%s' % ('ON' if self.options.shared else 'OFF')
    ])

    self.run('cmake %s %s %s ' % (self.conanfile_directory, cmake.command_line, args))
    self.run('cmake --build . --target install %s' % cmake.build_config)

  def package_info(self):
    self.cpp_info.libs = ['conan-problem-project']
