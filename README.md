# LikelionMiniproject - 18년 상반기 미니프로젝트
<br><br>
멋쟁이사자처럼 성균관대학교<br><br>
팀원: 이동건, 유준형, 윤영민, 이찬종, 이소윤

## 주제
<p>공기청정기 구매 시 품질기준 / 성능데이터 등 관련정보를 보기 쉽게 소개하는 페이지 제작</p>
<br>
사전에 읽어볼 기사	
http://news.naver.com/main/read.nhn?mode=LSD&mid=sec&sid1=101&oid=277&aid=0004215759	<br>
	-> 공기청정기는 필터식, 음이온식, 복합식으로 구분됨. 음이온 방식은 오존 발생 가능성이 높아 몸에 좋지 않음<br>
	-> 성능 인증확인 마크: CA와 KS.<br>
==> 문제인식은 이 기사로 할 수 있고, 구체적으로 웹페이지를 만들기 위해서는 추가정보가 필요합니다.	<br>

방법	<br>
1. 조사할 내용	<br>
* 정보측면	<br>
   - 위에 올린 기사 외에도 공기청정기의 품질을 확인할 수 있는 항목이 어떤 것들이 있는지	
   - CA와 KS의 심사항목이 무엇이며 신뢰성은 어느 정도라고 볼 수 있는지.	
   - 인터넷에서 제공하는 공기청정기 제품 스크래핑이 가능한지.	
	
	
* 웹페이지 제작 측면	
    - 어떤 템플릿을 쓸 건지	
    - view는 얼마나 필요하며 Model은 몇 개가 필요할지	
	(모델의 개수는 조사한 정보를 어떻게 데이터베이스화 할 것인지에 따라 다릅니다.)
    - heroku 사용법. +  부트스트랩?	
	
2. 공부해야 할 내용들	
 - 웹 크롤링 방법	
	https://beomi.github.io/2017/01/20/HowToMakeWebCrawler/
	https://medium.com/@mjhans83/%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%9C%BC%EB%A1%9C-%ED%81%AC%EB%A1%A4%EB%A7%81-%ED%95%98%EA%B8%B0-908e78ee09e0 <br>
	beautifulsoup 사용해서 html 문서를 스크래핑 후 파싱하는 방법입니다. 웹크롤링의 가장 기본이지만, 서버가 html 문서를 어떻게 구성하는지에 따라 안 되는 사이트도 왕왕 있습니다. <br>
	https://blog.outsider.ne.kr/312 <br>
	"웹페이지에서 데이터를 가져오려면 반드시 필요한 개념 get과 post. 우리가 레일즈로 웹개발 할 때 routes에 get 'post/index' 쓰던 거에서 앞의 get이 바로 이거임. <br>
당장 이해하긴 쉽지 않더라도 한 번은 읽어보는 걸 추천합니다." <br>
	http://inspirit941.tistory.com/entry/%EC%84%B1%EB%8C%80-%ED%95%99%EC%83%9D%ED%9A%8C-%EA%B3%B5%EC%95%BD-%EB%AA%A8%EC%95%84%EB%B3%B4%EA%B8%B0-%EC%82%AC%EC%9D%B4%ED%8A%B8-%EB%A9%8B%EC%9F%81%EC%9D%B4%EC%82%AC%EC%9E%90%EC%B2%98%EB%9F%BC-%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8-1?category=759169 <br>
	웹크롤링 +  엑셀파일 정리방법 코드가 있는 제 포스트입니다.<br>
	
  - 데이터베이스 설계방법	
	http://inspirit941.tistory.com/category/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D <br>
	"작년 하반기에 제가 진행했던 프로젝트 내용입니다. - 얘는 실제로 데이터 크롤링을 마친 다음에야 설계가 가능함"
	
 - heroku 올리기	
	https://www.flearning.net/lectures/4/clips/21
	c9에서 헤로쿠 연결하는 방법을 설명한 동영상 강의입니다.
	그런데 레일즈가 업데이트되면서 이 방식 그대로 따라하면 오류 생김. 몇 가지 수정사항이 필요한데, 이건 나중에 만나서 설명예정. <br>
  <br>
  
  ## 1주차
  <br>
1. 사전 준비사항 <br>

  - 파이썬 아나콘다를 설치합니다. 올인원 패키지라 짱편함. 여기 포스팅에는 32bit 설치하라고 되어 있는데, 본인 컴퓨터 사양에 맞추면 됩니다.	<br>
  내 컴퓨터가 32인지 64인지 확인하려면 내 컴퓨터 -> 오른쪽버튼 -> 속성	<br>
    https://wikidocs.net/2825	<br>
<br>
2. 5월 18일 모임장소 강남 -> 설명내용 <br>

  - 웹크롤링의 기본 설명. python request, beautifulsoup 활용해 데이터 크롤링하는 방법을 설명하였음. 
