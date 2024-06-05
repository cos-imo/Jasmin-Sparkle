JASMINC ?= jasminc

all: run
	./run

alzette.s: alzette.jazz
	$(JASMINC) -o $@ $<

run: alzette.c alzette.s
	$(CC) -O2 -o $@ $^

clean:
	rm -f run alzette.s
