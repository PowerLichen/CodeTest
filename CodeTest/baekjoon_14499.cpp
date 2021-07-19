#include <iostream>
#include <vector>

using namespace std;

inline void swap(int& a, int& b) {
	int temp = a;
	a = b;
	b = temp;
}

class Dice {
public:
	int getTopNumber() {
		return line[0];
	}
	int getBottomNum() {
		return line[2];
	}
	void setDiceNumber(int num) {
		line[2] = num;
	}
	void rotateDice(int dir) {
		int temp;
		switch (dir) {
		case 1:
			swap(west, line[0]);
			swap(west, line[2]);
			swap(east, line[2]);
			break;
		case 2:
			swap(east, line[0]);
			swap(east, line[2]);
			swap(west, line[2]);
			break;
		case 3:
			temp = line[0];
			for (int i = 0; i < 3; i++)
				line[i] = line[i + 1];
			line[3] = temp;
			break;
		case 4:
			temp = line[3];
			for (int i = 3; i > 0; i--)
				line[i] = line[i - 1];
			line[0] = temp;
			break;
		default:
			break;
		};
	}

private:
	int line[4] = { 0,0,0,0 };
	int east = 0;
	int west = 0;
};

int main() {
	Dice dice;

	int mapHeight, mapWidth;
	int curX, curY;
	int count;
	cin >> mapHeight >> mapWidth >> curX >> curY >> count;

	vector<vector<int>> map(mapHeight, vector<int>(mapWidth,0));

	for (int i = 0; i < mapHeight; i++)
		for (int j = 0; j < mapWidth; j++)
			cin >> map[i][j];

	int num;
	for (int i = 0; i < count; i++) {
		cin >> num;

		int nextX = curX;
		int nextY = curY;
		
		switch (num) {
		case 1:
			nextY++; break;
		case 2:
			nextY--; break;
		case 3:
			nextX--; break;
		case 4:
			nextX++; break;
		default:
			break;
		};

		if (nextX < 0 || nextX >= mapHeight)
			continue;
		if (nextY < 0 || nextY >= mapWidth)
			continue;

		dice.rotateDice(num);

		curX = nextX;
		curY = nextY;

		if (map[curX][curY] == 0) {
			map[curX][curY] = dice.getBottomNum();
		}
		else {
			dice.setDiceNumber(map[curX][curY]);
			map[curX][curY] = 0;
		}


		cout << dice.getTopNumber() << endl;
	}
}