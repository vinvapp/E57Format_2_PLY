#makefile for project 
#Author: Vincent von Appen
#Variables

OBJ=obj/main.o

Compiler=g++
BaseFlags=-Wall -Wextra 
DebugFlags=-g
CC=${Compiler} ${BaseFlags}
WARNINGS= -Wall -Wextra

test: obj/main.o bin/E57Format_2_PLY
	./bin/E57Format_2_PLY

bin/E57Format_2_PLY: ${OBJ}
	@echo "Building $@"
	${CC} ${WARNINGS} ${OBJ} -o $@

obj/main.o: ./main.cpp
	@echo "Building $@"
	${CC} ${WARNINGS} -c $< -o $@


#submit all files in the repository to the remote 
submit:
	@echo "Everything will be pushed" ; \
	echo "Input the commit message and press [enter]" ; \
	read message ; \
	git add . ; \
	git commit -m "$${message}" ; \
	git push origin ; \
	git log -1	