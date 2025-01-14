# Configuration files
The format for the SGCT configuration files is JSON that defines the entire [Cluster](cluster) containing 1 or more [Node](node) fields, a [User](user) field, an optional [Settings](settings) field, an optional [Capture](capture) field, and an optional [Tracker](tracker) field. Each of the components in the configuration files are described in their own pages. Each configuration file has to fulfill the JSON schema which can be found in the [SGCT repository](https://raw.githubusercontent.com/sgct/sgct/master/sgct.schema.json).

This is an example configuration file. For more examples, check out the `config` folder that comes with SGCT or the [Examples](../examples) section in this documentation.

```{literalinclude} /assets/configs/examples/single.json
:language: json
:caption: A single node configuration file ([download](/assets/configs/examples/single.json))
```


:::{toctree}
:maxdepth: 2
:hidden:
:titlesonly:

cluster
node
window
viewport
projection/index
scene
user
settings
capture
device
tracker
types
:::
