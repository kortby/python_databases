import mysql.connector as mysql


def connect(db_name):
    try:
        return mysql.connect(
            host='localhost',
            user='root',
            password='',
            database=db_name
        )
    except Exception as e:
        print(e)


def add_new_project(cursor, project_title, project_desciption, task_descriptions):
    project_data = (project_title, project_desciption)
    cursor.execute(
        'INSERT INTO projects(title, description) VALUES (%s, %s)', project_data)
    project_id = cursor.lastrowid
    tasks_data = []

    for description in task_descriptions:
        task_data = (project_id, description)
        tasks_data.append(task_data)

    cursor.executemany(
        'INSERT INTO tasks(project_id, description) VALUES (%s, %s)', tasks_data)


if __name__ == '__main__':
    db = connect('projects')
    cursor = db.cursor()
    tasks = [
        'starting by the kitchen',
        'go to bathroom',
        'end with living room',
    ]
    add_new_project(cursor, 'Clean house', 'clean one at the time', tasks)
    db.commit()

    print('----------------------------------')
    cursor.execute('SELECT * FROM projects')
    project_records = cursor.fetchall()
    print(project_records)
    print('----------------------------------')

    cursor.execute('SELECT * FROM tasks')
    task_records = cursor.fetchall()
    print(task_records)

    db.close()
