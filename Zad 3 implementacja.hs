-- Zad 3 Implementacja Mateusz Buta

data A = Int 
data B = Bool 
data C = String
data D = Char

impl_rozdz :: (A -> B) -> (A -> C) -> A -> B -> C
proof_impl_rozdz h i j k = i j

impl_komp :: (A -> B) -> (B -> C) -> A -> C
proof_impl_komp h i j = i (h j)

impl_perm :: (A -> B -> C) -> B -> A -> C
proof_impl_perm h i j = h j i

impl_conj :: A -> B -> (A,B)
proof_impl_conj h i = (h,i)

conj_elim_l :: (A,B) -> A
proof_conj_elim_l (i,j) = i 

disj_intro_l :: A -> Either A B
proof_disj_intro_l h = Left h

rozl_elim :: Either A B -> (A -> C) -> (B -> C) -> C
proof_rozl_elim (Left h) i j = i h
proof_rozl_elim (Right h) i j = j h

diamencik :: (A -> B) -> (A -> C) -> (B -> C -> D) -> A -> D
proof_diamencik h i j k = j (h k)(i k)

slaby_peirce :: ((((A -> B) -> A) -> A) -> B) -> B
proof_slaby_peirce h = h (\i -> i (\j -> h (\k -> j)))

rozl_impl_rozdz :: ((Either A B) -> C) -> ((A -> C),(B -> C))
proof_rozl_impl_rozdz h = ((\i -> h (Left i)),(\j -> h (Right j)))

rozl_impl_rozdz_odw :: ((A -> C),(B -> C)) -> Either A B -> C
proof_rozl_impl_rozdz_odw (h,i) (Left j) = h j
proof_rozl_impl_rozdz_odw (h,i) (Right j) = i j

ccurry :: ((A,B) -> C) -> A -> B -> C
proof_ccurry h i j = h (i,j)

unccurry :: (A -> B -> C) -> (A,B) -> C
proof_unccurry h (i,j) = h i j

main = print "Zad3 Mateusz Buta"
