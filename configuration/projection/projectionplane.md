# Projection Plane
This projection method is based on providing three corner points that are used to construct a virtual image plane.

- `lowerleft` **[object]**

  Provides the location of the lower left corner of the projection plane. The object should have `x`, `y`, and `z` fields that provide the position in a relation to the [User](../user) location.

- `upperleft` **[object]**

  Provides the location of the upper left corner of the projection plane. The object should have `x`, `y`, and `z` fields that provide the position in a relation to the [User](../user) location.

- `upperright` **[object]**

  Provides the location of the upper right corner of the projection plane. The object should have `x`, `y`, and `z` fields that provide the position in a relation to the [User](../user) location.
