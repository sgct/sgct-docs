# Node
This type defines a single computing node that is contained in the described cluster. In general this corresponds to a single computer, but it is also possible to create multiple nodes on a local machine by using the `127.0.0.x` IP address with `x` from `0` to `255`. It is not possible to create multiple nodes on the same *remote* computer, however.

- `address` **[string]**

  The IP address or the DNS name of the node. If the `address` is a DNS name, the name resolution is delegated to the operating system and might include additional network traffic to the DNS host.  If the node ought to be the local machine either `127.0.0.x` with `x` from `0` to `255`, or `localhost` (which corresponds to `127.0.0.1`) can be used.

- `port` **[integer > 0]**

  The port at which this node is available at to the server. Since the server has to open bidirectional sockets to all of the client nodes, the `port` for each `Node` has to be mutually exclusive, meaning that no two `Node`s can have the same `port`. Please note that operating systems have restricted behavior when trying to open ports lower than a fixed limt.  For example, Unix does not allow non-elevated users to open ports < 1024. As a convention, SGCT usually uses ports staring at 20400, but this is an arbitrary convention without a specific reason.

- `datatransferport` **[integer > 0]** _optional_

  If this value is set, a socket connection is opened at the provided port that can be used by the application to transmit data between the server and the clients using the `dataTransfer*` callbacks and `transferData` function of the `NetworkManager`. If no value is specified this function will not work and the callbacks will never be called. Please note that operating systems have restricted behavior when trying to open ports lower than a fixed limt.  For example, Unix does not allow non-elevated users to open ports < 1024.

- `swapLock` **[boolean]** _optional_

  Determines whether this node should be part of an Nvidia swap group and should use the swap barrier. Please note that this feature only works on Windows and requires Nvidia Quadro cards + G-Sync synchronization cards. For more information on swap groups, see [here](https://www.nvidia.com/content/dam/en-zz/Solutions/design-visualization/quadro-product-literature/Quadro_GSync_install_guide_v4.pdf). The default value is `false`.

- `windows` **[object]**

  {math}`1-\infty` [Windows](window) objects
