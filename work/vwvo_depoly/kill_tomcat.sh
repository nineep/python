PROCESSES=`ps -ef | grep 'tomcat' | grep -v grep | grep -v kill_tomcat | awk '{ print $2}'`

for i in $PROCESSES
do
	echo "Killing tomcat process ${i}..."
	kill -9 $i
	while ps -p $i > /dev/null
	do
		echo "Waiting tomcat process to die..."
		sleep 1
	done
done

