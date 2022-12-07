#ifndef DAY7_HPP
# define DAY7_HPP

#include <map>
#include <vector>
#include <string>

using namespace std;

class dir
{
	public :
		int size() const {
			int t = file_size;
			for (auto it = subdir.begin(); it < subdir.end(); ++it)
				t += (*it).size();
			return t;
		}
	
	private :
		string name;
		int file_size;
		vector<dir> subdir;
};

#endif