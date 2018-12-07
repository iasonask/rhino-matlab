import RhinoMatlab

controller = RhinoMatlab.RhinoMatlab()

# start matlab
controller.start_server()

for i in range(0, 100):
    controller.execute_and_wait('A = magic(floor((rand(1)+1)*60))')
    print controller.read_data('A')


controller.disconnect(True)