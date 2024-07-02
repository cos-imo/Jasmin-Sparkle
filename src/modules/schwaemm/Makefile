JASMINC?= jasminc
JFLAGS?=
CC?=cc

OBJ:=asm/sparkle.o asm/schwaemm.o

.SUFFIXES: .c .s .jazz .o .so .a
.PRECIOUS: asm/%.s

all: sparkle sparkle_all schwaemm

schwaemm: schwaemm.so 

sparkle: sparkle_jasmin.so

sparkle_all: sparkle7_jasmin.so sparkle11_jasmin.so 

# Sparkle
## Sparkle 7

sparkle7.s: submodules/functions/sparkle7.jazz
	mkdir -p asm/
	$(JASMINC) $(JFLAGS) -I functions:submodules/functions -I utils:submodules/utils -o $@ $<

asm/sparkle7.o: sparkle7.s
	$(CC) -o $@ -c $<

sparkle7_jasmin.so: asm/sparkle7.o
	$(CC) -shared -o $@ $^

## Sparkle11 

sparkle11.s: submodules/functions/sparkle384_11.jazz submodules/functions/sparkle11.jazz
	mkdir -p asm/
	$(JASMINC) $(JFLAGS) -I functions:submodules/functions -I utils:submodules/utils -o $@ $<

asm/sparkle11.o: sparkle11.s
	$(CC) -o $@ -c $<

sparkle11_jasmin.so: asm/sparkle11.o
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
	$(RM) sparkle.s sparkle7.s sparkle11.s
	$(RM) schwaemm.s
