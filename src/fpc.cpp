#include <iostream>
#include <libglademm/xml.h>
#include <gtkmm.h>

int main(int argc, char* argv[])
{
    Gtk::Main kit(argc, argv);
    Glib::RefPtr<Gnome::Glade::Xml> refXml = Gnome::Glade::Xml::create("../glade/fpc.glade");
    kit.run();
    return 0;

}
