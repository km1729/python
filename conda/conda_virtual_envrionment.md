
가상환경 생성
```bash
conda create -n lfric
conda create -n lfric python=2.7 pip numby flask
```

가상환경 확인
conda의 가상환경은 콘다가 설치된 폴더의 하위 디렉토리에 생성된다.
```bash
(base) k@local:~$ conda info --envs
# conda environments:
#
base                  *  /home/k/miniconda3
lfric                    /home/k/miniconda3/envs/lfric
```

가상환경 활성화/비활성화
```bash
conda activate lfric
conda deactivate
```

가상환경 내 패키지 설치
가상환경이 활성화 된 상태에서
```bash
conda install --name lfric package name
```

패키지 검색 / 삭제
```bash
conda search '*pandas*'
conda remove pandas
```

가상환경 삭제
```bash
conda env remove -n lfric
```

가상환경 내보내기 / 만들기 with file
```bash
conda env export > requirements.yaml

```