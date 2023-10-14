# Cluster
The cluster XML node has attributes that determine the behavior of the overall cluster.  This node is required to be present in the XML file exactly once and also has to be the root of the document.

## Attributes
`masterAddress` \[ string \]
 > Contains the address of the node that acts as the server for this cluster.  This means that one of the `Node` elements described in this configuration file *has* to have an address that corresponds to this `masterAddress`.  This value can be either an IP address or a DNS name, which will be resolved at application startup.

`setThreadAffinity` *optional* \[ integer >=0 \]
 > Forces the thread affinity for the main thread of the application.  On Windows, this is achieved using the [SetThreadAffinityMask](https://docs.microsoft.com/en-us/windows/win32/api/winbase/nf-winbase-setthreadaffinitymask), but it might not be implemented on other operating systems.  The default value is that no thread affinity is set for the application.

`debugLog` *optional* \[ boolean \]
 > Determines whether the logging should include `Debug` level log messages.  The default value is `false`, such that only `Info` level log messages or above are added to the console, the file, or the registered callback.  Log messages that are not logged are discarded.

`externalControlPort` *optional* \[ integer > 0 \]
 > If this value is set, a socket will be opened at the provided port.  Messages being sent to that port will trigger a call to the callback function `externalDecode`.  If such a callback does not exist, the incoming messages are ignored.  The default behavior is that no such external port is opened.  Please note that operating systems have restricted behavior when trying to open ports lower than a fixed limt.  For example, Unix does not allow non-elevated users to open ports < 1024.

`firmSync` *optional* \[ boolean \]
 > Determines whether the server should frame lock and wait for all client nodes or not.  The default for this is `false`.  Additionally, it is possible (and more advised) to set the frame locking on an individual node bases for the cases where not all nodes are part of a swap group or the same swap group.

## Children
 - [`Capture`](capture) \[ 0-1 \]
 - [`Node`](node) \[ 1 - inf \]
 - [`Scene`](scene) \[ 0-1 \]
 - [`Settings`](settings) \[ 0-1 \]
 - [`Tracker`](tracker) \[ 0 - inf \]
 - [`User`](user) \[ 1 - inf \]
