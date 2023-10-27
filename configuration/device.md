# Device
This node specifies a single tracking device that belongs to a specific tracker group.

- `name` **[string]**

  Specifies the name of the device so that it can be referenced by a [User](user) or can be accessed programmatically by the application.

- `sensors` **[array]**

  This node represents a tracked sensor that provides orientation and position information to the application. The sensors can be accessed through the `TrackingManager` class and its related classes. Each item in the array must be an **[object]** that has the following values:
  - `vrpnaddress` **[string]**

    The VRPN address of this sensor.

  - `id` **[integer]**

    The sensor id for this device. This information is not used by SGCT directly but can be used by the application to distinguish different sensors if multiple sensors are specified in the configuration file.

- `buttons` **[array]**

  This node represents a group of toggle buttons that can be triggered through VRPN. The buttons can be accessed through the `TrackingManager` class and its related classes. Each item in the array must be an **[object]** that has the following values:

  - `vrpnaddress` **[string]**

    The VRPN address of this button group.

  - `count` **[integer]**

    The number of buttons that are advertised and received through the Device.

- `axes` **[array]**

  This node represents a number of independent 1D axes that are updated through VRPN. The axes can be accessed through the `TrackingManager` class and its related classes. Each item in the array must be an **[object]** that has the following values:

  - `vrpnaddress` **[string]**

    The VRPN address of this group of axes.

  - `count` **[integer]**

    The number of axes that are advertised by this VRPN device.

- `offset` **[object]** _optional_

  A linear offset that is added to the entire device. Must define three float attributes `x`, `y`, and `z`. The default values are `x=0`, `y=0`, `z=0`, leading to no offset being applied.

- `orientation` **[object]** _optional_

  Describes a fixed orientation for the virtual image plane as Euler angles. The object must contain all of the following attributes:

  - `pitch`: negative numbers tilt the camera downwards; positive numbers tilt upwards. The allowed range is `[-90, 90]`.
  - `yaw`: negative numbers pan the camera to the left; positive numbers pan to the right. The allowed range is `[-360, 360]`.
  - `roll`: negative numbers rotate the camera to the left; positive numbers to the right. The allowed range is `[-180, 180]`.

- `matrix` **[object]** _optional_

  A generic transformation matrix that is applied to this device. This value will overwrite the value specified in `Orientation`. The attributes used for the matrix are named `x0`, `y0`, `z0`, `w0`, `x1`, `y1`, `z1`, `w2`, `x2`, `y2`, `z2`, `w2`, `x3`, `y3`, `z3`, `w3` and are used in this order to initialize the matrix in a column-major order. All 16 of these values have to be present in this attribute and have to be floating point values.

  - `transpose` **[boolean]** _optional_

    If this value is present and `true` the values provided are interpreted as being in row-major order, rather than column-major order. The default is `false`, making the matrix column-major.
