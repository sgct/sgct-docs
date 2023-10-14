# Configuration files
The format for the SGCT configuration files is JSON that defines the entire [Cluster](cluster) containing 1 or more [Node](node) fields, a [User](user) field, an optional [Settings](settings) field, an optional [Capture](capture) field, and an optional [Tracker](tracker) field.  Each of the fields is described on this page further below.

Each configuration file has to fulfill the JSON schema which can be found in the [SGCT repository](https://raw.githubusercontent.com/sgct/sgct/master/sgct.schema.json).


## Examples
This section contains two almost minimal examples showing on a small variety of configuration options.  Check the `config` folder in SGCT for more examples.

Here is a minimal example of a single node, single window configuration.  This file creates a single node on `localhost` with a single window that has a size of 1280 by 720 pixels with a camera of 80 degrees horizontal field-of-view and approximately 50.5 degrees vertical field of view.
```{literalinclude} /assets/configs/example-single.json
:language: json
```

The following example is a configuration that creates two nodes, both running on the local machine, the difference being that their field-of-views are rotated by 40 degrees off the center.
```{literalinclude} /assets/configs/example-two-nodes.json
:language: json
```

The final example is a fisheye rendering which demonstrates a more sophisticated rendering setup, which internally consists of many projections that are automatically assembled by SGCT into a single circular fisheye output.
```{literalinclude} /assets/configs/example-fisheye.json
:language: json
```

## Element types
The rest of the documentation contains information about the configuration settings that can be added to the configuration files.

:::{toctree}
:maxdepth: 2
:titlesonly:

cluster
node
window
capture
viewport
projection/index
scene
user
settings
tracker
device
:::
