# Wedding Party Seating Solution
### Author: Brandon Long


To run my solution:
- Ensure that you have installed in your environment Python 3.0+. 
- From the terminal run `Python wedding_seating.py`
- The program will direct you on how to input tables and parties.

## Architecture Overview
- The `models` package contains the classes `Party`, `Table`, and `Venue`. These classes are 
used to represent parties, tables and the venue, respectively.
- `wedding_seating.py` contains the logic for the user to interact with (View) and makes use of 
the classes defined in `models.py` as the user provides input (~Controller)

## Sample Inputs

```
MGM Grand Hotel
A-8 B-8 C-7 D-7 
Thornton-3
Garcia-2
Owens-6 ! Thornton Taylor
Smith-1 ! Garcia
Taylor-5
Reese-7
done

```

```
Gaylord Hotel
A-8 B-8 C-7 D-7  E-10 F-8 G-10 H-12
Thornton-3
Garcia-2 ! Thornton
Owens-6 ! Thornton Taylor
Smith-1 ! Garcia Thornton
Taylor-5
Reese-12
Long-4 ! Garcia
Johnson-4 ! Taylor Owens
James-5 ! Smith
Robinson-8 ! Garcia Smith
Alexander-4 ! Long Taylor
Montgomery-9 ! Garcia
Kroger-3 ! James
Bacon-4 ! Taylor
done

```
