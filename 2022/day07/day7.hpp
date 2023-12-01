#ifndef DAY7_HPP
# define DAY7_HPP

#include <map>
#include <vector>
#include <string>
#include <exception>
#include <stdexcept>
#include <iostream>
#include <algorithm>
#include <utility>

using namespace std;

class dir
{
	public :

		// CONSTRUCTOR
		dir(string name="root") : _name(name), _files_size(0), _subdir() {};

		// METHODS
		int size() const {
			int t = _files_size;
			for (auto it = _subdir.begin(); it != _subdir.end(); ++it)
				t += (*it).size();
			return t;
		}

		void	add_subdir(string name){_subdir.push_back(dir(name));}

		dir&	searchsubdir(string name)
		{
			for (auto it = _subdir.begin(); it != _subdir.end(); ++it)
			{
				if ((*it)._name == name)
					return (*it);
			}
			throw(logic_error("no subdir with this name" + name));
		}

		// OVERLOAD
		void	operator+=(int n){_files_size+=n;}

		// GETTER
		string				get_name() const {return this->_name;}
		int					get_files_size() const {return this->_files_size;}
		vector<dir>	const&	get_subdir() const {return this->_subdir;}
	
	private :
		string		_name;
		int			_files_size;
		vector<dir>	_subdir;
};

bool cmp_alldirs(pair<string, int> &d1, pair<string, int> &d2){return (d1.second < d2.second);}

void	list_alldirs(vector<pair<string, int>> &alldirs, dir const&current_dir)
{
	alldirs.push_back(make_pair(current_dir.get_name(), current_dir.size()));
	for (auto it = current_dir.get_subdir().begin(); it != current_dir.get_subdir().end(); ++it)
	{
		list_alldirs(alldirs, *it);
	}
}

ostream& operator<<(ostream& os, const dir& dir)
{
	vector<pair<string, int>> alldirs;
	list_alldirs(alldirs, dir);
	sort(alldirs.begin(), alldirs.end(), cmp_alldirs);

	for (auto it = alldirs.begin(); it != alldirs.end(); ++it)
	{
		std::cout << (*it).first << " " << (*it).second << endl;
	}
	
    return os;
}

#endif