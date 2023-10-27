# Scene
This node determines an overall orientation of the scene and can be used to customize the rendering for a specific rendering window. A common use-case in planetariums, for example, is to account for a tilt in the display system by providing an `orientation` with the same pitch as the planetarium surface. This makes it possible to reuse the same application between the planetarium dome and fixed setups without the need for special care.

- `offset` **[object]** _optional_

  A linear offset of the scene center. Must define three float attributes `x`, `y`, and `z`. The default values are `x=0`, `y=0`, `z=0`, which means that no offset is applied to the center of the scene.

- `orientation` **[object]** _optional_

  Describes a fixed orientation for the virtual image plane as Euler angles. The object must contain all of the following attributes:

  - `pitch`: negative numbers tilt the camera downwards; positive numbers tilt upwards. The allowed range is `[-90, 90]`.
  - `yaw`: negative numbers pan the camera to the left; positive numbers pan to the right. The allowed range is `[-360, 360]`.
  - `roll`: negative numbers rotate the camera to the left; positive numbers to the right. The allowed range is `[-180, 180]`.

- `scale` **[float]** _optional_

  A scaling factor for the entire scene. The default value is `1.0`.
