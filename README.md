# 🛒 Coupang Test Automation

쿠팡 기능을 테스트하는 프로젝트

#### 1. 상품 검색 테스트 (구현)
- 웹 크롬으로 접속 후 검색 기능 정상 작동 여부 확인

실행방법
```
pytest tests/test_search.py
```

#### 2. 장바구니 테스트 (일부 구현)
- 웹 크롬으로 쿠팡 접속 후 상품을 장바구니에 추가한 후에 수량 변경, 삭제, 최대 수량 제한, 로그아웃 후 유지여부까지 전반적인 장바구니 기능이 정상 동작하는지 확인


#### 3. 상품 옵션 테스트 (미구현)
- 상품 클릭 후, 페이지에서 옵션 변경, 장바구니 추가, 뒤로 가기 등 옵션 선택 사항이 정상적 반영, 유지되는지 확인


#### 4. 검색 필터 테스트 (미구현)
- 쿠팡 웹 검색 필터(가격, 브랜드, 평점) 정상 적용 확인 및 초기화 기능 확인


#### 5. 판매 특가 테스트 (미구현)
- 판매자 특가 페이지에서 특가 상품 가격 비교, 할인율 정확성, 필터 기능이 정상 작동하는지 확인


#### 6. 최근 상품 테스트 (미구현)
- 최근 본 상품 목록에서 삭제 버튼 및 새로고침(F5) 이후 목록 유지 여부 확인



## 📅 진행기간
- 2025.03.17 - 2025.03.18

## 📋 환경정보
<img src="https://img.shields.io/badge/Google%20Chrome%20134ver-4285F4?style=for-the-badge&logo=GoogleChrome&logoColor=white">
<img src="https://img.shields.io/badge/Windows%2010-0078D6?style=for-the-badge&logo=windows&logoColor=white">

## 🔧 사용기술
<img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54">
<img src="https://img.shields.io/badge/-selenium-%43B02A?style=for-the-badge&logo=selenium&logoColor=white">
<img src="https://img.shields.io/badge/pytest-%23ffffff.svg?style=for-the-badge&logo=pytest&logoColor=2f9fe3">

## Commit Conventions
| Message  | Description                   |
| -------- | ----------------------------- |
| fix      | fixed bugs and errors         |
| feat     | added new feature             |
| refactor | updated existing feature/code |
| docs     | added/updated docs            |
| img      | added/updated images          |
| init     | added initial files           |
| ver      | updated version               |
| chore    | add library                   |
