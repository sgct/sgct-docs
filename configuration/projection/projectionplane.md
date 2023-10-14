# Projection Plane

This projection method is based on providing three corner points that are used to construct a virtual image plane.  The lower left, upper left, and upper right points have to be provided as children of this node in this exact order using `Pos` as the child name.  Each child needs to have float attributes `x`, `y`, and `z`.  So each child has to be the form `<Pos x="..." y="..." z="..." />`.
