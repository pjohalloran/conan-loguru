from conans import ConanFile, CMake
   
class LoguruConan(ConanFile):
   name = "loguru"
   version = "0.1"
   license="MIT"
   settings = "os", "compiler", "build_type", "arch"
   url = "https://github.com/pjohalloran/conan-loguru"

   def source(self):
       self.run("https://github.com/emilk/loguru")

   def build(self):
       #cmake = CMake(self.settings)
       #self.run('cd hello && cmake . %s' % cmake.command_line)
       #self.run("cd hello && cmake --build . %s" % cmake.build_config)

   def package(self):
       self.copy("loguru.hpp", dst="include", src="loguru")
       #self.copy("*.lib", dst="lib", src="hello/lib")
       #self.copy("*.a", dst="lib", src="hello/lib")

   def package_info(self):
self.cpp_info.libs = ["loguru"]