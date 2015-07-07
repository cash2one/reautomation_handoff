#========================================================================#
#   Project   	 : Selenium UI Automation                                #
#   Module       : Network Tests  1.0                                    #
# -----------------------------------------------------------------------#
#   Description  : Has configuration utils of ssh 						 #
# -----------------------------------------------------------------------#
#   $Revision	 : release 1.4                                           #
#   $Date		 : 04-10-2013                                            #
#   $Author		 : Srujan Kurapati                                       #
# -----------------------------------------------------------------------#
#   Department   : QA Bangalore                                          #
# ########################################################################
set exp_debug 1
package require Expect
namespace eval TCL_UTILS {
	exp_match_max -d 50000
}

proc Validate_IP {ip_address} {  
  #Checking IP address
  if { [regexp {[a-zA-z]+} $ip_address] } {
  return 0
  } 
  set ip_add_list [split $ip_address "."]
  if { [ llength $ip_add_list] !=4 } {
	return -1 
 }
  foreach element $ip_add_list {
    if {$element >255 || $element<0} {
      return -1
    }
  }
  
  if { $ip_address=="0.0.0.0"} {
		return -1
	}
  
  return 0
}


proc SSHLogin {ip_address login password protocol outssh_id {wait_time 20} {port 22}} {
    global spawn_id
    global tcl_platform
	global timeout 
    set expect_out(buffer) "NONE"
    set timeout $wait_time
    upvar $outssh_id id
	set prompt "(%|#|>|:~\\$|\\$)"
    log_user 1
    if {$tcl_platform(platform) == "unix"} {
			spawn ssh $ip_address -p $port -l $login
			expect {
			  timeout {
				 puts "-1 Unable to get the prompt"
				 return -1
			  }
			  -regexp ".*\\? " { 
				 send -- "yes\r"
			  }
			  -regexp "password: " {
				 send -- "$password\r"
			  }
			}
			expect -regexp ".*$prompt "
			set buffer $expect_out(buffer)
			if {[regexp {Permission denied} $buffer]} {
			  puts "-1 Permission Denied: check the password"
			  return -1
			}
			 set timeout 5
			send -- "\r"
			expect -regexp ".*$prompt "
			set id $spawn_id
 
    } else {
			puts "afdasdfsdf"
			if {$protocol == "telnet"} {
				puts "Connecting through telnet\r"
				exp_spawn plink -telnet  -l $login -P $port $ip_address
			} else {
				puts "Connecting through ssh.....\r"
				spawn plink -ssh $ip_address -l $login -P $port
			}
			after 15
			expect {
				-regexp ".*Login : " {
					 exp_send -- "$login\r"
					expect {
						 -regexp ".*Passport 32 Password : " {
						exp_send -- "$password\r"
					}
					}
				}
				-regexp -nocase "*password:" {
					exp_send -- "$password\r"
				}				
				-regexp "FATAL ERROR" {
				puts "-1 Unable to Establish the connection: check ip address"
				return -1
				}
				-regexp ".*\\) " {
					 send -- "y\r"
				}
				-regexp ".*password: " {
					send -- "$password\r"
				}
				
				-regexp ".*$prompt " {
					set id $spawn_id
					return 0
				}
				-regexp ".*Passport 32 Password : " {
					exp_send -- "$password\r"
				}
				timeout {
					puts "-1 Unable to get the prompt"
					return -1
				}				
				
			}
			
		# expect {
				
				# timeout {
			# puts "asdlsadklfhksdahf"
			# return -1
			# }
		# }
		expect {
			
			-regexp ".*$prompt " {
			 set timeout 5
			 send -- "\r"
			 set timeout 5
			}
			timeout {
			puts "-2 Unable to get the prompt"
			return -1
			}
			-regexp "Access denied" {
			puts "\n -1 Access Denied: check the password"
			return -1
			}
	  
		}
		expect -regexp ".*$prompt "
		set id $spawn_id
    }
	return 0
}

proc SSHSendCmd {outssh_id command cmd_output {wait_time 10}} {
		puts $outssh_id
  global spawn_id
  global tcl_platform
  # Output variable
  upvar $cmd_output out
  set prompt "(%|#|>|\\$|:~\\$)"
  set spawn_id $outssh_id
  set expect_out(buffer) ""

  global timeout 
  
  set timeout $wait_time
  puts "\r--------------\r"
  puts $command
  after 1000
  send -- $command
  after 8000
  expect -regexp ".*$prompt "
  after 200
  set buffer $expect_out(buffer)
  set timeout 5
  send -- "\r"
  after 200
  expect -regexp ".*$prompt "
  set out $buffer
  return 0
}

proc SSHLogout {outssh_id {wait_time 10}} {

  global spawn_id
  global tcl_platform
  global timeout 
  set prompt "(%|#|>|\\$|:~\\$)"
  set spawn_id $outssh_id
  # Logging out from the FTP session
  set timeout 5 
  send -- "\r"
  expect -regexp ".*$prompt "
  set timeout $wait_time
  send -- "exit\r"
  catch {
	  expect -regexp ".*$prompt "
	  send -- "exit\r"
  } out
  return 0

}

 array set OPTS {
    host    ""
    user    ""
    passwd  ""
	command ""
}
set i 0
foreach arg $::argv {
global OPTS
switch -exact -- $i {
		0     { set OPTS(host)        $arg }
        1     { set OPTS(user)        $arg }
        2     { set OPTS(passwd)      $arg }
        3     { set OPTS(command)      $arg }
        4     { set OPTS(protocol)      $arg }
        5     { set OPTS(port)      $arg }
		}
		incr i
		}
SSHLogin  $OPTS(host) $OPTS(user) $OPTS(passwd) $OPTS(protocol)  outssh_id 20 $OPTS(port)
SSHSendCmd $outssh_id $OPTS(command) cmd_output
puts "\r--------------\r"
# SSHLogout $outssh_id