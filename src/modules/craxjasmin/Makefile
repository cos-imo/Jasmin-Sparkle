JASMINC?= jasminc
JFLAGS?=
CC?=cc

OBJ:=asm/crax.o

.SUFFIXES: .c .s .jazz .o .so .a
.PRECIOUS: asm/%.s
.PHONY: run_aes128

libs: crax.so

crax.s: crax.jazz
	mkdir -p asm/
	$(JASMINC) $(JFLAGS) -o $@ $<

asm/crax.o: crax.s
	$(CC) -o $@ -c $<

crax.so: $(OBJ)
	$(CC) -shared -o $@ $^

clean:
	$(RM) -r asm/
	$(RM) crax.s

distclean: clean
	$(RM) test_ocaml test_rust run.*
