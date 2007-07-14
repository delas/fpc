from pysqlite2 import dbapi2 as sqlite
import time

# Si connette al database se esiste, se non esiste ne crea uno nuovo
# con il nome indicato (nello stesso percorso del sorgente pysql.py)
con = sqlite.connect("../data/archive.db", isolation_level = None)

# Crea un cursore che segue la connessione
cur = con.cursor()



def getAllProjects():
	cur.execute("SELECT *, (worked_mins/60*fee) AS total FROM projects ORDER BY name ASC")
	d = []
	for idx in cur:
		d.append(idx)
	return d


def getAllLogs():
	cur.execute("SELECT logs.operation_type, logs.time, projects.name FROM logs, projects WHERE logs.project_id=projects.id ORDER BY logs.time DESC")
	d = []
	for idx in cur:
		d.append(idx)
	return d


def addNewProject(name, worked_mins, fee):
	cur.execute(
		"INSERT INTO projects (name, worked_mins, work_start_timestamp, fee) VALUES (?, ?, 0, ?)",
		(name, worked_mins, fee)
	)
	cur.execute("SELECT id FROM projects ORDER BY id DESC LIMIT 0, 1")
	last_insert_id = cur.fetchone()[0]
	addLog(last_insert_id, 0)
	return last_insert_id


def removeProject(project_id):
	cur.execute("DELETE FROM projects WHERE id = ?", (project_id,))
	cur.execute("DELETE FROM logs WHERE project_id = ?", (project_id,))


def getNumberWorkingProjects():
	cur.execute("SELECT COUNT(*) AS total FROM projects WHERE work_start_timestamp>0")
	return cur.fetchone()[0]


def toggleWorkOnProjectID(project_id):
	cur.execute("SELECT work_start_timestamp FROM projects WHERE id = ?", (project_id,))
	session_worked_mins = cur.fetchone()[0]
	if (session_worked_mins == 0):
		cur.execute(
			"UPDATE projects SET work_start_timestamp = ?  WHERE id = ?",
			(time.time(), project_id)
		)
		addLog(project_id, 1)
	else:
		lavorati = round((time.time()-session_worked_mins)/60)
		cur.execute(
			"UPDATE projects SET work_start_timestamp = 0, worked_mins = worked_mins + ? WHERE id = ?",
			(lavorati, project_id)
		)
		addLog(project_id, 2)


def finishAllProjects():
	for project in getAllProjects():
		if (project[3] != 0):
			toggleWorkOnProjectID(project[0])


# The possible operation type values are:
# -1 - project removed -- not used
#  0 - project created
#  1 - start working
#  2 - stop working
#
def addLog(project_id, operation_type):
	cur.execute(
		"INSERT INTO logs (project_id, operation_type, time) VALUES (?, ?, ?)",
		(project_id, operation_type, time.time())
	)


def fromIntToOperationType(op_id):
	if op_id == -1:
		return _("Project removed")
	if op_id == 0:
		return _("Project created")
	if op_id == 1:
		return _("Start working")
	if op_id == 2:
		return _("Work finished")
