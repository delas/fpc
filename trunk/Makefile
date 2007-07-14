INSTALL_PATH = "/usr/share/fpc"
BIN_FILE = "/usr/bin/fpc"
ECHO = "echo"
MKDIR = "mkdir"
RM = "rm"
CP = "cp"
LN = "ln"
CHMOD = "chmod"

general:
	@$(ECHO) "Please use:"
	@$(ECHO) "\tmake install -- install application"
	@$(ECHO) "\tmake uninstall -- uninstall application"

install:
	@$(ECHO) "Starting installation..."
	@$(MKDIR) $(INSTALL_PATH)
	@$(ECHO) $(INSTALL_PATH)/src/fpc.py $(INSTALL_PATH)/src > $(INSTALL_PATH)/fpc
	@$(CHMOD) +x $(INSTALL_PATH)/fpc
	@$(CP) -R . $(INSTALL_PATH)
	@$(LN) -s $(INSTALL_PATH)/fpc $(BIN_FILE)
	@$(ECHO) "Installation complete!"
	@$(ECHO) "Use fpc to start the program!"

uninstall:
	@$(ECHO) "Starting unintalling..."
	@$(RM) -rf $(INSTALL_PATH) $(BIN_FILE)
	@$(ECHO) "FPC completely removed!"
