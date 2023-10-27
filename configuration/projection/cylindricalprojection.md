# Cylindrical Projection
This projection method renders the scene into a view that can be mapped on the inside or outside of a cylinder. This projection method is support by some live media curation tools. The forward-facing direction will be at the left border of the image unless changed via the `rotation` option.

- `type` **[string = "CylindricalProjection"]**

  Defines the type of this projection. The value must be "CylindricalProjection"

- `quality` **[low, medium, high, 256, 512, 1k, 1024, 1.5k, 1536, 2k, 2048, 4k, 4096, 8k, 8192, 16k, 16384]** _optional_

  Determines the pixel resolution of the cube map faces that are individually rendered to create the cylindrical rendering. The higher resolution these cube map faces have, the better quality the resulting cylindrical rendering, but this comes at the expense of increased rendering times. The named values are corresponding:
  - `low`: 256
  - `medium`: 512
  - `high`: 1024
  - `1k`: 1024
  - `1.5k`: 1536
  - `2k`: 2048
  - `4k`: 4096
  - `8k`: 8192
  - `16k`: 16384

  The default value is 512.

- `rotation` **[float]** _optional_

  Provides a rotation angle (in radians) around the z-axis around which the cylindrical projection is rotated.

- `heightoffset` **[float]** _optional_

  Offsets the height from which the cylindrical projection is generated. This is, in general, only necessary if the user position is offset and you want to counter that offset to continue producing a "standard" cylindrical projection

- `radius` **[float]** _optional_

  Sets the radius of the sphere, which is only used in the cases when stereoscopic rendering is used.

## Example
```{literalinclude} /assets/configs/projections/cylindrical.json
:language: json
:caption: Example file ([download](/assets/configs/projections/cylindrical.json))
```
