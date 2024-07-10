import json
import os
from .base import BaseTaskManager

class TaskManager(BaseTaskManager):
  def __init__(self,db_path):
    self.db_path=db_path
    if not os.path.exists(self.db_path):
      with open(self.db_path, 'w')as file:
        json.dump([],file)

  def create_task(self,task_data: str)-> str:
    task=json.loads(task_data)
    with open(self.db_path, 'r+')as file:
      data=json.load(file)
      task_id = str(len(data)+1)
      task['id']=task_id
      task['status']='open'
      data.append(task)
      file.seek(0)
      json.dump(data,file)
    return json.dumps({'id': task_id})

  def update_task_status(self,task_id: str,status: str)->str:
    with open(self.db_path, 'r+')
    data = json.load(file)
    for task in data:
      if task['id'] == task_id:
        task['status'] = status
        file.seek(0)
        json.dump(data,file)
        return json.dumps({'id': task_id, 'status': status})
        raise ValueError(f"Board with id {board_id} not found")
