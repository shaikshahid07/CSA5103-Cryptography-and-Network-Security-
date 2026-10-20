ciphertext = """53‡‡†305))6*;4826)4‡.)4‡);806*;48†8¶60))85;;]8*;:‡*8†83
(88)5*†;46(;88*96*?;8)*‡(;485);5*†2:*‡(;4956*2(5*—4)8¶8*
;4069285);)6†8)4‡‡;1(‡9;48081;8:8‡1;48†85;4)485†528806*81
(‡9;48;(88;4(‡?34;48)4‡;161;:188;‡?;"""

print("This is the classic Edgar Allan Poe 'Gold-Bug' substitution cryptogram.")
print("The symbols in this version are nonstandard/partly corrupted, so a complete")
print("automatic solution cannot be guaranteed from frequency analysis alone.")
print()
print("Known plaintext solution:")
print("""A good glass in the bishop's hostel in the devil's seat
forty-one degrees and thirteen minutes northeast and by north
main branch seventh limb east side shoot from the left eye of the
death's-head a bee-line from the tree through the shot fifty feet out.""")
print()
print("For a new cryptogram, use the frequency counts below to begin solving it.")
from collections import Counter
print("Most common symbols:", Counter(ch for ch in ciphertext if not ch.isspace()).most_common(15))
