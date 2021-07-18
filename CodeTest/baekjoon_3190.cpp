#include <iostream>
#include <utility>
#include <vector>
#include <deque>

using namespace std;

void draw_data() {

}

int main() {
	int snakeX = 0;
	int snakeY = 0;

	int moveX[] = { 0,1,0,-1 };
	int moveY[] = { 1,0,-1,0 };

	int size;
	cin >> size;

	int appleNum;
	cin >> appleNum;

	vector<pair<int, int>> appleP;
	for (int i = 0; i < appleNum; i++) {
		int mX, mY;
		cin >> mX >> mY;
		appleP.push_back(pair<int, int>(mX-1, mY-1));
	}

	int dirChangeCount;
	cin >> dirChangeCount;
	vector<pair<int, char>> dirChanges;
	for (int i = 0; i < dirChangeCount; i++) {
		int time;
		char direction;
		cin >> time >> direction;
		dirChanges.push_back(pair<int, char>(time, direction));
	}

	int time = 0;
	int dir_check = 0;
	int turn_data = 0;
	bool die = false;
	bool getApple;

	deque<pair<int,int>> snake;
	snake.push_back(pair<int,int>(0,0));


	//draw data
	vector<vector<char>> draw;
	for (int i = 0; i < size; i++) {
		draw.push_back(vector<char>(size, 'O'));
	}
	
	for (int i = 0; i < appleNum; i++) {
		draw[appleP[i].first][appleP[i].second] = 'A';
	}


	for (int i = 0; i < size; i++) {
		for (int j = 0; j < size; j++)
			std::cout << draw[i][j];
		std::cout << endl;
	}

	

	while (true) {
		time++;
		getApple = false;
		pair<int, int> head = snake.back();
		if (turn_data < 0)
			turn_data += 4;
		int nextX = head.first + moveX[turn_data % 4];
		int nextY = head.second + moveY[turn_data % 4];

		// 벽 체크
		if (nextX < 0 || nextY < 0 || nextX >= size || nextY >= size)
			break;
		
		//몸 체크
		for (int i = 0; i < snake.size(); i++) {
			if (snake[i].first == nextX && snake[i].second == nextY) {
				die = true;
				break;
			}
		}
		if (die)
			break;

		//사과를 먹는지 체크
		for (int i = 0; i < appleP.size(); i++) {
			if (appleP[i].first == nextX && appleP[i].second == nextY) {
				getApple = true;
				appleP.erase(appleP.begin() + i);
				break;
			}
		}
		if (!getApple) {
			snake.pop_front();
		}
		snake.push_back(pair<int, int>(nextX, nextY));

		//방향변환 체크
		if (dir_check < dirChangeCount) {
			if (dirChanges[dir_check].first == time) {
				// 왼쪽
				if (dirChanges[dir_check].second == 'L')
					turn_data--;
				//오른쪽
				if (dirChanges[dir_check].second == 'D')
					turn_data++;

				dir_check++;
			}
		}
		
	}

	std::cout << time;
}