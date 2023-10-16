# Spout Output Projection
This projection method provides the ability to share individual cube map faces or a fully reprojected image using the [Spout](https://spout.zeal.co/) library.  This library only supports the Windows operating system, so this projection will only work on Windows machines.  Spout's functionality is the abilty to shared textures between different applications on the same machine, making it possible to render images using SGCT and making them available to other real-time applications on the same machine for further processing.  Spout uses a textual name for accessing which texture should be used for sharing.  The SpoutOutputProjection has three different output types, outputting each cube map face, sharing a fisheye image, or sharing an equirectangular projection, as determined by the `mapping` attribute.

- `quality` **[low, medium, high, 256, 512, 1k, 1024, 1.5k, 1536, 2k, 2048, 4k, 4096, 8k, 8192, 16k, 16384]** _optional_

  Determines the pixel resolution of the cube map faces.  The named values are corresponding:
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

- `mapping` **[fisheye, equirectangular, or cubemap]** _optional_

  Determines the type of sharing that occurs with this projection and thus how many and which texture is shared via Spout.  For the "fisheye" and "equirectangular", only the single, final reprojected image is shared, for the "cubemap" method, all selected cubemaps will be provided through the Spout interface.  The default value is "cubemap".

- `mappingspoutname` **[string]** _optional_

  Sets the name of the texture if the `mapping` type is "fisheye" or "equirectangular".  If the `mapping` is "cubemap", this value is ignored.

- `drawmain` **[boolean]** _optional_

  Determines whether the main window gets rendered in addition to the six cube faces that are sent via Spout.

- `background` **[object]** _optional_

  This value determines the color that is used for the parts of the image that are not covered by the spherical mirror image.  The alpha component of this color has to be provided even if the final render target does not contain an alpha channel.  All attributes `r`, `g`, `b`, and `a` must be defined and be between 0 and 1.  The default color is a dark gray (0.3, 0.3, 0.3, 1.0).

- `channels` **[object]** _optional_

  Determines for the "cubemap" `mapping` type, which cubemap faces should be rendered and shared via spout.  The available boolean attributes that can be used to toggle the individual cube faces are `Right`, `zLeft`, `Bottom`, `Top`, `Left`, `zRight`.  By default all 6 cubemap faces are enabled.

- `orientation` **[object]** _optional_

  Describes a fixed orientation for the cube, whose faces are either shared or used to reproject into the fisheye or equirectangular image.  This can be provided either as Euler angles or as a quaternion.  The two modes *cannot* be mixed.  The following descibes the different attributes that can be used for the orientation.  Please note that *all* attributes for the chosen method have to be specified.  If the `Matrix` attribute is also specified, it will overwrite the value specified here.

  Euler angles:
  - `pitch`: negative numbers tilt the camera downwards;  positive numbers tilt upwards.  The allowed range is `[-90, 90]`.
  - `yaw`: negative numbers pan the camera to the left;  positive numbers pan to the right.  The allowed range is `[-360, 360]`.
  - `roll`: negative numbers rotate the camera to the left;  positive numbers to the right.  The allowed range is `[-180, 180]`.

  Quaternion:
  - `x`
  - `y`
  - `z`
  - `w`
