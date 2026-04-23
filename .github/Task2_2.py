def copy(nums:list[int]) -> list[int]:
    new_list = []
    for idx in range(len(nums)):
        new_list.append(nums[idx])     # Record each value of new_list and idx at the end of the loop body.
    return new_list                    # How does this loop differ from that above?

result = copy([4, 9, 2, 1])
# new_list = [4, 9, 2, 1]
# idx = 3
# the loop is different because it copies the values from the other list rater than add them up consecutively