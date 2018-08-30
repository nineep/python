#/bin/sh
CWD=$1
JAR_NAME=$2
CONSOLE_LOG=$3


if [ -z "$CWD" ] 
then
	echo ""
else
	cd $CWD
fi

if [ -z "$JAR_NAME" ]; then
	echo "Jar name is null."
	exit 1
fi

if [ -z "$CONSOLE_LOG" ]; then
	CONSOLE_LOG="/dev/null"
fi

echo "Restarting service process ${JAR_NAME}... "
echo "Logging console to ${CONSOLE_LOG}"

PROCESSES=`ps -ef | grep "java -jar ${JAR_NAME}" | grep -v grep | awk '{print $2}'`

for i in $PROCESSES
do	
	echo "Killing process ${i}..."
	kill -9 $i
	while ps -p $i > /dev/null
	do
		echo "Waiting process to die..."
		sleep 1
	done	
done

echo "Starting new process..."
nohup java -jar $JAR_NAME -Xmx512m -Xms128m -server >$CONSOLE_LOG 2>&1 &

echo "Service started."
