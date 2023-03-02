import uuid
from person import Person


class ChatRoom:
    def __init__(self) -> None:
        self.room_id: str = f'[{uuid.uuid1()}]'
        self.peoples: list[Person] = []
        print(f'Sala {self.room_id} foi criada.')

    def join(self, person: Person):
        person.chat_room = self
        self.peoples.append(person)
        self.broadcast(person.name, 'entrou na sala.')
        person.chat_log.insert(0, f"\n[{person.name} CHAT LOGS] ROOM-ID -> {self.room_id}")

    def broadcast(self, source: str, message: str) -> None:
        for people in self.peoples:
            if people.name != source:
                people.receive_message(source, message)
                
    def message(self, source, destination: str, message: str) -> None:
        for people in self.peoples:
            if people.name == destination:
                people.receive_message(source, message)