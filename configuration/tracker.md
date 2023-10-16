# Tracker
This node defines a group of tracking devices or sensors as they are advertised by the VRPN standard.  See its documentation for more information on this.

- `name` **[string]**

  The name of the tracker group.

- `devices` **[array]**

  {math}`0-\infty` [Device](device) objects

- `offset` **[object]** _optional_

  A linear offset of the class of trackers.  Must define three float attributes `x`, `y`, and `z`.  The default values are `x=0`, `y=0`, `z=0`, which means that no linear offset is applied to the tracker.

- `orientation` **[object]** _optional_

  Describes a fixed orientation of this class of trackers.  This can be provided either as Euler angles or as a quaternion.  The two modes *cannot* be mixed.  The following descibes the different attributes that can be used for the orientation.  Please note that *all* attributes for the chosen method have to be specified.  If the `matrix` attribute is also specified, it will overwrite the value specified here.

  Euler angles:
  - `pitch`: negative numbers tilt the camera downwards;  positive numbers tilt upwards.  The allowed range is `[-90, 90]`.
  - `yaw`: negative numbers pan the camera to the left;  positive numbers pan to the right.  The allowed range is `[-360, 360]`.
  - `roll`: negative numbers rotate the camera to the left;  positive numbers to the right.  The allowed range is `[-180, 180]`.

  Quaternion:
  - `x`
  - `y`
  - `z`
  - `w`

- `scale` **[float]** _optional_

  A scaling factor for this class of trackers.  The default value is `1.0`.

- `matrix` **[object]** _optional_

  A generic transformation matrix that is applied to all trackers in this group.  This value will overwrite the value specified in `orientation`.  The attributes used for the matrix are named `x0`, `y0`, `z0`, `w0`, `x1`, `y1`, `z1`, `w2`, `x2`, `y2`, `z2`, `w2`, `x3`, `y3`, `z3`, `w3` and are used in this order to initialize the matrix in a column-major order.  All 16 of these values have to be present in this attribute and have to be floating point values.

  - `transpose` **[boolean]** _optional_

    If this value is present and `true` the values provided are interpreted as being in row-major order, rather than column-major order.  The default is `false`, making the matrix column-major.
