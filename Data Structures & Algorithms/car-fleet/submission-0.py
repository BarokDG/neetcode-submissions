class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(position[i], speed[i]) for i in range(len(position))]
        pairs.sort(key=lambda k: k[0], reverse=True)

        fleet = []
        for (pos, speed) in pairs:
            time_to_reach_target = (target - pos) / speed

            if fleet and fleet[-1] >= time_to_reach_target:
                continue

            fleet.append(time_to_reach_target)

        return len(fleet)