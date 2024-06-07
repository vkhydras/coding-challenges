function threeSumClosest(nums, target) {
    nums.sort((a, b) => a - b); // Sort the array
    let closestSum = nums[0] + nums[1] + nums[2]; // Initialize closest sum to the sum of the first three elements

    for (let i = 0; i < nums.length - 2; i++) {
        // Skip the same element to avoid unnecessary calculations
        if (i > 0 && nums[i] === nums[i - 1]) {
            continue;
        }

        let left = i + 1;
        let right = nums.length - 1;

        while (left < right) {
            const currentSum = nums[i] + nums[left] + nums[right];

            // If the current sum is exactly the target, return it immediately
            if (currentSum === target) {
                return currentSum;
            }

            // Update the closest sum if the current sum is closer to the target
            if (Math.abs(currentSum - target) < Math.abs(closestSum - target)) {
                closestSum = currentSum;
            }

            // Move the pointers based on the comparison with the target
            if (currentSum < target) {
                left++;
            } else {
                right--;
            }
        }
    }

    return closestSum;
}

// Example usage
const nums1 = [-1, 2, 1, -4];
const target1 = 1;
console.log(threeSumClosest(nums1, target1)); // Output: 2

const nums2 = [0, 0, 0];
const target2 = 1;
console.log(threeSumClosest(nums2, target2)); // Output: 0
