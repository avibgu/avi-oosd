#ifndef PERSON_HPP_
#define PERSON_HPP_

class Person{

	string _name;
	string _id;

public:

	Person(string s, string id);

	string getName() { return _name; }

	string getId() { return _id; }
};

#endif /*PERSON_HPP_*/
