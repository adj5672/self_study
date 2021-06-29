# 산출물
> Vue CLI 기반 DevOps 개발환경 실습



### 1. Vue 프로젝트 생성 및 로컬 실행 확인

1. yarn 및 vue cli 설치

   ![image-20210629135235300](README.assets/image-20210629135235300.png)

   ![image-20210629135307080](README.assets/image-20210629135307080.png)

   

2. Vue 프로젝트 생성

   ![image-20210629135441925](README.assets/image-20210629135441925.png)



3. 프로젝트 확인

   ![image-20210629135712177](README.assets/image-20210629135712177.png)

   ![image-20210629135740257](README.assets/image-20210629135740257.png)



### 2. GitHub에 코드 Push 및 Pages에 수동 배포

1. vue-devops 프로젝트 생성

   ![github.com_adj5672_vue-devops](README.assets/github.com_adj5672_vue-devops.png)



2. 원격 저장소 설정 및 코드 푸시하기

   ![2](README.assets/2.png)



3. GitHub Pages로 배포하기 위한 라이브러리에 추가 및 package.json에서 배포에 필요한 정보 추가

   ![image-20210629140623015](README.assets/image-20210629140623015.png)

   ![image-20210629141035587](README.assets/image-20210629141035587.png)



4. 배포용 publicPath 설정

   ![image-20210629141249340](README.assets/image-20210629141249340.png)



5.  yarn deploy

   ![image-20210629141445691](README.assets/image-20210629141445691.png)



6. 설정에서 배포된 주소를 확인 후 접속 시도

   ![3](README.assets/3.png)



7. repository에서 웹사이트 주소 설정

   ![image-20210629141840309](README.assets/image-20210629141840309.png)



이제 Vue로 개발한 프로젝트를 yarn deploy 명령어로 GitHub Pages에 수동으로 빌드된 정적 파일을

배포해서 서비스를 운영할 수 있게 되었습니다.



### 2. GitHub Actions workflow로 배포 자동화

> - GitHub Actions는 GitHub의 소프트웨어개발 workflow에서 작업을 자동화하기 위한 패키지 스크립트
>
> - 개발자가 새 소스 코드를 Push하거나 Pull Request 같은 이벤트에 반응하여 트리거하도록 구성 가능
>
> - 이 기능을 사용하여 Vue로 작성된 소스 코드를 자동으로 테스트한 다음 빌드하여 GitHub Pages에
>
> 배포하는 작업을 자동화하여 빠르고 안정적인 배포 및 운영이 가능한 DevOps 환경을 구축하려고 한다.



1. GitHub Actions 메뉴의 첫 화면에서 보여주는 Simple workflow 파일(deploy.yml) 을 작성 및 커밋

   ![4](README.assets/4.png)

   

   ![5](README.assets/5.png)



2. 샘플 workflow가 동작됨을 확인

   ![6](README.assets/6.png)



3. git pull 및 GitHub Pages에 정상적으로 배포되는지 확인하기 위해 App.vue 수정

   ![image-20210629143114766](README.assets/image-20210629143114766.png)



4. 배포 스크립트인 workflow 파일(deploy.yml) 내용을 수정

   ![image-20210629143900755](README.assets/image-20210629143900755.png)



5. Commit & Push



6. Workflow 동작 결과와 자동 배포된 사이트 내용을 확인

   ![7](README.assets/7.png)

   ![8](README.assets/8.png)



### 3. 코드 수정 및 테스트 실패로 인한 자동 배포 실패 확인

> - 만약 빌드가 실패하거나 테스트를 통과하지 못하면 서비스에 반영이 되지 않는다.
> - 그래서 꼭 자동화된 배포 Workflow 또는 Pipeline에서는 테스트 절차가 필요하다.



1. yarn install, build 사이에 단위 테스트 step을 추가한다.

   ![image-20210629144513572](README.assets/image-20210629144513572.png)



2. 테스트가 실패하도록 `<h1>` 태그 값을 수정한다.

   ※ App.vue에서 전달한 props를 사용하지 않아 테스트에 실패하게 된다.

   ![image-20210629144631998](README.assets/image-20210629144631998.png)



3. Commit & Push



4. 자동 배포 실패 확인

   ![9](README.assets/9.png)

   ![image-20210629144927908](README.assets/image-20210629144927908.png)





### 3. 코드 재 수정 및 배포 성공 확인

> - 단위 테스트가 실패하면 build, deploy 가 진행되지 않아 사이트에 문제가 발생하지 않는다.
> - 컴포넌트를 만들 때 작성자의 의도대로 동작하는지 확인하는 테스트 코드를 꼭 작성 추천
> - 습관화가 잘 안된다면 테스트 코드를 먼저 작성하고 이후 테스트를 통과하는 기능을 개발하는 TDD를 활용해 보는 것도 하나의 방법



1. 테스트가 통과하도록 코드 수정

   ![image-20210629145239914](README.assets/image-20210629145239914.png)

   ![image-20210629145327521](README.assets/image-20210629145327521.png)



2. Commit & Push



3. 테스트 성공 확인

   ![10](README.assets/10.png)

   ![image-20210629145559640](README.assets/image-20210629145559640.png)