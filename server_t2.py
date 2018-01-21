##############################################################
#         MULIPROCESSING AND SOCKETS EXAMPLE PROGRAM         #
#   MADE BY @COSMICATECH // HTTPS://GITHUB.COM/COSMICATECH   #
#             Copyright (c) 2017 @COSMICATECH                #
##############################################################

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

# Note 2: Some comments are unusually long and may look bad in other text editors. They line up in the IDE I use,
# however (Atom). I also highly recommend using Atom, even though (disclaimer!) I am not affiliated with the company in any way.

# Note 3: Some obsolete code is included for convienience.

################################################# LICENSE ##################################################
# Also in license.txt
license = '''
		    GNU GENERAL PUBLIC LICENSE
		       Version 2, June 1991

 Copyright (C) 1989, 1991 Free Software Foundation, Inc.
 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA

 Everyone is permitted to copy and distribute verbatim copies
 of this license document, but changing it is not allowed.

			    Preamble

  The licenses for most software are designed to take away your
freedom to share and change it.  By contrast, the GNU General Public
License is intended to guarantee your freedom to share and change free
software--to make sure the software is free for all its users.  This
General Public License applies to most of the Free Software
Foundation's software and to any other program whose authors commit to
using it.  (Some other Free Software Foundation software is covered by
the GNU Library General Public License instead.)  You can apply it to
your programs, too.

  When we speak of free software, we are referring to freedom, not
price.  Our General Public Licenses are designed to make sure that you
have the freedom to distribute copies of free software (and charge for
this service if you wish), that you receive source code or can get it
if you want it, that you can change the software or use pieces of it
in new free programs; and that you know you can do these things.

  To protect your rights, we need to make restrictions that forbid
anyone to deny you these rights or to ask you to surrender the rights.
These restrictions translate to certain responsibilities for you if you
distribute copies of the software, or if you modify it.

  For example, if you distribute copies of such a program, whether
gratis or for a fee, you must give the recipients all the rights that
you have.  You must make sure that they, too, receive or can get the
source code.  And you must show them these terms so they know their
rights.

  We protect your rights with two steps: (1) copyright the software, and
(2) offer you this license which gives you legal permission to copy,
distribute and/or modify the software.

  Also, for each author's protection and ours, we want to make certain
that everyone understands that there is no warranty for this free
software.  If the software is modified by someone else and passed on, we
want its recipients to know that what they have is not the original, so
that any problems introduced by others will not reflect on the original
authors' reputations.

  Finally, any free program is threatened constantly by software
patents.  We wish to avoid the danger that redistributors of a free
program will individually obtain patent licenses, in effect making the
program proprietary.  To prevent this, we have made it clear that any
patent must be licensed for everyone's free use or not licensed at all.

  The precise terms and conditions for copying, distribution and
modification follow.

		    GNU GENERAL PUBLIC LICENSE
   TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION

  0. This License applies to any program or other work which contains
a notice placed by the copyright holder saying it may be distributed
under the terms of this General Public License.  The "Program", below,
refers to any such program or work, and a "work based on the Program"
means either the Program or any derivative work under copyright law:
that is to say, a work containing the Program or a portion of it,
either verbatim or with modifications and/or translated into another
language.  (Hereinafter, translation is included without limitation in
the term "modification".)  Each licensee is addressed as "you".

Activities other than copying, distribution and modification are not
covered by this License; they are outside its scope.  The act of
running the Program is not restricted, and the output from the Program
is covered only if its contents constitute a work based on the
Program (independent of having been made by running the Program).
Whether that is true depends on what the Program does.

  1. You may copy and distribute verbatim copies of the Program's
source code as you receive it, in any medium, provided that you
conspicuously and appropriately publish on each copy an appropriate
copyright notice and disclaimer of warranty; keep intact all the
notices that refer to this License and to the absence of any warranty;
and give any other recipients of the Program a copy of this License
along with the Program.

You may charge a fee for the physical act of transferring a copy, and
you may at your option offer warranty protection in exchange for a fee.

  2. You may modify your copy or copies of the Program or any portion
of it, thus forming a work based on the Program, and copy and
distribute such modifications or work under the terms of Section 1
above, provided that you also meet all of these conditions:

    a) You must cause the modified files to carry prominent notices
    stating that you changed the files and the date of any change.

    b) You must cause any work that you distribute or publish, that in
    whole or in part contains or is derived from the Program or any
    part thereof, to be licensed as a whole at no charge to all third
    parties under the terms of this License.

    c) If the modified program normally reads commands interactively
    when run, you must cause it, when started running for such
    interactive use in the most ordinary way, to print or display an
    announcement including an appropriate copyright notice and a
    notice that there is no warranty (or else, saying that you provide
    a warranty) and that users may redistribute the program under
    these conditions, and telling the user how to view a copy of this
    License.  (Exception: if the Program itself is interactive but
    does not normally print such an announcement, your work based on
    the Program is not required to print an announcement.)

These requirements apply to the modified work as a whole.  If
identifiable sections of that work are not derived from the Program,
and can be reasonably considered independent and separate works in
themselves, then this License, and its terms, do not apply to those
sections when you distribute them as separate works.  But when you
distribute the same sections as part of a whole which is a work based
on the Program, the distribution of the whole must be on the terms of
this License, whose permissions for other licensees extend to the
entire whole, and thus to each and every part regardless of who wrote it.

Thus, it is not the intent of this section to claim rights or contest
your rights to work written entirely by you; rather, the intent is to
exercise the right to control the distribution of derivative or
collective works based on the Program.

In addition, mere aggregation of another work not based on the Program
with the Program (or with a work based on the Program) on a volume of
a storage or distribution medium does not bring the other work under
the scope of this License.

  3. You may copy and distribute the Program (or a work based on it,
under Section 2) in object code or executable form under the terms of
Sections 1 and 2 above provided that you also do one of the following:

    a) Accompany it with the complete corresponding machine-readable
    source code, which must be distributed under the terms of Sections
    1 and 2 above on a medium customarily used for software interchange; or,

    b) Accompany it with a written offer, valid for at least three
    years, to give any third party, for a charge no more than your
    cost of physically performing source distribution, a complete
    machine-readable copy of the corresponding source code, to be
    distributed under the terms of Sections 1 and 2 above on a medium
    customarily used for software interchange; or,

    c) Accompany it with the information you received as to the offer
    to distribute corresponding source code.  (This alternative is
    allowed only for noncommercial distribution and only if you
    received the program in object code or executable form with such
    an offer, in accord with Subsection b above.)

The source code for a work means the preferred form of the work for
making modifications to it.  For an executable work, complete source
code means all the source code for all modules it contains, plus any
associated interface definition files, plus the scripts used to
control compilation and installation of the executable.  However, as a
special exception, the source code distributed need not include
anything that is normally distributed (in either source or binary
form) with the major components (compiler, kernel, and so on) of the
operating system on which the executable runs, unless that component
itself accompanies the executable.

If distribution of executable or object code is made by offering
access to copy from a designated place, then offering equivalent
access to copy the source code from the same place counts as
distribution of the source code, even though third parties are not
compelled to copy the source along with the object code.

  4. You may not copy, modify, sublicense, or distribute the Program
except as expressly provided under this License.  Any attempt
otherwise to copy, modify, sublicense or distribute the Program is
void, and will automatically terminate your rights under this License.
However, parties who have received copies, or rights, from you under
this License will not have their licenses terminated so long as such
parties remain in full compliance.

  5. You are not required to accept this License, since you have not
signed it.  However, nothing else grants you permission to modify or
distribute the Program or its derivative works.  These actions are
prohibited by law if you do not accept this License.  Therefore, by
modifying or distributing the Program (or any work based on the
Program), you indicate your acceptance of this License to do so, and
all its terms and conditions for copying, distributing or modifying
the Program or works based on it.

  6. Each time you redistribute the Program (or any work based on the
Program), the recipient automatically receives a license from the
original licensor to copy, distribute or modify the Program subject to
these terms and conditions.  You may not impose any further
restrictions on the recipients' exercise of the rights granted herein.
You are not responsible for enforcing compliance by third parties to
this License.

  7. If, as a consequence of a court judgment or allegation of patent
infringement or for any other reason (not limited to patent issues),
conditions are imposed on you (whether by court order, agreement or
otherwise) that contradict the conditions of this License, they do not
excuse you from the conditions of this License.  If you cannot
distribute so as to satisfy simultaneously your obligations under this
License and any other pertinent obligations, then as a consequence you
may not distribute the Program at all.  For example, if a patent
license would not permit royalty-free redistribution of the Program by
all those who receive copies directly or indirectly through you, then
the only way you could satisfy both it and this License would be to
refrain entirely from distribution of the Program.

If any portion of this section is held invalid or unenforceable under
any particular circumstance, the balance of the section is intended to
apply and the section as a whole is intended to apply in other
circumstances.

It is not the purpose of this section to induce you to infringe any
patents or other property right claims or to contest validity of any
such claims; this section has the sole purpose of protecting the
integrity of the free software distribution system, which is
implemented by public license practices.  Many people have made
generous contributions to the wide range of software distributed
through that system in reliance on consistent application of that
system; it is up to the author/donor to decide if he or she is willing
to distribute software through any other system and a licensee cannot
impose that choice.

This section is intended to make thoroughly clear what is believed to
be a consequence of the rest of this License.

  8. If the distribution and/or use of the Program is restricted in
certain countries either by patents or by copyrighted interfaces, the
original copyright holder who places the Program under this License
may add an explicit geographical distribution limitation excluding
those countries, so that distribution is permitted only in or among
countries not thus excluded.  In such case, this License incorporates
the limitation as if written in the body of this License.

  9. The Free Software Foundation may publish revised and/or new versions
of the General Public License from time to time.  Such new versions will
be similar in spirit to the present version, but may differ in detail to
address new problems or concerns.

Each version is given a distinguishing version number.  If the Program
specifies a version number of this License which applies to it and "any
later version", you have the option of following the terms and conditions
either of that version or of any later version published by the Free
Software Foundation.  If the Program does not specify a version number of
this License, you may choose any version ever published by the Free Software
Foundation.

  10. If you wish to incorporate parts of the Program into other free
programs whose distribution conditions are different, write to the author
to ask for permission.  For software which is copyrighted by the Free
Software Foundation, write to the Free Software Foundation; we sometimes
make exceptions for this.  Our decision will be guided by the two goals
of preserving the free status of all derivatives of our free software and
of promoting the sharing and reuse of software generally.

			    NO WARRANTY

  11. BECAUSE THE PROGRAM IS LICENSED FREE OF CHARGE, THERE IS NO WARRANTY
FOR THE PROGRAM, TO THE EXTENT PERMITTED BY APPLICABLE LAW.  EXCEPT WHEN
OTHERWISE STATED IN WRITING THE COPYRIGHT HOLDERS AND/OR OTHER PARTIES
PROVIDE THE PROGRAM "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED
OR IMPLIED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.  THE ENTIRE RISK AS
TO THE QUALITY AND PERFORMANCE OF THE PROGRAM IS WITH YOU.  SHOULD THE
PROGRAM PROVE DEFECTIVE, YOU ASSUME THE COST OF ALL NECESSARY SERVICING,
REPAIR OR CORRECTION.

  12. IN NO EVENT UNLESS REQUIRED BY APPLICABLE LAW OR AGREED TO IN WRITING
WILL ANY COPYRIGHT HOLDER, OR ANY OTHER PARTY WHO MAY MODIFY AND/OR
REDISTRIBUTE THE PROGRAM AS PERMITTED ABOVE, BE LIABLE TO YOU FOR DAMAGES,
INCLUDING ANY GENERAL, SPECIAL, INCIDENTAL OR CONSEQUENTIAL DAMAGES ARISING
OUT OF THE USE OR INABILITY TO USE THE PROGRAM (INCLUDING BUT NOT LIMITED
TO LOSS OF DATA OR DATA BEING RENDERED INACCURATE OR LOSSES SUSTAINED BY
YOU OR THIRD PARTIES OR A FAILURE OF THE PROGRAM TO OPERATE WITH ANY OTHER
PROGRAMS), EVEN IF SUCH HOLDER OR OTHER PARTY HAS BEEN ADVISED OF THE
POSSIBILITY OF SUCH DAMAGES.

		     END OF TERMS AND CONDITIONS

	    How to Apply These Terms to Your New Programs

  If you develop a new program, and you want it to be of the greatest
possible use to the public, the best way to achieve this is to make it
free software which everyone can redistribute and change under these terms.

  To do so, attach the following notices to the program.  It is safest
to attach them to the start of each source file to most effectively
convey the exclusion of warranty; and each file should have at least
the "copyright" line and a pointer to where the full notice is found.

    <one line to give the program's name and a brief idea of what it does.>
    Copyright (C) <year>  <name of author>

    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program; if not, write to the Free Software
    Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA


Also add information on how to contact you by electronic and paper mail.

If the program is interactive, make it output a short notice like this
when it starts in an interactive mode:

    Gnomovision version 69, Copyright (C) year name of author
    Gnomovision comes with ABSOLUTELY NO WARRANTY; for details type `show w'.
    This is free software, and you are welcome to redistribute it
    under certain conditions; type `show c' for details.

The hypothetical commands `show w' and `show c' should show the appropriate
parts of the General Public License.  Of course, the commands you use may
be called something other than `show w' and `show c'; they could even be
mouse-clicks or menu items--whatever suits your program.

You should also get your employer (if you work as a programmer) or your
school, if any, to sign a "copyright disclaimer" for the program, if
necessary.  Here is a sample; alter the names:

  Yoyodyne, Inc., hereby disclaims all copyright interest in the program
  `Gnomovision' (which makes passes at compilers) written by James Hacker.

  <signature of Ty Coon>, 1 April 1989
  Ty Coon, President of Vice

This General Public License does not permit incorporating your program into
proprietary programs.  If your program is a subroutine library, you may
consider it more useful to permit linking proprietary applications with the
library.  If this is what you want to do, use the GNU Library General
Public License instead of this License.
'''

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
|   MADE BY @COSMICATECH // HTTPS://GITHUB.COM/COSMICATECH   |
+------------------------------------------------------------+
COPYRIGHT DISCLAIMER : FOR FULL LICENSE CHECK SOURCE CODE OR TYPE 'license'
This program is created and distributed under the GNU General Public License, Version 2.

By distributing or modifying this program you show your acceptance of the
terms of the GNU Public License Version 2 and all later versions. Not complying
with the terms of this license (after distributing or modifying this program)
is illeagal and terminates any further rights you hold under this license.

ServStart version 25 (build 688), Copyright (C) 2018 @cosmicatech.
This version of ServStart comes with ABSOLUTELY NO WARRANTY; for details type 'license'. 
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
            elif "license" in action:
                print(license)
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
