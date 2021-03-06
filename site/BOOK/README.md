## "이것이 취업을 위한 코딩테스트다 with Python"
[[YouTube]](https://youtu.be/m-9pAwq1o3w)

## 주요 알고리즘 이론과 실전 문제
- [그리디]  
> 현재 상황에서 가장 좋아 보이는 것만을 선택하는 알고리즘.   
> 그리디 알고리즘 문제에서는 문제 풀이를 위한 최소한의 아이디어를 떠올리고 이것이 정당한지 검토 과정이 필요.   
> 예제    
>> [[거스름돈]](./greedy/거스름돈.py)   
> 실전   
>> [[큰수의법칙]](./greedy/큰수의법칙.py)   
>> [[숫자카드게임]](./greedy/숫자카드게임.py)   
>> [[1이될때까지]](./greedy/1이될때까지.py)   

- [구현]   
> 머릿속에 있는 알고리즘을 정확하고 빠르게 프로그램으로 작성하기.   
> 구현 유형의 문제는 '풀이를 떠올리는 것은 쉽지만 소스코드로 옮기기 어려운 문제'를 의미한다.   
> 예제   
>> [[상하좌우]](./구현/상하좌우.py)   
>> [[시각]](./구현/시각.py)   
> 실전문제   
>> [[왕실의나이트]](./구현/왕실의나이트.py)   
>> [[게임개발]](./구현/게임개발.py)
   
- [DFS/BFS]   
> 그래프를 탐색하기 위한 대표적인 두 가지 알고리즘   
> 탐색이란... 많은 양의 데이터 중에서 원하는 데이터를 찾는 과정  
> 자료구조란... 데이터를 표현하고 관리하고 처리하기 위한 구조
> 그중 스택과 큐는 자료구조의 기초 개념   
>> [스택](./DFS_BFS/스택예제.py)은 박스 쌓기에 비유할 수 있다. [선입후출 FILO | 후입선출 LIFO]   
>> [큐](./DFS_BFS/큐.py)는 대기 줄에 비유할 수 있다. [선입선출 FIFO]   
>> [재귀함수](./DFS_BFS/재귀함수예제.py)란 자기자신을 다시 호출하는 함수를 의미한다.
   
> [DFS는 Depth-First Search](./DFS_BFS/DFS예제.py), 깊이 우선 탐색이라고도 부르며, 그래프에서 [깊은 부분을 우선적]으로 탐색하는 알고리즘   
>> [인접 행렬(Adjacency Matrix)](./DFS_BFS/인접행렬예제.py) 2차원 배열로 그래프의 연결 관계를 표현하는 방식   
>> [인접 리스트(Adjacency List)](./DFS_BFS/인접리스트예제.py) 리스트로 그래프의 연결 관계를 표현하는 방식   
   
> [BFS는 Breadth First Search](./DFS_BFS/BFS예제.py) 너비 우선 탐색이라는 의미를 가진다. 쉽게 말해 [가까운 노드부터] 탐색하는 알고리즘   
  
> 실전문제   
>> [[음료수얼려먹기]](./DFS_BFS/음료수얼려먹기.py)   
>> [[미로탈출]](./DFS_BFS/미로탈출.py)   
   
- [정렬]   
> 연속된 데이터를 기준에 따라서 정렬하기 위한 알고리즘.   
> 정렬이란... 데이터를 특정한 기준에 따라서 순서대로 나열하는 것을 말한다.   
>> [[선택정렬]](./정렬/선택정렬.py) 매번 '가장 작은 것을 선택'한다.   
>> [[삽입정렬]](./정렬/삽입정렬.py) 특정한 데이터를 적절한 위치에 '삽입'한다.   
>> [[퀵정렬]](./정렬/퀵정렬.py) 기준(pivot)을 설정한 다음 큰 수와 작은 수를 교환한 후 리스트를 반으로 나누는 방식으로 동작한다.   
>> [[계수정렬]](./정렬/계수정렬.py) 특정한 조건(데이터의 크기 범위가 제한되어 정수 형태로 표현할 수 있을 때만) 이부합할 때만 사용할 수 있지만 매우 빠른 정렬 알고리즘이다.   
>> [[파이썬 정렬 라이브러리]](./정렬/파이썬정렬라이브러리.py)   
   
> 실전문제   
>> [[위에서아래로]](./정렬/위에서아래로.py)   
>> [[두배열의원소교체]](./정렬/두배열의원소교체.py)   
   
- [이진탐색]   
> 탐색 범위를 반으로 좁혀가며 빠르게 탐색하는 알고리즘.
> [[순차탐색]](./이진탐색/순차탐색.py) 리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서부터 데이터를 차례대로 확인하는 방법.   
> [[이진탐색]](./이진탐색/이진탐색.py) 배열 내부의 데이터가 정렬되어 있어야만 사용할 수 있는 알고리즘이다. 찾으려는 데이터와 중간점 위치에 있는 데이터를 반복적으로 비교하는 방법.
> 
   
- [트리자료구조]   
> 노드와 노드의 연결로 표현하며, 노드는 정보의 단위로서 사용되며 아래와 같은 특징들을 가진다.   
> 트리는 부모 노드와 자식 노드의 관계로 표현된다.   
> 트리의 최상단 노드를 루트 노드라고 한다.   
> 트리의 최하단 노드를 단말 노드라고 한다.   
> 트리에서 일부를 떼어내도 트리 구조이며 이를 서브 트리라 한다.   
> 트리는 파일 시스템과 같이 계층적이고 정렬된 데이터를 다루기에 적합하다.   
   
- [이진탐색트리]
> 트리 자료구조중 가장 간단한 형태이며 아래와 같은 특징들을 가진다.   
> 부모 노드보다 왼쪽 자식 노드가 작다.   
> 부모 노드보다 오른쪽 자식 노드가 크다.   
   
> 실전문제   
>> [[부품찾기]](./이진탐색/부품찾기.py)   
>> [[떡볶이떡만들기]](./이진탐색/떡볶이떡만들기.py)   
   
- [다이나믹프로그래밍]   
> 한번 계산한 문제는 다시 계산하지 않도록 하는 알고리즘.   
> * 조건   
> 1. 큰 문제를 작은 문제로 나눌 수 있다.   
> 2. 작은 문제에서 구한 정답은 그것을 포함하는 큰 문제에서도 동일하다.   
>   
> 재귀 함수를 이용하여 큰 문제를 해결하기 위해 작은 문제를 호출 - 탑다운 방식(하향식)   
> 단순히 반복문을 이용하여 작은문제부터 해결해 올라가는 - 보텀업 방식(상향식)   
>   
> 실전문제   
>> [[1로만들기]](./다이나믹프로그래밍/1로만들기.py)   
>> [[개미전사]](./다이나믹프로그래밍/개미전사.py)   
>> [[바닥공사]](./다이나믹프로그래밍/바닥공사.py)   
>> [[효율적인화폐구성]](./다이나믹프로그래밍/효율적인화폐구성.py)  
   
- [최단경로]   
> 특정 지점까지 가장 빠르게 도달하는 방법을 찾는 알고리즘   
> "최단 경로"(Shortest Path) 알고리즘은 말 그대로 가장 짧은 경로를 찾는 알고리즘이다.  
> 그래서 '길 찾기' 문제라고도 불린다.   
> 알고리즘 종류 [다익스트라], [플로이드 워셜], [벨만 포드]   
   
> [[다익스트라 최단 경로 알고리즘]](./최단경로/다익스트라.py)   
> 해당 알고리즘은 그래프에섯 여러 노드가 있을 때, 특정 노드에서 출발하여 다른 노드로 가는   
> 각각의 최단 경로를 구해주는 알고리즘.
## [Tips]
- [[수행 시간 측정 소스코드]](./Tips/수행시간측정소스코드.py)   
- [[빠르게 입력 받기]](./Tips/빠르게입력받기.py)   