# Examples
This section contains a number of example SGCT files showing off some of the capabilities of SGCT. Check the `config` folder in SGCT for more examples. Each example has a small description, the configuration file, and an image from the `Calibrator` application using that configuration file. These examples are meant both as working example files that can be used, but also as an inspiration to create custom configuration files.


## Single Node
Here is a minimal example of a single node, single window configuration. This file creates a single node on `localhost` with a single window that has a size of 1280 by 720 pixels with a camera of 80 degrees horizontal field-of-view and approximately 50.5 degrees vertical field of view.

```{literalinclude} /assets/configs/examples/single.json
:language: json
:caption: ([download](/assets/configs/examples/single.json))
```

![image](/assets/configs/examples/single.png)


## High-resolution
This example creates a window of full HD size (1920x1080) but the rendering is actually happening at 8K resolution (7680x4320). While this would not be useful under normal circumstances, native screenshots that are taking from this configuration file will be at the actual rendering resolution even if the screen would not support such high resolutions normally.

```{literalinclude} /assets/configs/examples/highres.json
:language: json
:caption: ([download](/assets/configs/examples/highres.json))
```

![image](/assets/configs/examples/highres.png)


## Two Nodes
The following example is a configuration that creates two nodes, both running on the local machine, the difference being that their field-of-views are rotated by 40 degrees off the center. This type of setup is useful when driving two or more projectors from a single computer. Instead of calculating the field-of-view settings, it is also possible to use the [ProjectionPlane](configuration/projection/projectionplane) that takes coordinates to the screen coordinates, which are easier to measure in the real world.

```{literalinclude} /assets/configs/examples/two-nodes.json
:language: json
:caption: ([download](/assets/configs/examples/two-nodes.json))
```

## Two Windows
This example is a variant on the [Two Nodes](#two-nodes) example above. Instead of starting the application twice with one window each, this configuration file is using one instance that renders into two windows instead.

```{literalinclude} /assets/configs/examples/two-windows.json
:language: json
:caption: ([download](/assets/configs/examples/two-windows.json))
```

![image](/assets/configs/examples/two-windows.png)

## Fisheye
This example is a fisheye rendering which demonstrates a more sophisticated rendering setup, which internally consists of many projections that are automatically assembled by SGCT into a single circular fisheye output.

```{literalinclude} /assets/configs/examples/fisheye.json
:language: json
:caption: ([download](/assets/configs/examples/fisheye.json))
```

![image](/assets/configs/examples/fisheye.png)

## Fisheye Presentation
This example creates two windows with different projection methods. The first window contains a fisheye rendering without any 2D UI graphics elements and the second contains only 2D elements. This type of setup is useful in cases where a presenter wants to show the rendered image to the audience, but does not want the user interface to show up.

```{literalinclude} /assets/configs/examples/fisheye-presentation.json
:language: json
:caption: ([download](/assets/configs/examples/fisheye-presentation.json))
```

![image](/assets/configs/examples/fisheye-presentation.png)

## Anaglyph Stereo
This example is rendering a stereo image of a flat projection using red-cyan anaglyph color mode. See [Stereo](configuration/window) for other stereo options.

```{literalinclude} /assets/configs/examples/anaglyph-stereo.json
:language: json
:caption: ([download](/assets/configs/examples/anaglyph-stereo.json))
```

![image](/assets/configs/examples/anaglyph-stereo.png)


## NDI Sharing
This example is sharing an equirectangular projection using the NDI protocol.

```{literalinclude} /assets/configs/examples/ndi.json
:language: json
:caption: ([download](/assets/configs/examples/ndi.json))
```

![alt text](/assets/configs/examples/ndi.png)


## Cubemap NDI Sharing
This example is sharing all six sides of a cubemap using the NDI protocol so that it can be ingested by another application.

```{literalinclude} /assets/configs/examples/cubemap-ndi.json
:language: json
:caption: ([download](/assets/configs/examples/cubemap-ndi.json))
```

![image](/assets/configs/examples/cubemap-ndi.png)
