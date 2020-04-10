#include      <bits/stdc++.h> /*{{{*/
using namespace std;

map <string, string> mp;

signed main() {
  ifstream mf("./unicode-to-utf8.txt");
  if (mf.is_open()) {
    string key, val;
    while (mf >> key >> val) {
      mp.insert(make_pair(key, val));
    }
  }
  string foo, emo, uni, utf8;
  ifstream md("./emoji-unicode-slicedunicode.txt");
  while (getline(md, foo)) {
    istringstream iss(foo);
    iss >> emo >> uni >> utf8;

    // cout << emo << ' ' << uni << ' ' << utf8 << '\n';

    auto it = mp.find(utf8);
    if (it != mp.end()) {
      cout << emo << ": " << "\"" << it->second << "\",\n";
    }
    else cout << emo << ": " << uni << '\n';
    cout << flush;
  }

  return EXIT_SUCCESS;
}


