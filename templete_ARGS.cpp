#include <iostream>
#include <algorithm>
#include <vector>
#include <numeric>
#include <string>
#include <cstdlib>

using namespace std;


int main(int argc, char *argv[]) {

//data roader
  //argcは引数の数(先頭の実行ファイルも含む)
  int m=argc-1;

  vector<int> a;

  //argvはコマンドライン引数
  //argvは文字列として読み込まれる
  for(int i=0;i<m;i++){
    a.emplace_back(atoi(argv[i+1]));
  }

  int ans=0;

  for(int i=0;i<a.size();i++){
    ans+=a[i];
    cout<<"argv["<<i<<"]"<<":";
    cout<<a[i]<<endl;
  }

  cout<<"sum:";
  cout<<ans<<endl;

  return 0;
}