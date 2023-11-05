# Node
This type defines a single computing node that is contained in the described cluster. In general this corresponds to a single computer, but it is also possible to create multiple nodes on a local machine by using the `127.0.0.x` IP address with `x` from `1` to `255`. It is not possible to create multiple nodes on the same *remote* computer, however, which means that providing the same IP address multiple times is not supported.

- `address` **[string]**

  The IP address or the DNS name of the node. If the `address` is a DNS name, the name resolution is delegated to the operating system and might include additional network traffic to the DNS host.  If the node ought to be the local machine either `127.0.0.x` with `x` from `0` to `255`, or `localhost` (which corresponds to `127.0.0.1`) can be used.

- `port` **[integer > 0]**

  The port at which this node is available at to the server. Please note that operating systems have restricted behavior when trying to open ports lower than a fixed limt.  For example, Unix does not allow non-elevated users to open ports < 1024. As a convention, SGCT usually uses ports staring at 20400, but this is an arbitrary convention without a specific reason.

- `windows` **[array, min 1]**

  Each object in this array has to be a valid [Windows](window) object that describe an individual window that will be opened for the application. There has to be at least one window for a node.

- `swaplock` **[boolean]** _optional_

  Determines whether this node should be part of an Nvidia swap group and should use the swap barrier. Please note that this feature only works on Windows and requires Nvidia Quadro cards + G-Sync synchronization cards. For more information on swap groups, see [here](https://www.nvidia.com/content/dam/en-zz/Solutions/design-visualization/quadro-product-literature/Quadro_GSync_install_guide_v4.pdf). The default value is `false`.

- `datatransferport` **[integer > 0]** _optional_

  If this value is set, a socket connection is opened at the provided port that can be used by the application to transmit data between the server and the clients using the `dataTransfer*` callbacks and `transferData` function of the `NetworkManager`. If no value is specified this function will not work and the callbacks will never be called. Please note that operating systems have restricted behavior when trying to open ports lower than a fixed limt. For example, Unix does not allow non-elevated users to open ports below 1024.
