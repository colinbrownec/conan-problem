from conans import ConanFile, CMake
import os

# This easily allows to copy the package in other user or channel
channel  = os.getenv('CONAN_CHANNEL',  'testing')
username = os.getenv('CONAN_USERNAME', 'colinbrownec')

class ConanProblemTestProject(ConanFile):
  settings = 'os', 'compiler', 'build_type', 'arch'
  generators = 'cmake'

  requires = ('ConanProblemProject/1.0@%s/%s' % (username, channel))

  def build(self):
    cmake = CMake(self.settings)
    self.run('cmake "%s" %s' % (self.conanfile_directory, cmake.command_line))
    self.run('cmake --build . %s' % cmake.build_config)

  def imports(self):
    if self.settings.os == 'Windows':
      self.copy(pattern='*.dll', dst='bin', src='bin')
      self.copy(pattern='*.lib', dst='lib', src='lib')
    else:
      self.copy(pattern='*.so', dst='bin', src='bin')
      self.copy(pattern='*.a', dst='lib', src='lib')

  def test(self):
    # equal to ./bin/greet, but portable win: .\bin\greet
    self.run(os.sep.join(['.', 'bin', 'conan-problem-test-project']))
