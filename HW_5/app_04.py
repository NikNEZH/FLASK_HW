from flask import Flask, jsonify, request
from pydantic import BaseModel


class Task(BaseModel):
    id: int
    title: str
    description: str
    status: bool


app = Flask(__name__)

tasks = []

# Возвращает список всех задач
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

# Возвращает задачу с указанным идентификатором
@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task:
        return jsonify(task)
    return jsonify({'message': 'Task not found'})

# Добавляет новую задачу
@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.get_json()
    try:
        task = Task(**data)
        tasks.append(task.dict())
        return jsonify({'message': 'Task created'})
    except Exception as e:
        return jsonify({'message': str(e)})

# Обновляет задачу с указанным идентификатором
@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.get_json()
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task:
        try:
            updated_task = Task(**data)
            task.update(updated_task.dict(exclude_unset=True))
            return jsonify({'message': 'Task updated'})
        except Exception as e:
            return jsonify({'message': str(e)})
    return jsonify({'message': 'Task not found'})

# Удаляет задачу с указанным идентификатором
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task:
        tasks.remove(task)
        return jsonify({'message': 'Task deleted'})
    return jsonify({'message': 'Task not found'})


if __name__ == '__main__':
    app.run()