# import uuid
class Task:
    def __init__(self, ID, name, description, priority, state):
        # self.id = uuid.uuid4()
        self.ID = ID
        self.name = name
        self.description = description
        self.priority = priority
        self.state = state

    def __str__(self):
        return f"""TASK {self.ID}:
            ID: {self.ID}
            Name: {self.name}
            Description: {self.description}
            Priority: {self.priority}
            State: {self.state}
        """
