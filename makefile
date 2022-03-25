#makefile for project 
#Author: Vincent von Appen
#Variables


Compiler=g++
BaseFlags=-Wall -Wextra 
DebugFlags=-g
CC=${Compiler} ${BaseFlags}
WARNINGS= -Wall -Wextra


test: src/ReaderImpl.cpp src/ReaderImpl.h
	@echo "Building $@"
	${CC} ${WARNINGS} -c $< -o $@