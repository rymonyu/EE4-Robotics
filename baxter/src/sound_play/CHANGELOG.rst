^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package sound_play
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

0.3.3 (2018-05-22)
------------------
* Fix gstreamer errors. Fixes `#108 <https://github.com/ros-drivers/audio_common/issues/108>`_
* Contributors: trainman419

0.3.2 (2018-05-02)
------------------
* [sound_play] add option to select audio device to play / record (`#87 <https://github.com/ros-drivers/audio_common/issues/87>`_)
  * [sound_play] add option to select audio device to play
  * [sound_play] reformat README to markdown; add usage to set device via rosparam
  * audio_capture: add option for selecting device to use
  * audio_play: add option to select device for playing audio
  * add device argument to launch files
  Conflicts:
  audio_capture/launch/capture.launch
  audio_capture/launch/capture_to_file.launch
  audio_capture/src/audio_capture.cpp
  audio_play/launch/play.launch
  sound_play/scripts/soundplay_node.py
* Merge pull request `#95 <https://github.com/ros-drivers/audio_common/issues/95>`_ from yujinrobot/volume_check
  [sound_play] volume check for cached sounds
* [sound_play] checks if sound's Gst instance's volume has changed and resets it
* Contributors: Austin, Naveed Usmani, Yuki Furuta

0.3.1 (2016-08-28)
------------------
* Update to new gstreamer rosdeps
* Update sound_play to gstreamer 1.0
* remove chance of uninitialised variable being called in a subscriber callback.
* Add changelogs
* Issue: The error checks for missing publisher/action client in sendMsg were inverted.
  The non-blocking brach tested the action client while the blocking branch
  tested the publisher.
  Fix: Inverted the blocking boolean for both branchs.
* sound_play: Fix build with -DCATKIN_ENABLE_TESTING=OFF.
  https://bugs.gentoo.org/show_bug.cgi?id=567466
* [soundplay_node] fix resources not being released on dict cleanup
  This was resulting in the number of sink inputs reaching the maximum threshold,
  (32 on ubuntu 14.04 with pulseaudio 4.0) after which no more sounds could be
  played by the node. It would only happen if the rate of sounds being played was
  slower than the dictionary cleanup.
* depend on actionlib.
* Introduce unit test to ensure soundclient is started correctly.
* Example of using the explicit blocking parameter to override the class setting.
* SoundClient can also explicitly specify whether or not to block while playing the sound.
  Each play/repeat/say/... method can take an option blocking=True|False argument (using **kwargs), which over-rides the class-wide setting.
* Merge pull request #62 from felixduvallet/set_queue_size
  Set queue_size in soundplay_node Publisher
* do both in same script.
* Added script showing the various blocking/non-blocking ways of using SoundClient.
* removed trailing whitespace only
* loginfo -> logdebug.
* Slightly more condensed version of thresholding.
* Enable blocking calls inside libsoundplay's SoundClient.
  This makes use of the actionlib interface provided by soundplay_node, by ensuring SoundClient receives a response before returning.
  Turn this on by: SoundClient(blocking=true).
* Use new-style python classes (inherits from object).
* removed trailing whitespace.
* Set the volume in each of the sound_play actionlib tests.
  This makes the script actually play the sounds it requests.
* Specify queue size explicitly.
  Removed warning message printed each time soundplay_node was started.
* remove trailing whitespace only.
* Change wiki urls
* Fix test target name collision. Fixes #49
* sound_play: cpp header conforms to the style guide
* sound_play: update scripts to allow volume to be set
* sound_play: updated tests to include volume changes
* sound_play: add ability to specify volume at which to play sounds
  Also changed error to warning as per todo
* sound_play: fix indentation and comment inconsistencies
* sound_play: remove some raw prints cluttering output
* sound_play: added queue_size to SoundClient init
  Should prevent warning being displayed whenever the client is created.
  Fixes issue #43
* add simple-actionlib functionality to sound_play
* sound_play: Added functions to play files relative to a package path
* Update maintainer email
* Contributors: Alexis Ballier, Austin, Daniel Stonier, David V. Lu, Felix Duvallet, Matthias Nieuwenhuisen, Michal Staniaszek, Neowizard, aginika, trainman419

0.2.11 (2016-02-16)
-------------------
* Add changelogs
* Fix bug in say.py. Fixes `#72 <https://github.com/ros-drivers/audio_common/issues/72>`_
* Contributors: trainman419

0.2.10 (2016-01-21)
-------------------
* Add changelogs
* Issue: The error checks for missing publisher/action client in sendMsg were inverted.
  The non-blocking brach tested the action client while the blocking branch
  tested the publisher.
  Fix: Inverted the blocking boolean for both branchs.
* sound_play: Fix build with -DCATKIN_ENABLE_TESTING=OFF.
  https://bugs.gentoo.org/show_bug.cgi?id=567466
* Contributors: Alexis Ballier, Neowizard, trainman419

0.2.9 (2015-12-02)
------------------
* Add changelogs
* [soundplay_node] fix resources not being released on dict cleanup
  This was resulting in the number of sink inputs reaching the maximum threshold,
  (32 on ubuntu 14.04 with pulseaudio 4.0) after which no more sounds could be
  played by the node. It would only happen if the rate of sounds being played was
  slower than the dictionary cleanup.
* depend on actionlib.
* Introduce unit test to ensure soundclient is started correctly.
* Example of using the explicit blocking parameter to override the class setting.
* SoundClient can also explicitly specify whether or not to block while playing the sound.
  Each play/repeat/say/... method can take an option blocking=True|False argument (using **kwargs), which over-rides the class-wide setting.
  Conflicts:
  sound_play/src/sound_play/libsoundplay.py
* do both in same script.
* Added script showing the various blocking/non-blocking ways of using SoundClient.
* removed trailing whitespace only
  Conflicts:
  sound_play/scripts/say.py
* loginfo -> logdebug.
* Enable blocking calls inside libsoundplay's SoundClient.
  This makes use of the actionlib interface provided by soundplay_node, by ensuring SoundClient receives a response before returning.
  Turn this on by: SoundClient(blocking=true).
  Conflicts:
  sound_play/src/sound_play/libsoundplay.py
* Use new-style python classes (inherits from object).
  Conflicts:
  sound_play/src/sound_play/libsoundplay.py
* removed trailing whitespace.
  Conflicts:
  sound_play/src/sound_play/libsoundplay.py
* Revert "Set the volume in each of the sound_play actionlib tests."
  This reverts commit 55ab08c882809fc6d21affb849a7dac9f1901867.
  Indigo-devel does not have the volume API
* Set the volume in each of the sound_play actionlib tests.
  This makes the script actually play the sounds it requests.
* Specify queue size explicitly.
  Removed warning message printed each time soundplay_node was started.
* remove trailing whitespace only.
* Fix wiki links
* Contributors: David V. Lu, Felix Duvallet, Michal Staniaszek, trainman419

0.2.8 (2015-10-02)
------------------
* Fix test target name collision. Fixes `#49 <https://github.com/ros-drivers/audio_common/issues/49>`_
* sound_play: remove some raw prints cluttering output
* sound_play: added queue_size to SoundClient init
  Should prevent warning being displayed whenever the client is created.
  Fixes issue `#43 <https://github.com/ros-drivers/audio_common/issues/43>`_
* add simple-actionlib functionality to sound_play
* sound_play: Added functions to play files relative to a package path
* Update maintainer email
* Contributors: Matthias Nieuwenhuisen, Michal Staniaszek, aginika, trainman419

0.2.7 (2014-07-25)
------------------

0.2.6 (2014-02-26)
------------------
* Fix path resolution in python soundplay lib.
* now importing roslib. closes `#33 <https://github.com/ros-drivers/audio_common/issues/33>`_
* Contributors: Piyush Khandelwal, trainman419

0.2.5 (2014-01-23)
------------------
* "0.2.5"
* Install sounds. Fixes `#29 <https://github.com/ros-drivers/audio_common/issues/29>`_.
* install sound_play.h and export include folder
* Contributors: ahendrix, trainman419, v4hn

0.2.4 (2013-09-10)
------------------
* Fix cmake ordering.
* Contributors: Austin Hendrix

0.2.3 (2013-07-15)
------------------
* Fix python.
* Contributors: Austin Hendrix

0.2.2 (2013-04-10)
------------------
* Actually add proper dependency on message generation.
* Reorder CMakeLists.txt.
* Contributors: Austin Hendrix

0.2.1 (2013-04-08 13:59)
------------------------

0.2.0 (2013-04-08 13:49)
------------------------
* Finish catkinizing audio_common.
* Start catkinizing sound_play.
* Fix typo in package.xml
* Versions and more URLs.
* Convert manifests to package.xml
* Ditch old makefiles.
* Use festival default voice from libsoundplay.
* Set myself as the maintainer.
* Fix filehandle leak and add debug statements.
* Updates manifest
* Updated manifests for rodep2
* Fixed sound_play
* Added test wave
* Cleaned up the test script
* Added default voice to say command
* Updated the gstreamer rosdeps
* Removed comment
* Added diagnostic_msgs to sound_play
* Added a rosdep.yaml file
* Added ability to use different festival voices
* Added exit(1) when import of pygame fails. This makes the error message easier to notice.
* Added Ubuntu platform tags to manifest
* Added a link to the troubleshooting wiki page in the diagnostic message as requested by `#4070 <https://github.com/ros-drivers/audio_common/issues/4070>`_.
* Took out the deprecated API.
* Sound play now publishes header timestamp in message. `#3822 <https://github.com/ros-drivers/audio_common/issues/3822>`_
* Cleaned up temp file generation when doing text to speach. Now uses the tempfile module.
* Adding missing export of headers for sound_play C++ API
* Changing node name for sound play diagnostics, `#3599 <https://github.com/ros-drivers/audio_common/issues/3599>`_
* Added test.launch to run sound server and a test client.
* Remove use of deprecated rosbuild macros
* Replaced review tag with standardized message
* Updated review status
* Added a launch file to start soundplay_node.py
* Made the sound_play client libraries be more explicit about what to do when the node is not running.
* Updated manifest description
* Updated copyright year
* fixed XML typo
* updated package description
* Added a copyright message.
* Removed debugging message from sound_play node.
* Added tests for new sound_play python API and fixed a few bugs.
* Fixed missing self arguments in sound_play libsoundplay.py
* Upgraded the python sound_play API
* Converted non-camelCase methods to camelCase in sound_play C++ API
* Changed Lock to RLock to fix `#2801 <https://github.com/ros-drivers/audio_common/issues/2801>`_
* Made the deprecation of SoundHandle into a warning.
* Added debug messages
* Updated soundplay_node to publish diagnostics and increased the number of active channels.
* Added diagnostic_msgs dependency to sound_play
* sound_play: Renamed SoundHandle to SoundClient. Added Sound-centric C++ API. Changed byte to int8 in msg file. Updated documentation.
* migration part 1
* Contributors: Austin Hendrix, Nate Koenig, blaise, blaisegassend, eitan, gerkey, kwc, nkoenig, watts, wheeler
