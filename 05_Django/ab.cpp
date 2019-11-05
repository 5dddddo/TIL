// #include <vector>
// #include <queue>
// using namespace std;
// int map[51][51];
// bool isNotOk[51][51];
// bool visited[51][51];
// int dir[8][2] = {{-1, -1}, {-1, 0}, {-1, 1}, {0, -1}, {0, 1}, {1, -1}, {1, 0}, {1, 1}};
// int n, res;
// queue<pair<int, int>> q;

// void check(int x, int y)
// {
//     int cnt = 0;
//     for (int k = 0; k < 9; k++)
//     {
//         int nx = x + dir[k][0];
//         int ny = y + dir[k][1];
//         if (nx > 0 && ny > 0 && nx <= n && ny <= n)
//         {
//             if (isNotOk[nx][ny])
//                 cnt++;
//         }
//     }
//     map[x][y] = cnt;
// }

// bool scheck(int x, int y)
// {
//     bool flag = false;
//     for (int k = 0; k < 9; k++)
//     {
//         int nx = x + dir[k][0];
//         int ny = y + dir[k][1];
//         if (nx > 0 && ny > 0 && nx <= n && ny <= n)
//         {
//             if (isNotOk[nx][ny])
//                 flag = true;
//         }
//     }
//     return flag;
// }
// void bfs(int x, int y)
// {
//     q.push({x, y});
//     while (!q.empty())
//     {
//         pair<int, int> tmp = q.front();
//         q.pop();
//         for (int i = 0; i < 9; i++)
//         {
//             int nx = tmp.first + dir[i][0];
//             int ny = tmp.second + dir[i][1];
//             if (nx > 0 && ny > 0 && nx <= n && ny <= n)
//             {
//                 if (!visited[nx][ny] && isNotOk[nx][ny] == false)
//                 {
//                     visited[nx][ny] = true;
//                     res++;
//                     if (!scheck(nx, ny))
//                         q.push({nx, ny});
//                 }
//             }
//         }
//     }
// }
// int solution(int N, vector<vector<int>> mine, vector<int> P)
// {
//     n = N;
//     for (int i = 0; i < mine.size(); i++)
//     {
//         vector<int> v = mine[i];
//         isNotOk[v[0]][v[1]] = true;
//     }
//     for (int i = 1; i <= N; i++)
//     {
//         for (int j = 1; j <= N; j++)
//         {
//             check(i, j);
//         }
//     }
//     visited[P[0]][P[1]] = true;
//     res++;
//     bfs(P[0], P[1]);
//     return res;
// }

#include <iostream>
#include <string>
using namespace std;
int udrl[4];
int solution(string s)
{
    int answer = 0;
    int min;


    for (int i = 0; i < s.length() -1; i++)
    {
        for (int j = 0; j < i * 2; j++)
        {
            if (s[i] == 'U')
                udrl[0]++;
            else if (s[i] == 'D')
                udrl[1]++;
            else if (s[i] == 'R')
                udrl[2]++;
            else
                udrl[3]++;
        }
        if (udrl[0] == udrl[1] && udrl[2] == udrl[3])
        {
            answer++;
            udrl[0] = udrl[1] = udrl[2] = udrl[3] = 0;
        }
    }

    return answer;
}


int main()
{

    cout << solution("URLLDRLR") << endl;
    cout << solution("RLDU") << endl;
    cout << solution("URDLDRULDLRUDLU") << endl;

}

