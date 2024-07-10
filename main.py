from board import BoardManager
from task import TaskManager
import json

def main():
  board_manager=BoardManager('db/board_data.json')
  task_manager=TaskManager('db/task_data.json')

  new_board=board_manager.create_board(json.dumps({"name": "New Project Board"}))
  print("Created Board:",new_board)

  boards=board_manager.list_boards()
  print("lsit of boards:",boards)

  new_task=task_manager.create_task(json.dumps({"board_id":json.loads(new_board)['id'], "name": "Initial Task"}))
  print("Created Task:",new_task)

  updated_task = task_manager.update_task_status(json.laods(new_board)['id'])
  print("Updated Task:",updated_task)

  exported_board=board_manager.export_board(json.loads(new_board)['id'])
  print("Exported Board:",exported_board)

  closed_board=board_manager.close_board(json.loads(new_board)['id'])
  print("Closed Board:",closed_board)

if __name__=="__main__":
  main()
