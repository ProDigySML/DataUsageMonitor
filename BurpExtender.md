# BurpExtender
## registerExtenderCallbacks
**Description**: Required for implementing Burp Extender

**Param**: `callbacks`: Burp callbacks within Extender

## _init_gui
**Description**: Initialises the GUI for the application

## getTabCaption
**Description**: Gets the caption within the tab

## getUiComponent
**Description**: Gets the tab set up in the UI initialisation component

## _reset_counter
**Description**: Resets the counter and updates the UI to replicate the reset

**Param**: `e`: `Event object`

## _update_gui
**Description**: Calculates the amount of usage based on the counter and allots into their respective category of size

## processHttpMessage
**Description**: Processes all messages that are sent through Burp. We use it to get the length of both the request and the response

**Param**: `toolFlag`: `Enum`: Tells which part of burp the request came from

**Param**: `messageIsRequest`: `Boolean`: Lets you know if the message is a request or a response

**Param**: `messageInfo`: `RequestResponse Object`: Holds both the request and the response
