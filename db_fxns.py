import sqlite3
conn = sqlite3.connect('data.db',check_same_thread=False)
c = conn.cursor()


def create_table():
	c.execute('CREATE TABLE IF NOT EXISTS taskstable(task TEXT,task_status TEXT,task_due_date DATE, requested_by TEXT, claimed_by TEXT)')

def view_all_data():
	c.execute('SELECT * FROM taskstable')
	data = c.fetchall()
	return data

def view_all_task_names():
	c.execute('SELECT DISTINCT task FROM taskstable')
	data = c.fetchall()
	return data

def get_task(task):
	c.execute('SELECT * FROM taskstable WHERE task="{}"'.format(task))
	data = c.fetchall()
	return data

def get_task_by_status(task_status):
	c.execute('SELECT * FROM taskstable WHERE task_status="{}"'.format(task_status))
	data = c.fetchall()

def add_data(task,task_status,task_due_date, requested_by, claimed_by):
	c.execute('INSERT INTO taskstable(task,task_status,task_due_date,requested_by,claimed_by) VALUES (?,?,?,?,?)',(task,task_status,task_due_date,requested_by,claimed_by))
	conn.commit()

def edit_task_data(new_task, new_task_status, new_task_due_date, new_requested_by, new_claimed_by, task, task_status, task_due_date, requested_by, claimed_by):
	c.execute("UPDATE taskstable SET task =?,task_status=?,task_due_date=?,requested_by=?,claimed_by=? WHERE task=? and task_status=? and task_due_date=? and requested_by=? and claimed_by=?",(new_task,new_task_status,new_task_due_date,new_requested_by,new_claimed_by,task,task_status,task_due_date,requested_by,claimed_by))
	conn.commit()
	data = c.fetchall()
	return data

def delete_data(task):
	c.execute('DELETE FROM taskstable WHERE task="{}"'.format(task))
	conn.commit()