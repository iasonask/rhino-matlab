import RhinoMatlab

# instantiate controller with default values
# modify accordingly (see init definition) for using different versions of Matlab or if the matlab.exe
# is not in the system path variable, by providing the full matlab path  of the matlab executable e.g.:
# controller = RhinoMatlab.RhinoMatlab(matlab_path='C:\MATLAB\matlab.exe')
controller = RhinoMatlab.RhinoMatlab()

# start matlab
controller.start_server()

for i in range(0, 100):
    # executing blocking command in matlab, client will wait until matlab is finished
    controller.execute_and_wait('A = magic(floor((rand(1)+1)*60));')
    # read a specific variable (a string representation)
    print controller.read_data('A')

# execute command in a non blocking way
controller.execute_command('A = 1;')

# close matlab and exit also
controller.disconnect(True)
