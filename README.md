# Capstone_Design_1
- Capstone Design Team Project
- In order to develop the ability to solve problems encountered in the field, students carry out a series of courses from planning to production instead of graduation papers.

# 자료조사
# 1. 자율주행차의 영상 기반 차간 거리 측정 기술 
- 허의남 교수님
## 참고 사이트
https://www.youtube.com/watch?v=qMrF4ycfV5w

# 논문
“차량 그림자를 이용한 주행 차량 검출 및 차간 거리 측정”, 김태희, 강문설, 2012
Driving Vehicle Detection and Distance Estimation using Vehicle Shadow
## 요약
- 차량 운전자들의 안전 운행을 보조하기 위해 운전자의 차량과 전방의 차량 간의 거리를 추정하고 안전거리 유무를 알려주기 위한 경보시스템 개발 논문. 실제 도로 환경에서 전방의 주행 차량을 검출하여 차간 거리를 측정하고 충돌 위험 상황을 감지하여 운전자에게 충돌 위험을 알리는 충돌 - 경고 시스템을 설계 및 구현
주행 차량 검출 및 차간 거리 측정 결과를 기반으로 충돌경고시스템을 설계
및 구현하였으며, 실제 도로상황에 적용하여 실험한 결과 매우 높은 정확도를 나타내어 안전 운전에 대응할 수 있
는 것으로 검증되었다.
## 방법
- 전방주시 카메라를 활용하여 촬영한 도로영상으로부터 도로와 차량에 해당하는 관심 영역을 추출하고, 관심 영역에서 전방 차량의 그림자 임계값 분석을 통해 전방 차량 객체를 추출한 후 전방 차량과의 거리를
계산하여 충돌 위험 경고를 알려준다. 

## 주요 내용
- 지능형 자동차의 경우 컴퓨터 하드웨어 성능의 발달로 컴퓨터 비전 및 영상처리 기술이 급속히 발달하였고,고해상도의 영상데이터를 분석할 수 있을 뿐만 아니라 실시간 동영상 처리까지 가능
- 다양한 보조시스템 개발, 차량에 카메라 탑재, 도로 전방의 영상 정보 수집 분석하여 운전자에게 시각 및 청각적인 정보를 제공하는 차간거리제어장치, 차선유지도움장치 등 자동차 관련 첨단기술이 연구 개발되어 상용화 되고 있다.
- 차선 및 차간 검추을 위한 영상 데이터에 대한 실시간 탐색 및 처리

    1. 차량 전방에 설치된 카메라를 활용하여 촬영한 도로영상으로부터 도로와 차량에 해당하는 관심 영역을 추출한다. 
    2. 추출한 관심 영역에 대한 허프 변환을 통해 직선 성분을 검출
    3. 확률 계산을 통해 차선을 확정하여 필터링 실시
    4. 관심 영역에서 전방 차량의 그림자 임계값 분석을 통해 전방 차량 객체를 추출하여 전방 차량과의 거리를 계산
    5. 주행 차량 검출 및 차간 거리 측정 결과를 기반으로 충돌경고 시스템을 설계 및 구현
### 차량 검출을 위한 전처리 과정
- 입력 영상 중 관심영역을 설정, 전처리 과정이 진행되어 차선과 차량 검출, 차간 거리 측정
    1. 입력된 도로 영상을 차선 및 차간 인식 알고리즘에 적용하기 위해 먼저 도로영상ㅇ에 대해 전처리가 선행되어야 한다. 관심영역을 정하고 그레이 스케일, 소벨 연산, 이진화를 이용하여 차선과 차량의 특징을 추출한다.
    2. 전처리 한 영역 바탕으로 허프 변환을 적용해서 영상 내 직선과 차량 성분을 검출
    3. 검출된 직선 성분을 분석하여 통계적으로 최대값 성분을 차선으로 인식
    4. 전방 차량 인식을 위해 관심 영역에서 임계값 이하면 차량 객체로 설정, 차량 여부를 식별하여 차간 거리 계산 
### 링크
http://koreascience.or.kr/article/JAKO201225841537997.pdf

### 그레이 스케일, 소벨 연산, 이진화, 허프 변환
### 충돌 경고 시스템 설계 및 구현
1. 차선 검출 과정
2. 차간 인식 및 거리 계산 과정
3. 차간 거리 및 차량 속도 계산
4. 하드웨어 구성, 시제품
### 실험 결과 분석

# 2. 영상(화재, 증기, 연기) 감지 기계학습 기술 개발
- 허의남 교수님

## 참고 논문
 https://repository.hanyang.ac.kr/bitstream/20.500.11754/23085/1/컴퓨터%20비전%20기반의%20연기감지%20기법.pdf
### 컴퓨터 비전 기반의 연기감지 기법
- 컴퓨터비전을 이용한 자동감시 시스템에 대한 요구는 지속적으로 증대되고 있다. 하지만 실제 높은 오감지율로 인해 실사용에 어려움이 있는 것이 사실이다. 본 논문은 컴퓨터 비전을 이용한 연기감지 기법에서 오감지율을 최소화 하고 연기감지가 이루어질 수 있게 하기 위해 제안되었다. 본 감지기법의 핵심으로는 밝기와 색으로 판단하는 연기픽셀을 정의하고 프레임의 변화에 따른 그것의 증가에 따라 각 객체의 연기량이 지속적으로 증대되는 것을 감지하는 방법을 이용한다. 그리고 중-근거리에서는 라벨링
알고리듬을 이용, 연기픽셀로 구성된 각 부분들을 각각 하나의 객체로써 구별할 수 있게 하고 객체마다 실제 연기에 해당하는 조건들을 적용해보고 연기의 움직임인지 판단한다. 실험결과 11개의 연기발생 영상과 2개의 CCTV영상 총 13개의 영상에서 11건의 영상에서 알고리듬이 정상적으로 작동하는 것으로 나타났다. 
1. 서론
2. 연기 감지 기법(밝기/색, 라벨링을 이용한 연기 분리 기법, 연기 픽셀 증가 이용, 연기의 특징을 이용한 감지능률 향상 기법)
3. 실험 결과 및 분석

# 3. 딥러닝 데이터 증대기법 연구
- 배성호 교수님
- 딥러닝 학습에 필요한 데이터를 인위적으로 증대시키기 위하여 data augmentation(참고: https://www.kdnuggets.com/2018/05/data-augmentation-deep-learning-limited-data.html)기술은 선행 조사 한 다음, 새로운 data augmentation기술을 개발한다.
## 참고 사이트
1. https://www.kdnuggets.com/2018/05/data-augmentation-deep-learning-limited-data.html
- How do I get more data, if I don’t have “more data”?에 대한 내용
2. https://woolulu.tistory.com/135
- Data Augmentation 개념
3. https://www.tensorflow.org/tutorials/images/data_augmentation

### 데이터 증강
- 이 튜토리얼에서는 이미지 회전과 같은 무작위(그러나 사실적인) 변환을 적용하여 훈련 세트의 다양성을 증가시키는 기술인 데이터 증강의 예를 보여줍니다. 두 가지 방법으로 데이터 증강을 적용하는 방법을 배웁니다. 먼저, Keras 전처리 레이어를 사용하고, 그 다음으로 tf.image를 사용합니다.

    1. 데이터세트 다운로드
    2. Keras 전처리 레이어 사용하기
    3. 데이터 증강
        - 옵션 1: 전처리 레이어를 모델의 일부로 만들기
        - 옵션 2: 데이터세트에 전처리 레이어 적용하기
    4. 데이터세트에 전처리 레이어 적용하기
    5. 모델 훈련하기
    6. 사용자 정의 데이터 증강
    7. tf.image 사용하기
    8. 이미지 뒤집기, 이미지를 회색조로 만들기, 이미지 포화시키기, 이미지 밝기 변경하기, 이미지 중앙 자르기
    9. 데이터세트에 증강 적용하기
    10. 데이터세트 구성하기
 ## 참고 블로그
 - Data Augmentation for Deep Learning
  https://towardsdatascience.com/data-augmentation-for-deep-learning-4fe21d1a4eb9

# 4. 다수의 칼라 카메라를 이용한 3차원 객체 형상 획득, 분리 및 객체 인식
- 이승규 교수님
- “3차원 형상 획득을 위하여 다수의 카메라를 정합하여 획득한 Point Cloud 데이터의 노이즈를 제거하고 Mesh 모델링을 수행한다. 칼라 정보간 정합을 위한 tone mapping을 수행하고, 카메라에서 보이지 않는 영역은 Hole filling을 수행한다. 최종적으로 획득한 3차원 모델을 VR 기기등을 통하여 Presentation 한다. ”
## 참고 사이트
1. https://scienceon.kisti.re.kr/srch/selectPORSrchPatent.do?cn=KOR1020150114825&dbt=KPTN
- 3차원 형상 측정 방법 

# 5. GAN을 이용한 사람 행동 생성
- 이승규 교수님
- GAN 네트워크를 이용하여 사람의 움직임을 학습하고, 이를 기반으로 새로운 사람의 행동을 생성하는 알고리즘을 개발한다.

## 참고 링크
https://github.com/tensorflow/gan

### TensorFlow-GAN (TF-GAN)
- TF-GAN is a lightweight library for training and evaluating Generative Adversarial Networks (GANs).
- Structure of the TF-GAN Library
- 핵심: GAN을 교육하는 데 필요한 주요 인프라. TF-GAN 라이브러리 호출, 사용자 정의 코드, 기본 TF 코드 및 기타 프레임워크의 조합으로 교육 설정
- 기능: 일반적인 GAN 작동 및 인스턴스 표준화 및 조건화 같은 표준화 기법.
- 손실: Wasserstein 손실, 경사로 벌칙, 상호 정보 벌칙 등과 같은 손실 및 벌칙
- 평가: 표준 GAN 평가 메트릭입니다. 사전 훈련된 Inception 네트워크와 함께 Inception Score, Frechet Distance 또는 Kernel Distance를 사용하여 무조건적인 생성 모델을 평가합니다. 더 구체적인 성능 번호에 대해 자체 사전 훈련된 분류기를 사용하거나 조건부 생성 모델을 평가하는 다른 방법을 사용할 수도 있습니다.
- 예: TF-GAN 사용 방법에 대한 간단한 예와 보다 복잡한 최첨단 예
- Training a GAN model 방법 있음(링크 참조)
# 6. 딥러닝 기반 실시간 다중 객체 추적 시스템
- 송규예 대표님
- 본 주제는 인공지능 기술을 바탕으로한 안전 솔루션 사업의 일환으로 CCTV 영상 데이터를 분석하여 범죄 및 사고 예방을 하기 위함. 사람을 추적하는 경우 미아, 치매노인 등의 사회적 약자를 안전하게 보호하는 것에 목적이 있음. 자동차를 추적하는 경우 도로상황에서의 각종 사건사고를 탐지하고 추적하는 것에 목적이 있음.
- 데이터는 온라인에 오픈된 데이터 중 원하는 대로 선택하여 진행(예:MARS등). 추적 객체는 자동차 또는 사람 중 선택. 딥러닝 기반 트래킹 기술은 칼만필터, SORT알고리즘, 헝가리안 알고리즘 등이 포함되어 함께 공부 필요.

## 자료 준비
http://www.utic.go.kr/guide/cctvOpenData.do?key=
- key gmail에 있음
## 참고 유투브 
https://www.youtube.com/watch?v=JatQ-lziHO4

## 참고할 깃허브
1. https://github.com/Zhongdao/Towards-Realtime-MOT
-  JDE(Joint Detection and Embedding) 모델의 코드베이스
- JDE는 공유 신경망에서 객체 감지 작업과 외관 임베딩 작업을 동시에 학습하는 빠르고 고성능 다중 객체 추적기
- ECCV 2020 문서에 설명 참고
- MOT-16 챌린지의 "비공개" 프로토콜에서 MOTA 64%+를 달성할 수 있으며, 22~38 FPS에서 실시간에 가까운 속도
- 훈련 데이터, 기준선 모델 및 평가 방법을 제공
- 응용 프로그램 사용을 위해 벨과 휘파람 없이 원시 비디오를 입력으로 사용하는 소형 비디오 데모도 제공합니다.

2. https://github.com/hu64/SpotNet
- 인간은 다른 종류의 물체를 검색할 때 시각적 주의를 관련 영역으로 유도하는 데 매우 능숙하다. 예를 들어, 우리가 차를 찾을 때, 우리는 건물 꼭대기가 아니라 거리를 볼 것이다. 이 논문의 동기는 네트워크가 다중 작업 학습 접근법을 통해 동일한 작업을 수행하도록 훈련하는 것이다. 시각적 주의를 훈련시키기 위해, 우리는 배경 감산 또는 광학 흐름을 사용하여 반지도 방식으로 전경/배경 분할 레이블을 생성한다. 이러한 레이블을 사용하여 대부분의 모델 매개 변수를 공유하면서 경계 상자뿐만 아니라 전경/배경 분할 맵을 생성하도록 객체 감지 모델을 훈련시킨다. 우리는 네트워크 내부의 이러한 분할 맵을 경계 상자를 생산하는 데 사용되는 특징 맵의 가중치를 매겨 관련이 없는 영역의 신호를 감소시키는 자기 주의 메커니즘으로 사용한다. 우리는 이 방법을 사용하여 UA-DETRAC와 UAVDT 모두에서 최첨단 결과와 함께 두 개의 트래픽 감시 데이터 세트에서 mAP를 크게 향상시킨다는 것을 보여준다.
- 관련 영상
https://www.youtube.com/watch?v=JatQ-lziHO4




## 참고 논문
### Real-Time Multiple Object Tracking
- Multiple object tracking
- Tracking-by-detection
    - Detection
    - Prediction
    - Association
- Real-time tracking
- Datasets
- Evaluation metrics
- 방법
    - C++ Sort
    - MOTChallenge
    - Tracking with different frame rates
    - Detecting and tracking in real-time

### 링크
https://www.diva-portal.org/smash/get/diva2:1146388/FULLTEXT01.pdf

## 참고 논문
- 다중 이동 객체의 실시간 인식 및 추적 시스템
https://scienceon.kisti.re.kr/commons/util/originalView.do?cn=JAKO201128451817658&oCn=JAKO201128451817658&dbt=JAKO&journal=NJOU00293531

- 실시간 영상에서 객체 추적 및 얼굴추출
https://scienceon.kisti.re.kr/srch/selectPORSrchArticle.do?cn=NPAP08040399&dbt=NPAP

- Real-Time Multiple Object Tracking
https://www.diva-portal.org/smash/get/diva2:1146388/FULLTEXT01.pdf

