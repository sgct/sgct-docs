# Window
This XML specifies a single window that is used to render content into.  There can be an arbitrary(*-ish*) number of windows for each node and they all will be created and initialized at start time.  Each window has at least one [Viewport](viewport) that specifies exactly where in the window the rendering occurs with which parameters.

# Attributes
`id` *optional* \[ int \]
> The numerical identifier of this window. By default windows are given numerical value equal to their position in the node-1, meaning that the first window of a node will have the id `0`, the second window id `1`, etc.  This value can be used to overwride this.  It is not possible to give the same ID to two different windows.

`name` *optional* \[ string \]
> The name of the window.  This is also used as the title of the window if window decorations are enabled.  The default name for a window if this value is not specified is "SGCT Node: %i (%s)" with `%i` = the address of this node and `%s` either "server" or "client", depending on whether the current node is the server or the client in the cluster.

`tags` *optional* \[ string \]
> A comma-separated list of tags that are associated with this window.  The tags themselves don't have any meaning inside of SGCT, but can be used by the application code as a filter.  One common use-case is to tag one of the windows as a "GUI" window, to restrict input to only that window, for example.  The default value for this attribute is an empty string.

`bufferBitDepth` *optional* \[ 8, 16, 16f, 32f, 16i, 32i, 16ui, or 32ui \]
> Sets the bit depth and format of the color texture that is used as the render backend for this entire window.  The parameters passed into this attribute are converted to the following OpenGL parameters (internal color format and data type) to the texture creation:
>
> - `8`: `GL_RGBA8`, `GL_UNSIGNED_BYTE`
> - `16`: `GL_RGBA16`, `GL_UNSIGNED_SHORT`
> - `16f`: `GL_RGBA16F`, `GL_HALF_FLOAT`
> - `32f`: `GL_RGBA32F`, `GL_FLOAT`
> - `16i`: `GL_RGBA16I`, `GL_SHORT`
> - `32i`: `GL_RGBA32I`, `GL_INT`
> - `16ui`: `GL_RGBA16UI`, `GL_UNSIGNED_SHORT`
> - `32ui`: `GL_RGBA32UI`, `GL_UNSIGNED_INT`
>
> The default value for this attribute is `8`.

`fullscreen` *optional* \[ boolean \]
> Determines whether the window should be created in an exclusive fullscreen mode.  The `Size` of this window will be used to set the screen resolution if this value is `true`.  See also the `monitor` attribute to determine which monitor should be used as the target for the fullscreen window.  The default value is `false`.

`autoiconify` *optional* \[ boolean \]
> Determines whether an exclusive fullscreen window will be automatically iconified if it loses focus.  This value will be ignored if the `fullscreen` value is not set or if it is `false`.  The default value for this setting is `false`.

`hideMouseCursor` *optional* \[ boolean \]
> If this value is set to `true`, the mouse cursor will never be visible above this window.  The default value for this setting is `false`.

`floating` *optional* \[ boolean \]
> Indicates whether the window is floating, meaning that it is rendered by the operating system always on top of other windows.  The default value is `false`.

`alwaysRender` *optional* \[ boolean \]
> Determines whether the content of the window should continue to render even if the window is not visible on screen.  Normally, the operating system will not invalidate a window when it is hidden (see `isHidden` attribute) and this attribute can be used to overwrite that behavior.  The default behavior is `false`.

`isHidden` *optional* \[ boolean \]
> Determines whether this window should be visible on screen or used as an offscreen rendering target.  If a window is hidden, you should also set `alwaysRender` to `true`, or otherwise the rendering might not occur as expected.  The default for this attribute is `false`.

`dbuffered` *optional* \[ boolean \]
> Sets the buffering to single buffering (if `false`) or double buffering or quad buffering for stereo (if `true`).  The default is `true`.

`msaa` *optional* \[ integer >= 0 \]
> Determines whether multisample antialiasing is used for the window and how many subsamples should be used for the antialiasing.  If the value is set to `0`, MSAA is disabled.  MSAA operates by rendering the scene at a higher resolution using multiple samples per pixel and combining these samples to reduce aliasing.  It produces good-looking results, but it increases the rendering time for the scene.  The maximum number of samples depends on the GPU that is used to start the application, but is usually around 32.  The default is `0`, disabling MSAA.

`hasAlpha` *optional* \[ boolean \]
> Determines whether screenshots created from this window should include an alpha channel or not.  If this value is `false`, the resulting image type is `RGB`, otherwise `RGBA`.  The default is `false`.

`fxaa` *optional* \[ boolean \]
> Determines whether fast approximate antialiasing is used for the contents of this window.  This antialiasing is a postprocessing that does not significantly increase rendering time, but the results are not as good as `msaa`.  The default is `false`.

`border` *optional* \[ boolean \]
> Enables or disables the window decorations.  Window decorations are the title bar that contains the name of the window and buttons to close, maximize or minimize a window.  On some operating systems, the window decorations also include a border around a window and potentially shadow effects, all of which can be disabled with this attribute.  The default is `true`.

`draw2D` *optional* \[ boolean \]
> Determines whether the `draw2D` callback should be called for viewports in this window.  The default value is `true`.

`draw3D` *optional* \[ boolean \]
> Determines whether the `draw` callback should be called for viewports in this window.  The default value is `true`.

`blitWindowId` *optional* \[ int \]
> If this value is specified, the 3D contents of a different window are blitted (=copied) into this window before calling its own rendering.  A common use-case for this are GUI windows that want to show the 3D rendering but not take the performance impact of rendering an expensive scene twice.  Instead of rendering the 3D scene, a GUI window would set `draw3D` to `false` and this attribute to the id of the main window, meaning that the contents of that other window are copied and then the 2D UI will be rendered on top of the blitted content.  Unless specified otherwise, a window's id is its position in the XML file inside a node, starting at 0.  So the first window of a node will have the id `0`, the second `1`, etc.  The default value is `-1` which means taht not blitting is performed.

`monitor` *optional* \[ integer >= -1 \]
> Determines which monitor should be used for the exclusive fullscreen in case `fullscreen` is set to `true`.  The list of monitors on the system are zero-based and range between 0 and the number of monitors - 1.  For this attribute, the special value `-1` can be used to denote that the primary monitor as defined by the operating system should be used, regardless of its index.  The default value is `-1`.

`mpcdi` *optional* \[ string \]
> If this value is set to a path that contains an MPCDI file that describes camera parameters and warping and blending masks, these values are used to initialize the contents of this window instead of providing explicit viewport information.  If this value is used, there cannot be any [Viewport](viewport)s defined in this window as as the `mpcdi` file takes care of this.  The default value is that no MPCDI is used.

## Children
`Stereo` \[ 0 - 1 \]
> Determines whether the contents of this window should be rendered stereoscopically and which stereoscopic rendering method should be used.  The only allowed attribute for this node is the `type`, which determines the type of stereo rendering.  It has to be one of:
>
> - `none`:  No stereo rendering is performed.  This is the same as if this entire node was not specified.
> - `active`:  Using active stereo using quad buffering.  This is only a valid option for systems that support quad buffering.
> - `checkerboard`:  Using a checkerboard pattern for stereoscopy in which left and right eyes are rendered on interleaved checkerboard patterns.
> - `checkerboard_inverted`:  Using the same pattern as `checkerboard`, but with the left and right eyes inverted
> - `anaglyph_red_cyan`:  Applying color filters to the rendering for the left and right eyes such that red-cyan anaglyph glasses can be used to view the stereo content.
> - `anaglyph_amber_blue`:  Applying color filters to the rendering for the left and right eyes such that amber-blue anaglyph glasses can be used to view the stereo content.
> - `anaglyph_wimmer`:  ¯\\_\(ツ\)_/¯
> - `vertical_interlaced`:  A stereo format in which the left and right eye images are interlaced vertically, meaning that each row of the final image is either left or right, switching each row.
> - `vertical_interlaced_inverted`:  The same as `vertical_interlaced`, but with the left and right eye flipped.
> - `dummy`:  A dummy stereo mode to test streoscopic rendering without needing extra equipment.  In this stereo mode, the left and the right eye images are rendered on top of each other without any other processing.  This option is available to verify that stereo rendering is working for a specific application.
> - `side_by_side`:  The resolution of the window is split into a left half and a right half, with each eye being rendered into its half.  This is a common stereo format for 3D TVs.
> - `side_by_side_inverted`:  The same as `side_by_side`, but the left and right images are flipped.
> - `top_bottom`:  The same as `side_by_side`, but instead of separating the window horizontally, the window is split vertically, with the left eye being rendered in the top half of the window and the right image being rendered in the bottom half.
> - `top_bottom_inverted`:  The same as `top_bottom_inverted`, but with the left and right eyes flipped.
>
> The default value is `none`.

`Pos` \[ 0 - 1 \]
> Sets the position of the window on the overall desktop space provided by the operating system.  This node must have `x` and `y` floating point attributes that specify the x-y location of the window.  Please note that these values also can be negative on some operating systems.  On Windows, for example, the top left corner of the primary monitor is (0,0) in this coordinate system, but there can be additional monitors to the left or the top of the primary monitor, which would require negative numbers.  The default values are `x=0` and `y=0`.

`Size` \[ 0 - 1 \]
> Sets the size of the window in pixels.  This node must have `x` and `y` floating point attributes that determine that size of the window.  The default values are `x=640` and `y=480`.

`Res` \[ 0 - 1 \]
> Sets the size of the internal framebuffer that is used to render the contents of the window. In a lot of cases, this resolution is the same resolution as the size of the window, but it is a useful tool when creating images that are larger than a window would be support on an operating system.  Some operating systems restrict windows to be no larger than what can fit on a specific monitor.  This node must have `x` and `y` floating point attributes that determine that size of the window.  By default the resolution of the framebuffer is equal to the size of the window.

- [Viewport](viewport) \[ 1 - inf \]
