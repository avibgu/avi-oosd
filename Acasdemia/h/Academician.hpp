#ifndef ACADEMICIAN_HPP_
#define ACADEMICIAN_HPP_

class Academician {

	list<Course*> _courses;

public:

	void addCourse(Course* c) { _courses.push_back(c); }

	void listCourses();
};

#endif /*ACADEMICIAN_HPP_*/
