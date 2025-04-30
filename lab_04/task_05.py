class TextDocument:
    def __init__(self, text=""):
        self.text = text

    def set_text(self, new_text):
        self.text = new_text

    def get_text(self):
        return self.text

    def create_memento(self):
        return Memento(self.text)

    def restore(self, memento):
        self.text = memento.get_state()


class Memento:
    def __init__(self, state):
        self._state = state

    def get_state(self):
        return self._state


class TextEditor:
    def __init__(self):
        self.document = TextDocument()
        self.history = []  # Список для збережених станів документа

    def write(self, text):
        self.history.append(self.document.create_memento())
        self.document.set_text(text)

    def undo(self):
        if self.history:
            last_state = self.history.pop()
            self.document.restore(last_state)
            print("Undo: ", self.document.get_text())
        else:
            print("No changes to undo.")

    def get_document(self):
        return self.document.get_text()


if __name__ == "__main__":
    editor = TextEditor()

    editor.write("Hello, world!")
    print("Current Text: ", editor.get_document())

    editor.write("Hello, Python!")
    print("Current Text: ", editor.get_document())

    editor.undo()
    print("After Undo: ", editor.get_document())

    editor.undo()
    print("After Undo: ", editor.get_document())

    editor.undo()
    print("After Undo: ", editor.get_document())

    editor.write("Hello, Python!")
    print("Current Text: ", editor.get_document())

    editor.undo()
    print("After Undo: ", editor.get_document())
