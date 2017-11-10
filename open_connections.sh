#Script to automate the log capruting and forwarding

clear

linkHash=( "http://www.google.com"
	"http://www.thegeekstuff.com/2010/03/netstat-command-examples/"
	"http://youtube.com"
	"http://answers.splunk.com/answers/115127/error-while-validating-databases.html"
	"http://stackoverflow.com/questions/20796557/shell-script-about-insert-value-to-array"
	"http://www.netflix.com"
	"http://www.yahoo.com"
	"http://techcrunch.com/"
	"http://www.mactricksandtips.com/2012/01/generate-random-numbers-in-terminalbash.html"
	"http://www.staff.science.uu.nl/~oostr102/docs/nawk/nawk_101.html#SEC104"
	"http://answers.splunk.com/answers/9035/can-i-run-splunk-on-btrfs.html"
	"http://www.computerhope.com/unix/nc.htm"
	"http://docs.splunk.com/Documentation/Splunk/6.2.3/Data/Listofpretrainedsourcetypes"
	"https://linuxacademy.com/blog/linux/netstat-network-analysis-and-troubleshooting-explained/"
	"http://askubuntu.com/questions/175743/how-to-make-a-bash-script-generate-a-new-filename-every-time-its-run" );

hashLen=${#linkHash[@]}

for var in 0 1 2
do
	randNum=$[RANDOM % $hashLen]
	#echo "Opening Link at Index: $randNum"
	#open -a safari ${linkHash[randNum]}
done


#Generate a random number for the number of UDP connections that we want to open
udpConnCount=$[RANDOM%20]
#Array of IP addresses to which the script will open UDP connections
udpConnIP=( 172.70.55.68 171.68.249.161 )
pids=()
localPort=4000
destPort=30000

for var in $(seq 1 $udpConnCount)
do
	#Generate a random index for upConnIP array
	destIPIdx=$[RANDOM%2]
	#Open a UDP connection in the background using nc command
	nc -p $localPort -u ${udpConnIP[destIPIdx]} $destPort &
	procID=$!
	#echo "Adding procID = $procID to pids array.."
	pids+=($procID)
	pids+=" "
	echo "opened udp connection to IP addr: ${udpConnIP[destIPIdx]} on local port = $localPort and destination port = $destPort"
	localPort=$((localPort+1))
	destPort=$((destPort+1))
done

#echo ${pids[*]}

#Get Netstat here...
filename="/Users/sansshar/Desktop/forwarder_logs/netstat$(date "+%m%d%H%M%Y%S").log"
echo "FileName --> $filename;"
netstat -a | awk '{if ($6=="Foreign") {print $1,",",$2,",",$3,",Local_Addr",",Foreign_Addr",",State"} if(match($1,/tcp/)||match($1,/udp/)) {print $1,",",$2,",",$3,",",$4,",",$5,",",$6}}' >> $filename

#Close all UDP connections
#for i in $(seq 0 ${#pids[@]})
for pid in ${pids[@]}
do
	kill $pid
	echo "Killed Process: $pid. Return Val = $?"
done

echo "END..!!!"