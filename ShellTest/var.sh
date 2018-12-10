#!/bin/bash

var="Paozi"
echo "${var}"

echo ""
echo "只读变量"
readonly var1="tett"
echo "${var1}"

echo "删除变量"
unset var
echo "${var}"

