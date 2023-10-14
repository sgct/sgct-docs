# Settings
This node controls global settings that affect the overall behavior of the SGCT library that are not limited just to a single window.

## Attributes
`DepthBufferTexture` *optional* \[ boolean \]
 > If this value is set to `true` and a non-linear projection method if provided in a window, SGCT will also provide a buffer containing the reprojected depth values of the non-linear projection.  This value defaults to `false`.

`NormalTexture` *optional* \[ boolean \]
 > If this value is set to `true` and a non-linear projection method if provided in a window, SGCT will also provide a buffer containing the reprojected normals values of the non-linear projection.  This value defaults to `false`.

`PositionTexture` *optional* \[ boolean \]
 > If this value is set to `true` and a non-linear projection method if provided in a window, SGCT will also provide a buffer containing the reprojected positions of the non-linear projection.  This value defaults to `false`.

`Precision` *optional* \[ 16 or 32 \]
 > Determines the floating point precision for the normal and position textures if they are enabled.  Setting this value if `NormalTexture` and `PositionTexture` are disabled does not have any effect.  This value defaults to `32`.

## Children
`Display` \[ 0 - 1 \]
 > Contains settings specific for the handling of display-related settings for the whole application.
 >
 > `swapInterval` *optional* \[ integer \]
 >  > Determines the swap interval for the application.  This determines the amount of V-Sync that should occur for the application.  The two most common values for this are `0` for disabling V-Sync and `1` for regular V-Sync.  The number provided determines the number of screen updates to wait before swapping the backbuffers and returning.  For example on a 60Hz monitor, `swapInterval="1"` would lead to a maximum of 60Hz frame rate, `swapInterval="2"` would lead to a maximum of 30Hz frame rate.  Using the same values for a 144Hz monitor would be a refresh rate of 144 and 72 respectively.  The default value is `0`, meaning that V-Sync is disabled.
 >
 > `refreshRate` *optional* \[ integer \]
 >  > Determines the desired refresh rate for full-screen windows of this configuration.  This value is disabled for windowed mode windows.  The default value is the highest possible refresh rate.
