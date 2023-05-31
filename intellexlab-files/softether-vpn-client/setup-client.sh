# Load the configurations file
source vpn_config

# Wait before executing next step
sleep 2

# Start the SoftEther client
vpnclient start

sleep 2

# Check if the SoftEther client is started properly
vpncmd /TOOLS /CMD check

sleep 2

# Create a virtual network interface to connect to the VPN server
vpncmd /CLIENT localhost /CMD NicCreate $NIC_NAME

sleep 2

# Configure the VPN account info and configs
vpncmd /CLIENT localhost /CMD AccountCreate $ACCOUNT_NAME

sleep 2

# Configure the VPN server password
vpncmd /CLIENT localhost /CMD AccountPassword $ACCOUNT_NAME