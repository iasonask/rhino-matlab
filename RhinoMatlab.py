# For Matlab versions >= 2016

# Import modules
import os
import socket
import subprocess

# define constants, default values
MATLAB_PATH = 'matlab.exe'
M_FILE = 'MatServer'
HOST = 'localhost'
PORT = 30000
PORT_RECEIVE = PORT + 2


class RhinoMatlab:
    # class constructor
    def __init__(self, matlab_path=MATLAB_PATH, m_file=M_FILE, host=HOST, port=PORT, port_receive=PORT_RECEIVE):
        self.MATLAB_PATH = matlab_path
        self.M_FILE = m_file
        self.HOST = host
        self.PORT = port
        self.PORT_RECEIVE = port_receive
        print "____Staring Matlab Controller____"

    def start_server(self, automation=False):
        print "____Staring Matlab ____"
        # open matlab, navigate to folder and run controller
        if automation:
            auto = ' -automation '
        else:
            auto = ' '
        # create matlab subprocess
        # comm = self.MATLAB_PATH + auto + '-nosplash -r run(\'' + self.M_FILE + '\')'
        comm = self.MATLAB_PATH + auto + '-nosplash -sd ' + os.getcwd() \
            + ' -r ' + self.M_FILE + '(' + str(self.PORT) + ')'
        # print comm
        subprocess.Popen(comm, stdout=subprocess.PIPE, bufsize=1)
        # wait until Matlab is up and ready
        print "waiting for Matlab..."
        print self.receive_data()

    def receive_data(self):
        # receive data from matlab
        # Create a socket object
        s_r = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s_r.bind((self.HOST, self.PORT_RECEIVE))
        s_r.listen(1)
        conn, addr = s_r.accept()
        buff_size = 65536
        data = ''
        # receive message
        while True:
            part = conn.recv(buff_size).decode()
            data += part
            if len(part) == 0:
                # end of data
                break
        s_r.close()
        return data

    def execute_command(self, command):
        # Create a socket object
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.HOST, self.PORT))

        # send command
        s.sendall(command.encode('utf-8'))
        # close the connection
        s.close()

    def execute_and_wait(self, command):
        # Create a socket object
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.HOST, self.PORT))

        # send command
        com = 'ex_and_wait/' + command
        s.sendall(com.encode('utf-8'))
        # close the connections
        s.close()
        # wait for matlab to respond after execution
        print self.receive_data()

    def read_data(self, command):
        # Create a socket object
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.HOST, self.PORT))

        # send command
        com = 'read/' + command
        s.sendall(com.encode('utf-8'))
        # close the connections
        s.close()
        # return a string representation of the data
        # can be really slow for large datasets, better to be implemented with .csv files
        return self.receive_data()

    def disconnect(self, also_exit=False):
        if also_exit:
            print "____Exiting Matlab____"
            self.execute_command('close/exit')
        else:
            print "____Disconnecting____"
            self.execute_command('close')
