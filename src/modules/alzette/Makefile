JASMINC?= jasminc
JFLAGS?=
CC?=cc

OBJ:=asm/alzette.o

.SUFFIXES: .c .s .jazz .o .so .a
.PRECIOUS: asm/%.s
.PHONY: run_aes128

libs: alzette.so

alzette.s: alzette.jazz
	mkdir -p asm/
	$(JASMINC) $(JFLAGS) -o $@ $<

asm/alzette.o: alzette.s
	$(CC) -o $@ -c $<

alzette.so: $(OBJ)
	$(CC) -shared -o $@ $^

clean:
	$(RM) -r asm/
	$(RM) alzette.s

distclean: clean
	$(RM) test_ocaml test_rust run.*
