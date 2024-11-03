# Fitness Function Definition

Each keyboard layout will be socred on the following criterion:
| Criterion         | Variable | Prop/Inv | Calculated by           | Importance |
| :---------------- | :------- | :------- | :---------------------- | :--------- |
| # of Columns      | C        | P        | Count                   | High       |
| # of Overlaps     | O        | P        | Count                   | High       |
| # of Duplicates   | D        | P        | Count                   | Low        |
| N-gram Consistency| G        | IP       | n-grams > 1 contain root| Medium     |
| # of Splits       | S        | P        | Weighted Count by Freq  | Low        |
| Finger Movement   | M        | P        | Direct Keyword Test     | High       |
| Mistrokeibility   | P        | P        | Distance of freq letters| Low        |
| Homerow Usage     | H        | IP       | Count N-grams in homerow| Medium     |
| Unused Chords     | U        | P/IP     | Approaches 0 quickly    | Medium     |

Where the function is defined as:

$Score = ((4e^{-U} + 1)\times\frac{2O\times(M + 30S)}{H}  + \frac{100D}{G^2} + P)^C$

and a lower score is a better fit.
