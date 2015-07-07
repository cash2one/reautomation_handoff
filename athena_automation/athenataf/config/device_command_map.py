class CommandMap:
	'''
	This class will be used by the devicehandler.py to pick the commands to be executed.
	'''
	
	
	IAP_COMMON = {
						"GET_DEVICE_STATUS" : "show ap debug athena",
						 "GET_RUN_CONFIG" : "show running-config",
							"PULL_DEVICE_UP" : "debug_athena_server "
				}
				
	SWITCH_COMMON = {
						"GET_DEVICE_STATUS" : "show ap debug athena",
						 "GET_RUN_CONFIG" : "show running-config",
							"PULL_DEVICE_UP" : "debug aruba-central connection ip ",
                            "NO_PAGE" : "no paging"
				}
				
	IAP = {
				'4.0.0.8'  : {
							"GET_DEVICE_STATUS" : "show ap debug cloud-server",	
						 "GET_RUN_CONFIG" : "show running-config"							
							},
							
				4.1	: {
						"GET_DEVICE_STATUS" : "show ap debug cloud-server",
						 "GET_RUN_CONFIG" : "show running-config",
						 "PULL_DEVICE_UP" : "debug-cloud-server "
							},
							
							
				4.0	: {
						"GET_DEVICE_STATUS" : "show ap debug athena",
						 "GET_RUN_CONFIG" : "show running-config",
						 "PULL_DEVICE_UP" : "debug-athena-server ",
						 "show_summary" : "show summary | i Allow",
						 "AP_ENV" : "show ap-env",
							"show_ids_detection_config" : "show ids-detection config",
							"show_radio_config" : "show radio config",
							"show_ids_protection_config" : "show ids-protection config",
							"show_arm_config" : "show arm config",
							"show_ip_interface_brief": "show ip interface brief"
				 },
                '4.1.2.1'	: {
						"GET_DEVICE_STATUS" : "show ap debug cloud-server",
						 "GET_RUN_CONFIG" : "show running-config",
						 "PULL_DEVICE_UP" : "debug-cloud-server ",
						 "show_summary" : "show summary | i Allow",
                        "show_summary_Band" : "show summary | i Band",
						 "AP_ENV" : "show ap-env",
							"show_ids_detection_config" : "show ids-detection config",
							"show_radio_config" : "show radio config",
							"show_ids_protection_config" : "show ids-protection config",
							"show_arm_config" : "show arm config",
							"show_ip_interface_brief": "show ip interface brief",
                            "show_summary_extended_ssid": "show summary | i Extended"
				 },
				 '4.1.2.2'	: {
						"GET_DEVICE_STATUS" : "show ap debug cloud-server",
						 "GET_RUN_CONFIG" : "show running-config",
						 "PULL_DEVICE_UP" : "debug-cloud-server ",
						 "show_summary" : "show summary | i Allow",
                        "show_summary_Band" : "show summary | i Band",
						 "AP_ENV" : "show ap-env",
							"show_ids_detection_config" : "show ids-detection config",
							"show_radio_config" : "show radio config",
							"show_ids_protection_config" : "show ids-protection config",
							"show_arm_config" : "show arm config",
							"show_ip_interface_brief": "show ip interface brief",
                            "show_summary_extended_ssid": "show summary | i Extended"
				 },
				 '4.1.1.6'	: {
						"GET_DEVICE_STATUS" : "show ap debug cloud-server",
						 "GET_RUN_CONFIG" : "show running-config",
						 "PULL_DEVICE_UP" : "debug-cloud-server ",
						 "show_summary" : "show summary | i Allow",
                        "show_summary_Band" : "show summary | i Band",
						 "AP_ENV" : "show ap-env",
							"show_ids_detection_config" : "show ids-detection config",
							"show_radio_config" : "show radio config",
							"show_ids_protection_config" : "show ids-protection config",
							"show_arm_config" : "show arm config",
							"show_ip_interface_brief": "show ip interface brief",
                            "show_summary_extended_ssid": "show summary | i Extended"
				 },
                '4.1.2.3'	: {
						"GET_DEVICE_STATUS" : "show ap debug cloud-server",
						 "GET_RUN_CONFIG" : "show running-config",
						 "PULL_DEVICE_UP" : "debug-cloud-server ",
						 "show_summary" : "show summary | i Allow",
                        "show_summary_Band" : "show summary | i Band",
						 "AP_ENV" : "show ap-env",
							"show_ids_detection_config" : "show ids-detection config",
							"show_radio_config" : "show radio config",
							"show_ids_protection_config" : "show ids-protection config",
							"show_arm_config" : "show arm config",
							"show_ip_interface_brief": "show ip interface brief",
                            "show_summary_extended_ssid": "show summary | i Extended"
				 }
			}

	SWITCH = {
				4.0  : {
							"GET_DEVICE_STATUS" : "show aruba-central",	
							"GET_RUN_CONFIG" : "show running-config",
							"show_vlan" : "show vlan",
							"show_dhcp" : "show ip dhcp database",
                            "show_poe" : "show poe interface brief",
                            "show_port" : "show port status",
                            "show_run_vlan_nat" : "show running-config interface vlan 3",
                            "show_run_vlan_mulvlan" : "show running-config interface vlan 2-7",
                            "show_dom" : "show ip domain-name",
							"show_switchinfo" : "show switchinfo",
							"show_run" : "show run"
							}

			}