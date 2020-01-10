#include <iostream>
#include <algorithm>
#include <vector>
#include <numeric>
#include <string>
#include <cstdlib>

using namespace std;

//参考url:https://qiita.com/zenrshon/items/cd19361842ae887afe8a


int main() {

//data roader
  
  //Nは入力数
  int N;

  cin>>N;

  vector<int> a;
  int l=0;

  for(int i=0;i<N;i++){
    cin>>l;
    a.emplace_back(l);
  }


  int ans=0;

  for(int i=0;i<a.size();i++){
    ans+=a[i];
    cout<<"input["<<i<<"]"<<":";
    cout<<a[i]<<endl;
  }

  cout<<"sum:";
  cout<<ans<<endl;

  return 0;
}