#! /bin/bash

source=`find ./../pyproj -type f \( -name "*.py" \)  -print0 | xargs -0 cat |grep -v -e ^// -e ^$ -e "^[ ]\*" -e "$\*"| wc -l`

echo "total lines=$source"