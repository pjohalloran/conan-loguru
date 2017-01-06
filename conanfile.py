from conans import ConanFile, CMake
   
class LoguruConan(ConanFile):
  name = "loguru"
  version = "1.0"
  description = "A lightweight C++ logging library"
  license="MIT"
  settings = "os", "compiler", "build_type", "arch"
  url = "https://github.com/pjohalloran/conan-loguru"
  options = {"compiler_version": ["11", "14"]}
  default_options = "compiler_version=14",

  def source(self):
    self.run("git clone https://github.com/emilk/loguru")

  def package(self):
    self.copy("loguru.hpp", dst="include", src="loguru")

  def package_info(self):
    self.cpp_info.sharedlinkflags = ["-std=c++%s" % self.options.compiler_version]
    self.cpp_info.exelinkflags = ["-std=c++%s" % self.options.compiler_version]
    self.cpp_info.libs = ["stdc++", "pthread", "dl"]
    self.cpp_info.cppflags = ["-std=c++%s" % self.options.compiler_version, "-stdlib=libc++"]