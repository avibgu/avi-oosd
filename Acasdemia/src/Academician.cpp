#include <Academician.hpp>

#include <string>


void Academician::listCourses(){

	std::list<Course*>::iterator iter;

	for (iter=_courses.begin(); iter != _courses.end(); iter++) {

		std::cout << (*iter)->getId() << std::endl;
	}
}
