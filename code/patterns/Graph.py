class UndirectedGraph:
    def __init__(self, links: dict = None):
        self.links = links if links else {}
        self.start=None

    def addLink(self, a, b):
        self.links.setdefault(a, set()).add(b)
        self.links.setdefault(b, set()).add(a)
        self.start=a

    def extractGraph(self, start):
        found = {start}
        nex = [start]
        while nex:
            cur = nex.pop()
            curset = self.links[cur] - found
            found |= curset
            nex += list(curset)
        return found

    def connectionSplit(self):
        graphs = []
        for e in list(self.links):
            if e not in self.links:
                continue
            curset = self.extractGraph(e)
            if len(curset) == len(self.links):
                self.start = e
                graphs.append(self)
                break
            links = {e: self.links.pop(e) for e in curset}
            graph = UndirectedGraph(links)
            graph.start = e
            graphs.append(graph)
        return graphs

    def ends(self):
        return [e for e, v in self.links.items() if len(v) == 1]


def main():
    print("This is a template.")


if __name__ == "__main__":
    main()
