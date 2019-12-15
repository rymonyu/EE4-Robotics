# CMake generated Testfile for 
# Source directory: /home/rob/baxter/src/sound_play
# Build directory: /home/rob/baxter/build/sound_play
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(_ctest_sound_play_nosetests_scripts.test "/home/rob/baxter/build/sound_play/catkin_generated/env_cached.sh" "/usr/bin/python" "/opt/ros/kinetic/share/catkin/cmake/test/run_tests.py" "/home/rob/baxter/build/sound_play/test_results/sound_play/nosetests-scripts.test.xml" "--return-code" "\"/usr/bin/cmake\" -E make_directory /home/rob/baxter/build/sound_play/test_results/sound_play" "/usr/bin/nosetests-2.7 -P --process-timeout=60 --where=/home/rob/baxter/src/sound_play/scripts/test --with-xunit --xunit-file=/home/rob/baxter/build/sound_play/test_results/sound_play/nosetests-scripts.test.xml")
subdirs(gtest)
subdirs(test)
