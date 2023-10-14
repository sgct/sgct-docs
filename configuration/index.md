# General layout
The format for the SGCT configuration files is XML with a single [Cluster](cluster) tag that can contain 1 or more [Node](node) tags, a [User](user) tag, an optional [Settings](settings) tag, an optional [Capture](capture) tag, and an optional [Tracker](tracker) tag.  Each of the tags is described on this page further below.


## Examples
This section contains two almost minimal examples showing on a small variety of configuration options.  Check the `config` folder in SGCT for more examples.

Here is a minimal example of a single node, single window configuration.  This file creates a single node on `localhost` with a single window that has a size of 1280 by 720 pixels with a camera of 80 degrees horizontal field-of-view and approximately 50.5 degrees vertical field of view.
```xml
<?xml version="1.0" ?>
<Cluster masterAddress="localhost">
  <Node address="localhost" port="20401">
    <Window fullScreen="false">
      <Size x="1280" y="720" />
      <Viewport>
        <Pos x="0.0" y="0.0" />
        <Size x="1.0" y="1.0" />
          <PlanarProjection>
            <FOV down="25.267007923362" left="40.0" right="40.0" up="25.267007923362" />
            <Orientation heading="0.0" pitch="0.0" roll="0.0" />
          </PlanarProjection>
      </Viewport>
    </Window>
  </Node>
  <User eyeSeparation="0.06">
    <Pos x="0.0" y="0.0" z="4.0" />
  </User>
</Cluster>
```
The following example is a configuration that creates two nodes, both running on the local machine, the difference being that their field-of-views are rotated by 40 degrees off the center.
```xml
<?xml version="1.0" ?>
<Cluster masterAddress="127.0.0.1">
  <Node address="127.0.0.1" port="20401">
    <Window fullScreen="false">
      <Pos x="0" y="300" />
      <Size x="640" y="360" />
      <Viewport>
        <Pos x="0.0" y="0.0" />
        <Size x="1.0" y="1.0" />
          <PlanarProjection>
            <FOV down="25.267007923362" left="40.0" right="40.0" up="25.267007923362" />
            <Orientation heading="-20.0" pitch="0.0" roll="0.0" />
          </PlanarProjection>
      </Viewport>
    </Window>
  </Node>
  <Node address="127.0.0.2" port="20402">
    <Window fullScreen="false">
      <Pos x="640" y="300" />
      <Size x="640" y="360" />
      <Viewport>
        <Pos x="0.0" y="0.0" />
        <Size x="1.0" y="1.0" />
          <PlanarProjection>
            <FOV down="25.267007923362" left="40.0" right="40.0" up="25.267007923362" />
            <Orientation heading="20.0" pitch="0.0" roll="0.0" />
          </PlanarProjection>
      </Viewport>
    </Window>
  </Node>
  <User eyeSeparation="0.06">
    <Pos x="0.0" y="0.0" z="4.0" />
  </User>
</Cluster>
```

The final example is a fisheye rendering which demonstrates a more sophisticated rendering setup, which internally consists of many projections that are automatically assembled by SGCT into a single circular fisheye output.
```xml
<?xml version="1.0" ?>
<Cluster masterAddress="localhost">
  <Node address="localhost" port="20401">
    <Window fullScreen="false">
      <Stereo type="none" />
      <Size x="512" y="512" />
      <Viewport name="fisheye">
        <Pos x="0.0" y="0.0" />
        <Size x="1.0" y="1.0" />
        <FisheyeProjection fov="180" quality="medium" tilt="27.0">
          <Background r="0.1" g="0.1" b="0.1" a="1.0" />
        </FisheyeProjection>
      </Viewport>
    </Window>
  </Node>
  <User eyeSeparation="0.06">
    <Pos x="0.0" y="0.0" z="0.0" />
  </User>
</Cluster>
```

## Element types
The rest of the documentation contains information about the different types of XML nodes that can be added to the configuration files.  For the nomenclature, *Attributes* are parameters of an XML node where as *Children* are child XML node of the node that is currently discussed.  Some *Attributes* are maked as *optional* which means that they do not have to be present and their default behavior depends on the particular option, which is mentioned in the description.  For *Children*, it is mentioned how many children are allowed or have to be preset for a specific node.

:::{toctree}
:maxdepth: 2
:titlesonly:

capture
cluster
device
node
projection/index
scene
settings
tracker
user
viewport
window
:::
