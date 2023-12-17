BISON_FILE = g
FLEX_FILE = lex
EXECUTABLE = parser

CC = gcc
CFLAGS = -Wall -Wextra -g
LIBS = -ll

all: $(EXECUTABLE)

$(EXECUTABLE): $(BISON_FILE).tab.c $(FLEX_FILE).yy.c
	$(CC) $(CFLAGS) -o $@ $^ $(LIBS)

$(BISON_FILE).tab.c: $(BISON_FILE).y
	bison -d $<

$(FLEX_FILE).yy.c: $(FLEX_FILE).l
	flex $<

$(FLEX_FILE).yy.c: $(BISON_FILE).tab.h

clean:
	rm -f $(EXECUTABLE) $(BISON_FILE).tab.c $(BISON_FILE).tab.h $(FLEX_FILE).yy.c
	rm -rf parser.dSYM/

.PHONY: all clean
