(* Mateusz Buta
 * Zadanie domowe 1, czesc 1
 *  structure file
 *)
structure id291392 :> PART_ONE =
struct
  exception NotImplemented

  datatype 'a tree= Leaf of 'a | Node of 'a tree * 'a * 'a tree

(*---------------------- Funkcje liczb całkowitych ----------------------*)
fun sum n =
	if n=1 then
        1
    else
        n+sum (n-1)
;
fun fac n =
    if n=1 then
        1
    else
        n*fac (n-1)
;
fun fib n =
    if n<=1 then
        1
    else
        fib (n-2) + fib (n-1)
;
fun gcd (m,n) =
	if m=0 then 
		n
	else
	if n=0 then
		m
	else
    if m=n then 
        m
    else  
    if m<n then 
        gcd (m,(n mod m))
    else
        gcd ((m mod n),n)
; 
fun max [] = 0
  | max [head] = head
  | max l = 
    if (hd l)> max (tl l) then
		(hd l)
    else
        max (tl l)
;
(*---------------------- Funkcje na drzewach binarnych ----------------------*)

fun sumTree (Leaf n) = n
 |  sumTree (Node(left,n,right)) = (n + sumTree left + sumTree right)
;
fun depth (Leaf n) = 0
 |  depth (Node(left,n,right)) = 
    if depth left > depth right then 
        1+depth left
    else
        1+depth right
;
fun binSearch (Leaf n) x = 
    n=x 
 |  binSearch (Node(left,n,right)) x = 
    if n=x then
        true
    else
        if x<n then
            binSearch (left) x
        else  
            binSearch (right) x
;
fun preorder (Leaf n) = [n]
 |  preorder (Node(left,n,right)) =
    (n::preorder left@preorder right)
;
(*---------------------- Funkcje na listach liczb całkowitych ----------------------*)
fun listAdd l1 l2 =
    if null l1=true then 
		l2 
	else
    if null l2=true then 
		l1
    else 
		(hd l1 + hd l2 :: listAdd (tl l1) (tl l2))
;
fun insert m l =
    if (null l=true) then 
		[m] 
    else  
    if m<hd l then
        (m::l)
    else
        (hd l :: insert m (tl l))
;
fun insort [] = 
	[]
 |  insort l =
    insert (hd l) (insort (tl l))
; 
(*---------------------- Funkcje wyzszego rzedu ----------------------*)
fun compose f g = 
    (fn x=> g (f x))
;
fun curry f x y  =  
    f(x,y) 
;
fun uncurry f (x,y) = 
    f x y
;
fun multifun f n =
    if n=1 then
        f
    else
        compose f (multifun f (n-1))
;
(*---------------------- . Funkcje na liście ’a list ----------------------*)  
fun ltake l i =
    if null l=true then
        []
    else
    if i=0 then
        []
    else
        (hd l::ltake (tl l) (i-1))
;
fun lall f [head] =
    f head 
 |  lall f l = 
    if f (hd l) then
        lall f (tl l)
    else
        false
;
fun lmap f [] =
    []
 |  lmap f l = 
    (f (hd l) :: lmap f (tl l))
;
fun lrev [] =
    []
 |  lrev l = 
    lrev (tl l) @ [hd l]
;
fun lzip (l1,[])=[]
 |  lzip ([],l2)=[]
 |  lzip (l1,l2)=
    (hd l1,hd l2)::(lzip (tl l1,tl l2))
;
fun split []=
    ([],[])
 |  split [head] = 
    ([head],[])
 |  split (head1::head2::tail) =
    let 
		val (tail1,tail2) = split tail
        in ((head1::tail1),(head2::tail2)) 
	end
;
fun cartprod l [] =
    []
 |  cartprod [] l =
    []
 |  cartprod l1 l2 =
    (hd l1,hd l2)::(cartprod [hd l1] (tl l2))@(cartprod (tl l1) l2 )
;

end
