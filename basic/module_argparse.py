import argparse

# 객체 생성
parser = argparse.ArgumentParser(prog="AAA", description= " basic math sum")

# 명령줄 인자 정의
parser.add_argument('integers', metavar='N', type=int, help='an integer for the accumulator')
parser.add_argument('--sum', nargs='+', type=int, help='sum of arguments')


# 인자 파싱
args = parser.parse_args()

# 합계 계산 및 출력
if args.sum:
    print(f"합계: {sum(args.sum)}")