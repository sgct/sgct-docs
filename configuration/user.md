# User
This node specifies a user position and parameters. In most cases, only a single unnamed user is necessary. However, in more general cases, it is possible to assign `User`s to specific [Viewports](viewport) to provide a more fine-grained control over the rendering that occurs in that viewport.

- `name` **[string]** _special_

  Specifies the name of this user. Each user needs to have a unique name, but there also *has* to be exactly one user present that has an empty name (or without a `name` attribute) which is used as the default user.

- `eyeseparation` **[float >= 0]** _optional_

  Determines the eye separation used for stereoscopic viewports. If no viewports in the configuration are using stereo, this setting is ignored.

- `pos` **[object]** _optional_

  A linear offset of the user position. Must define three float attributes `x`, `y`, and `z`. The default values are `x=0`, `y=0`, `z=0`, meaning that no linear offset is applied to the user's position.

- `orientation` **[object]** _optional_

  Describes a fixed orientation for the virtual image plane as Euler angles. The object must contain all of the following attributes:

  - `pitch`: negative numbers tilt the camera downwards; positive numbers tilt upwards. The allowed range is `[-90, 90]`.
  - `yaw`: negative numbers pan the camera to the left; positive numbers pan to the right. The allowed range is `[-360, 360]`.
  - `roll`: negative numbers rotate the camera to the left; positive numbers to the right. The allowed range is `[-180, 180]`.

- `matrix` **[object]** _optional_

  A generic transformation matrix that is applied to the orientation of this user. This value will overwrite the value specified in `Orientation`. The attributes used for the matrix are named `x0`, `y0`, `z0`, `w0`, `x1`, `y1`, `z1`, `w2`, `x2`, `y2`, `z2`, `w2`, `x3`, `y3`, `z3`, `w3` and are used in this order to initialize the matrix in a column-major order. All 16 of these values have to be present in this attribute and have to be floating point values.

  - `transpose` **[boolean]** _optional_

    If this value is present and `true` the values provided are interpreted as being in row-major order, rather than column-major order. The default is `false`, making the matrix column-major.

- `tracking` **[object]** _optional_

  Provides information about whether this user should be tracked using a VRPN-based tracker. This child node contains two attributes with information about the tracker that this user should be associated with.

  - `tracker` **[object]** _optional_

    The name of the tracker group that this user should be linked with. This name must be a name of a [Tracker](tracker) that is specified in this configuration.

  - `device` **[object]** _optional_

    The name of the device in the tracker group that should be used to control the tracking for this user. The specified device has to be a [Device](device) that was specified in the [Tracker](tracker) `tracker`.
