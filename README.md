# Linak Desk Application
This is desktop application controlling Linak office desks. Application functionality is 
similar to application proviced by Linak -- official application does not support Linux
operating systems.

Application was tested on DPG1C desk panel containing built-in Bluetooth module.

Communication protocol between DPG1C module and official application was
reverse engineered mostly by mocking DPG1C Bluetooth service.


## Features
- scanning for nearby devices
- moving up/down
- moving to favourite position
- system tray icon


## Modules
- linakdeskapp.main -- entry point for the application
- linakdeskmock -- Bluetooth service mocking Linak desk service
- testlinakdeskapp -- unit tests for the application


### Running application

To run application simply execute *linakdeskapp/main.py* file. Application
can be run in profiler mode. 


### Running mock service

To run mock simply execute *linakdeskmock/main.py* file.


### Running tests

To run tests execute *src/runtests.py*. It can be run with code profiling 
and code coverage options.

In addition there is demo application not requiring Bluetooth connection. It 
can be run by *testlinakdeskapp/gui/main_window_example.py*.


## Examples of use of not obvious Python mechanisms:
- use of *EnumMeta* class (*linak_service.py*)
- defining method decorators (*synchronied.py*)
- properly killing (Ctrl+C) PyQt (*sigint.py*)
- use of threading: *Thread*, *Event*, *Timer*
- code profiling (*cProfile*)
- code coverage (*coverage*)


## References:
- https://www.linak.com/products/controls/dpg-with-reminder/
- https://www.linak.com/products/controls/desk-control-apps/
- https://ianharvey.github.io/bluepy-doc/index.html
- https://github.com/Vudentz/BlueZ/tree/master/doc

