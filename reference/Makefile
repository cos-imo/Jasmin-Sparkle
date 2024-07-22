all: build build/sparkle_reference.so build/schwaemm_reference.so # build/esch_reference.so crax_reference

build:
	mkdir -p $@

build/sparkle_reference.so: sparkle_src/sparkle.c sparkle_src/sparkle.h
	$(CC) -Iinclude -shared sparkle_src/sparkle.c -o $@

build/schwaemm_reference.so: schwaemm/src/sparkle.c schwaemm/src/schwaemm.c
	$(CC) -Iinclude -shared schwaemm/src/sparkle.c schwaemm/src/schwaemm.c -o $@

#build/esch_reference.so: esch/src/esch.c esch/src/sparkle.c
#       $(CC) -Iesch/src -fPIC -shared esch/src/esch.c esch/src/sparkle.c -o $@

