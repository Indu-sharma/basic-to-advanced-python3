## Refer to the link for details-> https://telecombigdata.blogspot.in/2018/03/how-to-share-internet-via-linux-box-to.html

if [ $# -ne 3 ] ; then
	echo "Usage : `basename $0` <private nework> <Internet facing interface name> <Private networking facing interface>"
        echo "Example: `basename $0` '10.2.0.0/16' eth1 eth0"
	exit
fi
private_net=$1
internet=$2
private=$3  
echo 1 > /proc/sys/net/ipv4/ip_forward
sudo iptables -A FORWARD -o $internet -i $private -m conntrack --ctstate -NEW -j ACCEPT
sudo iptables -t nat -F POSTROUTING
sudo iptables -t nat -A POSTROUTING -s $private_net -o $internet -j MASQUERADE 
sudo iptables-save | sudo tee /etc/iptables.sav
sudo iptables-restore < /etc/iptables.sav
