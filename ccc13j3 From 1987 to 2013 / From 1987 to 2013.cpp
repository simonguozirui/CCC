#include <iostream>
#include <vector>
using namespace std;
int main(){
	int a
	cin >>a
}

for (int i=a; i<=10234; i++){
	vector <bool> occur(10,false);
	int num = i;
	while (num>0){
		if (occurred[num%10]){
			break;
		}
		occur[num %10] = true;
		num/=10;
	}
	if (num==0){
		cout << num << endl;
		break;
	}
	return 0;
}