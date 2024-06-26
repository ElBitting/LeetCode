class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        movecounter = 0
        seats = sorted(seats)
        for seat in seats:
            if seat in students:
                students.pop(students.index(seat))
            else:
                y = min(students)
                movecounter += abs(seat - y)
                students.pop(students.index(y))
        return(movecounter)
