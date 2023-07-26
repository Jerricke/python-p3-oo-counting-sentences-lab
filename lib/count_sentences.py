#!/usr/bin/env python3


class MyString:
    def __init__(self, value=""):
        self.value = value

    def is_sentence(self):
        print(self.value[-1])
        if self.value and self.value[-1] == ".":
            return True
        else:
            return False

    def is_question(self):
        print(self.value[-1])
        if self.value and self.value[-1] == "?":
            return True
        else:
            return False

    def is_exclamation(self):
        print(self.value[-1])
        if self.value and self.value[-1] == "!":
            return True
        else:
            return False

    def get_value(self):
        return self._value

    def set_value(self, value):
        if type(value) is str:
            self._value = value
        else:
            print("The value must be a string.")

    def count_sentences(self):
        # res = []
        # for punc in [".", "?", "!"]:
        #     res.append(self.value.split(punc))
        # return len(res)
        value = self.value
        for punc in ["!", "?"]:
            value = value.replace(punc, ".")

        sentences = [s for s in value.split(".") if s]

        return len(sentences)

    value = property(get_value, set_value)


hello = MyString("Hello World. Hi World! What is wrong world?")
hello.is_sentence()
hello.count_sentences()
