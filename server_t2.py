##############################################################
#         MULIPROCESSING AND SOCKETS EXAMPLE PROGRAM         #
#   MADE BY @SHAUNAKG // HTTPS://GITHUB.COM/COSMICATECH      #
#             Copyright (c) 2017 @SHAUNAKG                   #
##############################################################

# Note: Updated creator username - still the same person, I just changed my Github username

### Current Version: 2.0 ###
# Changelog for this version:
#   - added 'new' command
#   - added 'kill ' command
#   - Improved process spawning and killing technique
#   - Improved server error handling
#   - More comments
#   - Changed the version number
#   - Fixed bugs
#   - Added more bugs (see BUGS section)

### KNOWN BUG(s) ###
#   - The 'new' command has been known to cause OSError: [WinError 10048] exceptions. (~ Line 95) <<FIXED>>
#   - Can still get stuck in the unresponsive state, see >Note 1

# Note 1: a lot of the time you will get 'stuck' in the program as the processes are still running but there is
# no interface. A lot of efforts have been made to prevent this but I have not found a way to exit from the
# unresponsive state. You will have to close the terminal window or use a program like Task Manager to end the process(es).
# You can also open a command prompt in Windows and run `taskkill /im python.exe`

# Note 2: Some comments are unusually long and may look bad in other text editors.

# Note 3: Some obsolete code is included for convienience.


############################################### CODE START #################################################

# Import the required modules. NOTE: Commented out because I can save memory by including this in the seperate
# functions. For example, the main function doesn't need the sockets module. See below for memory optimization details:
# Memory taken (per server process) BEFORE optimization: 4.5 megabytes
# Memory taken (per server process) AFTER optimization: 4.2 megabytes
#
#import socket
#import multiprocessing
#import time
#import sys

######################### Main function if the program is not imported #########################
def main():
    # Import the required modules here for memory optimization
    import multiprocessing
    import time
    import sys

    startart = """\
+------------------------------------------------------------+
|   SERVSTART - MULIPROCESSING AND SOCKETS EXAMPLE PROGRAM   |
|   MADE BY @SHAUNAKG // HTTPS://GITHUB.COM/COSMICATECH      |
+------------------------------------------------------------+
- COPYRIGHT DISCLAIMER : FOR FULL LICENSE CHECK SOURCE CODE -
This program is created and distributed under the GNU General Public License, Version 2.
By distributing or modifying this program you show your acceptance of the
terms of the GNU Public License Version 2 and all later versions. Not complying
with the terms of this license (after distributing or modifying this program)
is illeagal and terminates any further rights you hold under this license.
ServStart version 25 (build 688), Copyright (C) 2018 @cosmicatech.
This version of ServStart comes with ABSOLUTELY NO WARRANTY; for details check license.txt
This is free software, and you are welcome to redistribute it under certain conditions. 

    """

    print(startart)

    # Check if the program is running in Python 3.X
    if int(sys.version.split()[0][0])<3:
        print("You are running this in Python " + sys.version.split()[0] + ". Please upgrade to Python 3.5 or newer.")
        input("Press Enter to quit.")
        exit("Incompatible Python Version!")

    print("Running on Python " + sys.version.split()[0])

    # --- Obsolete way that prevents server killing --- #
    #    jobs = []
    #    for i in range(5): #NUMBER OF SERVERS
    #        p = multiprocessing.Process(target=main, args=(i+50000,))
    #        jobs.append(p)
    #        print("New servers: ")
    #        for i in jobs:
    #            print(str(i))
    #        wreturn = p.start()
    #####################################################

    # ------ New way that allows server killing ------- #
    try:
        numberOfServers = int(input("Number of servers to start: "))
    except KeyboardInterrupt:
        print("Exiting program...")
        exit("KeyboardInterrupt")
    except:
        numberOfServers = 5 # Number of servers if the input fails
    #s1 = multiprocessing.Process(target=server, args=(50001,)) # used with only 5 servers, obsolete
    #s2 = multiprocessing.Process(target=server, args=(50002,)) # used with only 5 servers, obsolete
    #s3 = multiprocessing.Process(target=server, args=(50003,)) # used with only 5 servers, obsolete
    #s4 = multiprocessing.Process(target=server, args=(50004,)) # used with only 5 servers, obsolete
    #s5 = multiprocessing.Process(target=server, args=(50005,)) # used with only 5 servers, obsolete
    print("-------- Initialising with " + str(numberOfServers) + " servers --------")
    processes = []
    for i in range(numberOfServers):
        processes.append(multiprocessing.Process(name="Server on port: " + str(i+50000), target=server, args=(i+50000,))) # Create a server process and append it
    for i in processes:
        i.start() # start the server process
        print("STARTED: " + str(i))
    time.sleep(0.15*numberOfServers) # Allows some time so the servers can print their outputs
    while True:
        try:
            action = input("Input a command/action: ") # action input

            # MAIN IF SEQUENCE
            # Add new commands below
            if action == "killall": # Kill All servers action
                try:
                    for i in processes:
                        i.terminate() # Terminate the server
                        print(str(i.name) + " has been terminated. Connection aborted.")
                    processes = [] # Clear the processes list
                    numberOfServers = 0 # Make numberOfServers = 0, this prevents some issues in the rest of the program like the 'new' command
                except Exception as e:
                    print("Couldn't terminate some servers: " + str(e)) # This might be because there are none to terminate, it doesn't mean there is a fatal error.

            elif action == "exit": # Exit action
                try:
                    for i in processes: # Terminate all process to clean up nicely
                        i.terminate()
                        print(str(i) + " has been terminated. Connection aborted.")
                except Exception as e:
                    print("Couldn't terminate some servers: " + str(e)) # See above about this error
                return 0

            elif "new " in action: # New server action, not perfected! TODO
                try:
                    print("--- NOTE: If you get a OSError: [WinError 10048] Exception, run 'killall' before 'new' ---")
                    try:
                        newNumberOfServers = int(action.split('new ')[1]) # get the number of new servers to start
                        for i in range(newNumberOfServers):
                            processes.append(multiprocessing.Process(name="Server on port: " + str(i+50000+numberOfServers), target=server, args=(i+numberOfServers+50000,)))
                        for i in processes[numberOfServers:]:
                            i.start()
                            print("STARTED: " + str(i))
                        numberOfServers = numberOfServers+newNumberOfServers # to stop errors in the rest of the program
                    except Exception as e:
                        print("Error while creating new servers, " + str(e) + ". Proper usage: 'new [numberOfServers]'")
                    time.sleep(0.10*newNumberOfServers)
                except OSError:
                    print("An error occurred (OSError). Try running 'killall' before 'new'.")
                except Exception as e:
                    print("An error occurred (" + str(e) + "). ")

            elif action == "test": # put test code here
                try:
                    for i in processes:
                        i.stop()
                except Exception as e: # required, otherwise leads to a unresponsive state
                    print("Test failed, terminating servers. ERROR: " + str(e))
                    try:
                        for i in processes:
                            i.terminate()
                            print(str(i) + " has been terminated. Connection aborted.")
                    except Exception as e:
                        print("Couldn't terminate some servers: " + str(e))

            elif action == "hang":
                try:
                    for i in processes:
                        i.terminate()
                        print(str(i.name) + " has been terminated. Connection aborted.")
                except Exception as e:
                    print("Couldn't terminate some servers: " + str(e))
                print("\nCreating hanging process...")
                hangprocess = multiprocessing.Process(name="hanger", target=hang)
                print("Starting process...")
                hangprocess.start()
                print("Ending user interface...")
                print("---- Program now in unresponsive state ---")
                return 1

            elif "kill " in action: # KILL command, to kill a certain number of servers
                try:
                    killNum = int(action.split('kill ')[1])
                    numberOfServers = numberOfServers - killNum
                    killed = []
                    for i in processes[:killNum]:
                        i.terminate()
                        print(str(i) + " has been terminated. Connection aborted.")
                        killed.append(i)
                    for i in killed:
                        processes.remove(i)
                    print(str(killNum) + " processes terminated.")
                except Exception as e:
                    print("Error while killing servers, " + str(e) + ". Proper usage: 'kill [numberOfServers]'")

            elif "list" in action:
                try:
                    listNum = int(action.split('list ')[1])
                    print("Listing first " + str(listNum) + " processes...")
                    for i in range(listNum):
                        print(str(processes[i]))
                except Exception as e:
                    print("Listing all processes...")
                    for i in processes:
                        print(str(i))

            elif "eval" in action: # EVAL command.
                print("SERVER CONSOLE")
                while True:
                    try:
                        ein = input(">>> ")
                        if ein == "exit()":
                            break
                        elif ein == "quit()":
                            break
                        elif "server(" in ein:
                            print("")
                        else:
                            eval(ein)
                    except Exception as e:
                        print(str(e))
            else:
                print("'" + action + "' is not a valid command.")

        except KeyboardInterrupt: # This is important, it prevents being 'stuck' in the program a lot of the time
            print("\n-----------------------\nKeyboard interruption, closing all servers and processes...")
            try:
                for i in processes:
                    i.terminate()
                    print(str(i) + " has been terminated. Connection aborted.")
            except Exception as e:
                print("Couldn't terminate some servers: " + str(e))
            processes = []
            exit()
        except Exception as e:
            print("An error occurred (" + str(e) + "), closing all servers and processes...")
            try:
                for i in processes:
                    i.terminate()
                    print(str(i) + " has been terminated. Connection aborted.")
            except Exception as e:
                print("Couldn't terminate some servers: " + str(e))
            exit()
    print("---- Program in unresponsive state ---")
    print("There was an unknown error and this program is now in an unresponsive state.")
    print("In case this happens again you can open a command prompt and type 'taskkill /im python.exe'.")
    print("To free up now unnessecary memory, all servers are now being terminated...")
    try:
        for i in processes:
            i.terminate()
            print(str(i.name) + " has been terminated. Connection aborted.")
    except Exception as e:
        print("Couldn't terminate some servers: " + str(e))
    print("Restarting program...")
	return("unresponsive")

# Some function that was used before to reconnect a socket (s), but is now obsolete.
def reconnect(s):
    global conn
    global addr
    s.listen(1)
    conn, addr = s.accept()
    print('Connected by', addr)
    msg = "Confirm connection by " + str(addr)
    conn.sendall(msg.encode('utf-8'))

def hang(): # for testing
    while True:
        hangVar = True

# Server function, I should probably use a class for this
# Literally just an echo server, but it is easy to modify the code for it to make it something else.
# To modify the function edit the code around lines 619-661

def server(port):
    import socket
    try:
        HOST = ''# Symbolic name meaning all available interfaces
        PORT = port # The main program passes a port in the 50000-59999 range (or more if there are >10000 servers)
        portmsg = "Port " + str(PORT) + ": " # Just for convienience, because there are ~4 places in this function that use the same message
        print("New server, running on port: " + str(PORT))
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((HOST, PORT))
            s.listen(1)
            conn, addr = s.accept()
            with conn:
                print(portmsg + 'Connected by', addr)
                msg = portmsg + "Confirm connection by " + str(addr)
                conn.sendall(msg.encode('utf-8'))
                while True:
                    try:
                        data = conn.recv(1024)
                        if data.decode('utf-8') == "\x03":
                            msg = """\
                            -----------------------------\n
                            Closing socket connection...\n
                            -----------------------------\n
                            """
                            conn.sendall(msg.encode('utf-8'))
                            s.close()
                            print(portmsg + "Connection was closed by " + str(addr[0]) + " on port " + str(addr[1]) + ".")
                            return("Connection was closed by " + str(addr[0]) + " on port " + str(addr[1]) + ".")
                        if data.decode('utf-8') == "kill-110205":
                            msg = """\
                            ------------------------------\n
                            Confirm Killcode Authorisation\n
                             Closing socket connection...\n
                            ------------------------------\n
                            """
                            conn.sendall(msg.encode('utf-8'))
                            s.close()
                            print(portmsg + "Recieved killcode from " + str(addr[0]) + " on port " + str(addr[1]) + ".")
                            return "authkill"
                        print(portmsg + "Received: " + str(data))
                        datamodt = "Received: " + data.decode('utf-8') # RESPONSE MESSAGE
                        datamod = datamodt.encode('utf-8')
                        conn.sendall(datamod)
                    except ConnectionAbortedError:
                        print(portmsg + "Connection was closed by " + str(addr[0]) + " on port " + str(addr[1]) + "!\n")
                        s.listen(1)
                        conn, addr = s.accept()
                        print(portmsg + 'Connected by', addr)
                        msg = "Confirm connection by " + str(addr)
                        conn.sendall(msg.encode('utf-8'))
                        pass
                    except KeyboardInterrupt:
                        conn.sendall("Server shutting down: manual abort.".encode('utf-8'))
                        exit(portmsg + "MANUAL ABORT")
    except Exception as e:
        print("Server on port " + str(PORT) + " encountered an error: " + str(e) + ".")
        pass

# if-main loop, most of you will know what this does.
# Basically, if the program is not imported it runs the main() function.
if __name__ == '__main__':
	while True:
    	main()
