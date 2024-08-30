class InputReader:
    @staticmethod
    def read():
        N, M = map(int, input().split())
        A = list(map(int, input().split()))
        B = list(map(int, input().split()))
        return N, M, A, B