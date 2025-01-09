# Configuration files
The format for the SGCT configuration files is JSON that defines the entire [Cluster](cluster) containing 1 or more [Node](node) fields, a [User](user) field, an optional [Settings](settings) field, an optional [Capture](capture) field, and an optional [Tracker](tracker) field. Each of the fields is described on this page further below.

Each configuration file has to fulfill the JSON schema which can be found in the [SGCT repository](https://raw.githubusercontent.com/sgct/sgct/master/sgct.schema.json).


## Examples
This section contains two almost minimal examples showing on a small variety of configuration options. Check the `config` folder in SGCT for more examples.

Here is a minimal example of a single node, single window configuration. This file creates a single node on `localhost` with a single window that has a size of 1280 by 720 pixels with a camera of 80 degrees horizontal field-of-view and approximately 50.5 degrees vertical field of view.

```{literalinclude} /assets/configs/examples/single.json
:language: json
:caption: A single node configuration file ([download](/assets/configs/example/single.json))
```

The following example is a configuration that creates two nodes, both running on the local machine, the difference being that their field-of-views are rotated by 40 degrees off the center.

```{literalinclude} /assets/configs/examples/two-nodes.json
:language: json
:caption: A configuration file containing two local nodes ([download](/assets/configs/example/two-nodes.json))
```

The final example is a fisheye rendering which demonstrates a more sophisticated rendering setup, which internally consists of many projections that are automatically assembled by SGCT into a single circular fisheye output.

```{literalinclude} /assets/configs/examples/fisheye.json
:language: json
:caption: A configuration file for a single fisheye projection ([download](/assets/configs/example/fisheye.json))
```

## Base Types
This is a list of commonly used fundamental types in configuration files.

### ivec2
A vector containing of 2 values that are both whole integer numbers.

  - `x` **integer**
  - `y` **integer**

### ivec3
A vector containing of 3 values that are all whole integer numbers.

  - `x` **integer**
  - `y` **integer**
  - `z` **integer**

### ivec4
A vector containing of 4 values that are all whole integer numbers.

  - `x` **integer**
  - `y` **integer**
  - `z` **integer**
  - `w` **integer**

### vec2
A vector containing of 2 values that can both be fractional numbers.

  - `x` **number**
  - `y` **number**

### vec3
A vector containing of 3 values that can all be fractional numbers.

  - `x` **number**
  - `y` **number**
  - `z` **number**

### vec4
A vector containing of 4 values that can all be fractional numbers.

  - `x` **number**
  - `y` **number**
  - `z` **number**
  - `w` **number**

### color
A vector containing of 4 values that can all be fractional numbers. Each number must be between 0 and 1.

  - `x` **number between 0 and 1**
  - `y` **number between 0 and 1**
  - `z` **number between 0 and 1**
  - `w` **number between 0 and 1**

### orientation
Defines an orientation of some sorts. There are two ways of specifying the orientation. The first option is by providing yaw, pitch, and roll and the second is to provide a [Quaternion](https://en.wikipedia.org/wiki/Quaternion) directly.

#### Yaw/Pitch/Roll

  - `yaw` **number**

    The yaw of the orientation in a clockwise positive direction as viewed from the upper pole.

  - `pitch` **number**

    The pitch of the orientation, which is measured from the equator with positive values towards the upper pole.

  - `roll` **number**

    The roll of the orientation in a clockwise positive direction viewing straight ahead

#### Quaternion

  - `x` **number**
  - `y` **number**
  - `z` **number**
  - `w` **number**

### mat4
This type is a 4x4 matrix that is used as a homogeneous transformation matrix. This type is an array that consists of extact 16 **number**s.


:::{toctree}
:maxdepth: 2
:hidden:
:titlesonly:

cluster
node
window
viewport
projection/index
scene
user
settings
capture
device
tracker
:::
