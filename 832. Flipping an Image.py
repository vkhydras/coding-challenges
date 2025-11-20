class Solution(object):
    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """
        for m in image:
            m.reverse()
        
        for m in range(len(image)):
            for n in range(len(image[m])):
                if image[m][n] == 0:
                    image[m][n] = 1
                else:
                    image[m][n] = 0
        
        return image
        