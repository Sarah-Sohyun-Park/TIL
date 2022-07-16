# Git 내용정리

**집에서 다시 해보기**

*집에서 다시 해보기*

![붱철이 이미지](./img/bc.jpg)

```print('쉽지 않군')```

~~무를까~~

--------

1. [폴더 만들기](../Git/)

# 기본정보
1. gui는 그래픽, cli는 명령어로 작동
2. 이곳에서 상대경로를 많이 사용 (ex../Git/../파일명 )
3. git init 안의 모든 폴더는 git 관리대상
4. git hub에 있는 내용이 중심이 됨
5. git의 3가지 영역은 working directory/ staging area/ repository
6. working directory 는 실제 작업(untracked, 수정시 modify)
7. staging area 는 커밋 특정버전 관리(staged)
8. repository 커밋 확정(commited)
9.  처음 git commit 하기 전 메일, 사용자 이름 등록
   
# 기본 언어
- touch - 파일 생성 명령어
- mkdir - 폴더 생성
- ls - 폴더에 어떤 목록이 있는지 알림
- ls -a  숨김 폴더 확인 가능
- cd - 클릭해 폴더로 들어가는 것, 단 cd .. 는 상위 폴더로 나가기
- start - 파일 열기
- code - 코드 열기
- rm - 파일 제거
- rm -rf - 폴더 제거
- ./ - 작업하고 있는 폴더
- ../ - 현재 폴더의 상위 폴더
- git add - working directory 에서 staging area 갈 때 
- git commit - staging area 에서 repository 갈 때, 나갈 때 insert, 이름, esc/, :wq 또는 :wq!
- git commit -m - "_제목_" 은 메시지 같이 등록하는 옵션
- git status - staging area 상태를 알려줌
- git log - repository 상태 알려줌
- git diff - git log 히스토리 한줄로 알려줌
- git push _repo name_ _local branch_ - 올리기 (일반적으로 git push origin master)
- git remote -v - 원격저장소 목록 확인
- git remote add origin "_주소_" - 원격 저장소에 새로 등록
- (master)는 branch 확인용
    
# git 생성하기
1. [Repository 생성에서 NEW 클릭](https://github.com/)
2. repository name, public 또는 private 생성, add a README 파일,create repository클릭

# local 1 정리
1. 새롭게 연계할 파일 생성 및 git bash 오픈(vscode도 가능)
2. git init 으로 폴더 관리 대상으로 만들기
3. README.md 꼭 대문자로 설정(꼭 로컬 파일에서 생성)
4. 처음 설정시 사용자 이름, 메일 등록 - git config --global user.name "_github 이름_", git config --global user.email "_이메일_" 설정 
5. git config --list로 이름 메일 확인
6. git add . 로 특정 관리 버전을 만들기 (또는 git add "_파일명_")
7. git commit 또는 git commit -m - "_제목_" 으로 커밋 확정시킴
8. git branch -m master
9. git remote add origin "_주소_" 또는 git remote add origin {_주소_}
10. 주소 잘못 설정 시 git remote set url origin 사용
11. git push origin master

12. 이후 재 사용시 git clone "주소"
13. git push origin master
14. 파일 추가시 git remote add origin "_주소_"

# local 2 정리
1. 새로운 로컬에 clone 연계할 파일 생성 및 git bash 오픈(vscode도 가능)
2. git init 으로 폴더 관리 대상으로 만들기
3. 처음 설정시 사용자 이름, 메일 등록 - git config --global user.name "_github 이름_", git config --global user.email "_이메일_" 설정
4. git clone "_주소_" 또는 git clone {_주소_}
5. 이후 add commit push remote 사용





