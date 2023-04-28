from glob import glob 
# glob.glob() 함수는 파라미터에 명시된 저장 경로와 패턴에 해당하는 파일명을 리스트 형식으로 반환한다.

ls = glob.glob('temp/*.txt')

print(glob('*'))