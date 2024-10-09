#include <bits/stdc++.h>
using namespace std;
int calc(int x){
    int tanu=x*(x-1)/2;
    return tanu;
}
int dosomething(vector <int> &a){
        int ma = *max_element(a.begin()+1, a.end());
        std::vector<int> b(ma+1,0);
        for(int num : a) {
            b[num]++;
        }
        int maxy = *max_element(b.begin()+1, b.end());
        int maxy_index = -1;
        for(int i=1; i<b.size(); ++i) {
            if(b[i] == maxy) {
                maxy_index = i;
                break;
            }
        }
        maxy+=b[0];
        int tanu=maxy*(maxy-1)/2;
        for(int i=1;i<b.size();++i){
            if(b[i]!=0 && i!=maxy_index){
                tanu=tanu+calc(b[i]);
            }
        }
    return tanu;
}
int main() {
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        int ind,val;
        vector<int> a(n,0);
        vector<int> tanu(n,0);
        int t;
        for (int i = 0; i < n; ++i) {
            cin >> ind >> val;
            a[ind-1]=val;
            int t = dosomething(a);
            tanu.push_back(t);
        }
        for(int i = 0; i < n; ++i) {
            cout<<tanu[i]<<" ";
        }
        cout<<endl;
    }
}