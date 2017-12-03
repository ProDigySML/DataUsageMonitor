# BurpExtender
## [registerExtenderCallbacks](https://github.com/ProDigySML/DataUsageMonitor/blob/master/DataUsageMonitor.py#L16)
**Description**: Required for implementing Burp Extender

**Param**: `callbacks`: Burp callbacks within Extender

## [ _init_gui](https://github.com/ProDigySML/DataUsageMonitor/blob/master/DataUsageMonitor.py#L43)
**Description**: Initialises the GUI for the application

## [getTabCaption](https://github.com/ProDigySML/DataUsageMonitor/blob/master/DataUsageMonitor.py#L59)
**Description**: Gets the caption within the tab

## [getUiComponent](https://github.com/ProDigySML/DataUsageMonitor/blob/master/DataUsageMonitor.py#L65)
**Description**: Gets the tab set up in the UI initialisation component

## [_reset_counter](https://github.com/ProDigySML/DataUsageMonitor/blob/master/DataUsageMonitor.py#L71)
**Description**: Resets the counter and updates the UI to replicate the reset

**Param**: `e`: `Event object`

## [_update_gui](https://github.com/ProDigySML/DataUsageMonitor/blob/master/DataUsageMonitor.py#L79)
**Description**: Calculates the amount of usage based on the counter and allots into their respective category of size

## [processHttpMessage](https://github.com/ProDigySML/DataUsageMonitor/blob/master/DataUsageMonitor.py#L96)
**Description**: Processes all messages that are sent through Burp. We use it to get the length of both the request and the response

**Param**: `toolFlag`: `Enum`: Tells which part of burp the request came from

**Param**: `messageIsRequest`: `Boolean`: Lets you know if the message is a request or a response

**Param**: `messageInfo`: `RequestResponse Object`: Holds both the request and the response
