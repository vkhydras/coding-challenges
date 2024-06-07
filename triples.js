function threeSum(nums) {
    nums.sort((a, b) => a - b); // Sort the array
    const triplets = [];
    const n = nums.length;

    for (let i = 0; i < n; i++) {
        // Skip the same element to avoid duplicate triplets
        if (i > 0 && nums[i] === nums[i - 1]) {
            continue;
        }

        let left = i + 1;
        let right = n - 1;

        while (left < right) {
            const total = nums[i] + nums[left] + nums[right];

            if (total === 0) {
                triplets.push([nums[i], nums[left], nums[right]]);
                left++;
                right--;

                // Skip the same elements to avoid duplicate triplets
                while (left < right && nums[left] === nums[left - 1]) {
                    left++;
                }
                while (left < right && nums[right] === nums[right + 1]) {
                    right--;
                }
            } else if (total < 0) {
                left++;
            } else {
                right--;
            }
        }
    }

    return triplets;
}

// Example usage
const nums1 = [-1, 0, 1, 2, -1, -4];
console.log(threeSum(nums1)); // Output: [[-1, -1, 2], [-1, 0, 1]]

const nums2 = [0, 1, 1];
console.log(threeSum(nums2)); // Output: []

const nums3 = [0, 0, 0];
console.log(threeSum(nums3)); // Output: [[0, 0, 0]]
