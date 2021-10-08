from .manager import Manager
from models.tournament import Tournament

tm = Manager(Tournament, lambda x: x.id)
