class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:               
            return True
        if not numCourses:
            return True
        
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
            return False #Cycle return False

        return True
		

