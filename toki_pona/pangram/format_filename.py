def SpaceSeperatedString_to_CamelCase(s: str) -> str:
    slist = s.split(" ")
    return ''.join(slist[0:1]+[s.capitalize() for s in slist[1:]])
def main():
    print(SpaceSeperatedString_to_CamelCase("ku suli"))
if __name__ == '__main__':
    main()