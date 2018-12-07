function MatServer(port_server)
port = port_server;
port_send = port_server + 2;

import java.net.ServerSocket;
import java.io.*;

% inform python module that Matlab server is ready
send_response('Matlab ready...', port_send);

server = ServerSocket(port);

% start listening continuously
while(true)
    disp('Waiting for client request');
    % creating socket and waiting for client connection
    socket = server.accept;
    % read from socket to ObjectInputStream object
    ois = socket.getInputStream;
    % convert ObjectInputStream object to String
    message = '';
    while(true)
        ch = ois.read;
        if ch ~= -1
            message = [message char(ch)];
        else
            break;
        end
    end
    disp(['Command Received:  ' message]);
    
    if isempty(message)
        disp(strcat('Cannot process command'));
        continue;
    end
   
    if contains(message,'close')
            % terminate the server if client sends exit request
            break;
    elseif contains(message,'read')
        ois.close();
        var_to_read = strsplit(message, '%');
        var_to_read = var_to_read(2);
        var = string(var_to_read);
        if exist(var)
            eval('response = mat2str(' + var + ');');
        else
            response = 'Variable does not exist in matlab workspace';
        end    
        send_response(response, port_send)
        
    elseif contains(message,'ex_and_wait')
        ois.close();
        command = strsplit(message, '%');
        command = command(2);
        try
            % evaluate Matlab command
            eval(string(command));
            % when finished send signal back to the client
            send_response('finished', port_send);
        catch ME
            % catch matlab errors and forward them to the client
            send_response(ME.message, port_send);
        end
    else
        try
            % evaluate Matlab command
            eval(string(command));
        catch ME
            disp(ME.message)
        end
    end
end

disp('Shutting down Socket server!!');
% close the ServerSocket object
server.close();

if contains(message,'exit')
    exit;
end

end

function send_response(response, port_send)

import java.net.Socket;
import java.io.*;

socket_send = Socket('localhost', port_send);
oos = socket_send.getOutputStream;
d_oos = DataOutputStream(oos);
d_oos.writeBytes(char(response));
d_oos.flush;
oos.close();
socket_send.close();
		
end