# Device
This node specifies a single tracking device that belongs to a specific tracker group.

## Attributes
`name` \[ string \]
> Specifies the name of the device so that it can be referenced by a [User](user) or can be accessed programmatically by the application.

## Children
`Sensor` \[ 0 - inf \]
 > This node represents a tracked sensor that provides orientation and position information to the application.  The sensors can be accessed through the `TrackingManager` class and its related classes.
 >
 > `vrpnAddress` \[ string \]
 >  > The VRPN address of this sensor.
 >
 > `id` \[ integer \]
 >  > The sensor id for this device.  This information is not used by SGCT directly but can be used by the application to distinguish different sensors if multiple sensors are specified in the configuration file.

`Buttons` \[ 0 - inf \]
> This node represents a group of toggle buttons that can be triggered through VRPN.  The buttons can be accessed through the `TrackingManager` class and its related classes.
>
> `vrpnAddress` \[ string \]
> > The VRPN address of this button group.
>
> `count` \[ integer \]
> > The number of buttons that are advertised and received through the Device.

`Axes` \[ 0 - inf \]
> This node represents a number of independent 1D axes that are updated through VRPN.  The axes can be accessed through the `TrackingManager` class and its related classes.
>
> `vrpnAddress` \[ string \]
> > The VRPN address of this group of axes.
>
> `count` \[ integer \]
> > The number of axes that are advertised by this VRPN device.

`Offset` \[ 0 - 1 \]
 > A linear offset that is added to the entire device.  Must define three float attributes `x`, `y`, and `z`.  The default values are `x=0`, `y=0`, `z=0`, leading to no offset being applied.

`Orientation` \[ 0 - 1 \]
 > Describes a fixed orientation for the device.  This can be provided either as Euler angles or as a quaternion.  The two modes *cannot* be mixed.  The following descibes the different attributes that can be used for the orientation.  Please note that *all* attributes for the chosen method have to be specified.  If the `Matrix` attribute is also specified, it will overwrite the value specified here.
 >
 > Euler angles:
 >  - `pitch` or `elevation`: negative numbers tilt the camera downwards;  positive numbers tilt upwards.  The allowed range is \[-90, 90\].
 >  - `yaw`, `heading`, or `azimuth`: negative numbers pan the camera to the left;  positive numbers pan to the right.  The allowed range is \[-360, 360\].
 >  - `roll` or `bank`: negative numbers rotate the camera to the left;  positive numbers to the right.  The allowed range is \[-180, 180\].
 >
 > Quaternion:
 >  - `x`
 >  - `y`
 >  - `z`
 >  - `w`
 >
 >  Example:  `<Orientation pitch="20.0" elevation="-12.0" roll="0.0" />`

`Matrix` \[ 0 - 1 \]
> A generic transformation matrix that is applied to this device.  This value will overwrite the value specified in `Orientation`.  The attributes used for the matrix are named `x0`, `y0`, `z0`, `w0`, `x1`, `y1`, `z1`, `w2`, `x2`, `y2`, `z2`, `w2`, `x3`, `y3`, `z3`, `w3` and are used in this order to initialize the matrix in a column-major order.  All 16 of these values have to be present in this attribute and have to be floating point values.
>
> `transpose` *optional* \[ boolean \]
>  > If this value is present and `true` the values provided are interpreted as being in row-major order, rather than column-major order.  The default is `false`, making the matrix column-major.
