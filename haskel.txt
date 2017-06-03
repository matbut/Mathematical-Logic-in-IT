data A = Int 
data B = Bool 
data C = String
data D = Char

impl_rozdz :: (A -> B) -> (A -> C) -> A -> B -> C
impl_rozdz h i j k = i j

impl_komp :: (A -> B) -> (B -> C) -> A -> C
impl_komp h i j = i (h j)

impl_perm :: (A -> B -> C) -> B -> A -> C
impl_perm h i j = h j i

impl_conj :: A -> B -> (A,B)
impl_conj h i = (h,i)

conj_elim_l :: (A,B) -> A
conj_elim_l (i,j) = i 

disj_intro_l :: A -> Either A B
disj_intro_l h = Left h

rozl_elim :: Either A B -> (A -> C) -> (B -> C) -> C
rozl_elim (Left h) i j = i h
rozl_elim (Right h) i j = j h

diamencik :: (A -> B) -> (A -> C) -> (B -> C -> D) -> A -> D
diamencik h i j k = j (h k)(i k)

slaby_peirce :: ((((A -> B) -> A) -> A) -> B) -> B
slaby_peirce h = h (\i -> i(\j -> h (\k -> j)))
--slaby_peirce = \h -> h (\i -> i(\j -> h (\k -> j)))

rozl_impl_rozdz :: ((Either A B) -> C) -> ((A -> C),(B -> C))
rozl_impl_rozdz h = h (\i Left k -> l)
rozl_impl_rozdz h = h (\j Right k -> l)

main = print "Zad3"

