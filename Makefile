JASMINC?= jasminc
JFLAGS?=
CC?=cc

OBJ:=src/asm/alzette.o

.SUFFIXES: .s .jazz .o .so 
.PRECIOUS: asm/%.s

all: shared/alzette.so shared/crax.so shared/esch.so shared/schwaemm.so shared/sparkle.so shared/sparkle_suite.so clean

libs: alzette.so

src/alzette.s: src/alzette.jazz
	mkdir -p shared
	mkdir -p src/asm/
	$(JASMINC) $(JFLAGS) -o $@ $<

src/asm/alzette.o: src/alzette.s
	$(CC) -o $@ -c $<

shared/alzette.so: $(OBJ)
	$(CC) -shared -o $@ $^

src/crax.s: src/crax.jazz
	mkdir -p shared
	mkdir -p src/asm/
	$(JASMINC) $(JFLAGS) -o $@ $<

src/asm/crax.o: src/crax.s
	$(CC) -o $@ -c $<

shared/crax.so: $(OBJ)
	$(CC) -shared -o $@ $^

src/esch.s: src/esch.jazz
	mkdir -p shared
	mkdir -p src/asm/
	$(JASMINC) $(JFLAGS) -o $@ $<

src/asm/esch.o: src/esch.s
	$(CC) -o $@ -c $<

shared/esch.so: $(OBJ)
	$(CC) -shared -o $@ $^

src/schwaemm.s: src/schwaemm.jazz
	mkdir -p shared
	mkdir -p src/asm/
	$(JASMINC) $(JFLAGS) -o $@ $<

src/asm/schwaemm.o: src/schwaemm.s
	$(CC) -o $@ -c $<

shared/schwaemm.so: $(OBJ)
	$(CC) -shared -o $@ $^

src/sparkle.s: src/sparkle.jazz
	mkdir -p shared
	mkdir -p src/asm/
	$(JASMINC) $(JFLAGS) -o $@ $<

src/asm/sparkle.o: src/sparkle.s
	$(CC) -o $@ -c $<

shared/sparkle.so: $(OBJ)
	$(CC) -shared -o $@ $^

src/sparkle_suite.s: src/sparkle_suite.jazz
	mkdir -p shared
	mkdir -p src/asm/
	$(JASMINC) $(JFLAGS) -o $@ $<

src/asm/sparkle_suite.o: src/sparkle_suite.s
	$(CC) -o $@ -c $<

shared/sparkle_suite.so: $(OBJ)
	$(CC) -shared -o $@ $^

clean:
	$(RM) -r src/asm/
	$(RM) src/alzette.s
	$(RM) src/crax.s
	$(RM) src/esch.s
	$(RM) src/schwaemm.s

distclean: clean
	$(RM) test_ocaml test_rust run.*
