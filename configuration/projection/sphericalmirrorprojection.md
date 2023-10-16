# Spherical Mirror Projection
This node type is used to create a projection used for Paul Bourke's spherical mirror setup (see [here](http://paulbourke.net/dome/)), which makes it possible to use an off-the-shelf projector to create a planetarium-like environment by bouncing the image of a shiny metal mirror.  Please note that this is not the only way to produce these kind of images.  Depending on your setup and availability of warping meshes, it might suffice to use the [FisheyeProjection](fisheyeprojection) node type instead and add a single mesh to the parent [Viewport](../viewport) instead.  The `config` folder in SGCT contains an example of this using a default 16x9 warping mesh.  This projection type specifically deals with the case where you have four different meshes, one for the bottom, top, left, and right parts of the distorted image.

- `quality` **[low, medium, high, 256, 512, 1k, 1024, 1.5k, 1536, 2k, 2048, 4k, 4096, 8k, 8192, 16k, 16384]** _optional_

  Determines the pixel resolution of the cube map faces that are reprojected to create the spherical mirror projection rendering.  The higher resolution these cube map faces have, the better quality the resulting spherical mirror projection rendering, but at the expense of increased rendering times.  The named values are corresponding:
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

- `tilt` **[float]** _optional_

  Determines the tilt of the "up vector" of the spherical mirror projection.  With a tilt of 0, the center of the spherical mirror image is the apex of the half-sphere that is used to reproject the cube map.  The default value is 0.

- `background` **[object]** _optional_

  This value determines the color that is used for the parts of the image that are not covered by the spherical mirror image.  The alpha component of this color has to be provided even if the final render target does not contain an alpha channel, in which case the alpha value is ignored.  All attributes `r`, `g`, `b`, and `a` must be defined and be between 0 and 1.  The default color is a dark gray (0.3, 0.3, 0.3, 1.0).

- `geometry` **[object]**

  Describes the warping meshes used for the spherical mirror projection.  All four warping meshes have to be present.
  - `bottom` **[string]**

    The path to the warping mesh that is loaded for the bottom part of the spherical mirror projection.

  - `top` **[string]**

    The path to the warping mesh that is loaded for the bottom part of the spherical mirror projection.

  - `left` **[string]**

    The path to the warping mesh that is loaded for the bottom part of the spherical mirror projection.

  - `right` **[string]**

    The path to the warping mesh that is loaded for the bottom part of the spherical mirror projection.
