# BOJ
BOJ 코테 모음


1. git add 를 사용하면 파일이 작업폴더 -> 스테이징 에리어로이동 (스테이징한다~이말이야)
1-1. git status 를 쓰면 스테이징 된 파일을 볼수있다
1-2. git log 를 쓰면 커밋한 로그 볼수있음 

2. git commit 을 사용하면 파일이 스테이징 에리어 -> 레퍼지토리로 이동 
2.1 커밋은 간단한 "기능1개" "덩어리1개" 추가했을때마다 주기적으로 한다


3. git push 로 마무리

4. 새로운 브랜치를 만들고 그 브랜치로 이동하는 명령어
   git checkout -b test

5. 브랜치를 합치는방법 merge!!


정리 : 
브랜치 생성은 git checkout -b 브랜치명 
브랜치 이동은 git checkout 브랜치명 or git switch 브랜치명
브랜치 합치기는 main 브런치에서 git merge 브랜치명
충돌해결은 코드고치고 git add & git commit 

6. 깃플로우 전략