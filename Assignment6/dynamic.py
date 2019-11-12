
char_to_int = {'A': 0, 'C': 1, 'G': 2, 'T': 3, '-': 4}

class AlignmentFinder:

    def __init__(self, s1, s2, scoring):
        self.s1 = s1
        self.s2 = s2
        self.Table = None
        self.scoring = scoring

    def find_global_alignment(self):
        self.Table = [[0] * (len(self.s2)+1) for i in range(len(self.s1)+1)]
        self.fillTable()
        return self.pointers()

    def fillTable(self):
        for i in range(1, len(self.s1) + 1):
            for j in range(1, len(self.s2) + 1):

                self.Table[i][j] = max(self.Table[i - 1][j - 1] + self.getScore(i, j),
                                       self.Table[i - 1][j],
                                       self.Table[i][j - 1])


    def getScore(self, i, j):
        return self.scoring[char_to_int[self.s1[i-1]]][char_to_int[self.s2[j-1]]]

    def getPair(self, i, j):
        if i > 0:
            n1 = self.s1[i-1]
        else:
            n1 = "-"

        if j > 0:
            n2 = self.s2[j-1]
        else:
            n2 = "-"

        return (n1, n2)

    def pointers(self):
        alignment = []
        i = len(self.s1)
        j = len(self.s2)
        while i > 0 and j > 0:
            if self.Table[i - 1][j - 1] + self.getScore(i, j) == self.Table[i][j]:
                alignment.append(self.getPair(i, j))
                i -= 1
                j -= 1
            elif self.Table[i - 1][j] == self.Table[i][j]:
                alignment.append(self.getPair(i, 0))
                i -= 1
            else:
                alignment.append(self.getPair(0, j))
                j -= 1
        while i > 0:
            alignment.append(self.getPair(i, 0))
            i -= 1
        while j > 0:
            alignment.append(self.getPair(0, j))
            j -= 1

        alignment.reverse()
        return alignment


    def print_sequences(self, pairs):
        x = []
        y = []

        for (b, t) in pairs:
            y.append(b)
            x.append(t)

        print("x:", end= " ")
        for i in x:
            print(i, end=" ")
        print("")

        print("y:", end=" ")
        for i in y:
            print(i, end=" ")
        print("")

        score = 0
        for p in pairs:
            score += self.scoring[char_to_int[p[0]]][char_to_int[p[1]]]
        print("Score: ", score)

