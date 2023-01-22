EXEC = ytdp
# HARDCODED (change if needed):
USR_BIN = /usr/local/bin/

all: install

transform:
	cp ytd.py $(EXEC)
	@# Set the shebang python at the top of the file (hardcoded /bin/python, make sure exists)
	sed -i "1 i\#\!/bin/python" $(EXEC)
	chmod u+x $(EXEC)

install: transform
	sudo mv $(EXEC) $(USR_BIN)

uninstall:
	-sudo rm $(USR_BIN)$(EXEC)

clean:
	-rm $(EXEC)

