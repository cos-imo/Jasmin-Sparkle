JASMINC?= jasminc
JFLAGS?=
CC?=cc

OBJ:=asm/sparkle.o asm/schwaemm.o

.SUFFIXES: .c .s .jazz .o .so .a
.PRECIOUS: asm/%.s

all: esch 

esch.s: submodules/functions/esch.jazz
	mkdir -p asm/
	$(JASMINC) $(JFLAGS) -I functions:submodules/functions -I utils:submodules/utils -o $@ $<

asm/esch.o: esch.s
	$(CC) -o $@ -c $<

esch.so: asm/esch.so
	$(CC) -shared -o $@ $^ -v

clean:
	$(RM) -r asm/
	$(RM) esch.s
