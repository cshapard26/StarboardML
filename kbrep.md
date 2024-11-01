# Keyboard Representation

How do I represent a keyboard in code? Well, for my OPOCKeyboard, the rows are ortholinear, so a matrix would work perfectly:
```
[S T P H
 S K W R]
```
However, the system is also chorded, so multiple keys can be pressed at the same time to represent a new key. In my previous designs, I have represented this with a stacked matrix:
```
[STR ST  ST  STH
 SR  S   T   TH
 SR  R   H   TH
 SHR L   L   THR]
```
where the corners represent three presses, the edges represent two presses, and the centers represent one press. So the top left `STR` represents pressing all three center keys along the corner: `S` `T` and `R`. The example above is of a 2x2 keyboard. Note that the combination of `RH` produces `L`. Since RH is not a sound that appears in the English language, we can substitute it for a different, more useful letter.

This representation is inefficient because of its many duplicates, and it becomes much harder to use for larger matricies.

Instead, I plan to use a matrix-map hybrid. The matrix will contain the direct keys, and the matrix will contain combinations of them. For example:
```
[R T
 S H
 L M]
+
{TR: R;T,
 F: S;R,
 SL: S;L,
 N: S;L,
 ...
}
```

Thus, if the bigram "SHR" appears in the text, then the dictionary will be queried for "SHR" wherepon it returns the direct keys in the chord. Note that some keys are mapped to the same chord. This occurs when a single chord can have multiple possible representations, which is useful when two letters are very rarely--but still possibly--used together and could be more efficently converted to a third character.

The matrix will be created using nested lists where each sublist is a column. So the matrix in the previous example would be
```
[[R, S, L],
 [T, H, M]]
```
in python.

The dataset is based on the following n-grams for beginning clusters:

- 1-grams: B, D, F, G, H, J, K, L, M, N, P, Q, R, S, T, V, W, Y, Z
- 2-grams: BL, BR, DR, FL, FR, GL, GR, KH, KL/CL, KR, PL, PR, SH, SK, SF, SL, SM, SN, SP, SQ, ST, SW, TH, TR, TW
- 3-grams: SHR, STR, SPL, SKR, SPR, SKH, THR

With the special, weighted cases:
- KW = Q
- C = K
- WH = W
- WR = R
- PH = F
