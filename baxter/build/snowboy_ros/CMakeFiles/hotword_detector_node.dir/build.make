# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.5

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/rob/baxter/src/snowboy_ros

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/rob/baxter/build/snowboy_ros

# Include any dependencies generated for this target.
include CMakeFiles/hotword_detector_node.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/hotword_detector_node.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/hotword_detector_node.dir/flags.make

CMakeFiles/hotword_detector_node.dir/src/hotword_detector_node.cpp.o: CMakeFiles/hotword_detector_node.dir/flags.make
CMakeFiles/hotword_detector_node.dir/src/hotword_detector_node.cpp.o: /home/rob/baxter/src/snowboy_ros/src/hotword_detector_node.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/rob/baxter/build/snowboy_ros/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/hotword_detector_node.dir/src/hotword_detector_node.cpp.o"
	/usr/bin/c++   $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/hotword_detector_node.dir/src/hotword_detector_node.cpp.o -c /home/rob/baxter/src/snowboy_ros/src/hotword_detector_node.cpp

CMakeFiles/hotword_detector_node.dir/src/hotword_detector_node.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/hotword_detector_node.dir/src/hotword_detector_node.cpp.i"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/rob/baxter/src/snowboy_ros/src/hotword_detector_node.cpp > CMakeFiles/hotword_detector_node.dir/src/hotword_detector_node.cpp.i

CMakeFiles/hotword_detector_node.dir/src/hotword_detector_node.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/hotword_detector_node.dir/src/hotword_detector_node.cpp.s"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/rob/baxter/src/snowboy_ros/src/hotword_detector_node.cpp -o CMakeFiles/hotword_detector_node.dir/src/hotword_detector_node.cpp.s

CMakeFiles/hotword_detector_node.dir/src/hotword_detector_node.cpp.o.requires:

.PHONY : CMakeFiles/hotword_detector_node.dir/src/hotword_detector_node.cpp.o.requires

CMakeFiles/hotword_detector_node.dir/src/hotword_detector_node.cpp.o.provides: CMakeFiles/hotword_detector_node.dir/src/hotword_detector_node.cpp.o.requires
	$(MAKE) -f CMakeFiles/hotword_detector_node.dir/build.make CMakeFiles/hotword_detector_node.dir/src/hotword_detector_node.cpp.o.provides.build
.PHONY : CMakeFiles/hotword_detector_node.dir/src/hotword_detector_node.cpp.o.provides

CMakeFiles/hotword_detector_node.dir/src/hotword_detector_node.cpp.o.provides.build: CMakeFiles/hotword_detector_node.dir/src/hotword_detector_node.cpp.o


# Object files for target hotword_detector_node
hotword_detector_node_OBJECTS = \
"CMakeFiles/hotword_detector_node.dir/src/hotword_detector_node.cpp.o"

# External object files for target hotword_detector_node
hotword_detector_node_EXTERNAL_OBJECTS =

/home/rob/baxter/devel/.private/snowboy_ros/lib/snowboy_ros/hotword_detector_node: CMakeFiles/hotword_detector_node.dir/src/hotword_detector_node.cpp.o
/home/rob/baxter/devel/.private/snowboy_ros/lib/snowboy_ros/hotword_detector_node: CMakeFiles/hotword_detector_node.dir/build.make
/home/rob/baxter/devel/.private/snowboy_ros/lib/snowboy_ros/hotword_detector_node: /home/rob/baxter/devel/.private/snowboy_ros/lib/libhotword_detector.so
/home/rob/baxter/devel/.private/snowboy_ros/lib/snowboy_ros/hotword_detector_node: /opt/ros/kinetic/lib/libroscpp.so
/home/rob/baxter/devel/.private/snowboy_ros/lib/snowboy_ros/hotword_detector_node: /usr/lib/x86_64-linux-gnu/libboost_filesystem.so
/home/rob/baxter/devel/.private/snowboy_ros/lib/snowboy_ros/hotword_detector_node: /usr/lib/x86_64-linux-gnu/libboost_signals.so
/home/rob/baxter/devel/.private/snowboy_ros/lib/snowboy_ros/hotword_detector_node: /opt/ros/kinetic/lib/librosconsole.so
/home/rob/baxter/devel/.private/snowboy_ros/lib/snowboy_ros/hotword_detector_node: /opt/ros/kinetic/lib/librosconsole_log4cxx.so
/home/rob/baxter/devel/.private/snowboy_ros/lib/snowboy_ros/hotword_detector_node: /opt/ros/kinetic/lib/librosconsole_backend_interface.so
/home/rob/baxter/devel/.private/snowboy_ros/lib/snowboy_ros/hotword_detector_node: /usr/lib/x86_64-linux-gnu/liblog4cxx.so
/home/rob/baxter/devel/.private/snowboy_ros/lib/snowboy_ros/hotword_detector_node: /usr/lib/x86_64-linux-gnu/libboost_regex.so
/home/rob/baxter/devel/.private/snowboy_ros/lib/snowboy_ros/hotword_detector_node: /opt/ros/kinetic/lib/libxmlrpcpp.so
/home/rob/baxter/devel/.private/snowboy_ros/lib/snowboy_ros/hotword_detector_node: /opt/ros/kinetic/lib/libdynamic_reconfigure_config_init_mutex.so
/home/rob/baxter/devel/.private/snowboy_ros/lib/snowboy_ros/hotword_detector_node: /opt/ros/kinetic/lib/libroscpp_serialization.so
/home/rob/baxter/devel/.private/snowboy_ros/lib/snowboy_ros/hotword_detector_node: /opt/ros/kinetic/lib/librostime.so
/home/rob/baxter/devel/.private/snowboy_ros/lib/snowboy_ros/hotword_detector_node: /opt/ros/kinetic/lib/libcpp_common.so
/home/rob/baxter/devel/.private/snowboy_ros/lib/snowboy_ros/hotword_detector_node: /usr/lib/x86_64-linux-gnu/libboost_system.so
/home/rob/baxter/devel/.private/snowboy_ros/lib/snowboy_ros/hotword_detector_node: /usr/lib/x86_64-linux-gnu/libboost_thread.so
/home/rob/baxter/devel/.private/snowboy_ros/lib/snowboy_ros/hotword_detector_node: /usr/lib/x86_64-linux-gnu/libboost_chrono.so
/home/rob/baxter/devel/.private/snowboy_ros/lib/snowboy_ros/hotword_detector_node: /usr/lib/x86_64-linux-gnu/libboost_date_time.so
/home/rob/baxter/devel/.private/snowboy_ros/lib/snowboy_ros/hotword_detector_node: /usr/lib/x86_64-linux-gnu/libboost_atomic.so
/home/rob/baxter/devel/.private/snowboy_ros/lib/snowboy_ros/hotword_detector_node: /usr/lib/x86_64-linux-gnu/libpthread.so
/home/rob/baxter/devel/.private/snowboy_ros/lib/snowboy_ros/hotword_detector_node: /usr/lib/x86_64-linux-gnu/libconsole_bridge.so
/home/rob/baxter/devel/.private/snowboy_ros/lib/snowboy_ros/hotword_detector_node: /home/rob/baxter/src/snowboy_ros/3rdparty/snowboy/lib/ubuntu64/libsnowboy-detect.a
/home/rob/baxter/devel/.private/snowboy_ros/lib/snowboy_ros/hotword_detector_node: /opt/ros/kinetic/lib/libroscpp.so
/home/rob/baxter/devel/.private/snowboy_ros/lib/snowboy_ros/hotword_detector_node: /usr/lib/x86_64-linux-gnu/libboost_filesystem.so
/home/rob/baxter/devel/.private/snowboy_ros/lib/snowboy_ros/hotword_detector_node: /usr/lib/x86_64-linux-gnu/libboost_signals.so
/home/rob/baxter/devel/.private/snowboy_ros/lib/snowboy_ros/hotword_detector_node: /opt/ros/kinetic/lib/librosconsole.so
/home/rob/baxter/devel/.private/snowboy_ros/lib/snowboy_ros/hotword_detector_node: /opt/ros/kinetic/lib/librosconsole_log4cxx.so
/home/rob/baxter/devel/.private/snowboy_ros/lib/snowboy_ros/hotword_detector_node: /opt/ros/kinetic/lib/librosconsole_backend_interface.so
/home/rob/baxter/devel/.private/snowboy_ros/lib/snowboy_ros/hotword_detector_node: /usr/lib/x86_64-linux-gnu/liblog4cxx.so
/home/rob/baxter/devel/.private/snowboy_ros/lib/snowboy_ros/hotword_detector_node: /usr/lib/x86_64-linux-gnu/libboost_regex.so
/home/rob/baxter/devel/.private/snowboy_ros/lib/snowboy_ros/hotword_detector_node: /opt/ros/kinetic/lib/libxmlrpcpp.so
/home/rob/baxter/devel/.private/snowboy_ros/lib/snowboy_ros/hotword_detector_node: /opt/ros/kinetic/lib/libdynamic_reconfigure_config_init_mutex.so
/home/rob/baxter/devel/.private/snowboy_ros/lib/snowboy_ros/hotword_detector_node: /opt/ros/kinetic/lib/libroscpp_serialization.so
/home/rob/baxter/devel/.private/snowboy_ros/lib/snowboy_ros/hotword_detector_node: /opt/ros/kinetic/lib/librostime.so
/home/rob/baxter/devel/.private/snowboy_ros/lib/snowboy_ros/hotword_detector_node: /opt/ros/kinetic/lib/libcpp_common.so
/home/rob/baxter/devel/.private/snowboy_ros/lib/snowboy_ros/hotword_detector_node: /usr/lib/x86_64-linux-gnu/libboost_system.so
/home/rob/baxter/devel/.private/snowboy_ros/lib/snowboy_ros/hotword_detector_node: /usr/lib/x86_64-linux-gnu/libboost_thread.so
/home/rob/baxter/devel/.private/snowboy_ros/lib/snowboy_ros/hotword_detector_node: /usr/lib/x86_64-linux-gnu/libboost_chrono.so
/home/rob/baxter/devel/.private/snowboy_ros/lib/snowboy_ros/hotword_detector_node: /usr/lib/x86_64-linux-gnu/libboost_date_time.so
/home/rob/baxter/devel/.private/snowboy_ros/lib/snowboy_ros/hotword_detector_node: /usr/lib/x86_64-linux-gnu/libboost_atomic.so
/home/rob/baxter/devel/.private/snowboy_ros/lib/snowboy_ros/hotword_detector_node: /usr/lib/x86_64-linux-gnu/libpthread.so
/home/rob/baxter/devel/.private/snowboy_ros/lib/snowboy_ros/hotword_detector_node: /usr/lib/x86_64-linux-gnu/libconsole_bridge.so
/home/rob/baxter/devel/.private/snowboy_ros/lib/snowboy_ros/hotword_detector_node: /usr/lib/libblas.so
/home/rob/baxter/devel/.private/snowboy_ros/lib/snowboy_ros/hotword_detector_node: CMakeFiles/hotword_detector_node.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/rob/baxter/build/snowboy_ros/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable /home/rob/baxter/devel/.private/snowboy_ros/lib/snowboy_ros/hotword_detector_node"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/hotword_detector_node.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/hotword_detector_node.dir/build: /home/rob/baxter/devel/.private/snowboy_ros/lib/snowboy_ros/hotword_detector_node

.PHONY : CMakeFiles/hotword_detector_node.dir/build

CMakeFiles/hotword_detector_node.dir/requires: CMakeFiles/hotword_detector_node.dir/src/hotword_detector_node.cpp.o.requires

.PHONY : CMakeFiles/hotword_detector_node.dir/requires

CMakeFiles/hotword_detector_node.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/hotword_detector_node.dir/cmake_clean.cmake
.PHONY : CMakeFiles/hotword_detector_node.dir/clean

CMakeFiles/hotword_detector_node.dir/depend:
	cd /home/rob/baxter/build/snowboy_ros && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/rob/baxter/src/snowboy_ros /home/rob/baxter/src/snowboy_ros /home/rob/baxter/build/snowboy_ros /home/rob/baxter/build/snowboy_ros /home/rob/baxter/build/snowboy_ros/CMakeFiles/hotword_detector_node.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/hotword_detector_node.dir/depend

