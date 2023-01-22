EXEC = ytdp

all: transform

transform:
	cp ytd.py $(EXEC)
	@# Set the shebang python at the top of the file (hardcoded /bin/python, make sure exists)
	sed -i "1 i\#\!/bin/python" $(EXEC)
	chmod u+x $(EXEC)

clean:
	-rm $(EXEC)
