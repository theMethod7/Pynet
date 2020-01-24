#!/bin/bash
#loops through targets
HOSTLIST="HOST1 HOST2 HOST3"
#List of packet sizes to use
SIZELIST="64 128 256 512 1024 1280 1472 3000"

echo -e "IP Address\tPacket Size\t\tRTT\tStandard Deviation" # Header for formatting

for x in $HOSTLIST
do
    for y in $SIZELIST
    do
        RESULT=`supercmd ping -f -c 150 -s $y $x | fgrep rtt | cut -d" " -f4` # Runs ping command with required options and greps
        if [[ "$RESULT" = "" ]] #no result unreachable host
        then
            echo "Failed to reach target: $x" # This will provide Host Address that is not reachable
            break # This will exit the loop
        else
            # Else will get the RTT and the SD from the result
            RTT=`echo $RESULT | cut -d"/" -f2`
            SD=`echo $RESULT | cut -d"/" -f4`
            printf "%10s \t %10s \t %10s \t %10s \n" $x $y $RTT $SD #Print the output in size 10 fields with default alignment
        fi
    done
    echo "------------------------------------------------------------" # Provides a separator for all hosts.
done
