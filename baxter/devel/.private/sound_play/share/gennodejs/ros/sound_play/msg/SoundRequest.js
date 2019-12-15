// Auto-generated. Do not edit!

// (in-package sound_play.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class SoundRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.sound = null;
      this.command = null;
      this.volume = null;
      this.arg = null;
      this.arg2 = null;
    }
    else {
      if (initObj.hasOwnProperty('sound')) {
        this.sound = initObj.sound
      }
      else {
        this.sound = 0;
      }
      if (initObj.hasOwnProperty('command')) {
        this.command = initObj.command
      }
      else {
        this.command = 0;
      }
      if (initObj.hasOwnProperty('volume')) {
        this.volume = initObj.volume
      }
      else {
        this.volume = 0.0;
      }
      if (initObj.hasOwnProperty('arg')) {
        this.arg = initObj.arg
      }
      else {
        this.arg = '';
      }
      if (initObj.hasOwnProperty('arg2')) {
        this.arg2 = initObj.arg2
      }
      else {
        this.arg2 = '';
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type SoundRequest
    // Serialize message field [sound]
    bufferOffset = _serializer.int8(obj.sound, buffer, bufferOffset);
    // Serialize message field [command]
    bufferOffset = _serializer.int8(obj.command, buffer, bufferOffset);
    // Serialize message field [volume]
    bufferOffset = _serializer.float32(obj.volume, buffer, bufferOffset);
    // Serialize message field [arg]
    bufferOffset = _serializer.string(obj.arg, buffer, bufferOffset);
    // Serialize message field [arg2]
    bufferOffset = _serializer.string(obj.arg2, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type SoundRequest
    let len;
    let data = new SoundRequest(null);
    // Deserialize message field [sound]
    data.sound = _deserializer.int8(buffer, bufferOffset);
    // Deserialize message field [command]
    data.command = _deserializer.int8(buffer, bufferOffset);
    // Deserialize message field [volume]
    data.volume = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [arg]
    data.arg = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [arg2]
    data.arg2 = _deserializer.string(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += object.arg.length;
    length += object.arg2.length;
    return length + 14;
  }

  static datatype() {
    // Returns string type for a message object
    return 'sound_play/SoundRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'd098ce4a040686259137ece23a625167';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    # IMPORTANT: You should never have to generate this message yourself.
    # Use the sound_play::SoundClient C++ helper or the
    # sound_play.libsoundplay.SoundClient Python helper.
    
    # Sounds
    int8 BACKINGUP = 1
    int8 NEEDS_UNPLUGGING = 2
    int8 NEEDS_PLUGGING = 3
    int8 NEEDS_UNPLUGGING_BADLY = 4
    int8 NEEDS_PLUGGING_BADLY = 5
    
    # Sound identifiers that have special meaning
    int8 ALL = -1 # Only legal with PLAY_STOP
    int8 PLAY_FILE = -2
    int8 SAY = -3
    
    int8 sound # Selects which sound to play (see above)
    
    # Commands
    int8 PLAY_STOP = 0 # Stop this sound from playing
    int8 PLAY_ONCE = 1 # Play the sound once
    int8 PLAY_START = 2 # Play the sound in a loop until a stop request occurs
    
    int8 command # Indicates what to do with the sound
    
    # Volume at which to play the sound, with 0 as mute and 1.0 as 100%.
    float32 volume
    
    string arg # file name or text to say
    string arg2 # other arguments
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new SoundRequest(null);
    if (msg.sound !== undefined) {
      resolved.sound = msg.sound;
    }
    else {
      resolved.sound = 0
    }

    if (msg.command !== undefined) {
      resolved.command = msg.command;
    }
    else {
      resolved.command = 0
    }

    if (msg.volume !== undefined) {
      resolved.volume = msg.volume;
    }
    else {
      resolved.volume = 0.0
    }

    if (msg.arg !== undefined) {
      resolved.arg = msg.arg;
    }
    else {
      resolved.arg = ''
    }

    if (msg.arg2 !== undefined) {
      resolved.arg2 = msg.arg2;
    }
    else {
      resolved.arg2 = ''
    }

    return resolved;
    }
};

// Constants for message
SoundRequest.Constants = {
  BACKINGUP: 1,
  NEEDS_UNPLUGGING: 2,
  NEEDS_PLUGGING: 3,
  NEEDS_UNPLUGGING_BADLY: 4,
  NEEDS_PLUGGING_BADLY: 5,
  ALL: -1,
  PLAY_FILE: -2,
  SAY: -3,
  PLAY_STOP: 0,
  PLAY_ONCE: 1,
  PLAY_START: 2,
}

module.exports = SoundRequest;
