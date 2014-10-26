# Expose methods for opening and closing gzipped files. Note that if the file
# is not gzipped, gzopen still works.
cdef extern from "zlib.h":

    ctypedef void* gzFile
    gzFile gzopen(const char* file_name, const char* mode)
    void gzclose(gzFile f)

# Expose methods declared in the kseq macros.
cdef extern from "kseq.h":

    ctypedef struct kseq_t:
        pass

    kseq_t* kseq_init(gzFile f)

    int kseq_read(kseq_t* seq)

    void kseq_destroy(kseq_t* ks)

    char* kseq_get_name(kseq_t* ks)
    size_t kseq_get_name_len(kseq_t* ks)
    
    char* kseq_get_sequence(kseq_t* ks)
    size_t kseq_get_sequence_len(kseq_t* ks)

    char* kseq_get_quality(kseq_t* ks)
    size_t kseq_get_quality_len(kseq_t* ks)

# Finally, expose functions for reversing or reverse complementing a string.
cdef extern from "reverse_complement.h":

    void reverse_complement(char* s, size_t s_len)
    void reverse(char* s, size_t s_len)
