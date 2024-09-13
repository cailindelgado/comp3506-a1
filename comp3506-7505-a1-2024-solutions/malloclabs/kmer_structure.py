"""
Skeleton for COMP3506/7505 A1, S2, 2024
The University of Queensland
Joel Mackenzie and Vladimir Morozov

MallocLabs K-mer Querying Structure
"""

from typing import Any

"""
You may wish to import your data structures to help you with some of the
problems. Or maybe not.
"""
from structures.dynamic_array import DynamicArray

class KmerStore:
    """
    A data structure for maintaining and querying k-mers.
    You may add any additional functions or member variables
    as you see fit.
    At any moment, the structure is maintaining n distinct k-mers.
    """

    def compl(self, nuc: str) -> str:
        """
        Given nucleotide, return the complement nucleotide
        """
        if nuc == 'A':
            return 'T'
        if nuc == 'T':
            return 'A'
        if nuc == 'C':
            return 'G'
        if nuc == 'G':
            return 'C'

    def nuc_ix(self, nuc: str) -> int:
        """
        Given nucleotide, map to integer
        """
        if nuc == 'A':
            return 0
        if nuc == 'T':
            return 1
        if nuc == 'C':
            return 2
        if nuc == 'G':
            return 3

    def pair_ix(self, pair: tuple[str, str]) -> int:
        """
        Mapping nucleotides to integer indexes
        """
        n1, n2 = pair
        return self.nuc_ix(n1) * 4 + self.nuc_ix(n2)


    NUC = ['A', 'C', 'T', 'G']

    def __init__(self, k: int) -> None:
        """
        Our approach stores an array of k-mers with a buddy-array
        containing cumulative sums of frequency counts.
        """
        self._k = k
        self._starts = DynamicArray()
        for _ in range(16):
            self._starts.append(0)

        self._size = 0
        self._arr = DynamicArray()
        self._cumulative = DynamicArray()

    def __str__(self):
        return str(self._arr)

    def __repr__(self):
        return self.__str__()

    def read(self, infile: str) -> None:
        """
        Given a path to an input file, break the sequences into
        k-mers and load them into your data structure.
        """
        # https://www.youtube.com/watch?v=OIzOUXAAyZM
        pass

    def batch_insert(self, inkmers: list[str]) -> None:
        """
        Given a list of m k-mers, insert them into the structure keeping duplicates. 
        [V2: Correction]
        If the data structure contains n elements, and the input kmer list
        contains m elements, the targeted time complexity is:
        O(m log m) + O(n + m) amortized time (or better, of course!)
        """
        if len(kmers) == 0:
            return

        kmers = DynamicArray()
        kmers.build_from_list(inkmers)
        kmers.sort()
        groups = DynamicArray()

        # Walk the kmers and build tuples of kmer/counts
        ix = 0
        groups.append((kmers[0], 1))
        for k in kmers[1:]:
            kmer, cnt = groups[ix]
            if k == kmer:
                groups[ix] = (kmer, cnt + 1)
            else:
                groups.append((k, 1))
                ix += 1
       
        # The annoying bit - cleaning up the insertion with what we already have
        iold = 0
        inew = 0
        new_arr = DynamicArray()
        while iold < self._arr.get_size() or inew < groups.get_size():
            if iold < self._arr.get_size() and inew < groups.get_size():
                kold, cntold = self._arr[iold]
                knew, cntnew = groups[inew]
                if kold < knew:
                    new_arr.append((kold, cntold))
                    iold += 1
                elif kold > knew:
                    new_arr.append((knew, cntnew))
                    inew += 1
                else:
                    new_arr.append((knew, cntnew + cntold))
                    inew += 1
                    iold += 1
            elif iold < self._arr.get_size():
                new_arr.append(self._arr[iold])
                iold += 1
            else:
                new_arr.append(groups[inew])
                inew += 1

        self._arr = new_arr

        # Take care of the complement queries
        for i in range(16):
            self._starts[i] = 0

        self._cumulative = DynamicArray()
        cumulative = 0

        for k, count in new_arr.iterate():
            self._starts[self.pair_ix((k[0], k[1]))] += count

            self._cumulative.append(cumulative)
            cumulative += count

        self._size = cumulative


    def batch_delete(self, kmers: list[str]) -> None:
        """
        Given a list of m k-mers, delete the matching ones
        (including all duplicates).
        [V2: Correction]
        If the data structure contains n elements, and the input kmer list
        contains m elements, the targeted time complexity is:
        O(m log m) + O(n + m) amortized time (or better, of course!)
 
        """
        if len(kmers) == 0:
            return
        if self._size == 0:
            return

        kmers.sort()
        groups = DynamicArray()

        ix = 0
        groups.append((kmers[0], 1))
        for k in kmers[1:]:
            kmer, cnt = groups[ix]
            if k == kmer:
                groups[ix] = (kmer, cnt + 1)
            else:
                groups.append((k, 1))
                ix += 1

        iold = 0
        inew = 0
        new_arr = DynamicArray()
        while iold < self._arr.get_size() or inew < groups.get_size():
            if iold < self._arr.get_size() and inew < groups.get_size():
                kold, cntold = self._arr[iold]
                knew, cntnew = groups[inew]
                if kold < knew:
                    new_arr.append((kold, cntold))
                    iold += 1
                elif kold > knew:
                    inew += 1
                else:
                    inew += 1
                    iold += 1

            elif iold < self._arr.get_size():
                new_arr.append(self._arr[iold])
                iold += 1

        self._arr = new_arr

        for i in range(16):
            self._starts[i] = 0

        self._cumulative = DynamicArray()
        cumulative = 0

        for k, count in new_arr.iterate():
            self._starts[self.pair_ix((k[0], k[1]))] += count

            self._cumulative.append(cumulative)
            cumulative += count

        self._size = cumulative

    def freq_geq(self, m: int) -> list[str]:
        """
        Given an integer m, return a list of k-mers that occur
        >= m times in your data structure.
        Time complexity for full marks: O(n)
        """

        # Idea: Walk the array (it is O(n) after all) and just add to the
        # list if the count is geq m
        ans = []
        for kmer, cnt in self._arr.iterate(): 
            if cnt >= m:
                ans.append(kmer)
        return ans

    def count(self, kmer: str) -> int:
        """
        Given a k-mer, return the number of times it appears in
        your data structure.
        Time complexity for full marks: O(log n)
        """
       
        # Idea: Just binary search for the kmer!

        if self._arr.get_size() == 0:
            return 0

        start = 0
        end = self._arr.get_size() - 1 

        while start < end:
            mid = (start + end) // 2
            k, cnt = self._arr[mid]
            if k == kmer:
                return cnt
            elif k < kmer:
                start = mid + 1
            else:
                end = mid - 1
        
        k, cnt = self._arr[start]
        if k == kmer:
            return cnt
        return 0

    def count_geq(self, kmer: str) -> int:
        """
        Given a k-mer, return the total number of k-mers that
        are lexicographically greater or equal.
        Time complexity for full marks: O(log n)
        """
        # We store nothing - back out
        if self._arr.get_size() == 0:
            return 0

        # The query is larger than our largest - back out
        if kmer > self._arr[self._arr.get_size() - 1][0]:
            return 0

        # The query is smaller than our smallest - return total size
        if kmer <= self._arr[0][0]:
            return self._size

        # OK, better do some real work now...
        start = 0
        end = self._arr.get_size() - 1

        # Good old binary search!
        while start < end:
            mid = (start + end) // 2
            k, cnt = self._arr[mid]
            if k == kmer:
                return self._size - self._cumulative[mid] 
            elif k < kmer:
                start = mid + 1
            else:
                end = mid - 1
        
        # Final check: If the element we landed at is less than the query
        # kmer, our cumulative sum needs to be on the element to the right
        k, cnt = self._arr[start]
        if k < kmer:
            start += 1

        return self._size - self._cumulative[start]

    def compatible(self, kmer: str) -> int:
        """
        Given a k-mer, return the total number of compatible
        k-mers. You will be using the two suffix characters
        of the input k-mer to compare against the first two
        characters of all other k-mers.
        Time complexity for full marks: O(1) :-)
        """

        # Hard work done during insertion, just return the count
        n1 = self.compl(kmer[self._k - 2]) 
        n2 = self.compl(kmer[self._k - 1]) 
        return self._starts[self.pair_ix((n1, n2))]

