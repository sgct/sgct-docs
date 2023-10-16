# Equirectangular Projection
This projection method renderes an equirectangular projection (also called lat-long projection or equidistant cylindrical projection) is a default projection method used for spherical objects or maps.

- `quality` **[low, medium, high, 256, 512, 1k, 1024, 1.5k, 1536, 2k, 2048, 4k, 4096, 8k, 8192, 16k, 16384]** _optional_

  Determines the pixel resolution of the cube map faces that are reprojected to create the fisheye rendering. The higher resolution these cube map faces have, the better quality the resulting fisheye rendering, but at the expense of increased rendering times. The named values are corresponding:
  - `low`: 256
  - `medium`: 512
  - `high`: 1024
  - `1k`: 1024
  - `1.5k`: 1536
  - `2k`: 2048
  - `4k`: 4096
  - `8k`: 8192
  - `16k`: 16384

  The default value is 512.
