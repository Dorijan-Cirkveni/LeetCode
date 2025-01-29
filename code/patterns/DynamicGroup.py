class DynamicGroupList:
    def __init__(self,size:int):
        self.lead=[i for i in range(size)]

    def flatten(self,cur):
        l=self.lead
        while l[cur]!=l[l[cur]]:
            l[cur]=l[l[cur]]
        return l[cur]

    def check(self,a,b):
        return self.flatten(a)==self.flatten(b)

    def join(self,a,b):
        la=self.flatten(a)
        lb=self.flatten(b)
        self.lead[b]=la
        self.lead[lb]=la


def main():
    print("This is a template.")


if __name__ == "__main__":
    main()
