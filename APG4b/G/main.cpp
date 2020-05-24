#include <iostream>
using namespace std;

int main()
{
  int a, b;
  string op;
  cin >> a >> op >> b;

  if (op == "+")
  {
    cout << a + b << endl;
  }
  else if (op == "-")
  {
    cout << a - b << endl;
  }
  else if (op == "*")
  {
    cout << a * b << endl;
  }
  else if (op == "/" && b != 0)
  {
    cout << a / b << endl;
  }
  else
  {
    cout << "error" << endl;
  }
  return 0;
}