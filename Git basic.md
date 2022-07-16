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
2. git init 안의 모든 폴더는 git 관리대상
3. git의 3가지 영역은 working directory/ staging area/ repository
4. working directory 는 실제 작업(untracked, 수정시 modify)
5. staging area 는 커밋 특정버전 관리(staged)
6. repository 커밋 확정(commited)
7.  처음 git commit 할 때는 메일, 사용자 이름 등록
   
# 기본 언어
1. touch 파일 생성 명령어
2. ls 폴더에 어떤 목록이 있는지 알림
3. cd 클릭해 폴더로 들어가는 것, 단 cd .. 는 상위 폴더로 나가기
4. start 파일 열기
5. code 코드 열기
6. rm 파일 제거
7. rm -rf 폴더 제거
8. ./ 작업하고 있는 폴더
9.  ../ 현재 폴더의 상위 폴더

10. git add working directory 에서 staging area 갈 때 
11. git commit staging area 에서 repository 갈 때
12. git commit -m "_제목_" 은 메시지 같이 등록하는 옵션
13. git status staging area 상태를 알려줌
14. git log repository 상태 알려줌
15. git diff git log 히스토리 한줄로 알려줌
    
# git 생성하기
1. [Repository 생성에서 NEW 클릭](https://github.com/)
2. repository name, public 또는 private 생성, add a README 파일,create repository클릭

# local 1 정리
1. 새롭게 연계할 파일 생성 및 git bash 오픈(vscode도 가능)
2. git init 으로 폴더 관리 대상으로 만들기
3. README.md 꼭 대문자로 설정
4. 처음 설정시 사용자 이름, 메일 등록 - git config --global user.name "_github 이름_", git config --global user.email "_이메일_" 설정
5. 


# local 2 정리
1. 새로운 로컬에 clone 연계할 파일 생성 및 git bash 오픈(vscode도 가능)
2. git init 으로 폴더 관리 대상으로 만들기
3. 처음 설정시 사용자 이름, 메일 등록 - git config --global user.name "_github 이름_", git config --global user.email "_이메일_" 설정
4. git clone "_git주소_"
5. 이후 add commit push 사용





