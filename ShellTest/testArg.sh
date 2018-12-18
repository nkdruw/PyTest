#!/bin/bash

#日志文件存放路径
logfile="./test.log"

#若入参数不为1，提示错误
if [ $# -ne 1 ];then
    echo "$* not 1 arg"
#检查第一个入参是不是非数字
elif [ `echo $1|grep "[^0-9]"` ];then
    echo "$1 not a num"
else
    #若日志文件存在则先删除
    if [ -e $logfile ];then
        rm -f $logfile
    fi
    #循环打印日期，并重定向到日志文件中
    for i in `seq 1 1 $1`
    do
        echo $i | tee -a $logfile
        date "+%Y-%m-%d %H:%M:%S" | tee -a $logfile
    done
fi
