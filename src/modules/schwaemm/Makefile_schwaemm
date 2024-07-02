JASMINC?= jasminc
JFLAGS?=
CC?=cc

OBJ:=asm/schwaemm.o

.SUFFIXES: .c .s .jazz .o .so .a
.PRECIOUS: asm/%.s

libs: schwaemm.so

schwaemm.s: schwaemm.jazz
	mkdir -p asm/
	$(JASMINC) $(JFLAGS) -I functions:submodules/functions -I utils:submodules/utils -o $@ $<

asm/schwaemm.o: schwaemm.s
	$(CC) -o $@ -c $<

schwaemm.so: $(OBJ)
	$(CC) -shared -o $@ $^

clean:
	$(RM) -r asm/
	$(RM) schwaemm.s
