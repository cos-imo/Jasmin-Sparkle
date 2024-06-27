JASMINC?= jasminc
JFLAGS?=
CC?=cc

OBJ:=asm/sparkle.o asm/schwaemm.o

.SUFFIXES: .c .s .jazz .o .so .a
.PRECIOUS: asm/%.s

all: sparkle schwaemm

schwaemm: schwaemm.so 

sparkle: sparkle_jasmin.so

# Sparkle

sparkle.s: submodules/functions/sparkle_export.jazz submodules/functions/sparkle384.jazz
	mkdir -p asm/
	$(JASMINC) $(JFLAGS) -I functions:submodules/functions -I utils:submodules/utils -o $@ $<

asm/sparkle.o: sparkle.s
	$(CC) -o $@ -c $<

sparkle_jasmin.so: asm/sparkle.o
	$(CC) -shared -o $@ $^

# Schwaemm

schwaemm.s: schwaemm.jazz
	mkdir -p asm/
	$(JASMINC) $(JFLAGS) -I functions:submodules/functions -I utils:submodules/utils -o $@ $<

asm/schwaemm.o: schwaemm.s
	$(CC) -o $@ -c $<

schwaemm.so: asm/schwaem.so
	$(CC) -shared -o $@ $^

clean:
	$(RM) -r asm/
	$(RM) sparkle.s
	$(RM) schwaemm.s
