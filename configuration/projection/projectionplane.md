# Projection Plane
This projection method is based on providing three corner points that are used to construct a virtual image plane.

- `type` **[string = "ProjectionPlane"]**

  Defines the type of this projection. The value must be "ProjectionPlane"

- `lowerleft` **[object]**

  Provides the location of the lower left corner of the projection plane. The object should have `x`, `y`, and `z` fields that provide the position in a relation to the [User](../user) location specified in the [cluster](../cluster).

- `upperleft` **[object]**

  Provides the location of the upper left corner of the projection plane. The object should have `x`, `y`, and `z` fields that provide the position in a relation to the [User](../user) location.

- `upperright` **[object]**

  Provides the location of the upper right corner of the projection plane. The object should have `x`, `y`, and `z` fields that provide the position in a relation to the [User](../user) location.

```{literalinclude} /assets/configs/projections/projectionplane.json
:language: json
:caption: Example file ([download](/assets/configs/projections/projectionplane.json))
```
