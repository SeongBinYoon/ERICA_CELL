# ERICA_CELL

Hanyang University ERICA Division of Computer Science

2019082206 윤성빈 yoonseongbin4925@gmail.com  
2019089034 김현진 hikhjin@gmail.com


The Zombie 사용자 매뉴얼



A.	본 게임 방법

1.	생존자 캠프를 찾아서 떠날지 선택한다. 떠나지 않을 경우 게임이 종료된다.
2.	반주사위를 굴리면 1~3까지 랜덤하게 수가 출력된다.
3.	질문이 출력되고, 선택지 1 과 2 중 적절한 선택지를 골라 숫자(1 또는 2)를 입력한다.
4.	만약 적절한 답을 입력한다면 A-3의 반주사위를 굴려 나온 수 대로 전진하게 되고 현재 자신의 칸을 출력한다. 그러나 틀린 답을 입력한다면 사망 위기에 처하며, 미니게임을 통해 생존 기회를 얻을 수 있다.
5.	이렇게 게임을 진행하면서 자신의 칸이 20칸을 넘게 되면 백신을 구해 이기게 된다.


B.	미니게임(숫자맞추기게임) 방법

숫자맞추기게임은 사용자가 잘못된 선택지를 골라 사망 위기에 처했을 때 주어지는 생존 기회이다. 이를 통과해야 다음 칸으로 전진할 수 있다.
컴퓨터가 임의로 세자리 수를 만든다. 이 때, 각 자리의 수는 모두 달라야 하며 첫째 자리 수에 0을 입력할 수 없다. 이 세자리 수를 주어지는 단서, 즉 strike와 ball을 이용해 맞추는 게임이다. 단, 기회는 8번이다.
1. Strike: 숫자와 위치가 전부 맞음
2. Ball: 숫자는 맞았지만 위치가 틀림.
3. Out: 숫자와 위치가 전부 틀림.
예를 들어, 컴퓨터가 만든 세 자리 수를 172 이라고 해보자. 이 때 사용자가 123 이라는 수로 추측하여 이를 입력한다면, 1은 숫자와 위치 모두 맞으므로 strike: 1 이라고 호출될 것이고, 2는 숫자는 맞지만 위치가 다르므로 ball: 1 이라고 호출될 것이다. 나머지 3은 숫자와 위치 모두 틀렸으므로 out이다. 총 기회가 8번이므로 단서를 얻을 수 있는 기회는 7번이다. 이 안에 모든 숫자와 위치를 알아내서 입력해야 한다. 


C.	미니게임(스도쿠게임) 방법

스도쿠게임은 숫자맞추기게임과 같이 사용자가 잘못된 선택지를 골라 사망 위기에 처했을 때 주어지는 생존 기회이다. 이를 통과해야 다음 칸으로 전진할 수 있다.
가로와 세로 각각 6칸씩, 모두 36칸으로 이루어진 정사각형의 빈칸을 채우는 게임이다. 이를 다시 ‘구역’ 이라고 하는 가로 세로 각 2칸, 모두 4칸인 작은 사각형으로 나눈다. 몇몇 자리에는 이미 수가 채워져 있다. 채워진 숫자들을 이용하여 나머지 빈칸에 1부터 6까지의 숫자가 겹치지 않도록 채워나간다. 각 세로줄과 가로줄의 빈 칸에는 숫자를 한 번만 사용해야 한다.
사용자는 먼저 난이도(상, 중, 하)를 선택한다. 난이도에 따라 빈칸의 수가 정해진다. 난이도가 높을수록 빈칸이 많다.
추론한 수를 입력하기 위해서는 먼저 가로의 몇 번째 줄인지, 세로의 몇 번째 줄인지 입력해야한다. 순서대로 입력 후 사용자가 추론한 수를 입력한다.

