#include "day7.hpp"
#include <fstream>
#include <iostream>
#include <map>
#include <string>

void	fill_dir(ifstream &f, dir& current_dir)
{
	std::string line;
	if (getline(f, line ))
	{
		if (line.compare(0, 3, "dir") == 0)
		{
			current_dir.add_subdir(line.substr(4));
			fill_dir(f, current_dir);
		}
		else if (line == "$ cd ..")
			return ;
		else if (line == "$ ls")
			fill_dir(f, current_dir);
		else if (line[0] >= '0' && line[0] <= '9')
		{
			current_dir += stoi(line);
			fill_dir(f, current_dir);
		}
		else if (line.compare(0, 4, "$ cd") == 0)
		{
			fill_dir(f, current_dir.searchsubdir(line.substr(5)));
			fill_dir(f, current_dir);
		}
		else
			throw(logic_error("strange line : " + line));
	}
}

int main()
{
	ifstream f("./input.txt");
	dir root;
	string temp;

	getline(f, temp);  // skip cd /
	getline(f, temp);  // skip ls
	try
	{
		fill_dir(f, root); // parse the whole input.txt file
	}
	catch (exception &e)
	{
		cout << e.what() << std::endl;
		return (1);
	}

	// DEBUG
	//cout << root;

	vector<pair<string, int>> alldirs;
	list_alldirs(alldirs, root);
	sort(alldirs.begin(), alldirs.end(), cmp_alldirs);
	
	int under_100k = 0;
	auto it = alldirs.begin();
	while (it != alldirs.end() && (*it).second < 100000)
	{
		under_100k += (*it).second;
		++it;
	}
	cout << "PART1 : Total size of dirs < 100000 : " << under_100k << endl;

	int	unused_space = 70000000 - root.size();
	it = alldirs.begin();
	while (it != alldirs.end() && (unused_space + (*it).second) < 30000000)
		++it;

	cout << "PART2 : Size of the dir to delete :   " << (*it).second << endl;

	return (0);
}