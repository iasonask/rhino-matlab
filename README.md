# rhino-matlab
Requires Python 2.x, Windows and Matlab version >= 2016.

Simplified and low-level socket based matlab controller, for use in the integrated IronPython of 
Rhinocerus software. 

The controller creates a Matlab process and executes the MatServer.m matlab function that is intended to 
serve requests usings sockets i.e. evaluting commands and reading variables.

In order to use the Matlab controller you need to import the RhinoMatlab module while keeping in the same
 folder the MatServer.m file.

In test_rhino_mat.py specific instructions are provided.

This implementation is intended to be used in Windows, for Unix/Mac you can use a different approach 
based on pipes for example: https://github.com/awesomebytes/python-mlabwrap

Remark: For big datasets the read_data() method is not recommended. Instead employ a matlab command 
(i.e. csvwrite()) to store the data locally and afterwards read them from python. For the same reasons, 
while it is possible to send a large number of semicolon-separated commands for execution by calling the 
relevant methods, huge strings (with concatenated commands) should be avoided.  

