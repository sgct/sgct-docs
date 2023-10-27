# Spout Flat Projection
This projection method provides the ability to share a single flat image using the [Spout](https://spout.zeal.co/) library. This library only supports the Windows operating system, so this projection will only work on Windows machines. Spout's functionality is the abilty to shared textures between different applications on the same machine, making it possible to render images using SGCT and making them available to other real-time applications on the same machine for further processing. Spout uses a textual name for accessing which texture should be used for sharing.

- `type` **[string = "SpoutFlatProjection"]**

  Defines the type of this projection. The value must be "SpoutFlatProjection"

- `width` **[integer > 0]** _optional_

  Determines the width of the window that is shared in pixels. If the value is not specified, a width of 1280 is used.

- `height` **[integer > 0]** _optional_

  Determines the height of the window that is shared in pixels. If the value is not specified, a height of 720 is used.

- `mappingspoutname` **[string]** _optional_

  The Spout name under which the rendering is shared. If the name is not specified, `SPOUT_SGCT_MAPPING` is used.

- `drawmain` **[boolean]** _optional_

  Determines whether the main window gets rendered in addition to the shared window. By default the main window is not rendered.

- `background` **[object]** _optional_

  This value determines the color that is used for the parts of the image that are not covered by the spherical mirror image. The alpha component of this color has to be provided even if the final render target does not contain an alpha channel. All attributes `r`, `g`, `b`, and `a` must be defined and be between 0 and 1. The default color is a dark gray (0.3, 0.3, 0.3, 1.0).

- `planarprojection` **[object]**

  Defines the [PlanarProjection](planarprojection) that is used in this viewport.

## Example
```{literalinclude} /assets/configs/projections/spoutflat.json
:language: json
:caption: Example file ([download](/assets/configs/projections/spoutflat.json))
```
