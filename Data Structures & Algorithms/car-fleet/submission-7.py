class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Sort by position DESCENDING (closest to target first)
        cars = [(position[i], speed[i]) for i in range(len(position))]
        cars.sort(reverse=True)
        
        fleets = 0
        last_time = -1.0
        
        for pos, spd in cars:
            time = (target - pos) / spd
            if time > last_time:
                fleets += 1
                last_time = time
        
        return fleets
