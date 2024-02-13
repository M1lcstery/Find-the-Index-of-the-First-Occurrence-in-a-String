class Solution(object):
    def strStr(self, haystack, needle):
      try:
        index = haystack.index(needle)
        return index
      except ValueError:
          return -1

       