# rhino-matlab
Simplified and low-level socket based matlab controller, for use in the integrated IronPython of Rhinocerus software 

The controller creates a Matlab process and executes the MatServer.m matlab function that is intended to serve requests usings sockets i.e. evaluting commands and reading variables.

In order to use the matlab controller you need to import the RhinoMatlab module while keeping in the same folder the MatServer.m file.

In test_rhino_mat.py specific instructions are provided.

This implementation is for Windows, for Unix/Mac you can use a different approach based on pipes for example:
https://github.com/awesomebytes/python-mlabwrap
