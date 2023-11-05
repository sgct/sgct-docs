# Cluster
Overall cluster settings are provided at the root of the JSON object.

- `masteraddress` **[string]**

  Contains the address of the node that acts as the server for this cluster. This means that one of the [Node](node) elements described in this configuration file *has* to have an address that corresponds to this `masteraddress`. This value can be either an IP address or a DNS name, which will be resolved at application startup.

- `nodes` **[array, min 1]**

  Each object in this array has to be a valid [Node](node). At least one of the described nodes has to have an address that matches the cluster's `masteraddress`.

- `users` **[array, min 1]**

  Each object in this array has to be a valid [User](user). The first value in the array is considered to be the default user for the application.
  :::{warning}
  The VRPN support in SGCT is currently non-functional and providing more than one [User](user) currently does not do anything.
  :::

- `scene` **[[Scene](scene) object]** _optional_

  This settings describes general settings about the scene, such as global rotations, scaling, etc. See the [Scene](scene) page for more information.


- `threadaffinity` **[integer >=0]** _optional_

  Forces the thread affinity for the main thread of the application. On Windows, this is achieved using the [SetThreadAffinityMask](https://docs.microsoft.com/en-us/windows/win32/api/winbase/nf-winbase-setthreadaffinitymask), but this functionality might not be implemented on other operating systems. The default value is that no thread affinity is set for the application and is left up to the operating system kernel.

- `debuglog` **[boolean]** _optional_

  Determines whether the logging should include `Debug` level log messages. The default value is `false`, such that only `Info` level log messages or above are added to the console, the file, or the registered callback. Log messages that are not logged are discarded.

- `firmsync` **[boolean]** _optional_

  Determines whether the server should frame lock and wait for all client nodes or not. The default for this is `false`. Additionally, it is possible (and more advised) to set the frame locking on an individual node bases for the cases where not all nodes are part of a swap group or the same swap group.

- `settings` **[[Settings](settings) object]** _optional_

  This object describes general {math}`0-1` [Settings](settings) for the application. The scene specific settings can be found under the `scene` menu instead.

- `capture` **[[Capture](capture) object]** _optional_

  The object provides attributes that describe how the application will treat screen captures, if any are taken. The  [Capture](capture) pages describes the available values in greater detail.

- `trackers` **[array]** _optional_

  Each object in this array has to be a valid [Tracker](tracker) which describes a VRPN tracker.
  :::{warning}
  The VRPN support in SGCT is currently non-functional and objects assigned to the `trackers` currently do not do anything
  :::

