# Viewport
This node describes a single viewport inside a [Window](window). Every window can contain an arbitrary number of viewports that are all rendered independently. The viewports are positioned inside the window using a normalized coordinate system.

- `pos` **[vec2]** _optional_

  Specifies the position of the viewport inside its parent [Window](window). The coordinates for `x` and `y`, which must both be specified for the object, are between 0 and 1, but are not restricted to that range. Parts of the viewport that are outside this range would lie outside the bounds of the window and are clipped. Viewports are free to overlap and the viewports are rendered in the order in which they are specified in the window and are rendered on top of each other.

- `size` **[vec2]** _optional_

  Specifies the size of this viewport inside its parent [Window](window). The coordinate for `x` and `y`, which must both be specified for the object, are between 0 and 1, but are not restricted to that range. Parts of the viewport that are outside this range would lie outside the bounds of the window and are clipped. Viewports are free to overlap and the viewports are rendered in the order in which they are specified in the window and are rendered on top of each other.

- `projection` **[object]**

  Defines the type of [Projection](projection/index) that is used in this viewport. This value has to exist and must contain at least a key `type` that names the projection being used. The following projection types are supported:
  - [PlanarProjection](projection/planarprojection)
  - [FisheyeProjection](projection/fisheyeprojection)
  - [SphericalMirrorProjection](projection/sphericalmirrorprojection)
  - [EquirectangularProjection](projection/equirectangularprojection)
  - [CylindricalProjection](projection/cylindricalprojection)
  - [SpoutOutputProjection](projection/spoutoutputprojection)
  - [SpoutFlatProjection](projection/spoutflatprojection)
  - [ProjectionPlane](projection/projectionplane)

- `tracked` **[boolean]** _optional_

  Determines whether the field-of-view frustum used for this viewport should be tracking changes to the window configuration, for example when resizing the window. If this value is set to `false`, the field of view set in the beginning will stay unchanged.

- `mesh` **[string]** _optional_

  Determines a warping mesh file that is used to warp the resulting image. The application's rendering will always be rendered into a rectangular framebuffer, which is then mapped as a texture to the geometry provided by this file. This makes it possible to create non-linear or curved output geometries from a regular projection by providing the proper geometry of the surface that you want to project on. The reader for the warping mesh is determined by the file extension of the file that is provided in this attribute. The default is that no warping mesh is applied.

  Supported geometry mesh formats:
  - SCISS Mesh (`sgc` extension)

    A mesh format that was introduced by SCISS for the Uniview software. SCISS created two versions for this file format, one for 2D warping meshes and a second for 3D cubemap lookups. SGCT only supports the first version of that file format, however.

  - Scalable Mesh (`ol` extension)

    A mesh format created by [Scalable](http://www.scalabledisplay.com/products/scalable-sdk/).

  - Dome Projection (`csv` extension)

  - Paul Bourke Mesh (`data` extension)

    A file format created by [Paul Bourke](http://paulbourke.net/dataformats/meshwarp/), his webpage also contains more information abuot the individual steps of the warping.

  - Waveform OBJ (`obj` extension)

    The well known textual mesh format.

  - MPCDI (`mpcdi` extension)

    A subset of the VESA standard.

  - SimCAD (`simcad` extension)

- `user` **[string]** _optional_

  The name of the [User](user) that this viewport should be linked to. If a viewport is linked to a user that has a sensor, the positions of the sensor will be automatically reflected in the user position that is used to render this viewport. The name provided here has to be the name of a user specified in the `users` section of the [Cluster](cluster) The default is that no user is linked with this viewport.
  :::{warning}
  The VRPN support in SGCT is currently non-functional and linking a viewport to a [User](user) currently does not work.
  :::

- `overlay` **[string]** _optional_

  This attribute is a path to an overlay texture that is rendered on top of the viewport after the applications rendering is finished. This can be used to add logos or other static assets on top of an application. The default is that no overlay is rendered.

- `blendmask` **[string]** _optional_

  This value is a path to a texture that is used as a mask to remove parts of the rendered image. The image that is provided in this should be a binary black-white image which is applied by SGCT after the application loading is finished. All parts where the `blendmask` image is black will be removed. The default is that no mask is applied.

- `blacklevelmask` **[string]** _optional_

  The file referenced in this attribute is used as a postprocessing step for this viewport. The image should be a grayscale image, where each pixel will be multiplied with the resulting image from the application in order to perform a black level adaptation. If a pixel is completely white, the resulting pixel is the same as the applications output, if a pixel is black, the resulting pixel will be back, if it is 50% grey, the resolution pixel will be half brightness. This setting is the more The default is that no black level mask is applied.

- `eye` **[center, left, or right]** _optional_

  Forces this viewport to be rendered with a specific eye, using the corresponding [User](user)s eye separation to compute the correct frustum. If this value is not set, the viewport will be rendered according to the parent [Window](window)'s `stereo` attribute.

