#! /usr/bin/env bash
while (true);do
    out=$(~/printfile /tmp/attack.txt)
    if [[ $(echo "$out" | wc -l) == 1 ]];then
        echo $out
	fi
    sleep .001
done
