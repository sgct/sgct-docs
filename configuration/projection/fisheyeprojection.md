# Fisheye Projection

This node describes a fisheye projection that is used to render into its parent [Viewport](../viewport).  By default, a fisheye rendering is covering 180 degrees field of view and has a 1:1 aspect ratio, though these parameters can be changed with the attributes provided in this node.  This projection type counts as a non-linear projection, which requires 4-6 render passes of the application, meaning that the application might render slower when using these kind of projections than a flat projection.  In either case, the application does not need to be aware of the projection as this abstract is handled internally and the applications `draw` method is only called multiple times per frame with different projection methods that are used to create the full fisheye projection.

Depending on the field of view, a cube map is created consisting of 4-6 cube maps that are reprojected in a post-processing into a fisheye of the desired field-of-view.

- `fov` `[float > 0]` _optional_

  Describes the field of view that is covered by the fisheye projection in degrees.  The resulting image will always be a circle, and this value determines how much of a field of view is covered by this circle.  Please note specifically that this also includes field-of-view settings >180, in which a larger distortion is applied to the image.  The default value is 180.

- `quality` **[low, medium, high, 256, 512, 1k, 1024, 1.5k, 1536, 2k, 2048, 4k, 4096, 8k, 8192, 16k, 16384]** _optional_

  Determines the pixel resolution of the cube map faces that are reprojected to create the fisheye rendering.  The higher resolution these cube map faces have, the better quality the resulting fisheye rendering, but at the expense of increased rendering times.  The named values are corresponding:
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

- `interpolation` **[linear or cubic]** _optional_

  Determines the texture interpolation method that is used by SGCT when reprojecting the cube maps into the final fisheye rendering.  The default value is "linear".

- `diameter` **[float > 0]** _optional_

  Sets the diameter in meters for the "sphere" that the fisheye is reprojected based on.  This value is only used for stereoscopic rendering to compute the frustum offset using the [User](../user)s `eyeSeparation`.  The default value is 14.8.

- `tilt` **[float]** _optional_

  Determines the tilt of the "up vector" of the fisheye.  With a tilt of 0, the center of the fisheye image is the apex of the half-sphere that is used to reproject the cube map.  A tilted fisheye rendering is useful when projecting on a tilted planetarium dome.  A value of 90, for example, would result in the forward facing direction being at the center of the fisheye circular image.  The default value is 0.

- `keepaspectratio` **[boolean]** _optional_

  Determines whether the application should try to maintain the original aspect ratio when resizing the window or whether the field of view should be recalculated based on the window's new aspect ratio.  The default value is `true`.

- `crop` **[object]** _optional_

  This node can be used to crop the fisheye after the post processing has been performed.  This might be useful for domes running a single projector with a fisheye lens.  Normally a projector has a 16:9, 16:10, or 4:3 aspect ratio, but the fiehye output has a 1:1 aspect ratio.  This circle can be squared by cropping the 1:1 aspect ratio fisheye image down to the aspect ratio of the projector that is used.  By default, no cropping is applied to the image, leaving it in a 1:1 aspect ratio.

  - `left` **[0 < float < 1]** _optional_

    The ratio of the image that is cropped from the left.  If the value is 0, the image is not cropped at all from this side, if it is 1, the entire image is cropped. However, this cropping value must not be larger than the `1 - right` cropping value as these value might not overlap.  The default value is 0.

  - `right` **[0 < float < 1]** _optional_

    The ratio of the image that is cropped from the right.  If the value is 0, the image is not cropped at all from this side, if it is 1, the entire image is cropped. However, this cropping value must not be larger than the `1 - left` cropping value as these value might not overlap.  The default value is 0.

  - `bottom` **[0 < float < 1]** _optional_

    The ratio of the image that is cropped from the bottom.  If the value is 0, the image is not cropped at all from this side, if it is 1, the entire image is cropped. However, this cropping value must not be larger than the `1 - top` cropping value as these value might not overlap.  The default value is 0.

  - `top` **[0 < float < 1]** _optional_

    The ratio of the image that is cropped from the top.  If the value is 0, the image is not cropped at all from this side, if it is 1, the entire image is cropped. However, this cropping value must not be larger than the `1 - bottom` cropping value as these value might not overlap.  The default value is 0.

- `offset` **[object]** _optional_

  A linear offset in meters that is added to the virtual planes used to project the fisheye rendering.  This can be used for off-axis projections.  Must define three float attributes `x`, `y`, and `z`.  The default values are `x=0`, `y=0`, `z=0`, meaning that no offset is applied to the center of the fisheye sphere.

- `background` **[object]** _optional_

  This value determines the color that is used for the parts of the image that are not covered by the spherical fisheye image.  The alpha component of this color has to be provided even if the final render target does not contain an alpha channel, in which case the alpha value is ignored.  All attributes `r`, `g`, `b`, and `a` must be defined and be between 0 and 1.  The default color is a dark gray (0.3, 0.3, 0.3, 1.0).
