class Compress:

    def __init__(self):
        self.compressed = []
        self.values = {}
        self.text = ""

    def compress(self, text):
        palabras = text.split(" ")
        palabras_repetidas = []
        x = 1
        for i in range(len(palabras)):
            if palabras[i] in palabras_repetidas:
                self.compressed.append(self.values[palabras[i]])
            else:
                self.compressed.append(x)
                self.values[palabras[i]] = x
                palabras_repetidas.append(palabras[i])
                x += 1

        return [self.compressed, self.values]

    def uncompress(self, compressed, values):
        for i in range(len(compressed)):
            self.text += list(values.keys())[list(values.values()).index(
                compressed[i])] + " "
        return self.text[:-1]
