# Base Types
This is a list of commonly used fundamental types found in configuration files.


## ivec2
A vector containing of 2 values that are both whole integer numbers.

  - `x` **integer**
  - `y` **integer**


## ivec3
A vector containing of 3 values that are all whole integer numbers.

  - `x` **integer**
  - `y` **integer**
  - `z` **integer**


## ivec4
A vector containing of 4 values that are all whole integer numbers.

  - `x` **integer**
  - `y` **integer**
  - `z` **integer**
  - `w` **integer**


## vec2
A vector containing of 2 values that can both be fractional numbers.

  - `x` **number**
  - `y` **number**


## vec3
A vector containing of 3 values that can all be fractional numbers.

  - `x` **number**
  - `y` **number**
  - `z` **number**


## vec4
A vector containing of 4 values that can all be fractional numbers.

  - `x` **number**
  - `y` **number**
  - `z` **number**
  - `w` **number**


## color
A vector containing of 4 values that can all be fractional numbers. Each number must be between 0 and 1.

  - `x` **number between 0 and 1**
  - `y` **number between 0 and 1**
  - `z` **number between 0 and 1**
  - `w` **number between 0 and 1**


## orientation
Defines an orientation of some sorts. There are two ways of specifying the orientation. The first option is by providing yaw, pitch, and roll and the second is to provide a [Quaternion](https://en.wikipedia.org/wiki/Quaternion) directly.

### Yaw/Pitch/Roll

  - `yaw` **number**

    The yaw of the orientation in a clockwise positive direction as viewed from the upper pole. This value is provided in degrees.

  - `pitch` **number**

    The pitch of the orientation, which is measured from the equator with positive values towards the upper pole. This value is provided in degrees.

  - `roll` **number**

    The roll of the orientation in a clockwise positive direction viewing straight ahead. This value is provided in degrees.

### Quaternion

  - `x` **number**
  - `y` **number**
  - `z` **number**
  - `w` **number**


## mat4
This type is a 4x4 matrix that is used as a homogeneous transformation matrix. This type is an array that consists of extact 16 **number**s.

