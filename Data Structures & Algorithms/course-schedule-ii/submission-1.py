class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if not numCourses:
            return []

        prereqToCourseMap = defaultdict(list)
        for course, prereq in prerequisites:
            prereqToCourseMap[prereq].append(course)
            
        courseToPrereqCountMap = {}
        for course in range(numCourses):
            courseToPrereqCountMap[course] = 0
            
        for prereq, dependentCourses in prereqToCourseMap.items():
            for dependentCourse in dependentCourses:
                courseToPrereqCountMap[dependentCourse] += 1
            
        coursesWithNoPrereqs = deque([])
        for course, prereqCount in courseToPrereqCountMap.items():
            if prereqCount == 0:
                coursesWithNoPrereqs.append(course)
            
        coursesInOrder = []
        while coursesWithNoPrereqs:
            currentCourse  = coursesWithNoPrereqs.popleft()
            coursesInOrder.append(currentCourse)
            currentCourseDependants = prereqToCourseMap[currentCourse]
                
            for dependantCourse in currentCourseDependants:
                courseToPrereqCountMap[dependantCourse] -= 1
                if courseToPrereqCountMap[dependantCourse] == 0:
                    coursesWithNoPrereqs.append(dependantCourse)
            
        if len(coursesInOrder) !=numCourses:
            return []#Cycle return False

        return coursesInOrder
		