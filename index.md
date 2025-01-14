# Simple Graphics Cluster Toolkit
SGCT is a free cross-platform C++ library for developing OpenGL applications that are synchronized across a cluster of image generating computers (IGs). SGCT is designed to be as simple as possible to use for the developer and targets the use in immersive real-time applications. SGCT supports a large number of output formats, such as planetarium/domes, fisheye projections, equirectangular projections, and many other types of projection types. SGCT also supports a variety of stereoscopic formats such as active quad buffers, passive side-by-side, passive over-and-under, checkerboard/DLP/pixel interlaced, and different kinds of anaglyphic stereoscopy. SGCT applications are scalable and use a JSON configuration file format in which all IGs and their properties are specified. With this approach, there is no need for recompilation of an application for different immersive environments and applications extend naturally to a server-client clustered architecture without recompilation either. In all cases, the client code only needs to render its scene using the provided projection matrices and compositing is then handled internally.

## Terminology
We use the following terminology to talk about the way how SGCT works. There is a single *Cluster* that consists of 1 or more *Node*s, usually corresponding to a single computer. Each *Node* contains 1 or more *Window*s with each *Window* containing 1 or more *Viewport*s. Some viewport types, such as Fisheye projections, can contain multiple *Subviewport*s, which are created automatically. One of the *Node*s in the *Cluster* is designated as the *server*, where as the other *Nodes* are *client*s or *Image Generator*s (IGs).

Please note that in this nomenclature, even if an application is running only on a single machine, it is still considered a cluster, but only consisting of 1 node that also acts as the server for 0 clients.

## Examples
The `src/apps` folder in the SGCT repository contain a large amount of examples. These can be compiled by enabling the `SGCT_EXAMPLES` CMake option.

## License
SGCT is licensed under the [3-clause BSD license](https://choosealicense.com/licenses/bsd-3-clause/)

```text
Copyright (c) 2012-2025
Miroslav Andel, Linköping University
Alexander Bock, Linköping University

Contributors: Alexander Fridlund, Joel Kronander, Daniel Jönsson, Erik Sundén, Gene Payne

For any questions or information about the SGCT project please contact: alexander.bock@liu.se

Redistribution and use in source and binary forms, with or without modification,
are permitted provided that the following conditions are met:

1.   Redistributions of source code must retain the above copyright
     notice, this list of conditions and the following disclaimer.
2.   Redistributions in binary form must reproduce the above copyright
     notice, this list of conditions and the following disclaimer in the
     documentation and/or other materials provided with the distribution.
3.   Neither the name of the copyright holder nor the names of its contributors
     may be used to endorse or promote products derived from this software
     without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS ''AS IS''
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
IN NO EVENT SHALL THE COPYRIGHT HOLDERS AND CONTRIBUTORS BE LIABLE FOR ANY DIRECT,
INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA,
OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
```

For any questions or further information about the SGCT project, please contact [alexander.bock@liu.se](mailto:alexander.bock@liu.se) or [erik.sunden@liu.se](mailto:erik.sunden@liu.se).

## External libraries
SGCT uses and acknowledges the following external third-party libraries:
  - [Catch2](https://github.com/catchorg/Catch2)
  - [FreeType2](http://www.freetype.org)
  - [GLAD](https://github.com/Dav1dde/glad)
  - [GLFW](https://www.glfw.org)
  - [GLM](http://glm.g-truc.net)
  - [gstreamer](https://gstreamer.freedesktop.org/)
  - [nlohmann json](https://json.nlohmann.me/)
  - [json-schema-validator](https://github.com/pboettch/json-schema-validator)
  - [libpng](http://www.libpng.org)
  - [NDI](https://ndi.video/)
  - [OpenVR](https://github.com/ValveSoftware/openvr)
  - [scnlib](https://github.com/eliaskosunen/scnlib)
  - [Spout](https://github.com/box/spout)
  - [stb_image](https://github.com/let-def/stb_image)
  - [TinyXML](https:/github.com/leethomason/tinyxml2)
  - [Tracy](https://github.com/nette/tracy)
  - [VRPN](https://github.com/vrpn/vrpn)
  - [zlib](https://www.zlib.net)



:::{toctree}
:caption: Users
:maxdepth: 1
:hidden:

users/configuration/index
users/commandline-arguments
users/examples
:::


:::{toctree}
:caption: Developers
:maxdepth: 1
:hidden:

developers/features
developers/how-it-works
developers/getting-started
:::
