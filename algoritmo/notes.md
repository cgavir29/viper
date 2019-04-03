new notes cuz prev ones are lost

1.
>if change to rust deemed necessary, use HashBrown for hashing,
>or at least try it. Also use HashSet maybe? See how both behave
> with optimized code

2.
>the whole system now uses strings as a way to communicate instead
>of sending objects. Since classes are pretty much immutable, 
>then i have decided not to include them in the solucion class 
>and rather get them trough an array in ga_engine
>will try to make it so clase doesnt need curso as a reference
> !!PROBLEM!! set_clprof needs clase.eval_prof, and if i were
> to switch to a string system, then i would need to get the info
> for a course from an hash external to the clase class, but i will not
> be able to call that array from Solucion
> SOL: make it so Clase inherits from a course, tho it still requires copying data so that might not work so good

3. 
>maybe eval_prof only needs to consider teachers who can TEACH the course anyway, regardless of schedule, maybe the whole teacher evaluation for each course can be done as we go....

4.
>aight so
>rn the algorithm runs with a simulated dataset. In this would be universe every teacher can teach any class at any time. In a more constricted data set, it might happen that there is not enough teachers to give a course because all of its candidates are assigned, prepare for this. Look up how to fix it, maybe a local search (whatever that is)? maybe discard the solution?
>performance is issue number 2. not sure how i could fix it. 1: most of it is coming form corss over and even tho i havent tried it id bet most of it is coming from gene repair. in a more constricted data set gene repair should take a lot less. however since it still might be an issue, you might have to re write the code in rust, most of the algorithm has been made so its somewhat easily translatable.


5. 
>fuggin triple cuadruple check crossover

6.
>so i made it so teachers have a "score", the score is produced when the>teacher is created, this way, if there ever is anything within "prof_eval" aside from these parameters, i dont have to compute that function again OR copy its values


7.
>yay it apparently works
>you should seriously take your time to look
>at if the code is consistent or not, this time make a backup
>the sweetspot for the lower bound of roll in roulette is 
>somewhere between 0 and x<t_fitness/3
>plateau is reaces around gen 20



>maybe make gen_repair random again?
>dont sort fit hash either



>HOLYYYYYYYYYYYYYYY FUCKKKKKKKKKKKKK
CHECK THAT THE SOL EVALUTATION FUNCTION IS NOT COUNTING ONLY A SINGLE TEACHER
FOR EXAMPLE; IF TEACHER A IS ASSIGNED TO CLASSES C AND D, MAKE SURE HIS SCORE
IS COUNTED TWICE, SINCE HE IS IN BOTH CLASSES


ALSO START CONSIDERING THE AMOUNT OF PROFESSORS IN A SOLUTION

`performance`
>change horarios to be arrays
>presize hashes 


`result`
- make it so gene repair is not random (done but can be improved)
- implment the mixed selection thing he mentioned !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
- sort candidates (done)
- include greedy sol
- keep best solutions from prev
- converging sol (maybe not)
- sort classes and assign in order of candidates (done)
- increasing mutation probability !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
- gene repair and maybe solution creation using LNS !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


so:
since they only care about the professors score then theres no need to even implement something that is not greedy. EXCEPT that there is. y'see the best solution is one where the best possible teachers are assigned, since that will always add up to the higher score.
When you assign a teacher to a class, regardless of the amount of classes he can teach only decreases by one..... EXCEPT NOT HA. it decreases by the amount of classes he can't teach that day because they're in a different venue. 

so: 
>You'll want to include this venue thing in the evaluation function.
>You'll also want to prevent teachers from having one class. 


The reason lns currently doesnt work is because we're not considering things like sedes or giving every teacher a fair amount of classes
[p1][p1][p1][p1][p2][p2][p3][p2][p3][p5][p6][p7]
score = p1 x 4 +p2 x 3+ p3*2 +p5 +p6 + p7







## preguntas
>sedes max?

## reunion 4
>919 clases adultos
>36 h max
