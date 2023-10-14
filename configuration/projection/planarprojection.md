# Planar Projection

This projection node describes a projection for the [Viewport](../viewport) that is a flat projection described by simple frustum, which may be asymmetric.

## Children
`FOV` \[ 1 \]
> This element describes the field of view used the camera in this planar projection.
>
> `down` \[ float \]
> > The angle (in degrees) that is covered by the camera between the central point and the bottom border of the of the viewport.  The `down` and `up` angles added together are the vertical field of view of the viewport.
>
> `up` \[ float \]
> > The angle (in degrees) that is covered by the camera between the central point and the top border of the of the viewport.  The `down` and `up` angles added together are the vertical field of view of the viewport.
>
> `left` \[ float \]
> > The angle (in degrees) that is covered by the camera between the central point and the left border of the of the viewport.  The `left` and `right` angles added together are the vertical field of view of the viewport.
>
> `right` \[ float \]
> > The angle (in degrees) that is covered by the camera between the central point and the right border of the of the viewport.  The `left` and `right` angles added together are the vertical field of view of the viewport.
>
> `distance` *optional* \[ float \]
> > The distance (in meters) at which the virtual render plane is placed.  This value is only important when rendering this viewport using stereocopy as the `distance` and the [User](../user)s `eyeSeparation` are used to compute the change in frustum between the left and the right eyes.

`Offset` \[ 0 - 1 \]
 > A linear offset in meters that is added to the virtual image plane.  Must define three float attributes `x`, `y`, and `z`.  The default values are `x=0`, `y=0`, `z=0`, meaning that no offset is applied to the image plane.

`Orientation` \[ 0 - 1 \]
 > Describes a fixed orientation for the virtual image plane.  This can be provided either as Euler angles or as a quaternion.  The two modes *cannot* be mixed.  The following descibes the different attributes that can be used for the orientation.  Please note that *all* attributes for the chosen method have to be specified.  If the `Matrix` attribute is also specified, it will overwrite the value specified here.
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
