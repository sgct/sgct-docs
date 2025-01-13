# Commandline arguments
Any application build with SGCT can receive the following commandline options that control the applications behavior.

- `--config [string]` or `-c [string]`

  Sets the configuration file that should be loaded by the application to use as the cluster system. This path should be either an absolute path, or a path relative to the current working directory.

- `--help`

  Displays the help message listing all available commandline arguments supported by SGCT.

- `--local [integer]` or `-l [integer]`

  Forces the node configuration to be `localhost`. The index that is provided is the index that is used for indexing multiple node settings in the cluster setup. Index `0` corresponds to `127.0.0.1`, index `1` is `127.0.0.2`, etc.

- `--client`

  Sets the node to run as a client. This is only available when running as a local node, as otherwise the IP address is used to set the client and server setup.

- `--debug`

  Set the notification level of the Log to include `Debug` level messages which provides more information to debug potential bugs or issues from faulty configuration files.

- `--firm-sync`

  Enables a firm frame synchronization using whatever method that is available, overwriting the settings that are provided in the cluster configuration.

- `--loose-sync`

  Disables the firm frame synchronization, overwriting the settings that are provided in the cluster configuration.

- `--ignore-sync`

  Disables the frame synchronization entirely, which will completely decouple the rendering nodes. This should only be set if you are absolutely sure you know what you are doing.

- `--notify [debug, info, warning, or error ]`

  Sets the notification level of the Log to include only the messages of the chosen log level or higher. Setting this value to `debug` achieves the same as setting the `-debug` commandline flag. If `--debug` and `--notify` is specified in the same command `--notify` takes precedence.

- `--number-capture-threads [integer]`

  Sets the maximum number of threads that should be used for frame capturing. If no frames are captured, this setting is ignored.

- `--screenshot-path [string]`

  Sets the base file path in which screenshots are stored. Each screenshot be stored with a unique base name and a frame counter.

- `--screenshot-prefix [string]`

  Sets the prefix used for the screenshots taken by this application. The default value for the prefix is "SGCT".

- `--add-node-name-in-screenshot`

  If set, screenshots will contain the name of the node in multi-node configurations. The default value is that the numerical identifier for the node is not used in the screenshots.

- `--omit-node-name-in-screenshot`

  If set, screenshots will not contain the name of the window if multiple windows exist. The default is that the name of the window is included.

- `--print-wait-message`

  If this is set to `true` (the default), SGCT will print a message to the console log while the server is waiting for all clients to connect. If this value is `false` no such message is printed.

- `--wait-timeout`

  This value determines how long the server should wait for all clients to connect and for how long the clients should wait for the server to start.
