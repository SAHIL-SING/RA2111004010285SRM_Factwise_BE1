import json
import os
from .base import BaseBoardManager

class BoardManager(BaseBoardManager):
  def __init__(self,db_path):
    self.db_path=db_path
    if not os.path.exists(self.db_path):
      with open(self.db_path, 'w')as file:
        json.dump([],file)

  def create_board(self,board_data: str) ->str:
    board=json.loads(board_data)
    with open(self.db_path, 'r+')as file:
      data=json.load(file)
      board_id=str(len(data) +1)
      board['id']=board_id
      board['status']='open'
      data.append(board)
      file.seek(0)
      json.dump(data,file)
    return json.dumps({'id':board_id})

  def close_board(self,board_id: str)->str:
    with open(self.db_path, 'r+')as file:
      data=json.load(file)
      for board in data:
        if board['id'] == board_id:
          board['status'] = 'closed'
          file.seek(0)
          json.dump(data,file)
          return json.dumps({'id':board_id, 'status': 'closed'})
      raise ValueError(f"Board with id {board_id} not found")

  def list_board(self) ->str:
    with open(self.db_path, 'r')as file:
      data=json.load(file)
      return json.dumps(data)

  def export_board(self,board_id: str)->str:
    with open(self.db_path, 'r')as file:
      data=json.load(file)
      for board in data:
        if board['id'] == board_id:
          return json.dumps(board)
      raise ValueError(f"Board with id {board_id} not found")
      
    
