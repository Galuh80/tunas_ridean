from read_input import InputReader
from maximize_skill import SkillMaximizer

def main():
    N, M, A, B = InputReader.read()
    maximizer = SkillMaximizer(N, M, A, B)
    result = maximizer.solve()
    print(result)

if __name__ == "__main__":
    main()