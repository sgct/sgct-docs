# Planar Projection
This projection node describes a projection for the [Viewport](../viewport) that is a flat projection described by simple frustum, which may be asymmetric. If you are building a new configuration file and do not know which projection type you should use, this type is probably the right one.

- `type` **[string = "PlanarProjection"]**

  Defines the type of this projection. The value must be "PlanarProjection"

- `fov` **[object]**

  This object describes the field of view used the camera in this planar projection. The angles for the field of view can be provided in two ways. Either by providing the `up`, `down`, `left`, and `right` angles, which enables asymmetric frustums, or alternatively providing horizontal (`hfov`) and vertical (`vfov`) angles for symmetric frustums.

  Option 1:
  - `down` **[float]**

    The angle (in degrees) that is covered by the camera between the central point and the bottom border of the of the viewport. The `down` and `up` angles added together are the vertical field of view of the viewport.

  - `up` **[float]**

    The angle (in degrees) that is covered by the camera between the central point and the top border of the of the viewport. The `down` and `up` angles added together are the vertical field of view of the viewport.

  - `left` **[float]**

    The angle (in degrees) that is covered by the camera between the central point and the left border of the of the viewport. The `left` and `right` angles added together are the vertical field of view of the viewport.

  - `right` **[float]**

    The angle (in degrees) that is covered by the camera between the central point and the right border of the of the viewport. The `left` and `right` angles added together are the vertical field of view of the viewport.

  Option 2:
  - `hfov` **[float]**

    The angle (in degrees) covered by the camera in the horizontal direction. This is a symmetric frustum around the center and provides the same result as providing the `left` and `right` values with the half-angle.

  - `vfov` **[float]**

    The angle (in degrees) covered by the camera in the vertical direction. This is a symmetric frustum around the center and provides the same result as providing the `up` and `down` values with the half-angle.

- `orientation` **[object]** _optional_

  Describes a fixed orientation for the virtual image plane as Euler angles. The object must contain all of the following attributes:

  - `pitch`: negative numbers tilt the camera downwards; positive numbers tilt upwards. The allowed range is `[-90, 90]`.
  - `yaw`: negative numbers pan the camera to the left; positive numbers pan to the right. The allowed range is `[-360, 360]`.
  - `roll`: negative numbers rotate the camera to the left; positive numbers to the right. The allowed range is `[-180, 180]`.

- `distance` **[float]** _optional_

  The distance (in meters) at which the virtual render plane is placed. This value is only important when rendering this viewport using stereocopy as the `distance` and the [User](../user)'s `eyeseparation` are used to compute the change in frustum between the left and the right eyes.

- `offset` **[object]** _optional_

  A linear offset in meters that is added to the virtual image plane. The object must contain three float attributes `x`, `y`, and `z`. The default values are `x=0`, `y=0`, `z=0`, meaning that no individual offset is applied to the image plane.

## Example
```{literalinclude} /assets/configs/projections/planar-symmetric.json
:language: json
:caption: Example file for a symmetric frustum ([download](/assets/configs/projections/planar-symmetric.json))
```

```{literalinclude} /assets/configs/projections/planar-asymmetric.json
:language: json
:caption: Example file for an asymmetric frustum ([download](/assets/configs/projections/planar-asymmetric.json))
```

```{literalinclude} /assets/configs/projections/planar-orientation.json
:language: json
:caption: Example file with an off-center and angled frustum ([download](/assets/configs/projections/planar-orientation.json))
```
