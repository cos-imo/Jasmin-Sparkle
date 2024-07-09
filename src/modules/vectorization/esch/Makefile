JASMINC?= jasminc
JFLAGS?=
CC?=cc

OBJ:=asm/sparkle.o asm/schwaemm.o

.SUFFIXES: .c .s .jazz .o .so .a
.PRECIOUS: asm/%.s

all: esch.so esch_reference.so sparkle_reference.so 

esch.s: functions/esch.jazz
	mkdir -p asm/
	$(JASMINC) $(JFLAGS) -I functions:functions -I sparkle:../sparkle -I alzette:../alzette -o $@ $<

asm/esch.o: esch.s
	$(CC) -o $@ -c $< 

esch.so: asm/esch.o
	$(CC) -shared -o $@ $^ 

asm/esch_reference.o: reference/esch.c reference/esch.h
	$(CC) -o $@ -c $<

asm/sparkle.o: reference/sparkle.c reference/esch.h
	$(CC) -o $@ -c $<

esch_reference.so: asm/esch_reference.o sparkle_reference.so 
	$(CC) -shared -Ireference -o $@ $^

asm/sparkle_reference.o: reference/sparkle.c reference/sparkle.h 
	$(CC) -o $@ -c $< -g

sparkle_reference.so: asm/sparkle_reference.o 
	$(CC) -shared -Ireference -o $@ $^

clean:
	$(RM) -r asm/
	$(RM) esch.s
