# cython: profile=True
from libc.stdlib cimport malloc, free
from libc.string cimport strncpy

cimport ckseq

# Provide simple wrapper classes to make FastxIO compatible with
# pbcore.io.Fast[aq]IO
class FastaReader(FastxReader):
    pass    

class FastaRecord(FastxRecord):
    pass 

class FastqReader(FastxReader):
    pass

class FastqRecord(FastxRecord):
    pass

cdef class FastxReader:
    """FastxReader wraps the IO functions in kseq.h. It is iterable and
    is an iterator. It yields FastxRecords.
    """
    cdef ckseq.gzFile _gzfile
    cdef ckseq.kseq_t* _c_kseq

    def __cinit__(self, char* file_name):
       self._gzfile = ckseq.gzopen(file_name, "r")
       self._c_kseq = ckseq.kseq_init(self._gzfile)
    
    def __iter__(self):
        return self

    def __next__(self):
        """Step to the next record in the file, and return it.

        Note that cython requires iterator be __next__, not next.
        """
        ret = ckseq.kseq_read(self._c_kseq)

        if ret == -1:
            raise StopIteration
        
        record = FastxRecord()
        record._init_from_kseq(self._c_kseq)

        return record

    def __dealloc__(self):
       self.close()

    def close(self):
        ckseq.kseq_destroy(self._c_kseq)
        ckseq.gzclose(self._gzfile)
    
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

cdef class FastxRecord:
    """Interface to a Fasta or Fastq record.
    
    Note that the strings from kseq.h aren't null-terminated.
    """ 

    cdef char* _name
    cdef size_t _name_len

    cdef char* _sequence
    cdef size_t _sequence_len

    cdef char* _quality
    cdef size_t _quality_len
    
    def __cinit__(self):
        self._name = NULL
        self._sequence = NULL
        self._quality = NULL
        self._name_len = 0
        self._sequence_len = 0
        self._quality_len = 0

    cdef _reset(self):
        if self._name is not NULL: free(self._name)
        if self._sequence is not NULL: free(self._sequence)
        if self._quality is not NULL: free(self._quality)
        self._name_len = 0
        self._sequence_len = 0
        self._quality_len = 0

    def __dealloc__(self):
        self._reset()
    
    def reverseComplement(self):
        """Create a new FastxRecord that's the reverse complement of
        this one, and return it.
        """

        rec = FastxRecord()
        
        rec._init_from_c_strings(
            self._name, self._name_len, self._sequence, self._sequence_len,
            self._quality, self._quality_len)
        
        rec.reverseComplementInPlace()

        return rec
    
    def reverseComplementInPlace(self):
        """Reverse complement the sequence in-place. This only requires
        a little O(1) space.
        """
        
        ckseq.reverse_complement(self._sequence, self._sequence_len)
        ckseq.reverse(self._quality, self._quality_len)

    cdef void _init_from_c_strings(self, char* name, size_t name_len,
                                   char* sequence, size_t sequence_len,
                                   char* quality, size_t quality_len):
        """Initialize a FastxRecord from C strings and lengths. Optionally,
        reverse complement those string.
        """
        self._reset()
         
        self._name_len = name_len
        self._name = <char*>malloc(self._name_len + 1)
        strncpy(self._name, name, self._name_len)
        self._name[self._name_len] = '\0'
        
        self._sequence_len = sequence_len
        self._sequence = <char*>malloc(self._sequence_len + 1)
        strncpy(self._sequence, sequence, self._sequence_len)
        self._sequence[self._sequence_len] = '\0'
    
        self._quality_len = quality_len
        self._quality = <char*>malloc(self._quality_len)
        strncpy(self._quality, quality, self._quality_len)
        self._quality[self._quality_len] = '\0'

    cdef void _init_from_kseq(self, ckseq.kseq_t* kseq):
        """Initialize a FastxRecord from a kseq_t object."""        
        self._reset() 

        self._name_len = ckseq.kseq_get_name_len(kseq) 
        self._name = <char*>malloc(self._name_len + 1)
        strncpy(self._name, ckseq.kseq_get_name(kseq), self._name_len)
        self._name[self._name_len] = '\0'

        self._sequence_len = ckseq.kseq_get_sequence_len(kseq) 
        self._sequence = <char*>malloc(self._sequence_len + 1)
        strncpy(self._sequence, ckseq.kseq_get_sequence(kseq), self._sequence_len)
        self._sequence[self._sequence_len] = '\0'
    
        self._quality_len = ckseq.kseq_get_quality_len(kseq) 
        self._quality = <char*>malloc(self._quality_len + 1)
        strncpy(self._quality, ckseq.kseq_get_quality(kseq), self._quality_len)
        self._quality[self._quality_len] = '\0'

        
    @property
    def name(self):
        return self._name
    
    @property
    def sequence(self):
        return self._sequence

    @property
    def quality(self):
        return self._quality
