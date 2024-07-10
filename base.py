#Base CLass
import json
from abc import ABC,abstractmethod

class BaseUserManager(ABC):
  def create_user(self,user_data: str)->str:
    pass
  def get_user(self,user_id:str)->str:
    pass

class BaseTeamManager(ABC):
  def create_team(self,team_data: str)->str:
    pass
  def get_team(self,team_id: str)->str:
    pass

class BaseBoardManager(ABC):
  def create_board(self,board_data: str)->str:
    pass
  def close_board(self,board_id: str)->str:
    pass
  def list_board(self) ->str:
    pass
  def export_board(self,board_id: str)->str:
    pass

class BaseTaskManager(ABC):
  def create_task(self,task_data: str)->str:
    pass
  def update_task_status(self,task_id: str,status: str)->str:
    pass
  
