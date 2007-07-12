from pysqlite2 import dbapi2 as sqlite
import time

# Si connette al database se esiste, se non esiste ne crea uno nuovo
# con il nome indicato (nello stesso percorso del sorgente pysql.py)
con = sqlite.connect("../data/archive.db")

# Crea un cursore che segue la connessione
cur = con.cursor()



def getAllProjects():
	cur.execute("SELECT * FROM projects")
	d = []
	for idx in cur:
		d.append(idx)
	return d


def addNewProject(name, worked_mins):
	cur.execute(
		"INSERT INTO projects (name, worked_mins) VALUES (?, ?)",
		(name, worked_mins)
	)
	con.commit()
	cur.execute("SELECT id FROM projects ORDER BY id DESC LIMIT 0, 1")
	last_insert_id = cur.fetchone()[0]
	addLog(last_insert_id, 0)
	return last_insert_id


# The possible operation type values are:
# -1 - project removed
#  0 - project created
#  1 - start working
#  2 - stop working
#
def addLog(project_id, operation_type):
	cur.execute(
		"INSERT INTO logs (project_id, operation_type, time) VALUES (?, ?, ?)",
		(project_id, operation_type, time.time())
	)
	con.commit()
