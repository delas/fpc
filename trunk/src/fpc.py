import os
import gtk
import gtk.glade
import kernel


class fpc:

	def __init__( self ):

		# Set the Glade file
		self.gladefile = "../data/fpc.glade"
		self.wTree = gtk.glade.XML(self.gladefile, "fpc")

		dic = {
			"on_fpc_destroy":		self.quit
		}

		#Connessione delle calllback
		self.wTree.signal_autoconnect(dic)

		#print kernel.addNewProject("aaa", 0)
		#print kernel.getAllProjects()

		gtk.main()


	def quit( self, *args ):
		print "Exit now..."
		gtk.main_quit()






# Rock'n'roll
_fpc = fpc()
