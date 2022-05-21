# hexadocu

Just a regular sudoku puzzle EXCEPT there are 16 possible values.

Possible values:
1~9 and A~G
* I know regular hex values range from 0~9 and A~F but wtf. fk it.

## Build Plan
1. Use python to generate thousands of possible sudoku puzzles with varying difficulty.
2. Store the generated puzzles in a database
3. Access and fetch appropriate puzzle from the database (js)
4. Display the fetched puzzle to user (js)
5. Check the user submitted version with the solution (js)
6. Assign score and put on leaderboard (js)
    - Only store top 100